# Portfólio Grupo Encopetro — 2026

Portfólio web da Encopetro e ESEEL Engenharia Estrutural, no formato da apresentação
do Grupo Petrus para a GWM (seções em tela cheia, capítulos numerados, modo apresentação).

- **Para quem:** clientes e contatos da Encopetro.
- **Fonte do conteúdo:** `PORTFÓLIO GRUPO ENCOPETRO_2026_2.pdf` (50 páginas) e o site
  encopetroengenharia.com.br (serviços, filiais, equipe, currículos, clientes e instituições).
  A seção de projetos integrados usa a arte "Projetos Integrados" do grupo. Os títulos de seção
  são redação nova.

## O que mandar

| Arquivo | Uso |
|---|---|
| `portfolio-encopetro.html` | arquivo único (~16 MB) com fotos e fontes embutidas; abre offline em qualquer navegador e mostra o conteúdo mesmo sem JavaScript |
| `portfolio-encopetro.pdf` | 31 páginas 16:9, uma por seção, com o logo de 40 anos no canto |

## Como editar

Edite `fonte.html` e rode `python montar.py` (precisa de Python com Pillow e do Chrome em
`C:\Program Files\Google\Chrome\Application`). Ele gera:

- `index.html` — prévia leve que usa `fotos/` e `fontes/` ao lado;
- `portfolio-encopetro.html` e `portfolio-encopetro.pdf`.

`python montar.py --sem-pdf` pula o PDF. As fotos em `fotos/` foram extraídas do PDF de origem
e convertidas para WebP; no PDF elas entram como JPEG (WebP vira bitmap sem compressão e o
arquivo passava de 90 MB).

## Modo apresentação

Botão **Apresentar** (canto superior direito): tela cheia; `→`/`Espaço` avança uma seção,
`←` volta, `Esc` sai. Na galeria de projetos e recuperações, clicar abre todas as fotos do projeto.
