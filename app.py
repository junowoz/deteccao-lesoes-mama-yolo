"""Demo interativa de detecção de lesões mamárias em ultrassom com YOLO.

Carrega o modelo treinado (model.pt) e abre uma interface Gradio onde o
usuário envia uma imagem de ultrassom e recebe as detecções anotadas
(lesões com aparência benigna/maligna e o grau de confiança).

Prova de conceito de pesquisa — não é um dispositivo médico.

Uso:
    pip install -r requirements.txt
    python app.py
"""

import glob
import os
import sys

import gradio as gr
from ultralytics import YOLO

MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model.pt")

if not os.path.exists(MODEL_PATH) or os.path.getsize(MODEL_PATH) < 1_000_000:
    # Um model.pt minúsculo é um ponteiro do Git LFS, não o peso real
    sys.exit(
        "Erro: model.pt não encontrado ou incompleto.\n"
        "Os pesos do modelo são versionados com Git LFS. Execute:\n"
        "    git lfs install && git lfs pull"
    )

model = YOLO(MODEL_PATH)


def detectar(imagem, confianca):
    results = model(imagem, conf=confianca)
    return results[0].plot()


exemplos_dir = os.path.join(os.path.dirname(MODEL_PATH), "amostras")
exemplos = [[img, 0.25] for img in sorted(glob.glob(os.path.join(exemplos_dir, "*.png")))]

demo = gr.Interface(
    fn=detectar,
    inputs=[
        gr.Image(type="numpy", label="Imagem de ultrassom"),
        gr.Slider(0.05, 0.9, value=0.25, step=0.05, label="Confiança mínima"),
    ],
    outputs=gr.Image(label="Detecções (achado sugestivo)"),
    title="Detecção de Lesões Mamárias em Ultrassom (YOLO)",
    description=(
        "Envie uma imagem de ultrassom de mama para localizar lesões com aparência "
        "benigna ou maligna. Modelo YOLO treinado com o dataset BUSI "
        "(Breast Ultrasound Images Dataset).\n\n"
        "As detecções são **achados sugestivos**, em referência ao léxico BI-RADS, "
        "não um diagnóstico.\n\n"
        "⚠️ **Aviso:** ferramenta de pesquisa / prova de conceito. **Não** é dispositivo "
        "médico aprovado (FDA/ANVISA), não constitui diagnóstico e não substitui a "
        "avaliação de um profissional de saúde."
    ),
    examples=exemplos or None,
    cache_examples=False,
)

if __name__ == "__main__":
    demo.launch()
