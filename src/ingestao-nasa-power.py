import os
import requests
import pandas as pd
from datetime import datetime

def obter_caminho_raiz():
    """
    Calcula dinamicamente a raiz do projeto com base na localização deste arquivo,
    garantindo que o script funcione independente de onde seja executado no terminal.
    """
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def inicializar_diretorios_destino():
    """
    Garante que a estrutura de pastas da camada Bronze exista localmente.
    """
    raiz = obter_caminho_raiz()
    pasta_bronze = os.path.join(raiz, "data", "01.bronze")
    os.makedirs(pasta_bronze, exist_ok=True)
    return pasta_bronze

def extrair_dados_nasa_power():
    """
    Consome a API do NASA POWER para coletar dados históricos de precipitação
    de todos os estados brasileiros com base em suas coordenadas centrais.
    """
    print("🚀 Iniciando extração de dados meteorológicos via API NASA POWER...")
    
    # Lista de coordenadas aproximadas por estado (UF, Latitude, Longitude)
    estados = [
        ('AC', -9.97, -67.81), ('AL', -9.66, -35.74), ('AP', 0.03, -51.05),
        ('AM', -3.12, -60.02), ('BA', -12.97, -38.50), ('CE', -3.73, -38.52),
        ('DF', -15.79, -47.88), ('ES', -20.32, -40.34), ('GO', -16.68, -49.25),
        ('MA', -2.53, -44.30), ('MT', -12.64, -55.42), ('MS', -20.44, -54.64),
        ('MG', -19.92, -43.94), ('PA', -1.45, -48.50), ('PB', -7.12, -34.88),
        ('PR', -25.42, -49.27), ('PE', -8.05, -34.88), ('PI', -5.09, -42.80),
        ('RJ', -22.90, -43.20), ('RN', -5.79, -35.20), ('RS', -30.03, -51.23),
        ('RO', -8.76, -63.90), ('RR', 2.82, -60.67), ('SC', -27.59, -48.54),
        ('SP', -23.55, -46.63), ('SE', -10.91, -37.07), ('TO', -10.18, -48.33)
    ]
    
    # Parâmetros temporais para a API (Exemplo: Histórico de 2000 a 2024)
    ano_inicio = "2000"
    ano_fim = datetime.now().strftime("%Y")
    
    dados_consolidados = []
    
    for uf, lat, lon in estados:
        print(f"🛰️ Requisitando dados para: {uf} (Lat: {lat}, Lon: {lon})...")
        
        # URL da API do NASA POWER (Mensal/Regional)
        url = (
            f"https://power.larc.nasa.gov/api/temporal/monthly/point?"
            f"parameters=PRECTOTCORR_SUM&community=AG&longitude={lon}&latitude={lat}"
            f"&start={ano_inicio}&end={ano_fim}&format=JSON"
        )
        
        try:
            resposta = requests.get(url, timeout=30)
            
            if resposta.status_code != 200:
                print(f"⚠️ Erro HTTP {resposta.status_code} para {uf}. Pulando...")
                continue
                
            dados_json = resposta.json()
            
            # Navega na estrutura do JSON retornado pela API da NASA
            precipitacao_mensal = dados_json['properties']['parameter']['PRECTOTCORR_SUM']
            
            for data_chave, valor in precipitacao_mensal.items():
                # Ignorar chaves de médias anuais fornecidas pela API (ex: '202013' ou '2020ANN')
                if len(data_chave) == 6 and not data_chave.endswith("13") and data_chave[:4].isdigit():
                    dados_consolidados.append({
                        'uf': uf,
                        'ano': int(data_chave[:4]),
                        'mes': int(data_chave[4:6]),
                        'chuva_mm': valor,
                        'id_carga': datetime.now().strftime('%Y%m%d_%H%M%S')
                    })
                    
        except Exception as e:
            print(f"❌ Falha de conexão ou processamento para o estado {uf}: {str(e)}")
            continue

    if not dados_consolidados:
        print("❌ Nenhum dado foi extraído com sucesso. O pipeline foi interrompido.")
        return None

    df_chuva = pd.DataFrame(dados_consolidados)
    return df_chuva

def salvar_na_camada_bronze(df):
    """
    Salva o DataFrame gerado em formato csv na camada Bronze.
    """
    if df is None or df.empty:
        return
        
    pasta_destino = inicializar_diretorios_destino()
    caminho_arquivo = os.path.join(pasta_destino, "nasa_power_chuva.csv")
    
    # Salva 
    df.to_csv(caminho_arquivo, index=False, sep=";", encoding="utf-8")
    print(f"✅ Camada Bronze Alimentada! Arquivo salvo com sucesso em:\n👉 {caminho_arquivo}")
    print(f"📊 Total de registros processados: {len(df)}")

if __name__ == "__main__":
    # Orquestração local do script
    df_resultado = extrair_dados_nasa_power()
    salvar_na_camada_bronze(df_resultado)