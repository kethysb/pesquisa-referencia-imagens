"""
Extrator de Métricas de Design e Paleta de Cores para Programação Visual
Lê uma imagem de referência e gera um design_tokens.json pronto para ser
consumido por código (Playwright, Canvas, HTML/CSS).
"""
import sys
import json
from pathlib import Path
from PIL import Image

def rgb_to_hex(r, g, b) -> str:
    return f"#{r:02x}{g:02x}{b:02x}".upper()

def extrair_cores_dominantes(im: Image.Image, num_cores: int = 5) -> list[str]:
    # Reduz para velocidade mantendo proporções cromáticas
    pequena = im.convert("RGB").resize((150, 150))
    # Quantiza com octree para achar paleta representativa
    quant = pequena.quantize(colors=num_cores, method=Image.Quantize.MEDIANCUT)
    palette = quant.getpalette()[:num_cores * 3]
    cores = []
    for i in range(0, len(palette), 3):
        r, g, b = palette[i], palette[i+1], palette[i+2]
        cores.append(rgb_to_hex(r, g, b))
    return cores

def analisar_imagem(caminho_imagem: str, output_json: str = None) -> dict:
    p = Path(caminho_imagem)
    if not p.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_imagem}")

    with Image.open(p) as im:
        w, h = im.size
        razao = round(w / h, 3)

        if abs(razao - 0.8) < 0.05:
            formato = "Feed Vertical 4:5 (1080x1350)"
        elif abs(razao - 1.0) < 0.05:
            formato = "Quadrado 1:1 (1080x1080)"
        elif abs(razao - 0.562) < 0.05:
            formato = "Stories / Reels 9:16 (1080x1920)"
        else:
            formato = f"Customizado ({w}x{h} px, proporção {razao})"

        cores = extrair_cores_dominantes(im, 6)

    # Identifica potenciais papéis de cores
    fundo_estimado = cores[0]
    texto_estimado = cores[-1]
    acento_estimado = cores[1] if len(cores) > 1 else cores[0]

    tokens = {
        "arquivo_referencia": p.name,
        "dimensoes_originais": { "largura": w, "altura": h },
        "formato_detectado": formato,
        "safe_zone_instagram_feed_px": {
            "largura": min(w, 1080),
            "altura": min(w, 1080),
            "offset_topo_px": max(0, int((h - w) / 2)) if h > w else 0
        },
        "paleta_hex": {
            "fundo_canvas": fundo_estimado,
            "acento_principal": acento_estimado,
            "texto_dominante": texto_estimado,
            "todas_cores_extraidas": cores
        },
        "css_variables_snippet": (
            f":root {{\n"
            f"  --canvas-bg: {fundo_estimado};\n"
            f"  --brand-accent: {acento_estimado};\n"
            f"  --text-main: {texto_estimado};\n"
            f"}}"
        )
    }

    if output_json:
        out_path = Path(output_json)
        out_path.write_text(json.dumps(tokens, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Design tokens salvos com sucesso em: {out_path}")

    return tokens

if __name__ == "__main__":
    caminho = sys.argv[1] if len(sys.argv) > 1 else ""
    if caminho:
        saida = sys.argv[2] if len(sys.argv) > 2 else "design_tokens.json"
        res = analisar_imagem(caminho, saida)
        print(json.dumps(res, indent=2, ensure_ascii=False))
    else:
        print("Uso: python extrair_metricas.py <caminho_imagem> [caminho_saida_json]")