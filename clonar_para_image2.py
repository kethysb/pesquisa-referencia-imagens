"""
Script de Clonagem & Inicialização Modular: Hub de Referências -> Nova Geração Image 2
Permite pegar qualquer referência do hub e clonar uma esteira 100% isolada e pronta para rodar no Image 2.
Suporta nichos jurídicos, imobiliários e máquinas industriais têxteis (JV Usinagem - Pai James).
"""
import os
import sys
import shutil
import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RADAR_VIRAL = BASE_DIR.parent
AUTO_IMAGE2_DIR = Path(r"C:\Users\Kethely\Downloads\automações\automação image 2 chatgot")

CATALOGO_DIR = BASE_DIR / "04_banco_referencias_catalogadas"

CASOS_DISPONIVEIS = {
    "1": {
        "nome": "Trabalhista Bancário / PJ",
        "nicho": "advocacia",
        "anexo_1": "advocacia/ref_01_mercado_trabalhista_stonoga.png",
        "anexo_2": "advocacia/ref_01_behance_editorial_vertice.jpg",
        "tipo_densidade": "Media",
        "headline_sugestao": "Trabalhou sem carteira assinada ou horas extras não pagas?"
    },
    "2": {
        "nome": "Holding Familiar / Herança (Capa Minimalista)",
        "nicho": "advocacia",
        "anexo_1": "advocacia/ref_02_mercado_inventario_pouco_texto.jpg",
        "anexo_2": "advocacia/ref_02_behance_baixa_densidade.png",
        "tipo_densidade": "Baixa (Capa)",
        "headline_sugestao": "Seu patrimônio não deve terminar num inventário."
    },
    "3": {
        "nome": "Holding Familiar (4 Pilares Modulares)",
        "nicho": "advocacia",
        "anexo_1": "advocacia/ref_03_mercado_holding_muito_texto.jpg",
        "anexo_2": "advocacia/ref_03_behance_alta_densidade_modular.png",
        "tipo_densidade": "Alta (Grid 4 Caixas)",
        "headline_sugestao": "4 Motivos para Criar uma Holding Familiar Hoje"
    },
    "4": {
        "nome": "Defesa Bancária PJ / Dívidas (Dossiê & Split Screen)",
        "nicho": "advocacia",
        "anexo_1": "advocacia/ref_04_mercado_divida_pj_andrade.jpg",
        "anexo_2": "advocacia/ref_04_behance_dossie_contrato.png",
        "tipo_densidade": "Split Screen (50/50)",
        "headline_sugestao": "Parcela atrasada não precisa virar penhora ou bloqueio."
    },
    "5": {
        "nome": "Direito Imobiliário / Leilões e Dívidas Ocultas",
        "nicho": "imobiliario",
        "anexo_1": "imobiliario/ref_01_mercado_leilao_anzoategui.png",
        "anexo_2": "advocacia/ref_04_behance_dossie_contrato.png",
        "tipo_densidade": "Dossiê / Alerta",
        "headline_sugestao": "Cuidados cruciais antes de arrematar imóvel em leilão."
    },
    "6": {
        "nome": "Desfibradeira de Fibra Siliconada (JV Usinagem)",
        "nicho": "maquinas_industriais",
        "anexo_1": "maquinas_industriais/01_Desfibradeira_de_Fibra/01_visao_geral_completa.jpg",
        "anexo_2": "maquinas_industriais/01_Desfibradeira_de_Fibra/02_maquina_em_operacao_esteira.png",
        "tipo_densidade": "Editorial Técnico / Catálogo B2B",
        "headline_sugestao": "Desfibramento contínuo de alta velocidade com fibra siliconada volumosa e sem embolar."
    },
    "7": {
        "nome": "Enchedora Automática de Travesseiros (JV Usinagem)",
        "nicho": "maquinas_industriais",
        "anexo_1": "maquinas_industriais/02_Enchedora_de_Travesseiros/02_enchedora_visao_frontal.jpg",
        "anexo_2": "maquinas_industriais/02_Enchedora_de_Travesseiros/01_bocal_enchimento_travesseiro.jpg",
        "tipo_densidade": "Alta Velocidade / Sopro Pneumático",
        "headline_sugestao": "Enchimento instantâneo com peso padrão e zero desperdício de fibra."
    },
    "8": {
        "nome": "Tesourinha Cortadeira de Estopa (JV Usinagem)",
        "nicho": "maquinas_industriais",
        "anexo_1": "maquinas_industriais/03_Tesourinha_Cortadeira_de_Estopa/01_tesourinha_estopa_visao_geral.jpg",
        "anexo_2": "maquinas_industriais/03_Tesourinha_Cortadeira_de_Estopa/02_tesourinha_estopa_mecanismo_corte.jpg",
        "tipo_densidade": "Corte Contínuo / Alta Durabilidade",
        "headline_sugestao": "Corte contínuo de retalhos têxteis e estopa com afiação duradoura."
    },
    "9": {
        "nome": "Projetos Especiais Sob Medida (JV Usinagem)",
        "nicho": "maquinas_industriais",
        "anexo_1": "maquinas_industriais/04_Projetos_Especiais_Sob_Encomenda/01_projeto_maquina_sob_medida_1.jpg",
        "anexo_2": "maquinas_industriais/04_Projetos_Especiais_Sob_Encomenda/02_projeto_maquina_sob_medida_2.jpg",
        "tipo_densidade": "Dossiê Industrial / Engenharia Sob Encomenda",
        "headline_sugestao": "Máquinas industriais customizadas sob medida para a sua linha de produção."
    }
}

