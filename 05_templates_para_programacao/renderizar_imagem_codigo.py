"""
Motor de Renderização de Imagem por Programação (Zero IA)
Usa Playwright para renderizar templates HTML/CSS puros em PNG de alta resolução.
Formato: 1080x1350 px (4:5) com escala 2x = 2160x2700 px (Ultra-HD).
"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

def renderizar_template(html_path: str, output_png: str):
    p_html = Path(html_path).resolve()
    p_out = Path(output_png).resolve()
    p_out.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        # 1080x1350 com device_scale_factor: 2 gera 2160x2700 nítido
        context = browser.new_context(
            viewport={"width": 1080, "height": 1350},
            device_scale_factor=2
        )
        page = context.new_page()
        page.goto(p_html.as_uri(), wait_until="networkidle")
        page.wait_for_timeout(1000)
        page.screenshot(path=str(p_out), full_page=False)
        browser.close()

    print(f"Sucesso! Imagem renderizada por código: {p_out.name} ({round(p_out.stat().st_size / 1024, 1)} KB)")

if __name__ == "__main__":
    html = sys.argv[1] if len(sys.argv) > 1 else "template_04_split_screen_comparativo.html"
    out = sys.argv[2] if len(sys.argv) > 2 else "render_saida_1080x1350.png"
    renderizar_template(html, out)