import os
import webbrowser

def criar_estrutura_medalhao():
    # Encontra dinamicamente a raiz do projeto 
    caminho_script = os.path.abspath(__file__) # Caminho completo do init_datalake.py
    pasta_src = os.path.dirname(caminho_script)  # Pasta 'src'
    raiz_projeto = os.path.dirname(pasta_src)    # Pasta raiz do projeto
    
    camadas = [
        os.path.join(raiz_projeto, "dados", "00.raw"),
        os.path.join(raiz_projeto, "dados", "01.bronze"),
        os.path.join(raiz_projeto, "dados", "02.prata"),
        os.path.join(raiz_projeto, "dados", "03.ouro")
    ]
    
    print("⚙️ Inicializando estrutura de pastas local (Arquitetura Medalhão)...")
    for camada in camadas:
        if not os.path.exists(camada):
            os.makedirs(camada)
            print(f"  [+] Pasta criada com sucesso: {camada}")
        else:
            print(f"  [~] Pasta já existente: {camada}")

def main():
    # 1. Garante a infraestrutura de diretórios local
    criar_estrutura_medalhao()
    
    # 2. Link oficial da pasta 00.raw compartilhada pelo grupo
    url_drive_raw = "https://drive.google.com/drive/folders/1Phi-hjTSQcWXwQfdL70W_4mGYYLWJ5xP?usp=sharing"
    
    print("\n-------------------------------------------------------------------------")
    print("📥 INSTRUÇÃO DE INGESTÃO DA CAMADA 00.RAW")
    print("-------------------------------------------------------------------------")
    print("Para executar o pipeline, os arquivos brutos originais devem ser inseridos")
    print("manualmente na pasta local recém-criada: 'dados/00.raw/'")
    print(f"\n🔗 Acesse a pasta do Google Drive do projeto para fazer o download:")
    print(f"👉 {url_drive_raw}")
    print("-------------------------------------------------------------------------")
    print("\n💡 Arquivos estáticos obrigatórios que você deve baixar e salvar em dados/00.raw/:")
    print("  - MAPBIOMAS_PASTURE-COL.1-BIOME_STATE_MUNICIPALITY.xlsx")
    print("  - MAPBIOMAS_BRAZIL_COL.10.1_DEFORESTATION.xlsx")
    print("  - MAPBIOMAS_COBERTURA_BRASIL_NIVEL1.xlsx")
    print("  - MAPBIOMAS_DESMATAMENTO_BIOMA.xlsx")
    print("  - SEEG_EMISSOES_BRASIL.xlsx")
    print("  - agriculture-crop-yield.csv")
    print("\n[➔] Tentando abrir o link da pasta automaticamente no seu navegador...")
    
    try:
        webbrowser.open(url_drive_raw)
        print("  [✔] Navegador inicializado. Baixe os arquivos e coloque-os em dados/00.raw/")
    except Exception:
        print("  [⚠️] Não foi possível abrir o navegador automaticamente. Copie e cole o link acima.")

if __name__ == "__main__":
    main()