def clonar_para_image2(nome_cliente: str, opcao_caso: str = "6") -> Path:
    hoje = datetime.datetime.now().strftime("%Y%m%d")
    slug_cliente = "".join(c if c.isalnum() else "_" for c in nome_cliente.lower()).strip("_")
    nome_pasta = f"geracao_{hoje}_{slug_cliente}_image2"
    destino = RADAR_VIRAL / nome_pasta

    if destino.exists():
        print(f"[!] A pasta {destino.name} já existe! Usando destino existente.")
    else:
        destino.mkdir(parents=True, exist_ok=True)

    # Subpastas padronizadas
    (destino / "01_garimpo_semrush_meta_ads").mkdir(exist_ok=True)
    (destino / "02_referencias_duplas").mkdir(exist_ok=True)
    (destino / "03_brand_dna").mkdir(exist_ok=True)
    (destino / "04_roteiro_e_prompts_image2").mkdir(exist_ok=True)
    (destino / "05_imagens_geradas_image2").mkdir(exist_ok=True)

    caso = CASOS_DISPONIVEIS.get(str(opcao_caso), CASOS_DISPONIVEIS["6"])
    src_anexo1 = CATALOGO_DIR / caso["anexo_1"]
    src_anexo2 = CATALOGO_DIR / caso["anexo_2"]

    dst_anexo1 = destino / "02_referencias_duplas" / src_anexo1.name
    dst_anexo2 = destino / "02_referencias_duplas" / src_anexo2.name

    if src_anexo1.exists():
        shutil.copy2(src_anexo1, dst_anexo1)
    if src_anexo2.exists():
        shutil.copy2(src_anexo2, dst_anexo2)

    # Prompt inteligente: se for máquina industrial ou editorial tradicional
    if caso.get("nicho") == "maquinas_industriais":
        prompt_calibrado = f"""Create a photorealistic, ultra-high-definition industrial commercial photograph (vertical 4:5 aspect ratio, 1080x1350 px) showcasing this exact industrial textile machine from '{nome_cliente}':
- MACHINE DETAILS: Based faithfully on ATTACHMENT 1 and ATTACHMENT 2, showing the heavy-duty blue steel chassis, precision conveyor belts, Delta inverter control panel, gear drive, and electrical motors.
- SCENE & ENVIRONMENT: Clean, modern, bright industrial manufacturing facility. An operator in proper safety attire overseeing smooth operation. Crisp commercial lighting, cinematic depth of field, natural metallic textures and brushed steel sheen.
- CORE VALUE: {caso['headline_sugestao']}
ANTI-AI RESTRICTIONS: NO cartoon or 3D rendering looks, NO sci-fi futuristic nonsense, NO warped mechanical parts or impossible gears. Must look 100% like a genuine, high-end European industrial equipment catalog photograph."""
    else:
        prompt_calibrado = f"""Create a high-end editorial Instagram Feed post graphic (vertical 4:5 aspect ratio, 1080x1350 px) for '{nome_cliente}', fusing the attached reference images with STRICT TEXT DENSITY PARITY:
- ATTACHMENT 1 (Meta Ads): {caso['headline_sugestao']}
- ATTACHMENT 2 (Behance): Mirror this human editorial art direction, off-white paper canvas, and documentary natural lighting.
ANTI-AI RESTRICTIONS: NO 3D, NO golden glossy statues, NO CGI glowing effects, NO plastic skin."""

    script_executor = f"""# Executor Automático do Image 2 para {nome_cliente}
import sys
from pathlib import Path
AUTO_DIR = Path(r"{AUTO_IMAGE2_DIR}")
sys.path.insert(0, str(AUTO_DIR))

from fast_image2 import generate_image_fast

BASE = Path(__file__).resolve().parent
ANEXO_1 = str(BASE / "02_referencias_duplas" / "{src_anexo1.name}")
ANEXO_2 = str(BASE / "02_referencias_duplas" / "{src_anexo2.name}")
DEST_IMG = BASE / "05_imagens_geradas_image2" / "image2_oficial_peca_01.png"

prompt = \"\"\"{prompt_calibrado}\"\"\"

print("Gerando no Image 2 oficial do ChatGPT...")
res = generate_image_fast(
    prompt=prompt,
    image_ref_path=[ANEXO_1, ANEXO_2],
    dest=DEST_IMG,
    profile_dir="chatgpt-profile-conta-4"
)
print("Resultado:", res)
"""
    (destino / "executar_geracao_image2.py").write_text(script_executor, encoding="utf-8")
    (destino / "vercel.json").write_text('{"cleanUrls": true}', encoding="utf-8")

    print("\n" + "="*60)
    print(f"CLONAGEM REALIZADA COM SUCESSO!")
    print(f"Cliente: {nome_cliente}")
    print(f"Nicho / Caso Selecionado: {caso['nome']}")
    print(f"Pasta Isolada Criada: {destino}")
    print(f"Anexo 1: {dst_anexo1.name}")
    print(f"Anexo 2: {dst_anexo2.name}")
    print(f"Script Image 2 Pronto: {destino / 'executar_geracao_image2.py'}")
    print("="*60 + "\n")
    return destino

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cliente = sys.argv[1]
        opcao = sys.argv[2] if len(sys.argv) > 2 else "6"
        clonar_para_image2(cliente, opcao)
    else:
        print("=== CLONADOR MODULAR: HUB DE REFERÊNCIAS -> NOVO CLIENTE IMAGE 2 ===")
        print("Casos disponíveis:")
        for k, v in CASOS_DISPONIVEIS.items():
            print(f"  [{k}] {v['nome']} ({v['tipo_densidade']})")
        print("\nUso via comando:")
        print("python clonar_para_image2.py \"Nome do Cliente\" [numero_do_caso]")
        print("Exemplo Máquinas: python clonar_para_image2.py \"JV Usinagem\" 6")