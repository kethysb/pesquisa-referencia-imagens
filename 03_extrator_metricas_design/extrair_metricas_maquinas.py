"""
Extrator de Métricas e Design Tokens para as Máquinas Industriais do Pai James (JV Usinagem)
Analisa as fotos reais das 4 máquinas e extrai paleta cromática, proporções e tokens.
"""
import json
import sys
from pathlib import Path
from extrair_metricas import analisar_imagem

BASE_DIR = Path(__file__).resolve().parent.parent
MAQUINAS_DIR = BASE_DIR / "04_banco_referencias_catalogadas" / "maquinas_industriais"

MAQUINAS = {
    "01_desfibradeira": {
        "nome": "Desfibradeira de Fibra Siliconada",
        "foto_principal": MAQUINAS_DIR / "01_Desfibradeira_de_Fibra" / "01_visao_geral_completa.jpg",
        "subpasta": MAQUINAS_DIR / "01_Desfibradeira_de_Fibra"
    },
    "02_enchedora": {
        "nome": "Enchedora Automática de Travesseiros",
        "foto_principal": MAQUINAS_DIR / "02_Enchedora_de_Travesseiros" / "02_enchedora_visao_frontal.jpg",
        "subpasta": MAQUINAS_DIR / "02_Enchedora_de_Travesseiros"
    },
    "03_tesourinha": {
        "nome": "Tesourinha Cortadeira Contínua de Estopa",
        "foto_principal": MAQUINAS_DIR / "03_Tesourinha_Cortadeira_de_Estopa" / "01_tesourinha_estopa_visao_geral.jpg",
        "subpasta": MAQUINAS_DIR / "03_Tesourinha_Cortadeira_de_Estopa"
    },
    "04_especiais": {
        "nome": "Projetos Especiais Sob Medida",
        "foto_principal": MAQUINAS_DIR / "04_Projetos_Especiais_Sob_Encomenda" / "01_projeto_maquina_sob_medida_1.jpg",
        "subpasta": MAQUINAS_DIR / "04_Projetos_Especiais_Sob_Encomenda"
    }
}

def main():
    resultados = {}
    for chave, dados in MAQUINAS.items():
        foto = dados["foto_principal"]
        if foto.exists():
            tokens = analisar_imagem(str(foto))
            tokens["nome_maquina"] = dados["nome"]
            tokens["total_fotos_na_pasta"] = len(list(dados["subpasta"].glob("*.*")))
            resultados[chave] = tokens
            print(f"Processada: {dados['nome']}")
            print(f"  Formato: {tokens['formato_detectado']}")
            print(f"  Cores: {tokens['paleta_hex']['todas_cores_extraidas'][:4]}")

    out_file = MAQUINAS_DIR / "design_tokens_maquinas.json"
    out_file.write_text(json.dumps(resultados, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nSucesso! Arquivo salvo em: {out_file}")

if __name__ == "__main__":
    main()
