# Detecção e Classificação de Lesões Mamárias em Ultrassonografia com YOLO

Pesquisa de **visão computacional** que treina detectores da família **YOLO** para **localizar e classificar** lesões mamárias **benignas** e **malignas** em imagens de **ultrassom**, como prova de conceito de um sistema de **auxílio ao diagnóstico (CAD)**.

**Autores:** Juan José Gouvêa Cardenas e Felipe Ramirez Pereira Botero

> **Aviso.** Este é um projeto de **pesquisa acadêmica / prova de conceito**. O modelo **não é um dispositivo médico aprovado** (FDA/ANVISA), **não diagnostica câncer** e **não substitui** a avaliação de um profissional de saúde. Um modelo de imagem apenas **localiza uma lesão e sugere** se ela tem aparência benigna ou maligna; o diagnóstico definitivo exige correlação clínica e confirmação por biópsia.

## Sobre a pesquisa

O câncer de mama é o mais incidente entre mulheres no Brasil — o INCA estimou cerca de **73.610 casos novos/ano** para o triênio 2023–2025. O diagnóstico tardio, agravado pela escassez de equipamentos e radiologistas na rede pública, contribui para a mortalidade. A **ultrassonografia** é uma modalidade complementar importante (sobretudo em mamas densas), e detectores de objetos em tempo real como o **YOLO** podem servir de **ferramenta de apoio** à leitura dos exames.

- **Dataset:** [BUSI — *Breast Ultrasound Images Dataset*](https://www.kaggle.com/datasets/aryashah2k/breast-ultrasound-images-dataset) (Al-Dhabyani et al., **2020**) — 780 imagens de ultrassom (437 benignas, 210 malignas, 133 normais), com máscaras de segmentação.
- **Tarefa:** **detecção** (localizar a lesão com *bounding box*) **+ classificação** (benigna/maligna). As imagens normais entram como **exemplos negativos** (fundo).
- **Modelo:** **YOLO11s** (Ultralytics), ajustado por **transferência de aprendizado** a partir de pesos COCO.

### Rigor metodológico

Esta pesquisa adota práticas que evitam armadilhas comuns na literatura de BUSI:

1. **Deduplicação antes da divisão.** O BUSI tem ~19% de duplicatas documentadas (Pawlowska et al., 2023) que, espalhadas entre os conjuntos, causam *data leakage* e inflam métricas. Removemos duplicatas por *hash* de conteúdo.
2. **Divisão estratificada treino/validação/teste (70/15/15)**, com semente fixa e conjunto de teste cego.
3. **Avaliação adequada a detectores.** Em vez de tratar a detecção como classificação por imagem (`classification_report` sobre a primeira caixa — o que ignora a localização), usamos `model.val()` do Ultralytics, com casamento por **IoU** e métricas **por classe**: **mAP@50**, **mAP@50–95**, precisão, revocação e F1, além da **taxa de falsos positivos** nas imagens normais.
4. **Aumento de dados conservador** para ultrassom (rotações leves e *flip* horizontal; sem distorções geométricas agressivas, que prejudicam a anatomia).

### Resultados

Os resultados de detecção (mAP e métricas por classe) são gerados pelo notebook
([Seção 14](notebooks/treinamento-yolo11-busi.ipynb)) via `model.val()` no conjunto de teste e devem ser interpretados contra a faixa realista de detecção em **BUSI puro** reportada na literatura — e **não** contra os índices de 94–99% de *classificação* (tarefa diferente) ou de conjuntos aumentados/combinados, que não são comparáveis. A discussão completa e a tabela de métricas estão no [artigo](docs/artigo/main.tex).

> ℹ️ As métricas numéricas no artigo serão preenchidas após o re-treino com este pipeline (campos marcados em vermelho no LaTeX).

## Estrutura do repositório

```
├── app.py                                # Demo interativa (Gradio) com o modelo treinado
├── model.pt                              # Pesos do modelo treinado (Git LFS, ~40 MB)
├── requirements.txt                      # Dependências da demo
├── notebooks/
│   └── treinamento-yolo11-busi.ipynb     # Pipeline completo de treino e avaliação (Kaggle)
├── amostras/                             # Imagens de exemplo (B=benigno, M=maligno, N=normal)
└── docs/
    ├── artigo/                           # Artigo científico em LaTeX (main.tex)
    └── REFERENCIAS.md                    # Bibliografia comentada (ABNT)
```

## Como executar a demo

Requer Python 3.10+ e [Git LFS](https://git-lfs.com) (os pesos do modelo são versionados com LFS):

```bash
git clone https://github.com/junowoz/deteccao-lesoes-mama-yolo.git
cd deteccao-lesoes-mama-yolo
git lfs install && git lfs pull   # baixa o model.pt real (~40 MB)

python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python app.py
```

A interface abre no navegador: envie uma imagem de ultrassom (há exemplos prontos da pasta `amostras/`) e o modelo desenha as detecções com o grau de confiança.

## Como reproduzir o treinamento

O notebook [`notebooks/treinamento-yolo11-busi.ipynb`](notebooks/treinamento-yolo11-busi.ipynb) contém o pipeline completo (deduplicação, geração de rótulos, divisão estratificada, treino e avaliação por `model.val()`). Foi feito para rodar no Kaggle (GPU T4) com o dataset BUSI anexado.

## Artigo

O artigo científico está em [`docs/artigo/main.tex`](docs/artigo/main.tex) (LaTeX autocontido; veja as [instruções de compilação](docs/artigo/README.md)). A bibliografia comentada está em [`docs/REFERENCIAS.md`](docs/REFERENCIAS.md).

## Como citar

> GOUVEA CARDENAS, J. J.; BOTERO, Felipe Ramirez Pereira. **Detecção e classificação de lesões mamárias em ultrassonografia com visão computacional (YOLO).** 2026. Disponível em: https://github.com/junowoz/deteccao-lesoes-mama-yolo.

## Licença

Código sob licença MIT (ver [`LICENSE`](LICENSE)). O dataset BUSI segue os termos de uso dos autores originais (Al-Dhabyani et al., 2020).
