#!/usr/bin/env python3
"""
Reconstrói os metadados do corpus a partir dos arquivos Markdown em corpus/.

Gera:
  dados/turnos.csv    uma linha por turno de fala (humano ou IA)
  dados/catalogo.csv  uma linha por documento

Uso (na raiz do repositório):
  python3 scripts/extrair_turnos.py

Só usa a biblioteca padrão do Python (>= 3.8).
"""
import csv, glob, json, os, re, sys
from collections import Counter, defaultdict

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Uma linha de rótulo: "# Eu:", "Eu:", "# ChatGPT 5.6 Deep Guide diz:", "**Claude Opus 4.7 diz:**", "Gemini 3 Pro:" ...
ROTULO = re.compile(r"^#{0,6}\s*(?:\*\*)?\s*(?P<rot>[^#*\n:]{1,80}?)\s*(?:\*\*)?\s*:\s*(?:\*\*)?\s*$")
HUMANO = {"eu", "i", "me", "moi", "usuário", "usuario", "user"}
VERBO = re.compile(r"\b(diz|says|dit|responde|respondeu)\b", re.I)
FORNECEDORES = [
    ("openai", r"chatgpt|chagpt|\bgpt\b|\bo[134]\b"),
    ("google", r"gemin|notebooklm|bard"),
    ("anthropic", r"claude"),
    ("perplexity", r"perplexity"),
    ("xai", r"grok"),
    ("deepseek", r"deepseek"),
    ("mistral", r"mistral|le chat"),
    ("microsoft", r"copilot"),
    ("meta", r"llama|meta ai"),
]
PAPEIS = [
    ("deep_guide", r"deep\s*guide|deepguide"),
    ("prompt_instructor", r"prompt\s*instructor"),
    ("gpt_builder", r"gpt\s*builder"),
    ("gems_builder", r"gems?\s*builder"),
]
MODELO_PURO = re.compile(r"(chatgpt|chagpt|gemini?|claude|perplexity|grok|deepseek|copilot|mistral)[\w .\-]*", re.I)

def ler_frontmatter(txt):
    meta, corpo = {}, txt
    if txt.startswith("---\n"):
        fim = txt.find("\n---\n", 4)
        if fim > 0:
            for linha in txt[4:fim].split("\n"):
                if ":" in linha and not linha.startswith(" "):
                    k, v = linha.split(":", 1)
                    meta[k.strip()] = v.strip().strip('"')
            corpo = txt[fim + 5:]
    return meta, corpo

def classificar(rotulo):
    r = re.sub(r"^\d+[.)]?\s+", "", rotulo.replace("\\", "").strip())
    low = r.lower()
    if low in HUMANO:
        return {"falante": "humano", "fornecedor": "", "modelo": "", "papel": ""}
    tem_verbo = bool(VERBO.search(low))
    if not tem_verbo and not MODELO_PURO.fullmatch(low):
        return None
    fornecedor = next((f for f, rx in FORNECEDORES if re.search(rx, low)), "")
    papel = next((p for p, rx in PAPEIS if re.search(rx, low)), "")
    if not fornecedor and not papel:
        return None
    modelo = VERBO.sub("", r)
    for _, rx in PAPEIS:
        modelo = re.sub(rx, "", modelo, flags=re.I)
    modelo = re.sub(r"(?i)chagpt", "ChatGPT", modelo)
    modelo = re.sub(r"\s+", " ", modelo).strip(" -–:")
    modelo = re.sub(r"(?i)^gemin\b", "Gemini", modelo)
    if not fornecedor:
        modelo = ""  # rótulo sem fornecedor explícito (ex.: "Prompt Instructor 5 diz"): não adivinhamos
    return {"falante": "ia", "fornecedor": fornecedor or "desconhecido", "modelo": modelo, "papel": papel}

def turnos_do_texto(corpo):
    """Divide o texto em turnos. Retorna lista de dicts com linha inicial (1-based, relativa ao corpo)."""
    turnos, atual, buf = [], None, []
    def fecha():
        if atual is not None:
            atual["palavras"] = len(re.findall(r"\w+", "\n".join(buf)))
            turnos.append(atual)
    for i, linha in enumerate(corpo.split("\n"), start=1):
        m = ROTULO.match(linha.strip())
        c = classificar(m.group("rot")) if m else None
        if c:
            fecha()
            atual, buf = dict(c, rotulo_original=m.group("rot").replace("\\", "").strip(), linha=i), []
        else:
            buf.append(linha)
    fecha()
    return turnos

