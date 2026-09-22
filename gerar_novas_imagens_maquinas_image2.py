"""
Gerador Especializado de Novas Imagens no Image 2: Máquinas Industriais Têxteis (JV Usinagem - Pai James)
Integra as fotos reais das máquinas como referências físicas para produzir imagens fotorrealistas de alta fidelidade técnica.
"""
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
AUTO_DIR = Path(r"C:\Users\Kethely\Downloads\automações\automação image 2 chatgot")
MAQUINAS_DIR = BASE_DIR / "04_banco_referencias_catalogadas" / "maquinas_industriais"
OUTPUT_DIR = BASE_DIR / "novas_imagens_geradas_maquinas"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(AUTO_DIR))

CATALOGO_PROMPTS_MAQUINAS = {
    "1": {
        "id": "desfibradeira_visao_geral",
        "maquina": "Desfibradeira de Fibra Siliconada",
        "pasta": MAQUINAS_DIR / "01_Desfibradeira_de_Fibra",
        "referencias": [
            MAQUINAS_DIR / "01_Desfibradeira_de_Fibra" / "01_visao_geral_completa.jpg",
            MAQUINAS_DIR / "01_Desfibradeira_de_Fibra" / "02_maquina_em_operacao_esteira.png"
        ],
        "prompt": """Ultra-photorealistic commercial industrial photography of this exact heavy-duty Fiber Opener and De-shredding Machine (Desfibradeira de Fibra Siliconada) from 'JV Usinagem':
- MACHINE FIDELITY: Faithful reproduction of the physical machine in the attached images: signature industrial blue welded steel chassis, sturdy metal transmission guard, electric drive motor with tensioner chain mechanism, electrical control panel featuring a Delta variable frequency drive (VFD), and feeding conveyor belt.
- SCENE & ACTION: Set in a spacious, spotless, well-lit modern textile and upholstery factory. An operator wearing industrial safety uniform and gloves safely places rolls/batts of compact raw polyester fiber onto the conveyor belt. At the rear output chute, an abundant cloud of ultra-soft, opened, voluminous white siliconized fiber fluffs out into a collection bin.
- LIGHTING & STYLE: Professional Hasselblad commercial studio lighting, natural reflections on the painted metal frame, clean floor, subtle motion blur on the conveyor belt, crisp metallic textures.
ANTI-AI RESTRICTIONS: NO cartoon or 3D render look, NO sci-fi futuristic aesthetics, NO distorted mechanical gears, NO surreal artifacts. Pure authentic industrial engineering catalog imagery."""
    },
    "2": {
        "id": "enchedora_travesseiros_operacao",
        "maquina": "Enchedora Automática de Travesseiros",
        "pasta": MAQUINAS_DIR / "02_Enchedora_de_Travesseiros",
        "referencias": [
            MAQUINAS_DIR / "02_Enchedora_de_Travesseiros" / "02_enchedora_visao_frontal.jpg",
            MAQUINAS_DIR / "02_Enchedora_de_Travesseiros" / "01_bocal_enchimento_travesseiro.jpg"
        ],
        "prompt": """Ultra-realistic industrial photography of this automatic Pneumatic Pillow and Cushion Filling Machine (Enchedora de Travesseiros) from 'JV Usinagem':
- MACHINE FIDELity: Based strictly on the attached photos: the heavy industrial steel structure, large pneumatic blower nozzle tube, high-pressure air ducts, and ergonomic operator workstation.
- SCENE & ACTION: Inside an organized, clean bedding manufacturing facility. A skilled factory worker smoothly inserts the open end of a white fabric pillowcase over the cylindrical stainless steel nozzle. The machine instantly blows an exact, uniform volume of fluffy, cloud-soft siliconized fiber into the pillow in just 3 seconds, resulting in a plump, perfectly filled premium pillow.
- LIGHTING & STYLE: Bright commercial editorial lighting, realistic depth of field, authentic industrial textures and brushed metal finishes.
ANTI-AI RESTRICTIONS: NO CGI plastic gloss, NO distorted human hands, NO floating surreal elements. Genuine high-end industrial machinery showcase."""
    },
    "3": {
        "id": "tesourinha_cortadeira_estopa",
        "maquina": "Tesourinha Cortadeira Contínua de Estopa",
        "pasta": MAQUINAS_DIR / "03_Tesourinha_Cortadeira_de_Estopa",
        "referencias": [
            MAQUINAS_DIR / "03_Tesourinha_Cortadeira_de_Estopa" / "01_tesourinha_estopa_visao_geral.jpg",
            MAQUINAS_DIR / "03_Tesourinha_Cortadeira_de_Estopa" / "02_tesourinha_estopa_mecanismo_corte.jpg"
        ],
        "prompt": """Crisp, high-definition industrial photograph of the Continuous Textile Waste and Tow Cutter Machine (Tesourinha Cortadeira de Estopa) from 'JV Usinagem':
- MACHINE DETAILS: Preserving the exact mechanical design from the reference images: robust steel cutting head, high-speed rotary cutting blades of hardened carbon steel, mechanical drive chains, and feeding grip rollers.
- SCENE & ACTION: Active industrial recycling and textile processing plant. Continuous feed of fabric scraps and textile remnants passing through the rotary blades, cleanly slicing them into uniform shreds of cleaning tow (estopa) with zero jamming. Small specks of natural cotton fiber airborne in the sunlight.
- LIGHTING & STYLE: Sharp, documentary industrial cinematography, shallow depth of field focusing on the razor-sharp cutting assembly and protective steel housing.
ANTI-AI RESTRICTIONS: NO cartoonish elements, NO fantasy mechanical parts, NO melting shapes. Genuine industrial equipment photography."""
    },
    "4": {
        "id": "projetos_especiais_engenharia",
        "maquina": "Projetos Especiais Sob Medida & Linha de Montagem",
        "pasta": MAQUINAS_DIR / "04_Projetos_Especiais_Sob_Encomenda",
        "referencias": [
            MAQUINAS_DIR / "04_Projetos_Especiais_Sob_Encomenda" / "01_projeto_maquina_sob_medida_1.jpg",
            MAQUINAS_DIR / "04_Projetos_Especiais_Sob_Encomenda" / "02_projeto_maquina_sob_medida_2.jpg"
        ],
        "prompt": """Authentic industrial documentary photograph inside the custom machine manufacturing workshop of 'JV Usinagem':
- SCENE & SUBJECT: Expert machinists and mechanical engineers building custom industrial automation equipment under bespoke commission. A heavy welded steel chassis being precision assembled, with custom motor drives, gearboxes, laser-cut steel plates, and precision electrical conduits.
- ATMOSPHERE: High-end engineering facility, blueprint schematics on a clipboard, clean industrial workshop with warm tungsten task lights and cool ambient daylight, capturing authentic craftsmanship and bespoke industrial engineering.
ANTI-AI RESTRICTIONS: NO futuristic lasers, NO sci-fi glow, NO distorted tools. Real-world mechanical engineering and fabrication shop."""
    }
}

