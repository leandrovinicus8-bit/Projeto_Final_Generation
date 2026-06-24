# 📖 Dicionário de Dados — Inteligência Agroambiental
> **Projeto:** Inteligência Agroambiental - Agricultura de Precisão e Créditos de Carbono  
> **Versão:** 1.2 (Atualizado com a nova estrutura de pastas /dados)  
> **Escopo:** Mapeamento de Metadados de Ponta a Ponta (Raw → Bronze → Prata → Ouro)

---

## 🗄️ 00. Camada Raw (Dados Brutos)
Caminho físico: `dados/00.raw`
### 📄 [MAPBIOMAS_BRAZIL-COVERAGE_STATISTICS-COL.10.1-MUNICIPALITIES_STATES_BIOMES.xlsx](file:///G:/.shortcut-targets-by-id/1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI/PROJETO_FINAL_GENERATION/dados/00.raw/MAPBIOMAS_BRAZIL-COVERAGE_STATISTICS-COL.10.1-MUNICIPALITIES_STATES_BIOMES.xlsx)
*   **Caminho do arquivo:** `dados/00.raw/MAPBIOMAS_BRAZIL-COVERAGE_STATISTICS-COL.10.1-MUNICIPALITIES_STATES_BIOMES.xlsx`
*   **Tamanho:** `75.0496 MB`
*  **Abas**: READ_ME;  COVERAGE_10.1; PIVOT_COVERAGE; PIVOTCHART_COVERAGE; METADADOS; LEGEND_CODE
* Colunas da aba utilizada (COVERAGE_10.1):
  - country
  - biome
  - state
  - state acronym
  - municipality
  - class_id
  - class_level_0
  - class_level_1
  - class_level_2
  - class_level_3
  - class_level_4
A planilha também contém 01 coluna para cada ano de 1985 a 2024.
---

### 📄 [MAPBIOMAS_BRAZIL_COL.10.1_DEFORESTATION.xlsx](file:///G:/.shortcut-targets-by-id/1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI/PROJETO_FINAL_GENERATION/dados/00.raw/MAPBIOMAS_BRAZIL_COL.10.1_DEFORESTATION.xlsx)
*   **Caminho do arquivo:** `dados/00.raw/MAPBIOMAS_BRAZIL_COL.10.1_DEFORESTATION.xlsx`
*   **Tamanho:** `8.0908 MB`
*     **Abas**: READ_ME; STATE_REGION_BIOME; PT_STATE_REGION_BIOME; WATERSHED; PT_WATERSHED; UC; PT_UC; IL; PT_IL; METADADOS
* **Colunas por abas utilizadas:** STATE_REGION_BIOME:  
- country
  - biome
  - region
  - state
  - class
  - deforestation_class
  - class_level_0
  - class_level_1
  - class_level_2
  - class_level_3
  - class_level_4

**WATERSHED: **
- country
  - biome
  - region
  - watershed_lv1
  - watershed_lv2
  - watershed_lv3
  - class
  - deforestation_class
  - class_level_0
  - class_level_1
  - class_level_2
  - class_level_3
  - class_level_4
  
**UC:** 
- country
  - biome
  - region
  - watershed_lv1
  - watershed_lv2
  - watershed_lv3
  - class
  - deforestation_class
  - class_level_0
  - class_level_1
  - class_level_2
  - class_level_3
  - class_level_4

**IL:**
- country
  - biome
  - region
  - il_name
  - class
  - deforestation_class
  - class_level_0
  - class_level_1
  - class_level_2
  - class_level_3
  - class_level_4

As planilha também contém 01 coluna para cada ano de 1985 a 2024.

---
### 📄 [MAPBIOMAS_PASTURE-COL.1-BIOME_STATE_MUNICIPALITY]("G:\.shortcut-targets-by-id\1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI\PROJETO_FINAL_GENERATION\dados\00.raw\MAPBIOMAS_PASTURE-COL.1-BIOME_STATE_MUNICIPALITY.xlsx")
*   **Caminho do arquivo:** `dados/00.raw/MAPBIOMAS_BRAZIL-COVERAGE_STATISTICS-COL.10.1-MUNICIPALITIES_STATES_BIOMES.xlsx`
*  **Tamanho:** `75.0496 MB`
*  Abas: PASTURE_VIGOR; PASTURE_AGE; PASTURE_FIRSTTIME; PASTURE_LASTTIME; PIVOT_VIGOR; PIVOT_AGE; PIVOT_FIRSTTIME; PIVOT_LASTTIME; METADATA; LEGEND_CODE; READ_ME.

* **Colunas por abas Utilizadas:** PASTURE_VIGOR:
  - ID
  - territory_level_1_1
  - territory_level_2_1
  - territory_level_2_2
  - territory_level_3_2
  - feature_id_1
  - feature_id_2
  - class
  - class_level_0
  - class_level_1
  - class_level_2
  - 01 coluna por ano de 2000 a 2024
  
 **PASTURE AGE:**
 - ID
  - territory_level_1_1
  - territory_level_2_1
  - territory_level_2_2
  - territory_level_3_2
  - feature_id_1
  - feature_id_2
  - pasture_age_in_years
  - 01 coluna por ano de 1985 a 2024
  
 **PASTURE_FIRSTTIME:**
  - ID
  - territory_level_1_1
  - territory_level_2_1
  - territory_level_2_2
  - territory_level_3_2
  - feature_id_1
  - feature_id_2
  - pasture_first_time
  - y2023
  
 **PASTURE_LASTTIME:**
  - ID
  - territory_level_1_1
  - territory_level_2_1
  - territory_level_2_2
  - territory_level_3_2
  - feature_id_1
  - feature_id_2
  - pasture_last_time
  - y2023
   

---


### 📄 [crop_yield.csv](file:///G:/.shortcut-targets-by-id/1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI/PROJETO_FINAL_GENERATION/dados/00.raw/crop_yield.csv)
*   **Caminho do arquivo:** `dados/00.raw/crop_yield.csv`
*   **Tamanho:** `89.0808 MB`
*   **Colunas:** `10` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `Region` | *Texto* | Região geográfica original (Kaggle) | Texto | `West` |
| `Soil_Type` | *Texto* | Tipo físico do solo | Texto (ex: Sandy, Clay) | `Sandy` |
| `Crop` | *Texto* | Cultura agrícola semeada | Texto (ex: Rice, Cotton) | `Cotton` |
| `Rainfall_mm` | *Decimal* | Precipitação acumulada registrada | Milímetros (mm) | `897.0772391101236` |
| `Temperature_Celsius` | *Decimal* | Temperatura média do ar registrada | Graus Celsius (°C) | `27.676966373377603` |
| `Fertilizer_Used` | *Booleano* | Indica se houve aplicação de fertilizante químico | Booleano (True/False) | `False` |
| `Irrigation_Used` | *Booleano* | Indica se houve uso de irrigação artificial | Booleano (True/False) | `True` |
| `Weather_Condition` | *Texto* | Condição climática predominante | Texto (ex: Sunny, Rainy) | `Cloudy` |
| `Days_to_Harvest` | *Inteiro* | Número de dias necessários para a colheita | Dias | `122` |
| `Yield_tons_per_hectare` | *Decimal* | Produtividade da cultura por hectare | Toneladas por Hectare (t/ha) | `6.555816258223593` |

---

