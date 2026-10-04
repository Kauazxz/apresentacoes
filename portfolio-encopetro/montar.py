"""Monta o portfólio a partir de fonte.html.

Saídas:
  index.html                 -> prévia leve; usa fotos/ e fontes/ ao lado
  portfolio-encopetro.html   -> arquivo único para enviar (fotos e fontes embutidas)
  portfolio-encopetro.pdf    -> uma página 16:9 por seção (Chrome headless)

Uso: python montar.py [--sem-pdf]
"""
import base64, html as H, json, re, subprocess, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
CHROME = Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
MIME = {".webp": "image/webp", ".png": "image/png", ".jpg": "image/jpeg", ".woff2": "font/woff2"}

def data_uri(rel):
    p = AQUI / rel
    return f"data:{MIME[p.suffix]};base64," + base64.b64encode(p.read_bytes()).decode()

fonte = (AQUI / "fonte.html").read_text(encoding="utf-8")
mapa = (AQUI / "mapa-brasil.svg").read_text(encoding="utf-8")
fontes_css = (AQUI / "fontes" / "fontes.css").read_text(encoding="utf-8")
base = fonte.replace("<!--MAPA-->", mapa)

# grade de obras já pronta no HTML: aparece mesmo onde o JavaScript não roda
# (pré-visualização de arquivo no celular). O JS só liga os cliques.
bloco = fonte.split("var OBRAS = ")[1].split("];")[0] + "]"
obras = json.loads(re.sub(r'([{,])\s*(t|l|c|d|f):', lambda m: m.group(1) + '"' + m.group(2) + '":', bloco))
ico = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="5" width="18" height="14" rx="1"/>'
       '<circle cx="9" cy="10" r="2"/><path d="M21 16l-5-5-9 8"/></svg>')
cartoes = "".join(
    f'<button type="button" class="obra rv d{i % 4 + 1}" data-c="{o["c"]}" aria-label="Ver fotos: {H.escape(o["t"])}">'
    f'<img loading="lazy" src="fotos/{o["f"][0]}.webp" alt="">'
    f'<span class="qt">{ico}{len(o["f"])}</span>'
    f'<span class="ot"><span>{H.escape(o["l"])}</span><b>{H.escape(o["t"])}</b></span>'
    f'<span class="ver"><i>VER FOTOS</i></span></button>'
    for i, o in enumerate(obras))
alvo = '<div class="obras" id="grade-obras"></div>'
assert alvo in base
base = base.replace(alvo, f'<div class="obras" id="grade-obras">{cartoes}</div>')

# 1) prévia leve
(AQUI / "index.html").write_text(base.replace("/*FONTES*/", fontes_css), encoding="utf-8")

# 2) arquivo único
css_embutido = re.sub(r"url\((fontes/[^)]+)\)", lambda m: f"url({data_uri(m.group(1))})", fontes_css)
unico = base.replace("/*FONTES*/", css_embutido)
cache = {}
def troca(m):
    rel = m.group(0)
    if rel not in cache:
        cache[rel] = data_uri(rel)
    return cache[rel]
unico = re.sub(r"fotos/[\w.-]+\.(?:webp|png|jpg)", troca, unico)
# o JS monta caminhos "fotos/" + nome + ".webp": embute um mapa nome -> data URI
nomes = sorted({p.stem for p in (AQUI / "fotos").glob("*.webp")})
usados = {f for o in obras for f in o["f"]}
tabela = ",".join(f'"{n}":"{data_uri("fotos/" + n + ".webp")}"' for n in nomes if n in usados)
unico = unico.replace('function src(n){ return "fotos/" + n + ".webp"; }',
                      "var FOTOS={" + tabela + "};function src(n){ return FOTOS[n]; }")
saida = AQUI / "portfolio-encopetro.html"
saida.write_text(unico, encoding="utf-8")
print(f"index.html: {(AQUI/'index.html').stat().st_size/1024:.0f} KB")
print(f"portfolio-encopetro.html: {saida.stat().st_size/1024/1024:.2f} MB ({len(obras)} obras, {len(usados & set(nomes))} fotos na galeria)")
sobrou = re.findall(r'["(]fotos/[\w.-]+', unico)
print("referências a fotos/ que sobraram:", sobrou[:5] or "nenhuma")

# 3) PDF — o Chrome grava WebP como bitmap sem compressão (dezenas de MB);
#    para o PDF, as fotos entram como JPEG, que ele repassa já comprimido.
if "--sem-pdf" not in sys.argv:
    import io
    from PIL import Image
    def para_jpeg(m):
        tipo, b64 = m.group(1), m.group(2)
        if tipo != "webp":
            return m.group(0)
        im = Image.open(io.BytesIO(base64.b64decode(b64))).convert("RGB")
        buf = io.BytesIO(); im.save(buf, "JPEG", quality=80, optimize=True, progressive=False)
        return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    memo = {}
    def troca_jpeg(m):
        if m.group(0) not in memo:
            memo[m.group(0)] = para_jpeg(m)
        return memo[m.group(0)]
    versao_pdf = re.sub(r"data:image/(webp|png);base64,([A-Za-z0-9+/=]+)", troca_jpeg, unico)
    tmp = AQUI / "_para-pdf.html"
    tmp.write_text(versao_pdf, encoding="utf-8")
    pdf = AQUI / "portfolio-encopetro.pdf"
    try:
        subprocess.run([str(CHROME), "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        "--virtual-time-budget=15000", "--no-pdf-header-footer",
                        f"--print-to-pdf={pdf}", tmp.as_uri()],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    finally:
        tmp.unlink(missing_ok=True)
    print(f"portfolio-encopetro.pdf: {pdf.stat().st_size/1024/1024:.2f} MB")
