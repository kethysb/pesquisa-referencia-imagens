# 🔬 Projeto de Pesquisa de Referência de Imagens (Hub de Engenharia Reversa)

Esta pasta foi concebida de forma modular e independente para atuar como o **Motor de Pesquisa e Curadoria de Referências Visuais** para alimentar o seu **projeto de geração de imagem com programação** (Playwright, Puppeteer, Canvas, CSS/HTML ou Remotion).

> ⚠️ **Zero Dependência de Image 2**: Esta pasta não contém scripts de geração generativa. Seu foco é 100% mineração de mercado, direção de arte editorial de luxo, extração de paletas cromáticas e templates de código.

---

## 📂 Arquitetura da Pasta

```
Projeto_Pesquisa_Referencia_Imagens/
├── 01_minerador_meta_ads/
│   ├── catalogo_queries_semrush.json      # Mapeamento de 30+ nichos com dores e CPCs
│   └── gerador_urls_meta_ads.py           # Gerador de links pré-filtrados (media_type=image_and_meme)
│
├── 02_curador_behance_pinterest/
│   ├── guia_curadoria_luxo.md             # Guia de queries e estúdios internacionais de luxo
│   └── matriz_densidade_textual.json      # A regra dos 4 tipos de densidade textual
│
├── 03_extrator_metricas_design/
│   ├── extrair_metricas.py                # Script que lê qualquer imagem e extrai a paleta HEX e safe zone
│   └── exemplo_design_tokens.json         # Tokens prontos com variáveis CSS (:root)
│
├── 04_banco_referencias_catalogadas/
│   ├── catalogo_geral_referencias.json    # Catálogo de referências reais mineradas
│   ├── advocacia/                         # 4 cases reais pareados (Meta Ads vs Behance)
│   └── imobiliario/                       # Cases de leilões e contratos
│
├── 05_templates_para_programacao/
│   ├── template_01_editorial_suico.html   # Template 4:5 em HTML/CSS nativo
│   ├── template_04_split_screen_comparativo.html # Template 4:5 Split Screen 50/50
│   └── renderizar_imagem_codigo.py        # Motor Playwright que renderiza em PNG Ultra-HD (2160x2700 px)
│
├── index.html                             # Dashboard visual para navegar e copiar dados
├── vercel.json                            # Configuração de deploy limpo
└── README.md                              # Este manual
```

---

## 🚀 Como Levar Esta Pasta Para o Seu Projeto de Código

### Passo 1: Extrair a Paleta HEX e Métricas da Referência
Quando você tiver uma nova imagem de referência do Behance ou Pinterest, rode o extrator:
```bash
python 03_extrator_metricas_design/extrair_metricas.py caminho_da_imagem.png design_tokens.json
```
O script gerará as variáveis CSS prontas:
```css
:root {
  --canvas-bg: #F8F9F4;
  --brand-accent: #D4D2CB;
  --text-main: #21302F;
}
```

### Passo 2: Escolher o Tipo de Densidade Textual
Consulte a `02_curador_behance_pinterest/matriz_densidade_textual.json`:
- **Tipo 01 (Baixa Densidade)**: Para capas e ganchos curtos.
- **Tipo 02 (Dossiê Notarial)**: Para contratos com foto macro e card de blindagem.
- **Tipo 03 (Alta Densidade Modular)**: Para grades de 4 a 6 caixas simétricas com ícones.
- **Tipo 04 (Split Screen 50/50)**: Para tabelas comparativas (Antes vs Depois / Banco vs Defesa).

### Passo 3: Renderizar via Programação (Sem IA)
Dentro de `05_templates_para_programacao/`, basta executar:
```bash
python 05_templates_para_programacao/renderizar_imagem_codigo.py template_04_split_screen_comparativo.html saida.png
```
A imagem gerada terá proporção nativa vertical 4:5 (1080x1350 px) renderizada com `device_scale_factor: 2` (2160x2700 px em nitidez máxima de estúdio).