# Artigo (LaTeX)

Fonte do artigo científico: [`main.tex`](main.tex). É **autocontido** — usa apenas
pacotes do TeX Live padrão (`babel`, `natbib`, `booktabs`, `tabularx`, `hyperref`,
`xcolor`, `graphicx`, `lmodern`) e **não** depende de `.bib` externo.

## Como gerar o PDF

**Opção 1 — Overleaf (mais simples):** crie um projeto novo, envie o `main.tex` e
compile (*Recompile*). O compilador padrão (pdfLaTeX) já funciona.

**Opção 2 — Local (TeX Live / MacTeX):**

```bash
cd docs/artigo
pdflatex main.tex
pdflatex main.tex   # 2ª passada resolve citações e referências cruzadas
```

No macOS: `brew install --cask mactex-no-gui` (ou `basictex`).

## Antes de submeter

O artigo contém **placeholders em vermelho** (comando `\pend`, renderizados como
`[XX]`) em todos os pontos que dependem dos resultados reais do re-treino:
métricas (Tabelas 2 e 3), composição dos conjuntos (Tabela 1), taxa de falsos
positivos, versões do ambiente, afiliação e declarações.

1. Rode o notebook no Kaggle (ver [`CHECKLIST_KAGGLE.md`](../../CHECKLIST_KAGGLE.md)).
2. Preencha os `[XX]` com os números de `resultados_experimentais.json` /
   `tabela_resultados.md`.
3. Insira a figura de exemplos e a matriz de confusão.
4. Remova a "Nota aos autores" em vermelho no início da Seção de Resultados.
5. Confirme que **não resta nenhum `\pend`**: `grep -c '\pend' main.tex` deve dar 0.