"""
Disparador Oficial do Image 2 (ChatGPT / DALL-E 3) - Conta Kevin (chatgpt-profile-conta-3)
Fidelidade mecânica absoluta às máquinas reais do pai James (JV Usinagem).
"""
import os
import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE_DIR = Path(__file__).resolve().parent
MAQUINAS_DIR = BASE_DIR / "04_banco_referencias_catalogadas" / "maquinas_industriais"
DEST_DIR = BASE_DIR / "imagens_geradas_image2_oficial"
DEST_DIR.mkdir(parents=True, exist_ok=True)
PROFILE_DIR = r"C:\Users\Kethely\Downloads\automações\automação image 2 chatgot\chatgpt-profile-conta-3"

PROMPTS_OFICIAIS_IMAGE2 = {
    "1": {
        "nome": "01_Desfibradeira_de_Fibra",
        "refs": [
            MAQUINAS_DIR / "01_Desfibradeira_de_Fibra" / "01_visao_geral_completa.jpg"
        ],
        "dest": DEST_DIR / "01_desfibradeira_nova_image2_oficial.png",
        "prompt": (
            "Gere uma nova foto realista desta EXATA máquina mostrada na imagem anexada da JV Usinagem: "
            "Mantenha rigorosamente o design real da máquina: chassi compacto pintado de azul cobalto com carenagem lateral branca, "
            "calha superior com fibra siliconada fofa e branca, painel elétrico azul com luz verde acesa e chaves pretas, "
            "motor elétrico industrial azul na lateral com polia e correia, montada exatamente no mesmo chão cerâmico da oficina mecânica. "
            "Mostre a máquina inteira em um ângulo limpo e nítido de catálogo. "
            "ZERO invenções: NÃO crie fábricas gigantes, NÃO crie esteiras futuristas gigantescas, NÃO invente peças mecânicas que não existem na foto. Apenas a máquina real na oficina mecânica."
        )
    },
    "2": {
        "nome": "02_Enchedora_de_Travesseiros",
        "refs": [
            MAQUINAS_DIR / "02_Enchedora_de_Travesseiros" / "02_enchedora_visao_frontal.jpg"
        ],
        "dest": DEST_DIR / "02_enchedora_nova_image2_oficial.png",
        "prompt": (
            "Gere uma nova foto realista desta EXATA máquina enchedora de travesseiros mostrada na imagem anexada: "
            "Reproduza com total fidelidade a estrutura em perfil tubular pintada de verde-petróleo, o motor elétrico industrial azul na lateral, "
            "o caracol soprador cilíndrico e a calha funil de alimentação de fibra, montada exatamente no mesmo piso cerâmico da oficina mecânica. "
            "Foto limpa e nítida para catálogo profissional, sem textos, sem números de telefone, sem banners. "
            "ZERO invenções: máquina real na oficina mecânica do meu pai, rigorosamente igual à foto de referência."
        )
    },
    "3": {
        "nome": "03_Tesourinha_Cortadeira_de_Estopa",
        "refs": [
            MAQUINAS_DIR / "04_Projetos_Especiais_Sob_Encomenda" / "02_projeto_maquina_sob_medida_2.jpg"
        ],
        "dest": DEST_DIR / "03_tesourinha_2rolos_nova_image2_oficial.png",
        "prompt": (
            "Gere uma nova fotografia realista desta EXATA máquina cortadeira tesourinha de 2 rolos da imagem anexada: "
            "Chassi robusto de chapa e viga em aço azul com o grande motor elétrico industrial azul com grade traseira e caixa de ligação lateral, "
            "cilindros cortadores e bocal de saída, montada exatamente no chão cerâmico da oficina mecânica da JV Usinagem. "
            "Foto limpa de catálogo em ângulo nítido, sem a elipse preta de texto. "
            "ZERO invenções: fidelidade mecânica total à foto de referência."
        )
    }
}

