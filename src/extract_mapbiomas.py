import os
import glob
import pandas as pd

def init_directory_structure(base_dir):
    """Garante que a estrutura de pastas do Data Lake exista localmente."""
    bronze_path = os.path.join(base_dir, "dados", "01.bronze")
    os.makedirs(bronze_path, exist_ok=True)
    return bronze_path

def extract_raw_sheets_to_bronze():
    # 1. Definir caminhos relativos robustos ancorados na posição deste arquivo script
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_script_dir, ".."))
    
    raw_dir = os.path.join(project_root, "dados", "00.raw")
    bronze_dir = os.path.join(project_root, "dados", "01.bronze")
    
    print(f"[*] Buscando planilhas originais em: {raw_dir}")
    excel_files = glob.glob(os.path.join(raw_dir, "*.xlsx"))
    
    if not excel_files:
        print(f"[!] Erro: Nenhum arquivo .xlsx encontrado na pasta {raw_dir}.")
        print("[!] Certifique-se de baixar e depositar os arquivos originais do MapBiomas nela.")
        return

    # 2. Mapeamento exato das abas alvo solicitadas
    target_sheets = {
        "COVERAGE_10.1", 
        "PASTURE_VIGOR", 
        "PASTURE_AGE", 
        "PASTURE_FIRSTTIME", 
        "PASTURE_LAST_TIME",  # Tratado dinamicamente caso na planilha esteja com ou sem underline
        "STATE_REGION_BIOME", 
        "WATERSHED", 
        "UC", 
        "IL"
    }

    # Loop por todas as planilhas encontradas na camada Raw
    for file_path in excel_files:
        file_name = os.path.basename(file_path)
        
        if file_name.startswith("~$"):
            continue
        
        print(f"\n[+] Lendo metadados do arquivo: {file_name}")

        try:
            # Carrega apenas os nomes das abas para evitar gargalo de memória RAM
            excel_obj = pd.ExcelFile(file_path, engine='openpyxl')
            available_sheets = excel_obj.sheet_names
            
            for sheet in available_sheets:
                # Normalização simples para evitar falhas com "PASTURE_LASTTIME" vs "PASTURE_LAST_TIME"
                sheet_normalized = sheet.strip().upper()
                
                # Verifica se a aba atual está na nossa lista de alvos
                is_target = False
                matched_name = sheet
                
                if sheet_normalized in [s.replace("_", "").upper() for s in target_sheets] or sheet_normalized in target_sheets:
                    is_target = True
                
                if is_target:
                    print(f"    -> Extraindo aba alvo encontrada: '{sheet}'")
                    
                    # Carrega os dados da aba específica
                    df = pd.read_excel(file_path, sheet_name=sheet, engine='openpyxl')
                    
                    # Nome do arquivo CSV de saída padronizado em caixa baixa
                    output_csv_name = f"{sheet.strip().lower()}.csv"
                    output_path = os.path.join(bronze_dir, output_csv_name)
                    
                    # Salvando na camada Bronze com codificação UTF-8 e separador padrão de vírgula (,)
                    df.to_csv(output_path, index=False, encoding='utf-8', sep=',')
                    print(f"    [✔] Salvo com sucesso em: dados/01.bronze/{output_csv_name}")
                    
        except Exception as e:
            print(f"[!] Erro ao processar o arquivo {file_name}: {str(e)}")

    print("\n[✔] Etapa de Extração Raw para Bronze concluída!")

if __name__ == "__main__":
    extract_raw_sheets_to_bronze()