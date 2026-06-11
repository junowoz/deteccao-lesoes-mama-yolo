# Referências (bibliografia comentada)

Lista consolidada em formato **ABNT**, com uma nota sobre o papel de cada fonte
no trabalho. As referências formais aparecem em [`artigo/main.tex`](artigo/main.tex).

> Os PDFs de terceiros usados como apoio ficam na pasta local `RECURSOS/`
> (não versionada — ver `.gitignore`), pois seguem as licenças de seus autores.

## Dataset

- **AL-DHABYANI, W.; GOMAA, M.; KHALED, H.; FAHMY, A.** Dataset of breast ultrasound images. *Data in Brief*, v. 28, art. 104863, fev. 2020. DOI: 10.1016/j.dib.2019.104863.
  *Conjunto BUSI: 780 imagens de ultrassom (437 benignas / 210 malignas / 133 normais), com máscaras de segmentação. Base principal do trabalho. Ano correto: 2020 (não 2019).*

- **PAWLOWSKA, A.; KARWAT, P.; ZOLEK, N.** Letter to the editor. Re: "Dataset of breast ultrasound images". *Data in Brief*, v. 48, art. 109247, 2023. DOI: 10.1016/j.dib.2023.109247.
  *Documenta defeitos do BUSI (~19% de duplicatas, marcadores, Doppler, estruturas não mamárias). Justifica a deduplicação prévia à divisão dos dados.*

- **PAWLOWSKA, A. et al.** A curated benchmark dataset for ultrasound based breast lesion analysis (BrEaST). *Scientific Data*, v. 11, 2024. DOI: 10.1038/s41597-024-02984-z.
  *Conjunto curado para validação externa futura; reforça a discussão sobre qualidade de dados.*

## YOLO e arquiteturas

- **REDMON, J.; DIVVALA, S.; GIRSHICK, R.; FARHADI, A.** You Only Look Once: unified, real-time object detection. *CVPR*, 2016, p. 779–788. DOI: 10.1109/CVPR.2016.91.
  *Artigo fundacional do YOLO (detecção em uma única passagem).*

- **JOCHER, G.; QIU, J.** Ultralytics YOLO11. Software, v. 11.0.0, 2024. Disponível em: https://github.com/ultralytics/ultralytics.
  *Implementação usada (variante YOLO11s). YOLO11 é a versão estável recomendada para produção.*

- **KHANAM, R.; HUSSAIN, M.** YOLOv11: an overview of the key architectural enhancements. *arXiv*:2410.17725, 2024. DOI: 10.48550/arXiv.2410.17725.
  *Descreve os blocos C3k2 e C2PSA do YOLO11; base para a seção de arquitetura.*

- **TIAN, Y.; YE, Q.; DOERMANN, D.** YOLOv12: attention-centric real-time object detectors. *arXiv*:2502.12524, 2025. DOI: 10.48550/arXiv.2502.12524.
  *Citado para justificar a escolha de NÃO adotar o YOLOv12 (instabilidade de treino em datasets pequenos).*

- **ULTRALYTICS.** Ultralytics YOLO26 documentation. 2025–2026. Disponível em: https://docs.ultralytics.com/models/yolo26.
  *Versão mais recente (inferência sem NMS); citada como trabalho futuro.*

## CAD de mama (trabalhos relacionados)

- **ANAS, M.; HAQ, I. U.; HUSNAIN, G.; JAFFERY, S. A. F.** Advancing breast cancer detection: enhancing YOLOv5 network for accurate classification in mammogram images. *IEEE Access*, v. 12, p. 16474–16488, 2024. DOI: 10.1109/ACCESS.2024.3358686.
  *YOLOv5 + Mask R-CNN em mamografia (INbreast); MCC 92%, acurácia até 98%. Baseline metodológico (modalidade: mamografia).*

- **PRINZI, F.; INSALACO, M.; ORLANDO, A.; GAGLIO, S.; VITABILE, S.** A YOLO-based model for breast cancer detection in mammograms. *Cognitive Computation*, v. 16, p. 107–120, 2024. DOI: 10.1007/s12559-023-10189-6.
  *YOLOv5s com transferência de aprendizado (mAP 0,835; 5-fold). Evidência a favor de transfer learning e validação cruzada.*

- **MOHAMMED, A. D.; EKMEKCI, D.** Breast cancer diagnosis using YOLO-based multiscale parallel CNN and flattened threshold Swish. *Applied Sciences*, v. 14, n. 7, art. 2680, 2024. DOI: 10.3390/app14072680.
  *YOLO multiescala em mamografia (mAP@50 91,15%); evidência do CLAHE como pré-processamento útil.*

- **WURZEL, P.; MARTINS, M. O.** Classificação de imagens de mamografia com Machine Learning no auxílio de diagnósticos de câncer de mama. *Disciplinarum Scientia: Naturais e Tecnológicas*, v. 23, n. 2, p. 1–17, 2022. DOI: 10.37779/nt.v23i2.4140.
  *CNN-VGG em mamografia (CBIS-DDSM), acurácia ~91,3%. Evidência nacional de viabilidade de CNN em CAD mamário; contraste classificação por patch vs. detecção.*

- **JABEEN, K. et al.** Breast cancer classification from ultrasound images using probability-based optimal deep learning feature fusion. *Sensors*, v. 22, n. 3, art. 807, 2022. DOI: 10.3390/s22030807.
  *Classificação em BUSI (acurácia 99,18% sobre dados aumentados). Exemplo de número inflado por augmentation — citado com ressalva.*

## Contexto clínico e epidemiológico

- **INSTITUTO NACIONAL DE CÂNCER (INCA).** Estimativa 2023: incidência de câncer no Brasil. Rio de Janeiro: INCA, 2022. Disponível em: https://www.inca.gov.br/publicacoes/livros/estimativa-2023-incidencia-de-cancer-no-brasil.
  *~73.610 casos novos/ano (triênio 2023–2025); taxa bruta 66,54/100 mil. Motivação do problema.*

- **INSTITUTO NACIONAL DE CÂNCER (INCA).** Controle do câncer de mama no Brasil: dados e números 2024. Rio de Janeiro: INCA, 2024. Disponível em: https://www.inca.gov.br/mama.
  *Mortalidade, produção de mamografias no SUS e tempo até tratamento. Motivação do problema.*

- **CAMPOS, A. A. L. et al.** Time to diagnosis and treatment for breast cancer in public and private health services. *Revista Gaúcha de Enfermagem*, v. 43, e20210103, 2022. DOI: 10.1590/1983-1447.2022.20210103.en.
  *Mediana de ~70 dias até o diagnóstico, pior no SUS. Justifica ferramentas de apoio à triagem.*

- **PIRES, S. R.; MEDEIROS, R. B.; SCHIABEL, H.** Banco de imagens mamográficas para treinamento na interpretação de imagens digitais. *Radiologia Brasileira*, v. 37, n. 4, p. 239–244, 2004. DOI: 10.1590/S0100-39842004000400006.
  *Banco de imagens + software educacional BI-RADS. Citado na introdução (padronização de laudos, variabilidade interobservador).*

- **LÄNG, K. et al.** Artificial intelligence-supported screen reading versus standard double reading in the Mammography Screening with Artificial Intelligence trial (MASAI): interim safety analysis. *The Lancet Oncology*, v. 24, n. 8, p. 936–944, 2023. DOI: 10.1016/S1470-2045(23)00298-X.
  *Ensaio clínico de IA em rastreamento (mamografia). Evidência de que a IA atua como segundo leitor de apoio — não substituto.*
