# 🔬 Projeto de Pesquisa de Referência de Imagens (Hub de Engenharia Reversa)

Este repositório é o **Hub Central de Engenharia Reversa Visual, Mineração de Mercado & Clonagem Automática**, configurado tanto para **geração de imagens por código (Playwright/HTML/CSS puro)** quanto para **clonagem e disparo acelerado no Image 2 (ChatGPT GPT-4o / DALL-E 3)**.

🌐 **Links Oficiais**:
- **Repositório GitHub**: [https://github.com/kethysb/pesquisa-referencia-imagens](https://github.com/kethysb/pesquisa-referencia-imagens)
- **Painel Online na Vercel**: [https://pesquisa-referencia-imagens.vercel.app](https://pesquisa-referencia-imagens.vercel.app/)

---

## 🏭 Módulo Especial: Máquinas Industriais Têxteis (JV Usinagem - Pai James)

Este hub agora conta com integração completa das **19 fotos físicas reais em alta definição** das máquinas industriais desenvolvidas pela **JV Usinagem**:

| ID | Máquina Industrial | Fotos Reais | Destaques Técnicos | Prompt & Image 2 |
|---|---|---|---|---|
| **01** | **Desfibradeira de Fibra Siliconada** | 9 fotos + 1 gerada | Chassi azul naval, inversor Delta, esteira contínua | `Opção 6` |
| **02** | **Enchedora de Travesseiros Automática** | 4 fotos + 1 gerada | Bocal pneumático de alta pressão, enchimento em 3s | `Opção 7` |
| **03** | **Tesourinha Cortadeira de Estopa** | 4 fotos + 1 gerada | Facas rotativas de aço carbono, corte sem engasgo | `Opção 8` |
| **04** | **Projetos Especiais Sob Encomenda** | 2 fotos + 1 gerada | Linha de montagem customizada sob medida | `Opção 9` |

---

## 🚀 Como Criar Novas Imagens das Máquinas

### 1. Disparar Geração Direta no Image 2 (ChatGPT)
Para disparar a geração de novas imagens comerciais fotorrealistas no Image 2 com as fotos reais acopladas:
```bash
python gerar_novas_imagens_maquinas_image2.py 1  # 1=Desfibradeira, 2=Enchedora, 3=Tesourinha, 4=Projetos Especiais
```

### 2. Clonar Esteira Isolada para um Novo Projeto ou Campanha
Para criar uma pasta de geração 100% independente e pronta com os anexos e scripts calibrados:
```bash
python clonar_para_image2.py "JV Usinagem" 6
```
Casos disponíveis:
- `1` a `5`: Advocacia e Direito Imobiliário
- `6`: Desfibradeira de Fibra Siliconada
- `7`: Enchedora de Travesseiros
- `8`: Tesourinha Cortadeira de Estopa
- `9`: Projetos Especiais Sob Medida

### 3. Renderizar Arte Gráfica 4:5 Ultra-HD por Código Puro (Zero IA)
Para gerar uma imagem comercial de catálogo no formato vertical 4:5 (1080x1350 px com render 2x de **2160x2700 px**):
```bash
python 05_templates_para_programacao/renderizar_imagem_codigo.py 05_templates_para_programacao/template_05_catalogo_maquinas_industriais.html catalogo_desfibradeira.png
```

---

## 📂 Arquitetura da Pasta

```
Projeto_Pesquisa_Referencia_Imagens/
├── 01_minerador_meta_ads/                     # Mapeamento de dores e gerador de queries
├── 02_curador_behance_pinterest/             # Matriz de densidade e padrões de luxo
├── 03_extrator_metricas_design/              # Extrator de paleta HEX e design tokens
│   ├── extrair_metricas.py
│   └── extrair_metricas_maquinas.py          # Extrator calibrado para as máquinas industriais
├── 04_banco_referencias_catalogadas/
│   ├── catalogo_geral_referencias.json       # Catálogo completo (Advocacia + Máquinas Industriais)
│   ├── advocacia/                            # Cases jurídicos
│   ├── imobiliario/                          # Cases imobiliários
│   └── maquinas_industriais/                 # 19 fotos reais das máquinas do Pai James
│       ├── 01_Desfibradeira_de_Fibra/
│       ├── 02_Enchedora_de_Travesseiros/
│       ├── 03_Tesourinha_Cortadeira_de_Estopa/
│       └── 04_Projetos_Especiais_Sob_Encomenda/
├── 05_templates_para_programacao/
│   ├── template_01_editorial_suico.html
│   ├── template_04_split_screen_comparativo.html
│   ├── template_05_catalogo_maquinas_industriais.html # Novo template industrial 4:5
│   └── renderizar_imagem_codigo.py           # Motor Playwright Ultra-HD (2160x2700 px)
├── novas_imagens_geradas_maquinas/           # Novas variações comerciais geradas
├── clonar_para_image2.py                     # Script de clonagem modular de esteiras
├── gerar_novas_imagens_maquinas_image2.py    # Disparador mestre Image 2
├── index.html                                # Dashboard interativo (Vercel)
└── README.md
```