### 📄 [seeg_all.csv](file:///G:/.shortcut-targets-by-id/1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI/PROJETO_FINAL_GENERATION/dados/00.raw/seeg_all.csv)
*   **Caminho do arquivo:** `dados/00.raw/seeg_all.csv`
*   **Tamanho:** `152.1636 MB`
*   **Colunas:** `46` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `Emissao_Remocao_Bunker` | *Decimal* | Emissões de Gases de Efeito Estufa (GEE) | Toneladas de CO2e ou MtCO2e | `Emissão` |
| `Gas` | *Texto* | Gás de efeito estufa mensurado | Texto | `CH4 (t)` |
| `Setor_de_emissao` | *Decimal* | Emissões de Gases de Efeito Estufa (GEE) | Toneladas de CO2e ou MtCO2e | `Agropecuária` |
| `Categoria_emissora` | *Texto* | Metadado da tabela | Texto/Valor | `Cultivo de arroz` |
| `Sub_categoria_emissora` | *Texto* | Metadado da tabela | Texto/Valor | `Cultivo em sistema irrigado inundado` |
| `Produto_ou_sistema` | *Texto* | Metadado da tabela | Texto/Valor | `Arroz` |
| `Detalhamento` | *Texto* | Metadado da tabela | Texto/Valor | `Vegetal` |
| `Recorte` | *Texto* | Metadado da tabela | Texto/Valor | `Diretas` |
| `Atividade_geral` | *Texto* | Metadado da tabela | Texto/Valor | `Agricultura` |
| `Estado` | *Texto* | Nome do estado brasileiro por extenso | Texto | `Acre` |
| `Bioma` | *Texto* | Nome do bioma brasileiro por extenso | Texto | `Amazônia` |
| `ano_1990` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_1991` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_1992` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_1993` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_1994` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_1995` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_1996` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_1997` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_1998` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_1999` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_2000` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_2001` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_2002` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_2003` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_2004` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_2005` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_2006` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_2007` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_2008` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_2009` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_2010` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_2011` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_2012` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_2013` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_2014` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_2015` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_2016` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_2017` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_2018` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_2019` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_2020` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_2021` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_2022` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_2023` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `ano_2024` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |

---




## 🥉 01. Camada Bronze (Dados Ingeridos)
Caminho físico: `dados/01.bronze`
### 📄 [atividade-geral.csv]("G:\.shortcut-targets-by-id\1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI\PROJETO_FINAL_GENERATION\dados\01.bronze\SEEG\atividade-geral.csv")
*   **Caminho do arquivo:** `dados/01.bronze/SEEG/Atividade Geral.csv`
*   **Tamanho:** `0.0076 MB`
*   **Colunas:** `25` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `Categoria` | *Texto* | Metadado da tabela | Texto/Valor | `Pecuária` |
| `2000` | *Texto* | Metadado da tabela | Texto/Valor | `1691553177.3509192` |
| `2001` | *Texto* | Metadado da tabela | Texto/Valor | `1777678182.4623797` |
| `2002` | *Texto* | Metadado da tabela | Texto/Valor | `1897031593.487495` |
| `2003` | *Texto* | Metadado da tabela | Texto/Valor | `2359737258.7371345` |
| `2004` | *Texto* | Metadado da tabela | Texto/Valor | `2260622245.24656` |
| `2005` | *Texto* | Metadado da tabela | Texto/Valor | `1986970974.4059849` |
| `2006` | *Texto* | Metadado da tabela | Texto/Valor | `1685050477.819076` |
| `2007` | *Texto* | Metadado da tabela | Texto/Valor | `1447827929.3580272` |
| `2008` | *Texto* | Metadado da tabela | Texto/Valor | `1407058717.5778615` |
| `2009` | *Texto* | Metadado da tabela | Texto/Valor | `1068266078.3650266` |
| `2010` | *Texto* | Metadado da tabela | Texto/Valor | `1014051383.6719432` |
| `2011` | *Texto* | Metadado da tabela | Texto/Valor | `1048956547.660112` |
| `2012` | *Texto* | Metadado da tabela | Texto/Valor | `1045267803.5748768` |
| `2013` | *Texto* | Metadado da tabela | Texto/Valor | `1142167232.5064209` |
| `2014` | *Texto* | Metadado da tabela | Texto/Valor | `1110080556.0407238` |
| `2015` | *Texto* | Metadado da tabela | Texto/Valor | `1239310554.9882815` |
| `2016` | *Texto* | Metadado da tabela | Texto/Valor | `1289799340.30047` |
| `2017` | *Texto* | Metadado da tabela | Texto/Valor | `1139952015.1197133` |
| `2018` | *Texto* | Metadado da tabela | Texto/Valor | `1165734796.439089` |
| `2019` | *Texto* | Metadado da tabela | Texto/Valor | `1489382591.2477224` |
| `2020` | *Texto* | Metadado da tabela | Texto/Valor | `1455270122.22062` |
| `2021` | *Texto* | Metadado da tabela | Texto/Valor | `1596063945.1389985` |
| `2022` | *Texto* | Metadado da tabela | Texto/Valor | `1689088056.5233705` |
| `2023` | *Texto* | Metadado da tabela | Texto/Valor | `1469682136.0537794` |

---

### 📄 [emissao-total .csv]("G:\.shortcut-targets-by-id\1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI\PROJETO_FINAL_GENERATION\dados\01.bronze\SEEG\emissao-total.csv")
*   **Caminho do arquivo:** `dados/01.bronze/SEEG/Emissao total .csv`
*   **Tamanho:** `0.0026 MB`
*   **Colunas:** `25` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `Categoria` | *Texto* | Metadado da tabela | Texto/Valor | `Mudança de Uso da Terra e Floresta` |
| `2000` | *Texto* | Metadado da tabela | Texto/Valor | `1679274233.979499` |
| `2001` | *Texto* | Metadado da tabela | Texto/Valor | `1733470176.7053213` |
| `2002` | *Texto* | Metadado da tabela | Texto/Valor | `1835646220.380513` |
| `2003` | *Texto* | Metadado da tabela | Texto/Valor | `2412341729.4628606` |
| `2004` | *Texto* | Metadado da tabela | Texto/Valor | `2299484313.6631064` |
| `2005` | *Texto* | Metadado da tabela | Texto/Valor | `1895523972.3296475` |
| `2006` | *Texto* | Metadado da tabela | Texto/Valor | `1522919491.3711205` |
| `2007` | *Texto* | Metadado da tabela | Texto/Valor | `1264276401.0057862` |
| `2008` | *Texto* | Metadado da tabela | Texto/Valor | `1245079592.6574922` |
| `2009` | *Texto* | Metadado da tabela | Texto/Valor | `870638876.5390296` |
| `2010` | *Texto* | Metadado da tabela | Texto/Valor | `814182696.5704651` |
| `2011` | *Texto* | Metadado da tabela | Texto/Valor | `836065183.068563` |
| `2012` | *Texto* | Metadado da tabela | Texto/Valor | `887258604.5334427` |
| `2013` | *Texto* | Metadado da tabela | Texto/Valor | `1023029890.1622096` |
| `2014` | *Texto* | Metadado da tabela | Texto/Valor | `945751813.4981152` |
| `2015` | *Texto* | Metadado da tabela | Texto/Valor | `1076244554.5172064` |
| `2016` | *Texto* | Metadado da tabela | Texto/Valor | `1062669978.9768652` |
| `2017` | *Texto* | Metadado da tabela | Texto/Valor | `937750098.4270746` |
| `2018` | *Texto* | Metadado da tabela | Texto/Valor | `956538250.038538` |
| `2019` | *Texto* | Metadado da tabela | Texto/Valor | `1352941436.0899825` |
| `2020` | *Texto* | Metadado da tabela | Texto/Valor | `1332201957.9930034` |
| `2021` | *Texto* | Metadado da tabela | Texto/Valor | `1454084460.817088` |
| `2022` | *Texto* | Metadado da tabela | Texto/Valor | `1521705792.369775` |
| `2023` | *Texto* | Metadado da tabela | Texto/Valor | `1340945334.3477104` |

---

### 📄 [emissao-total-por-categoria.csv]("G:\.shortcut-targets-by-id\1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI\PROJETO_FINAL_GENERATION\dados\01.bronze\SEEG\emissao-total-por-categoria.csv")
*   **Caminho do arquivo:** `dados/01.bronze/SEEG/Emissao total por categoria.csv`
*   **Tamanho:** `0.0131 MB`
*   **Colunas:** `25` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `Categoria` | *Texto* | Metadado da tabela | Texto/Valor | `Alterações de uso da terra` |
| `2000` | *Texto* | Metadado da tabela | Texto/Valor | `1574784775.0` |
| `2001` | *Texto* | Metadado da tabela | Texto/Valor | `1625833019.0` |
| `2002` | *Texto* | Metadado da tabela | Texto/Valor | `1722807660.0` |
| `2003` | *Texto* | Metadado da tabela | Texto/Valor | `2265640353.0` |
| `2004` | *Texto* | Metadado da tabela | Texto/Valor | `2156464394.0` |
| `2005` | *Texto* | Metadado da tabela | Texto/Valor | `1781228612.0` |
| `2006` | *Texto* | Metadado da tabela | Texto/Valor | `1429910453.0` |
| `2007` | *Texto* | Metadado da tabela | Texto/Valor | `1186821491.0` |
| `2008` | *Texto* | Metadado da tabela | Texto/Valor | `1166984932.0` |
| `2009` | *Texto* | Metadado da tabela | Texto/Valor | `814000727.0` |
| `2010` | *Texto* | Metadado da tabela | Texto/Valor | `760176211.0` |
| `2011` | *Texto* | Metadado da tabela | Texto/Valor | `780662555.0` |
| `2012` | *Texto* | Metadado da tabela | Texto/Valor | `826579922.0` |
| `2013` | *Texto* | Metadado da tabela | Texto/Valor | `955922586.0` |
| `2014` | *Texto* | Metadado da tabela | Texto/Valor | `884457435.0` |
| `2015` | *Texto* | Metadado da tabela | Texto/Valor | `1007963016.0` |
| `2016` | *Texto* | Metadado da tabela | Texto/Valor | `996868238.0` |
| `2017` | *Texto* | Metadado da tabela | Texto/Valor | `878199782.0` |
| `2018` | *Texto* | Metadado da tabela | Texto/Valor | `895320133.0` |
| `2019` | *Texto* | Metadado da tabela | Texto/Valor | `1265699647.0` |
| `2020` | *Texto* | Metadado da tabela | Texto/Valor | `1243411953.0` |
| `2021` | *Texto* | Metadado da tabela | Texto/Valor | `1357795937.0` |
| `2022` | *Texto* | Metadado da tabela | Texto/Valor | `1419078207.0` |
| `2023` | *Texto* | Metadado da tabela | Texto/Valor | `1243321732.0` |

---

### 📄 [emissoes-totais-por-estado.csv]("G:\.shortcut-targets-by-id\1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI\PROJETO_FINAL_GENERATION\dados\01.bronze\SEEG\emissoes-totais-por-estado.csv")
*   **Caminho do arquivo:** `dados/01.bronze/SEEG/Emissoes totais por estado.csv`
*   **Tamanho:** `0.0135 MB`
*   **Colunas:** `25` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `Categoria` | *Texto* | Metadado da tabela | Texto/Valor | `Pará` |
| `2000` | *Texto* | Metadado da tabela | Texto/Valor | `430779837.6059282` |
| `2001` | *Texto* | Metadado da tabela | Texto/Valor | `562937836.0818092` |
| `2002` | *Texto* | Metadado da tabela | Texto/Valor | `505312836.505726` |
| `2003` | *Texto* | Metadado da tabela | Texto/Valor | `628868578.7904272` |
| `2004` | *Texto* | Metadado da tabela | Texto/Valor | `698109490.228883` |
| `2005` | *Texto* | Metadado da tabela | Texto/Valor | `566780987.4613879` |
| `2006` | *Texto* | Metadado da tabela | Texto/Valor | `540880460.4392514` |
| `2007` | *Texto* | Metadado da tabela | Texto/Valor | `453708217.2775004` |
| `2008` | *Texto* | Metadado da tabela | Texto/Valor | `467512679.6082389` |
| `2009` | *Texto* | Metadado da tabela | Texto/Valor | `320352699.03969634` |
| `2010` | *Texto* | Metadado da tabela | Texto/Valor | `277704501.4118104` |
| `2011` | *Texto* | Metadado da tabela | Texto/Valor | `252571078.62459537` |
| `2012` | *Texto* | Metadado da tabela | Texto/Valor | `267837971.86784917` |
| `2013` | *Texto* | Metadado da tabela | Texto/Valor | `301883040.9167922` |
| `2014` | *Texto* | Metadado da tabela | Texto/Valor | `295574049.6180336` |
| `2015` | *Texto* | Metadado da tabela | Texto/Valor | `340747505.85094935` |
| `2016` | *Texto* | Metadado da tabela | Texto/Valor | `375473771.94873375` |
| `2017` | *Texto* | Metadado da tabela | Texto/Valor | `307986024.2665722` |
| `2018` | *Texto* | Metadado da tabela | Texto/Valor | `336714836.2548778` |
| `2019` | *Texto* | Metadado da tabela | Texto/Valor | `467170466.6882832` |
| `2020` | *Texto* | Metadado da tabela | Texto/Valor | `478669258.2026661` |
| `2021` | *Texto* | Metadado da tabela | Texto/Valor | `537665779.1164702` |
| `2022` | *Texto* | Metadado da tabela | Texto/Valor | `490690742.5228792` |
| `2023` | *Texto* | Metadado da tabela | Texto/Valor | `436477188.4559962` |

---

### 📄 [emissao_total_por_bioma.csv]("G:\.shortcut-targets-by-id\1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI\PROJETO_FINAL_GENERATION\dados\01.bronze\SEEG\emissao-total-por-bioma.csv")
*   **Caminho do arquivo:** `dados/01.bronze/SEEG/Emissão Total por Bioma.csv`
*   **Tamanho:** `0.0035 MB`
*   **Colunas:** `25` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `Categoria` | *Texto* | Metadado da tabela | Texto/Valor | `Amazônia` |
| `2000` | *Texto* | Metadado da tabela | Texto/Valor | `1225801931.033635` |
| `2001` | *Texto* | Metadado da tabela | Texto/Valor | `1361451567.610745` |
| `2002` | *Texto* | Metadado da tabela | Texto/Valor | `1469713493.810548` |
| `2003` | *Texto* | Metadado da tabela | Texto/Valor | `1987087221.516172` |
| `2004` | *Texto* | Metadado da tabela | Texto/Valor | `1874831336.7388284` |
| `2005` | *Texto* | Metadado da tabela | Texto/Valor | `1579689355.598308` |
| `2006` | *Texto* | Metadado da tabela | Texto/Valor | `1261878153.353916` |
| `2007` | *Texto* | Metadado da tabela | Texto/Valor | `1067074500.9552344` |
| `2008` | *Texto* | Metadado da tabela | Texto/Valor | `1026396945.4007968` |
| `2009` | *Texto* | Metadado da tabela | Texto/Valor | `696092821.9577153` |
| `2010` | *Texto* | Metadado da tabela | Texto/Valor | `655519681.170969` |
| `2011` | *Texto* | Metadado da tabela | Texto/Valor | `688645880.6282842` |
| `2012` | *Texto* | Metadado da tabela | Texto/Valor | `677677380.6328534` |
| `2013` | *Texto* | Metadado da tabela | Texto/Valor | `769831647.3774413` |
| `2014` | *Texto* | Metadado da tabela | Texto/Valor | `760127851.8181676` |
| `2015` | *Texto* | Metadado da tabela | Texto/Valor | `896014024.34978` |
| `2016` | *Texto* | Metadado da tabela | Texto/Valor | `940576570.1336358` |
| `2017` | *Texto* | Metadado da tabela | Texto/Valor | `810292318.2407348` |
| `2018` | *Texto* | Metadado da tabela | Texto/Valor | `837368300.2384193` |
| `2019` | *Texto* | Metadado da tabela | Texto/Valor | `1179134538.2555127` |
| `2020` | *Texto* | Metadado da tabela | Texto/Valor | `1147351941.0876198` |
| `2021` | *Texto* | Metadado da tabela | Texto/Valor | `1280457201.443472` |
| `2022` | *Texto* | Metadado da tabela | Texto/Valor | `1351695033.5205095` |
| `2023` | *Texto* | Metadado da tabela | Texto/Valor | `1123395926.7925224` |

---

### 📄 [bronze_crop_yield.csv]("G:\.shortcut-targets-by-id\1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI\PROJETO_FINAL_GENERATION\dados\01.bronze\kaggle_yield\bronze_crop_yield.csv")
*   **Caminho do arquivo:** `dados/01.bronze/kaggle_yield/crop_yield_bronze.csv`
*   **Tamanho:** `80.3031 MB`
*   **Colunas:** `8` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `Region` | *Texto* | Região geográfica original (Kaggle) | Texto | `West` |
| `Crop` | *Texto* | Cultura agrícola semeada | Texto (ex: Rice, Cotton) | `Cotton` |
| `Soil_Type` | *Texto* | Tipo físico do solo | Texto (ex: Sandy, Clay) | `Sandy` |
| `Fertilizer_Used` | *Booleano* | Indica se houve aplicação de fertilizante químico | Booleano (True/False) | `False` |
| `Irrigation_Used` | *Booleano* | Indica se houve uso de irrigação artificial | Booleano (True/False) | `True` |
| `Rainfall_mm` | *Decimal* | Precipitação acumulada registrada | Milímetros (mm) | `897.0772391101236` |
| `Temperature_Celsius` | *Decimal* | Temperatura média do ar registrada | Graus Celsius (°C) | `27.676966373377603` |
| `Yield_tons_per_hectare` | *Decimal* | Produtividade da cultura por hectare | Toneladas por Hectare (t/ha) | `6.555816258223593` |

---
### 📄 [mapbiomas-desmatamento-estado-bioma.csv]("G:\.shortcut-targets-by-id\1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI\PROJETO_FINAL_GENERATION\dados\01.bronze\mapbiomas\mapbiomas-desmatamento-estado-bioma.csv")
*   **Caminho do arquivo:** `dados/01.bronze/mapbiomas/MAPBIOMAS_DEFORESTATION_STATE.REGION.BIOME.csv`
*   **Tamanho:** `0.3708 MB`
*   **Colunas:** `51` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `country` | *Texto* | Nome do país de referência (Inglês) | Texto | `Brasil` |
| `biome` | *Texto* | Metadado da tabela | Texto/Valor | `Amazônia` |
| `region` | *Texto* | Metadado da tabela | Texto/Valor | `Centro-oeste` |
| `state` | *Texto* | Metadado da tabela | Texto/Valor | `Mato Grosso` |
| `class` | *Texto* | Metadado da tabela | Texto/Valor | `3` |
| `deforestation_class` | *Texto* | Metadado da tabela | Texto/Valor | `Supressão Veg. Primária` |
| `class_level_0` | *Texto* | Metadado da tabela | Texto/Valor | `Natural` |
| `class_level_1` | *Texto* | Metadado da tabela | Texto/Valor | `1. Forest` |
| `class_level_2` | *Texto* | Metadado da tabela | Texto/Valor | `1.1. Forest Formation` |
| `class_level_3` | *Texto* | Metadado da tabela | Texto/Valor | `1.1. Forest Formation` |
| `class_level_4` | *Texto* | Metadado da tabela | Texto/Valor | `1.1. Forest Formation` |
| `y1985` | *Decimal* | Área de desmatamento no ano de 1985 | Hectares (ha) | `0` |
| `y1986` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `0` |
| `y1987` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `325568,172608027` |
| `y1988` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `310592,805813161` |
| `y1989` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `372290,951265271` |
| `y1990` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `265948,512213476` |
| `y1991` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `286042,82843443` |
| `y1992` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `417353,935642366` |
| `y1993` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `377958,612043328` |
| `y1994` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `564212,911118017` |
| `y1995` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `715870,30206625` |
| `y1996` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `588530,398677113` |
| `y1997` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `584539,169985486` |
| `y1998` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `562332,988025842` |
| `y1999` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `662393,674668187` |
| `y2000` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `487831,630522736` |
| `y2001` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `530009,980397711` |
| `y2002` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `720960,627225039` |
| `y2003` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `1051565,09154262` |
| `y2004` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `934645,880426251` |
| `y2005` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `685081,993214712` |
| `y2006` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `389634,175212902` |
| `y2007` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `259340,261450959` |
| `y2008` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `264929,199917418` |
| `y2009` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `96530,8045385864` |
| `y2010` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `90681,6575357056` |
| `y2011` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `162723,448724212` |
| `y2012` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `110133,95749361` |
| `y2013` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `155101,678256597` |
| `y2014` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `130569,364991503` |
| `y2015` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `158159,417861359` |
| `y2016` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `126097,498134631` |
| `y2017` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `132447,413824817` |
| `y2018` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `150341,665368463` |
| `y2019` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `219637,976869951` |
| `y2020` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `223786,793657076` |
| `y2021` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `211566,10998315` |
| `y2022` | *Inteiro/Decimal* | Ano de referência histórica | Ano (AAAA) | `251340,113711922` |
| `y2023` | *Decimal* | Área de desmatamento no ano de 2023 | Hectares (ha) | `207782,826294171` |
| `y2024` | *Decimal* | Área de desmatamento no ano de 2024 | Hectares (ha) | `138643,653729596` |

---

### 📄 [mapbiomas-uso-e-cobertura-solo.csv]("G:\.shortcut-targets-by-id\1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI\PROJETO_FINAL_GENERATION\dados\01.bronze\mapbiomas\mapbiomas-uso-e-cobertura-solo.csv")
*   **Caminho do arquivo:** `dados/01.bronze/mapbiomas/MAPBIOMAS_USOECOBERTURASOLO_coverage10.1.csv`
*   **Tamanho:** `0.0055 MB`
*   **Colunas:** `8` 
- Dados
- 1. Forest
- 2. Non Forest Natural Formation
- 3. Farming
- 4. Non vegetated area
- 5. Water and Marine Environment
- 6. Not Observed
- 7. Total Resultado

---


### 📄 [mapbiomas-pastagem.csv]("G:\.shortcut-targets-by-id\1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI\PROJETO_FINAL_GENERATION\dados\01.bronze\mapbiomas\mapbiomas-pastagem.csv")
*   **Caminho do arquivo:** `dados/01.bronze/mapbiomas/prata_pastagem.csv`
*   **Tamanho:** `5.8234 MB`
*   **Colunas:** `20` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `nome_pais` | *Texto* | Nome do país de referência | Texto | `Brasil` |
| `nome_bioma` | *Texto* | Nome do bioma brasileiro por extenso | Texto | `Amazônia` |
| `nome_estado` | *Texto* | Nome do estado brasileiro por extenso | Texto | `Acre` |
| `sigla_estado` | *Texto* | Sigla da Unidade Federativa | Texto (2 caract.) | `AC` |
| `id_recurso_bioma` | *Inteiro* | Código identificador do recurso de bioma | Inteiro | `1` |
| `id_recurso_estado` | *Inteiro* | Código identificador do recurso de estado | Inteiro | `1` |
| `idade_pastagem_anos` | *Decimal* | Idade da pastagem desde a primeira detecção de uso | Anos | `1.0` |
| `id_carga` | *Texto* | Identificador único da carga de dados | Texto | `20260617_192047` |
| `data_ingestao` | *Texto* | Data da ingestão do dado bruto | Texto (AAAA-MM-DD) | `2026-06-17` |
| `ano` | *Inteiro* | Ano civil de referência | Ano (AAAA) | `1985.0` |
| `area_ha` | *Decimal* | Área territorial sob a respectiva classe | Hectares (ha) | `402816.2735568082` |
| `data_processamento` | *Texto* | Data do processamento para a camada atual | Texto (AAAA-MM-DD) | `2026-06-17` |
| `origem_dados` | *Texto* | Identificador da tabela/fato de origem | Texto | `fato_pastagem_idade` |
| `ano_primeira_deteccao` | *Inteiro* | Ano em que a pastagem foi detectada pela primeira vez | Ano (AAAA) | `` |
| `area_ha_consolidada_2023` | *Decimal* | Área consolidada em pastagem no ano de 2023 | Hectares (ha) | `` |
| `ano_ultima_deteccao` | *Inteiro* | Ano em que a pastagem foi detectada pela última vez | Ano (AAAA) | `` |
| `classe_id` | *Texto* | Metadado da tabela | Texto/Valor | `` |
| `classe_nivel_0` | *Texto* | Origem da cobertura (Natural ou Antrópico) | Texto | `` |
| `classe_nivel_1` | *Texto* | Classe de uso e cobertura da terra Nível 1 | Texto | `` |
| `classe_nivel_2` | *Texto* | Classe de uso e cobertura da terra Nível 2 | Texto | `` |

---

## 🥈 02. Camada Prata (Dados Tratados)
Caminho físico: `dados/02.prata`

### 📄 [SEEG Dados Arrumados.xlsx](file:///G:/.shortcut-targets-by-id/1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI/PROJETO_FINAL_GENERATION/dados/02.prata/SEEG/Limpeza_Padrao_Prata/SEEG Dados Arrumados.xlsx)
*   **Caminho do arquivo:** `dados/02.prata/SEEG/Limpeza_Padrao_Prata/SEEG Dados Arrumados.xlsx`
*   **Tamanho:** `0.0693 MB`
*   **Colunas:** `3` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `Região` | *Texto* | Nome da região geográfica | Texto | `Norte` |
| `Ano` | *Inteiro* | Ano civil de referência | Ano (AAAA) | `2000` |
| `Emissão (Mt)` | *Decimal* | Volume de emissões acumulado | Megatoneladas (MtCO2e) | `798.7231` |

---

### 📄 [emissao_atividade_geral.csv](file:///G:/.shortcut-targets-by-id/1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI/PROJETO_FINAL_GENERATION/dados/02.prata/SEEG/Limpeza_Padrao_Prata/emissao_atividade_geral.csv)
*   **Caminho do arquivo:** `dados/02.prata/SEEG/Limpeza_Padrao_Prata/emissao_atividade_geral.csv`
*   **Tamanho:** `0.0111 MB`
*   **Colunas:** `3` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `categoria` | *Texto* | Categoria de análise (Estado, Bioma, etc.) | Texto | `Agricultura` |
| `ano` | *Inteiro* | Ano civil de referência | Ano (AAAA) | `2000` |
| `valor_mt` | *Decimal* | Volume de emissões acumulado | Megatoneladas (MtCO2e) | `376.0` |

---

### 📄 [emissao_categoria.csv](file:///G:/.shortcut-targets-by-id/1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI/PROJETO_FINAL_GENERATION/dados/02.prata/SEEG/Limpeza_Padrao_Prata/emissao_categoria.csv)
*   **Caminho do arquivo:** `dados/02.prata/SEEG/Limpeza_Padrao_Prata/emissao_categoria.csv`
*   **Tamanho:** `0.0221 MB`
*   **Colunas:** `3` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `categoria` | *Texto* | Categoria de análise (Estado, Bioma, etc.) | Texto | `Agropecuaria` |
| `ano` | *Inteiro* | Ano civil de referência | Ano (AAAA) | `2000` |
| `emissao_mt` | *Decimal* | Volume de emissões acumulado | Megatoneladas (MtCO2e) | `15.0` |

---

### 📄 [emissao_por_bioma.csv](file:///G:/.shortcut-targets-by-id/1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI/PROJETO_FINAL_GENERATION/dados/02.prata/SEEG/Limpeza_Padrao_Prata/emissao_por_bioma.csv)
*   **Caminho do arquivo:** `dados/02.prata/SEEG/Limpeza_Padrao_Prata/emissao_por_bioma.csv`
*   **Tamanho:** `0.0035 MB`
*   **Colunas:** `3` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `categoria` | *Texto* | Categoria de análise (Estado, Bioma, etc.) | Texto | `Amazonia` |
| `ano` | *Inteiro* | Ano civil de referência | Ano (AAAA) | `2000` |
| `emissao_mt` | *Decimal* | Volume de emissões acumulado | Megatoneladas (MtCO2e) | `1226.0` |

---

### 📄 [emissao_por_estado.csv](file:///G:/.shortcut-targets-by-id/1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI/PROJETO_FINAL_GENERATION/dados/02.prata/SEEG/Limpeza_Padrao_Prata/emissao_por_estado.csv)
*   **Caminho do arquivo:** `dados/02.prata/SEEG/Limpeza_Padrao_Prata/emissao_por_estado.csv`
*   **Tamanho:** `0.0139 MB`
*   **Colunas:** `3` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `categoria` | *Texto* | Categoria de análise (Estado, Bioma, etc.) | Texto | `Acre` |
| `ano` | *Inteiro* | Ano civil de referência | Ano (AAAA) | `2000` |
| `emissao_mt` | *Decimal* | Volume de emissões acumulado | Megatoneladas (MtCO2e) | `41.0` |

---

### 📄 [emissao_regiao.csv](file:///G:/.shortcut-targets-by-id/1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI/PROJETO_FINAL_GENERATION/dados/02.prata/SEEG/Limpeza_Padrao_Prata/emissao_regiao.csv)
*   **Caminho do arquivo:** `dados/02.prata/SEEG/Limpeza_Padrao_Prata/emissao_regiao.csv`
*   **Tamanho:** `0.0035 MB`
*   **Colunas:** `3` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `regiao` | *Texto* | Região geográfica original (Kaggle) | Texto | `Centro-Oeste` |
| `ano` | *Inteiro* | Ano civil de referência | Ano (AAAA) | `2000` |
| `emissao_mt` | *Decimal* | Volume de emissões acumulado | Megatoneladas (MtCO2e) | `686.4035` |

---

### 📄 [emissao_subcategoria.csv](file:///G:/.shortcut-targets-by-id/1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI/PROJETO_FINAL_GENERATION/dados/02.prata/SEEG/Limpeza_Padrao_Prata/emissao_subcategoria.csv)
*   **Caminho do arquivo:** `dados/02.prata/SEEG/Limpeza_Padrao_Prata/emissao_subcategoria.csv`
*   **Tamanho:** `0.0287 MB`
*   **Colunas:** `3` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `categoria` | *Texto* | Categoria de análise (Estado, Bioma, etc.) | Texto | `Aereo` |
| `ano` | *Inteiro* | Ano civil de referência | Ano (AAAA) | `2000` |
| `emissao_mt` | *Decimal* | Volume de emissões acumulado | Megatoneladas (MtCO2e) | `9.61` |

---

### 📄 [emissao_total_setores.csv](file:///G:/.shortcut-targets-by-id/1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI/PROJETO_FINAL_GENERATION/dados/02.prata/SEEG/Limpeza_Padrao_Prata/emissao_total_setores.csv)
*   **Caminho do arquivo:** `dados/02.prata/SEEG/Limpeza_Padrao_Prata/emissao_total_setores.csv`
*   **Tamanho:** `0.0034 MB`
*   **Colunas:** `3` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `setor` | *Texto* | Setor econômico simplificado | Texto | `Agropecuaria` |
| `ano` | *Inteiro* | Ano civil de referência | Ano (AAAA) | `2000` |
| `emissao_mt` | *Decimal* | Volume de emissões acumulado | Megatoneladas (MtCO2e) | `437.0` |

---

### 📄 [prata_seeg_all.csv](file:///G:/.shortcut-targets-by-id/1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI/PROJETO_FINAL_GENERATION/dados/02.prata/SEEG/prata_seeg_all.csv)
*   **Caminho do arquivo:** `dados/02.prata/SEEG/prata_seeg_all.csv`
*   **Tamanho:** `342.7308 MB`
*   **Colunas:** `15` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `ano` | *Inteiro* | Ano civil de referência | Ano (AAAA) | `2000` |
| `estado` | *Texto* | Nome do estado brasileiro por extenso | Texto | `Acre` |
| `bioma` | *Texto* | Nome do bioma brasileiro por extenso | Texto | `Amazônia` |
| `setor_nivel1` | *Texto* | Setor econômico Nível 1 (SEEG) | Texto | `Agropecuária` |
| `setor_nivel2` | *Texto* | Setor econômico Nível 2 (SEEG) | Texto | `Cultivo de arroz` |
| `setor_nivel3` | *Texto* | Setor econômico Nível 3 (SEEG) | Texto | `Cultivo em sistema irrigado inundado` |
| `atividade_geral` | *Texto* | Atividade geral emissora (SEEG) | Texto | `Agricultura` |
| `recorte` | *Texto* | Recorte das emissões (Diretas ou Indiretas) | Texto | `Diretas` |
| `tipo_emissao` | *Texto* | Classificação das emissões (Emissão ou Remoção) | Texto | `Emissão` |
| `gas` | *Texto* | Gás de efeito estufa mensurado | Texto | `CH4 (t)` |
| `emissao_toneladas` | *Decimal* | Volume de emissões de GEE | Toneladas (t) | `0.0` |
| `emissao_liquida_toneladas` | *Decimal* | Volume de emissões líquidas (emissões - remoções) | tCO2e (GWP-AR5) | `0.0` |
| `_processed_at` | *Texto* | Data e hora do processamento do pipeline | Texto | `20260617_134831` |
| `_source_table` | *Texto* | Caminho da tabela fonte original | Texto | `dados/00.raw/seeg_all.csv` |
| `_camada` | *Texto* | Identificador da camada no data lake | Texto (ex: SILVER) | `SILVER` |

---

### 📄 [crop_yield_silver.csv](file:///G:/.shortcut-targets-by-id/1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI/PROJETO_FINAL_GENERATION/dados/02.prata/kaggle_crop_yield/crop_yield_silver.csv)
*   **Caminho do arquivo:** `dados/02.prata/kaggle_crop_yield/crop_yield_silver.csv`
*   **Tamanho:** `80.2324 MB`
*   **Colunas:** `8` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `regiao` | *Texto* | Região geográfica original (Kaggle) | Texto | `West` |
| `cultura` | *Texto* | Cultura agrícola semeada (traduzida) | Texto (ex: Algodão, Arroz) | `Cotton` |
| `tipo_solo` | *Texto* | Tipo físico do solo (traduzido) | Texto (ex: Arenoso, Argiloso) | `Sandy` |
| `fertilizante_utilizado` | *Booleano* | Indica se houve aplicação de fertilizante químico | Booleano (True/False) | `False` |
| `irrigacao_utilizada` | *Booleano* | Indica se houve uso de irrigação artificial | Booleano (True/False) | `True` |
| `chuva_mm` | *Decimal* | Precipitação acumulada | Milímetros (mm) | `897.0772391101236` |
| `temperatura_celsius` | *Decimal* | Temperatura média do ar registrada | Graus Celsius (°C) | `27.676966373377603` |
| `produtividade_ton_ha` | *Decimal* | Produtividade da cultura por hectare | Toneladas por Hectare (t/ha) | `6.555816258223593` |

---

### 📄 [prata_cobertura_brasil_nivel1.csv](file:///G:/.shortcut-targets-by-id/1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI/PROJETO_FINAL_GENERATION/dados/02.prata/mapbiomas/prata_cobertura_brasil_nivel1.csv)
*   **Caminho do arquivo:** `dados/02.prata/mapbiomas/prata_cobertura_brasil_nivel1.csv`
*   **Tamanho:** `0.0284 MB`
*   **Colunas:** `14` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `ano` | *Inteiro* | Ano civil de referência | Ano (AAAA) | `2000` |
| `classe_nivel_1_en` | *Texto* | Classe de uso e cobertura da terra Nível 1 (Inglês) | Texto | `1. Forest` |
| `classe_nivel_1` | *Texto* | Classe de uso e cobertura da terra Nível 1 | Texto | `1. Floresta` |
| `grupo_uso` | *Texto* | Grupo de uso simplificado (ex: Vegetação Nativa, Agropecuária) | Texto | `Vegetação Nativa` |
| `area_ha` | *Decimal* | Área territorial sob a respectiva classe | Hectares (ha) | `558642159.22` |
| `pais` | *Texto* | Nome do país de referência | Texto | `Brasil` |
| `escopo_geografico` | *Texto* | Escopo da análise espacial | Texto | `Brasil (nacional)` |
| `nivel_classe` | *Inteiro* | Nível taxonômico da classe MapBiomas | Inteiro | `1` |
| `colecao_mapbiomas` | *Decimal* | Coleção MapBiomas de origem | Decimal | `10.1` |
| `unidade_medida` | *Texto* | Unidade de medida física da área | Texto (ex: hectares) | `hectares` |
| `_camada` | *Texto* | Identificador da camada no data lake | Texto (ex: SILVER) | `SILVER` |
| `_arquivo_origem` | *Texto* | Caminho do arquivo de origem bruta | Texto | `MAPBIOMAS_USOECOBERTURASOLO_coverage1...` |
| `_data_processamento` | *Texto* | Data e hora do processamento do pipeline | Texto (AAAAMMDD_HHMMSS) | `20260616_202143` |
| `_periodo_integracao` | *Texto* | Período de integração temporal | Texto | `2000–2024` |

---

### 📄 [prata_desmatamento.csv](file:///G:/.shortcut-targets-by-id/1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI/PROJETO_FINAL_GENERATION/dados/02.prata/mapbiomas/prata_desmatamento.csv)
*   **Caminho do arquivo:** `dados/02.prata/mapbiomas/prata_desmatamento.csv`
*   **Tamanho:** `62.7128 MB`
*   **Colunas:** `23` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `nome_pais` | *Texto* | Nome do país de referência | Texto | `Brasil` |
| `nome_bioma` | *Texto* | Nome do bioma brasileiro por extenso | Texto | `Amazônia` |
| `nome_regiao` | *Texto* | Nome da região geográfica | Texto | `Centro-oeste` |
| `nome_terra_indigena` | *Texto* | Nome da Terra Indígena afetada | Texto | `Apiaka/Kayabi` |
| `classe_id` | *Texto* | Metadado da tabela | Texto/Valor | `3` |
| `tipo_supressao` | *Texto* | Tipo de supressão vegetal | Texto | `Supressão Veg. Primária` |
| `classe_nivel_0` | *Texto* | Origem da cobertura (Natural ou Antrópico) | Texto | `Natural` |
| `classe_nivel_1` | *Texto* | Classe de uso e cobertura da terra Nível 1 | Texto | `1. Forest` |
| `classe_nivel_2` | *Texto* | Classe de uso e cobertura da terra Nível 2 | Texto | `1.1. Forest Formation` |
| `classe_nivel_3` | *Texto* | Classe de uso e cobertura da terra Nível 3 | Texto | `1.1. Forest Formation` |
| `classe_nivel_4` | *Texto* | Classe de uso e cobertura da terra Nível 4 | Texto | `1.1. Forest Formation` |
| `id_carga` | *Texto* | Identificador único da carga de dados | Texto | `20260617_192047` |
| `data_ingestao` | *Texto* | Data da ingestão do dado bruto | Texto (AAAA-MM-DD) | `2026-06-17` |
| `ano` | *Inteiro* | Ano civil de referência | Ano (AAAA) | `1987` |
| `area_ha` | *Decimal* | Área territorial sob a respectiva classe | Hectares (ha) | `172.2351301269534` |
| `data_processamento` | *Texto* | Data do processamento para a camada atual | Texto (AAAA-MM-DD) | `2026-06-17` |
| `origem_dados` | *Texto* | Identificador da tabela/fato de origem | Texto | `fato_desmatamento_terra_indigena` |
| `nome_estado` | *Texto* | Nome do estado brasileiro por extenso | Texto | `` |
| `categoria_uc` | *Texto* | Categoria da Unidade de Conservação (ex: APA, Rebio) | Texto | `` |
| `nome_unidade_conservacao` | *Texto* | Nome da Unidade de Conservação afetada | Texto | `` |
| `bacia_hidrografica_nv1` | *Texto* | Nome da Bacia Hidrográfica Nível 1 | Texto | `` |
| `bacia_hidrografica_nv2` | *Texto* | Nome da Bacia Hidrográfica Nível 2 | Texto | `` |
| `bacia_hidrografica_nv3` | *Texto* | Nome da Bacia Hidrográfica Nível 3 | Texto | `` |

---

### 📄 [prata_desmatamento_estado_bioma.csv](file:///G:/.shortcut-targets-by-id/1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI/PROJETO_FINAL_GENERATION/dados/02.prata/mapbiomas/prata_desmatamento_estado_bioma.csv)
*   **Caminho do arquivo:** `dados/02.prata/mapbiomas/prata_desmatamento_estado_bioma.csv`
*   **Tamanho:** `3.2191 MB`
*   **Colunas:** `21` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `pais` | *Texto* | Nome do país de referência | Texto | `Brasil` |
| `bioma` | *Texto* | Nome do bioma brasileiro por extenso | Texto | `Amazônia` |
| `regiao` | *Texto* | Região geográfica original (Kaggle) | Texto | `Norte` |
| `estado` | *Texto* | Nome do estado brasileiro por extenso | Texto | `Acre` |
| `uf` | *Texto* | Sigla da Unidade Federativa | Texto (2 caract.) | `AC` |
| `codigo_classe` | *Texto* | Metadado da tabela | Texto/Valor | `3` |
| `tipo_supressao` | *Texto* | Tipo de supressão vegetal | Texto | `Supressão Veg. Primária` |
| `tipo_supressao_simples` | *Texto* | Classificação simplificada do desmatamento | Texto | `Desmatamento Primário` |
| `nivel_0_origem` | *Texto* | Origem da cobertura (Natural ou Antrópico) | Texto | `Natural` |
| `classe_nivel_1` | *Texto* | Classe de uso e cobertura da terra Nível 1 | Texto | `1. Forest` |
| `ano` | *Inteiro* | Ano civil de referência | Ano (AAAA) | `2000` |
| `area_ha` | *Decimal* | Área territorial sob a respectiva classe | Hectares (ha) | `55316.1398804933` |
| `tem_desmatamento` | *Texto* | Metadado da tabela | Texto/Valor | `True` |
| `periodo_politica` | *Texto* | Fase das políticas públicas de combate ao desmatamento | Texto | `1. Pré-PPCDAm (antes 2004)` |
| `colecao_mapbiomas` | *Decimal* | Coleção MapBiomas de origem | Decimal | `10.1` |
| `unidade_medida` | *Texto* | Unidade de medida física da área | Texto (ex: hectares) | `hectares` |
| `_camada` | *Texto* | Identificador da camada no data lake | Texto (ex: SILVER) | `SILVER` |
| `_arquivo_origem` | *Texto* | Caminho do arquivo de origem bruta | Texto | `MAPBIOMAS_DEFORESTATION_STATE.REGION....` |
| `_encoding_original` | *Texto* | Codificação original do arquivo bruto | Texto | `latin-1` |
| `_data_processamento` | *Texto* | Data e hora do processamento do pipeline | Texto (AAAAMMDD_HHMMSS) | `20260616_202143` |
| `_periodo_integracao` | *Texto* | Período de integração temporal | Texto | `2000–2024` |

---

### 📄 [prata_pastagem.csv](file:///G:/.shortcut-targets-by-id/1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI/PROJETO_FINAL_GENERATION/dados/02.prata/mapbiomas/prata_pastagem.csv)
*   **Caminho do arquivo:** `dados/02.prata/mapbiomas/prata_pastagem.csv`
*   **Tamanho:** `5.8234 MB`
*   **Colunas:** `20` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `nome_pais` | *Texto* | Nome do país de referência | Texto | `Brasil` |
| `nome_bioma` | *Texto* | Nome do bioma brasileiro por extenso | Texto | `Amazônia` |
| `nome_estado` | *Texto* | Nome do estado brasileiro por extenso | Texto | `Acre` |
| `sigla_estado` | *Texto* | Sigla da Unidade Federativa | Texto (2 caract.) | `AC` |
| `id_recurso_bioma` | *Inteiro* | Código identificador do recurso de bioma | Inteiro | `1` |
| `id_recurso_estado` | *Inteiro* | Código identificador do recurso de estado | Inteiro | `1` |
| `idade_pastagem_anos` | *Decimal* | Idade da pastagem desde a primeira detecção de uso | Anos | `1.0` |
| `id_carga` | *Texto* | Identificador único da carga de dados | Texto | `20260617_192047` |
| `data_ingestao` | *Texto* | Data da ingestão do dado bruto | Texto (AAAA-MM-DD) | `2026-06-17` |
| `ano` | *Inteiro* | Ano civil de referência | Ano (AAAA) | `1985.0` |
| `area_ha` | *Decimal* | Área territorial sob a respectiva classe | Hectares (ha) | `402816.2735568082` |
| `data_processamento` | *Texto* | Data do processamento para a camada atual | Texto (AAAA-MM-DD) | `2026-06-17` |
| `origem_dados` | *Texto* | Identificador da tabela/fato de origem | Texto | `fato_pastagem_idade` |
| `ano_primeira_deteccao` | *Inteiro* | Ano em que a pastagem foi detectada pela primeira vez | Ano (AAAA) | `` |
| `area_ha_consolidada_2023` | *Decimal* | Área consolidada em pastagem no ano de 2023 | Hectares (ha) | `` |
| `ano_ultima_deteccao` | *Inteiro* | Ano em que a pastagem foi detectada pela última vez | Ano (AAAA) | `` |
| `classe_id` | *Texto* | Metadado da tabela | Texto/Valor | `` |
| `classe_nivel_0` | *Texto* | Origem da cobertura (Natural ou Antrópico) | Texto | `` |
| `classe_nivel_1` | *Texto* | Classe de uso e cobertura da terra Nível 1 | Texto | `` |
| `classe_nivel_2` | *Texto* | Classe de uso e cobertura da terra Nível 2 | Texto | `` |

---

### 📄 [prata_nasa_chuva_estados_brasil.csv](file:///G:/.shortcut-targets-by-id/1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI/PROJETO_FINAL_GENERATION/dados/02.prata/nasa/prata_nasa_chuva_estados_brasil.csv)
*   **Caminho do arquivo:** `dados/02.prata/nasa/prata_nasa_chuva_estados_brasil.csv`
*   **Tamanho:** `0.1516 MB`
*   **Colunas:** `4` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `UF` | *Texto* | Sigla da Unidade Federativa | Texto (2 caract.) | `AC` |
| `Ano` | *Inteiro* | Ano civil de referência | Ano (AAAA) | `2000` |
| `Mes` | *Inteiro* | Mês civil de referência | Mês (1 a 12) | `1` |
| `Chuva_mm` | *Decimal* | Precipitação acumulada | Milímetros (mm) | `242.54` |

---

## 🥇 03. Camada Ouro (Dados Consolidados e KPIs)
Caminho físico: `dados/03.ouro`

### 📄 [gold_painel_esg_consolidado.csv](file:///G:/.shortcut-targets-by-id/1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI/PROJETO_FINAL_GENERATION/dados/03.ouro/gold_painel_esg_consolidado.csv)
*   **Caminho do arquivo:** `dados/03.ouro/gold_painel_esg_consolidado.csv`
*   **Tamanho:** `0.3421 MB`
*   **Colunas:** `14` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `ano` | *Inteiro* | Ano civil de referência | Ano (AAAA) | `2000` |
| `estado` | *Texto* | Nome do estado brasileiro por extenso | Texto | `Acre` |
| `bioma` | *Texto* | Nome do bioma brasileiro por extenso | Texto | `Amazônia` |
| `emissao_agro_tco2e` | *Decimal* | Emissão do setor agropecuário em toneladas de CO2e | tCO2e (GWP-AR5) | `11983112.766974015` |
| `area_pastagem_degradada_ha` | *Decimal* | Área de pastagem classificada com vigor baixo ou médio (degradada) | Hectares (ha) | `301162.3228214454` |
| `idade_media_pastagem` | *Decimal* | Idade média ponderada das pastagens na localidade | Anos | `9.567163683083702` |
| `area_desmatada_total_ha` | *Decimal* | Área total desmatada na localidade | Hectares (ha) | `58431.99593544319` |
| `area_desmatada_ti_ha` | *Decimal* | Área desmatada dentro de Terras Indígenas | Hectares (ha) | `23025.81299645997` |
| `area_desmatada_uc_ha` | *Decimal* | Área desmatada dentro de Unidades de Conservação | Hectares (ha) | `21076.248098791548` |
| `area_desmatada_bacia_ha` | *Decimal* | Área desmatada dentro de Bacias Hidrográficas | Hectares (ha) | `1885107.37781126` |
| `chuva_mm` | *Decimal* | Precipitação acumulada | Milímetros (mm) | `` |
| `potencial_sequestro_tco2e` | *Decimal* | Potencial estimado de sequestro de carbono por recuperação de pastagem | tCO2e/ano | `602324.6456428908` |
| `receita_potencial_carbono_brl` | *Decimal* | Receita financeira potencial com venda de créditos de carbono | Reais (R$) | `30116232.282144543` |
| `risco_compliance_eudr_ha` | *Decimal* | Área desmatada pós-2020 gerando risco de compliance EUDR | Hectares (ha) | `44102.06109525152` |

---

### 📄 [dim_bioma.csv](file:///G:/.shortcut-targets-by-id/1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI/PROJETO_FINAL_GENERATION/dados/03.ouro/star_schema/dim_bioma.csv)
*   **Caminho do arquivo:** `dados/03.ouro/star_schema/dim_bioma.csv`
*   **Tamanho:** `0.0001 MB`
*   **Colunas:** `1` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `bioma` | *Texto* | Nome do bioma brasileiro por extenso | Texto | `Amazônia` |

---

### 📄 [dim_calendario.csv](file:///G:/.shortcut-targets-by-id/1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI/PROJETO_FINAL_GENERATION/dados/03.ouro/star_schema/dim_calendario.csv)
*   **Caminho do arquivo:** `dados/03.ouro/star_schema/dim_calendario.csv`
*   **Tamanho:** `0.0003 MB`
*   **Colunas:** `1` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `ano` | *Inteiro* | Ano civil de referência | Ano (AAAA) | `1985.0` |

---

### 📄 [dim_estado.csv](file:///G:/.shortcut-targets-by-id/1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI/PROJETO_FINAL_GENERATION/dados/03.ouro/star_schema/dim_estado.csv)
*   **Caminho do arquivo:** `dados/03.ouro/star_schema/dim_estado.csv`
*   **Tamanho:** `0.0006 MB`
*   **Colunas:** `3` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `estado` | *Texto* | Nome do estado brasileiro por extenso | Texto | `Acre` |
| `sigla_estado` | *Texto* | Sigla da Unidade Federativa | Texto (2 caract.) | `AC` |
| `regiao` | *Texto* | Região geográfica original (Kaggle) | Texto | `Norte` |

---

### 📄 [fato_clima.csv](file:///G:/.shortcut-targets-by-id/1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI/PROJETO_FINAL_GENERATION/dados/03.ouro/star_schema/fato_clima.csv)
*   **Caminho do arquivo:** `dados/03.ouro/star_schema/fato_clima.csv`
*   **Tamanho:** `0.2223 MB`
*   **Colunas:** `4` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `ano` | *Inteiro* | Ano civil de referência | Ano (AAAA) | `2000` |
| `mes` | *Inteiro* | Mês civil de referência | Mês (1 a 12) | `1` |
| `estado` | *Texto* | Nome do estado brasileiro por extenso | Texto | `Acre` |
| `chuva_mm` | *Decimal* | Precipitação acumulada | Milímetros (mm) | `242.54` |

---

### 📄 [fato_desmatamento.csv](file:///G:/.shortcut-targets-by-id/1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI/PROJETO_FINAL_GENERATION/dados/03.ouro/star_schema/fato_desmatamento.csv)
*   **Caminho do arquivo:** `dados/03.ouro/star_schema/fato_desmatamento.csv`
*   **Tamanho:** `0.1204 MB`
*   **Colunas:** `6` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `ano` | *Inteiro* | Ano civil de referência | Ano (AAAA) | `1987` |
| `estado` | *Texto* | Nome do estado brasileiro por extenso | Texto | `Acre` |
| `bioma` | *Texto* | Nome do bioma brasileiro por extenso | Texto | `Amazônia` |
| `regiao` | *Texto* | Região geográfica original (Kaggle) | Texto | `Norte` |
| `tipo_recorte` | *Texto* | Metadado da tabela | Texto/Valor | `Total Estado` |
| `area_desmatada_ha` | *Decimal* | Área desmatada acumulada | Hectares (ha) | `43423.39092286989` |

---

### 📄 [fato_emissoes.csv](file:///G:/.shortcut-targets-by-id/1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI/PROJETO_FINAL_GENERATION/dados/03.ouro/star_schema/fato_emissoes.csv)
*   **Caminho do arquivo:** `dados/03.ouro/star_schema/fato_emissoes.csv`
*   **Tamanho:** `0.3957 MB`
*   **Colunas:** `5` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `ano` | *Inteiro* | Ano civil de referência | Ano (AAAA) | `2000` |
| `estado` | *Texto* | Nome do estado brasileiro por extenso | Texto | `Acre` |
| `bioma` | *Texto* | Nome do bioma brasileiro por extenso | Texto | `Amazônia` |
| `setor_nivel2` | *Texto* | Setor econômico Nível 2 (SEEG) | Texto | `Cultivo de arroz` |
| `emissao_agro_tco2e` | *Decimal* | Emissão do setor agropecuário em toneladas de CO2e | tCO2e (GWP-AR5) | `0.0` |

---

### 📄 [fato_pastagem.csv](file:///G:/.shortcut-targets-by-id/1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI/PROJETO_FINAL_GENERATION/dados/03.ouro/star_schema/fato_pastagem.csv)
*   **Caminho do arquivo:** `dados/03.ouro/star_schema/fato_pastagem.csv`
*   **Tamanho:** `0.1088 MB`
*   **Colunas:** `5` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `ano` | *Inteiro* | Ano civil de referência | Ano (AAAA) | `1985.0` |
| `estado` | *Texto* | Nome do estado brasileiro por extenso | Texto | `Acre` |
| `bioma` | *Texto* | Nome do bioma brasileiro por extenso | Texto | `Amazônia` |
| `area_pastagem_degradada_ha` | *Decimal* | Área de pastagem classificada com vigor baixo ou médio (degradada) | Hectares (ha) | `` |
| `idade_media_pastagem` | *Decimal* | Idade média ponderada das pastagens na localidade | Anos | `1.0` |

---

### 📄 [fato_produtividade_agricola.csv](file:///G:/.shortcut-targets-by-id/1LxU2y_h2XY8g0JiAOin2DcmjlXADV8uI/PROJETO_FINAL_GENERATION/dados/03.ouro/star_schema/fato_produtividade_agricola.csv)
*   **Caminho do arquivo:** `dados/03.ouro/star_schema/fato_produtividade_agricola.csv`
*   **Tamanho:** `80.2314 MB`
*   **Colunas:** `8` | **Registros:** `2 (mostra do cabeçalho)`

| Coluna | Tipo | Descrição | Unidade | Exemplo |
| :--- | :--- | :--- | :--- | :--- |
| `regiao` | *Texto* | Região geográfica original (Kaggle) | Texto | `West` |
| `cultura` | *Texto* | Cultura agrícola semeada (traduzida) | Texto (ex: Algodão, Arroz) | `Cotton` |
| `tipo_solo` | *Texto* | Tipo físico do solo (traduzido) | Texto (ex: Arenoso, Argiloso) | `Sandy` |
| `fertilizante_utilizado` | *Booleano* | Indica se houve aplicação de fertilizante químico | Booleano (True/False) | `False` |
| `irrigacao_utilizada` | *Booleano* | Indica se houve uso de irrigação artificial | Booleano (True/False) | `True` |
| `chuva_mm` | *Decimal* | Precipitação acumulada | Milímetros (mm) | `897.0772391101236` |
| `temperatura_celsius` | *Decimal* | Temperatura média do ar registrada | Graus Celsius (°C) | `27.676966373377603` |
| `produtividade_ton_ha` | *Decimal* | Produtividade da cultura por hectare | Toneladas por Hectare (t/ha) | `6.555816258223593` |

---