PT = set("de que não para uma com por mais como mas foi ao das dos seu sua ou quando muito também já está isso ele essa esse você".split())
FR = set("le la les des est une pour pas que qui dans sur avec ce cette sont mais nous vous ou du au aux être".split())
EN = set("the and of to is in that for it with as are this be on not or by an which you your can".split())

def idiomas(corpo):
    c = Counter(re.findall(r"[a-zà-ÿ]+", corpo.lower()))
    n = {k: sum(c[w] for w in s) for k, s in (("pt", PT), ("en", EN), ("fr", FR))}
    tot = sum(n.values()) or 1
    return {k: round(v / tot, 2) for k, v in n.items()}

def main():
    arquivos = sorted(glob.glob(os.path.join(RAIZ, "corpus", "*", "*.md")))
    arquivos = [a for a in arquivos if os.path.basename(a).lower() != "readme.md"]
    linhas_turnos, docs = [], defaultdict(lambda: {"arquivos": [], "palavras": 0, "turnos": [], "texto": ""})
    for arq in arquivos:
        rel = os.path.relpath(arq, RAIZ).replace(os.sep, "/")
        txt = open(arq, encoding="utf-8").read()
        meta, corpo = ler_frontmatter(txt)
        desloc = txt[: len(txt) - len(corpo)].count("\n")  # linhas do front matter
        doc_id = meta.get("id") or os.path.basename(arq).split("-")[0]
        d = docs[doc_id]
        d["meta"] = d.get("meta") or meta
        d["arquivos"].append(rel)
        d["palavras"] += len(re.findall(r"\w+", corpo))
        d["texto"] += corpo
        for t in turnos_do_texto(corpo):
            t["linha"] += desloc
            d["turnos"].append(t)
            linhas_turnos.append({"doc_id": doc_id, "arquivo": rel, "linha": t["linha"], "turno": len(d["turnos"]),
                                  "falante": t["falante"], "rotulo_original": t["rotulo_original"],
                                  "fornecedor": t["fornecedor"], "modelo": t["modelo"], "papel": t["papel"],
                                  "palavras": t["palavras"]})
    os.makedirs(os.path.join(RAIZ, "dados"), exist_ok=True)
    campos = ["doc_id", "arquivo", "linha", "turno", "falante", "rotulo_original", "fornecedor", "modelo", "papel", "palavras"]
    with open(os.path.join(RAIZ, "dados", "turnos.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos); w.writeheader(); w.writerows(linhas_turnos)
    cat = []
    for doc_id in sorted(docs, key=lambda k: (k[0] != "M", k[0] != "P", k)):
        d = docs[doc_id]; m = d["meta"]; tt = d["turnos"]
        forn = Counter(t["fornecedor"] for t in tt if t["falante"] == "ia")
        mods = Counter(t["modelo"] for t in tt if t["falante"] == "ia" and t["modelo"])
        idi = idiomas(d["texto"])
        cat.append({"doc_id": doc_id, "titulo_original": m.get("titulo_original", ""), "grupo": m.get("grupo", ""),
                    "arquivos": " ".join(d["arquivos"]), "criado_em_drive": m.get("criado_em_drive", ""),
                    "modificado_em_drive": m.get("modificado_em_drive", ""), "palavras": d["palavras"],
                    "turnos_humano": sum(1 for t in tt if t["falante"] == "humano"),
                    "turnos_ia": sum(1 for t in tt if t["falante"] == "ia"),
                    "turnos_ia_por_fornecedor": ";".join(f"{k}:{v}" for k, v in forn.most_common()),
                    "modelos_distintos": len(mods), "idioma_principal": max(idi, key=idi.get),
                    "prop_pt": idi["pt"], "prop_en": idi["en"], "prop_fr": idi["fr"],
                    "trechos_removidos": m.get("trechos_removidos", "0"),
                    "palavras_removidas": m.get("palavras_removidas", "0"),
                    "redacoes": m.get("redacoes", "0")})
    with open(os.path.join(RAIZ, "dados", "catalogo.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(cat[0].keys())); w.writeheader(); w.writerows(cat)
    print(f"{len(cat)} documentos, {len(linhas_turnos)} turnos -> dados/catalogo.csv, dados/turnos.csv")

if __name__ == "__main__":
    main()
