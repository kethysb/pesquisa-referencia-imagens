"""
Gerador de Links Pré-Filtrados da Meta Ads Library
Garante que a pesquisa já abra com os filtros de imagem e escala ativos.
"""
import urllib.parse

def gerar_url_meta_ads(termo_busca: str) -> str:
    params = {
        "active_status": "active",
        "ad_type": "all",
        "country": "BR",
        "media_type": "image_and_meme",
        "q": termo_busca,
        "sort_data[mode]": "total_impressions"
    }
    base = "https://www.facebook.com/ads/library/?"
    return base + urllib.parse.urlencode(params)

if __name__ == "__main__":
    exemplos = [
        "advogado trabalhista bancario",
        "holding familiar",
        "advogado divida banco",
        "distrato imovel",
        "liminar plano de saude"
    ]
    print("=== URLs DA META ADS LIBRARY PRONTAS ===")
    for ex in exemplos:
        print(f"\n[ {ex.upper()} ]")
        print(gerar_url_meta_ads(ex))