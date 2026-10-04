# Apresentações

Apresentações, portfólios e material de apoio produzidos por **Kauã Araujo de Souza**.
Cada apresentação fica numa pasta própria, com os arquivos finais prontos para enviar e a
fonte para editar.

## Apresentações

| Apresentação | Para quem | Formatos | Abrir |
|---|---|---|---|
| [**Grupo Encopetro — Portfólio 2026**](portfolio-encopetro/) | clientes e contatos da Encopetro e da ESEEL Engenharia Estrutural | página web (arquivo único, abre offline) e PDF de 31 páginas 16:9 | [PDF](portfolio-encopetro/portfolio-encopetro.pdf) · [HTML](portfolio-encopetro/portfolio-encopetro.html) · [Equipe técnica (PDF)](portfolio-encopetro/EQUIPE%20T%C3%89CNICA%20PRINCIPAL.pdf) |

### Grupo Encopetro — Portfólio 2026

Portfólio da Encopetro e da ESEEL Engenharia Estrutural em 21 seções de tela cheia: apresentação
do grupo, números, presença no país, áreas de atuação, projetos integrados, serviços, pontes e
inspeção de OAE, edificações, contenções, restauro e patrimônio, obras, clientes, equipe e
contato. Tem modo apresentação (tela cheia, navegação pelo teclado) e galeria de fotos por obra.

| Arquivo | O que é |
|---|---|
| [`portfolio-encopetro.html`](portfolio-encopetro/portfolio-encopetro.html) | versão para enviar: um arquivo só (~16 MB) com fotos e fontes embutidas; abre offline em qualquer navegador |
| [`portfolio-encopetro.pdf`](portfolio-encopetro/portfolio-encopetro.pdf) | versão PDF, 31 páginas 16:9, uma por seção |
| [`EQUIPE TÉCNICA PRINCIPAL.pdf`](portfolio-encopetro/EQUIPE%20T%C3%89CNICA%20PRINCIPAL.pdf) | currículos da equipe técnica principal, 6 páginas |
| [`index.html`](portfolio-encopetro/index.html) | prévia leve para edição; carrega `fotos/` e `fontes/` ao lado |
| [`fonte.html`](portfolio-encopetro/fonte.html) | fonte editável do portfólio |
| [`montar.py`](portfolio-encopetro/montar.py) | gera `index.html`, o HTML único e o PDF a partir da fonte |
| [`mapa-brasil.svg`](portfolio-encopetro/mapa-brasil.svg) | mapa da seção de presença |
| [`fotos/`](portfolio-encopetro/fotos/) | 149 imagens (obras, clientes, equipe e logos), em WebP e PNG |
| [`fontes/`](portfolio-encopetro/fontes/) | Barlow e Barlow Condensed em WOFF2, servidas localmente |

Instruções de edição e do modo apresentação: [`portfolio-encopetro/README.md`](portfolio-encopetro/README.md).

## Estrutura

```
apresentacoes/
├── README.md
└── portfolio-encopetro/
    ├── README.md
    ├── portfolio-encopetro.html   ← enviar
    ├── portfolio-encopetro.pdf    ← enviar
    ├── EQUIPE TÉCNICA PRINCIPAL.pdf
    ├── index.html
    ├── fonte.html
    ├── montar.py
    ├── mapa-brasil.svg
    ├── fotos/
    └── fontes/
```

## Convenções

- Uma pasta por apresentação, em minúsculas e sem acento (`nome-da-apresentacao/`), com um
  `README.md` dizendo para quem foi feita e quais arquivos enviar.
- Os arquivos finais (PDF, HTML único) ficam versionados junto da fonte, para quem só quer
  abrir e mandar.
- Nada de credencial, token ou senha no repositório.
- O GitHub recusa arquivo acima de 100 MB: vídeo e PPTX pesado vão comprimidos ou em PDF.

## Autor

Kauã Araujo de Souza — [kauaaraujo.com.br](https://kauaaraujo.com.br) · [github.com/Kauazxz](https://github.com/Kauazxz)
