# Artigo (LaTeX)

Fonte do artigo científico do projeto: [`main.tex`](main.tex).

É autocontido — usa apenas pacotes do TeX Live padrão (`babel`, `natbib`,
`booktabs`, `tabularx`, `hyperref`, `xcolor`) e **não** depende de `.bib` externo.

## Como gerar o PDF

**Opção 1 — Overleaf (mais simples):** crie um projeto novo, envie o `main.tex`
e compile (menu *Recompile*). O compilador padrão (pdfLaTeX) já funciona.

**Opção 2 — Local (TeX Live / MacTeX):**

```bash
cd docs/artigo
pdflatex main.tex
pdflatex main.tex   # 2ª passada resolve citações e referências cruzadas
```

No macOS, instale o MacTeX (`brew install --cask mactex-no-gui`) ou o BasicTeX
(`brew install --cask basictex`) caso ainda não tenha o `pdflatex`.

## Antes de publicar

A seção **Resultados** contém marcadores em vermelho (`[...]`) que devem ser
preenchidos com a saída de `model.val()` após o re-treino — veja o checklist no
[`README` do projeto](../../README.md) e no notebook de treinamento.