def disparar_geracao_image2(opcao: str = "1", profile: str = "chatgpt-profile-conta-4"):
    try:
        from fast_image2 import generate_image_fast
    except ImportError:
        print("[!] Erro: fast_image2 não encontrado no caminho configurado.")
        return

    item = CATALOGO_PROMPTS_MAQUINAS.get(str(opcao), CATALOGO_PROMPTS_MAQUINAS["1"])
    nome_saida = f"image2_{item['id']}.png"
    destino = OUTPUT_DIR / nome_saida

    refs = [str(r.resolve()) for r in item["referencias"] if r.exists()]
    print("=" * 60)
    print(f"DISPARANDO IMAGE 2 PARA: {item['maquina']}")
    print(f"Imagens de Referência ({len(refs)}):")
    for r in refs:
        print(f"  -> {Path(r).name}")
    print(f"Destino: {destino}")
    print(f"Perfil ChatGPT: {profile}")
    print("=" * 60)

    res = generate_image_fast(
        prompt=item["prompt"],
        image_ref_path=refs,
        dest=destino,
        profile_dir=profile
    )
    print("\nResultado da Geração:", res)
    return res

if __name__ == "__main__":
    if len(sys.argv) > 1:
        op = sys.argv[1]
        prf = sys.argv[2] if len(sys.argv) > 2 else "chatgpt-profile-conta-4"
        disparar_geracao_image2(op, prf)
    else:
        print("=== GERADOR DE IMAGENS IMAGE 2: MÁQUINAS PAI JAMES (JV USINAGEM) ===")
        print("Opções:")
        for k, v in CATALOGO_PROMPTS_MAQUINAS.items():
            print(f"  [{k}] {v['maquina']}")
        print("\nComo usar:")
        print("python gerar_novas_imagens_maquinas_image2.py [opcao 1-4] [perfil_chatgpt]")
        print("Exemplo: python gerar_novas_imagens_maquinas_image2.py 1 chatgpt-profile-conta-4")