def executar_geracao(opcao: str = "2"):
    item = PROMPTS_OFICIAIS_IMAGE2.get(str(opcao))
    if not item:
        print(f"Opção {opcao} inválida.")
        return False
        
    print("=" * 60)
    print(f"INICIANDO IMAGE 2 PARA: {item['nome']}")
    print(f"Referência Real: {item['refs'][0]}")
    print(f"Destino Final: {item['dest']}")
    print("=" * 60)
    
    dest_path = item["dest"]
    ref_path = str(item["refs"][0])
    prompt_text = item["prompt"]
    
    saved = False
    
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            PROFILE_DIR,
            channel="chrome",
            headless=False,
            viewport={"width": 1280, "height": 900},
            args=["--disable-blink-features=AutomationControlled", "--no-first-run"]
        )
        page = browser.pages[0] if browser.pages else browser.new_page()
        
        # Monitora o tráfego de rede para interceptar o download do DALL-E / Estuary
        def on_response(response):
            nonlocal saved
            url = response.url
            if "backend-api/estuary/content" in url:
                try:
                    body = response.body()
                    # A imagem gerada pela OpenAI tem > 1 MB (as fotos de upload têm 557 KB ou menos)
                    if len(body) > 1000000:
                        dest_path.write_bytes(body)
                        saved = True
                        print(f"\n[SUCESSO IMAGE 2] Imagem capturada da rede! {round(len(body)/1024/1024, 2)} MB salvos em: {dest_path.name}")
                except Exception:
                    pass
                    
        page.on("response", on_response)
        
        print("Abrindo ChatGPT...")
        page.goto("https://chatgpt.com", wait_until="domcontentloaded")
        page.wait_for_timeout(3500)
        
        # 1. Clica no botão plus do composer
        print("Ativando ferramenta Criar Imagem...")
        plus_btn = page.locator("button[data-testid='composer-plus-btn']").first
        plus_btn.click()
        page.wait_for_timeout(1000)
        
        # 2. Clica em 'Criar imagem' no menu
        page.evaluate("""() => {
            const els = Array.from(document.querySelectorAll('*')).filter(el => el.innerText && el.innerText.trim() === 'Criar imagem');
            if (els.length > 0) {
                const target = els[0].closest('[role="menuitem"], [role="option"], button, div') || els[0];
                target.click();
            }
        }""")
        page.wait_for_timeout(1500)
        
        # 3. Anexa o arquivo de referência real
        print(f"Anexando foto real de referência: {Path(ref_path).name}...")
        inp = page.locator("input[type='file']").first
        if inp.count():
            inp.set_input_files([ref_path])
            page.wait_for_timeout(2500)
            
        # 4. Fecha popup de aviso de armazenamento se existir
        page.keyboard.press("Escape")
        page.wait_for_timeout(500)
        
        # 5. Digita o prompt no composer
        print("Digitando prompt de alta fidelidade...")
        composer = page.locator("#prompt-textarea, div.ProseMirror, [contenteditable='true']").last
        composer.click(force=True)
        page.wait_for_timeout(500)
        page.keyboard.insert_text(prompt_text)
        page.wait_for_timeout(1500)
        
        # 6. Clica no botão de enviar (seta azul)
        send_btn = page.locator("button[data-testid='send-button'], button[aria-label*='Enviar'], button[aria-label*='Send']").last
        print(f"Botão de envio ativo: {send_btn.is_enabled()}")
        send_btn.click()
        print("Prompt enviado! Aguardando o Image 2 renderizar a nova máquina...")
        
        # 7. Aguarda a renderização (até 180s)
        start_t = time.time()
        while time.time() - start_t < 180:
            if saved:
                break
            elapsed = int(time.time() - start_t)
            if elapsed % 10 == 0:
                print(f"[{elapsed}s] Renderizando...")
            page.wait_for_timeout(3000)
            
        page.screenshot(path=f"screenshot_resultado_maq_{opcao}.png")
        browser.close()
        
    if saved and dest_path.exists():
        print(f"\n[OK] PROCESSO CONCLUIDO COM SUCESSO! {dest_path.name} gerada e validada ({round(dest_path.stat().st_size/1024/1024, 2)} MB).")
        return True
    else:
        print(f"\n[FALHA] Falha ou timeout na geracao da maquina {opcao}.")
        return False

if __name__ == "__main__":
    op = sys.argv[1] if len(sys.argv) > 1 else "2"
    executar_geracao(op)
