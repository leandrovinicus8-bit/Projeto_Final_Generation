# Catálogo de Fontes de Dados (Catalogo_Fontes_Dados.md)

Este documento centraliza o inventário técnico e de negócio de todas as fontes de dados consumidas no pipeline do projeto de Inteligência Agroambiental. Ele serve como referência para garantir a governança, integridade e o alinhamento de todo o time de engenharia e análise.

---

## 1. MapBiomas
* **Objetivo no Projeto:** Fornecer dados históricos geoespaciais e tabulares sobre a dinâmica de uso e cobertura da terra no Brasil. Essencial para correlacionar o avanço ou degradação de pastagens, recortes territoriais (biomas, estados, municípios, UCs e Terras Indígenas) e taxas de desmatamento com o potencial de sequestro ou emissão de carbono.
* **Coleções e Módulos Utilizados:** * Coleção de Pastagem (Vigor, Idade, Primeira e Última vez)
	  * Desmatamento
	  * Cobertura Brasil Nível 1
	  * Desmatamento Bioma
* **URL:** [https://mapbiomas.org/](https://mapbiomas.org/)
* **Método de Acesso:** Extração de relatórios e painéis públicos (formatos `.xlsx` e geoespaciais), integrados e convertidos programaticamente para a camada Bronze em formato CSV.
* **Período de Cobertura:** Histórico anual completo disponível nas coleções vigentes (geralmente cobrindo de 1985 até 2023).
* **Granularidade:** Anual, com recortes por Bioma, Estado, Município, Bacias Hidrográficas, Unidades de Conservação (UC) e Terras Indígenas (TI).
* **Variáveis Disponíveis:** Área total (hectares), classes de vigor de pastagem (alto, médio, baixo), idade da pastagem, ano do primeiro e último registro de uso, e áreas desmatadas por categorias territoriais.
* **Licença de Uso:** Creative Commons CC BY-SA 4.0 (Uso livre mediante citação obrigatória da fonte).
* **Data de Extração:** 16/06/2025

---

## 2. NASA POWER  (Dados Meteorológicos)
* **Objetivo no Projeto:** Fornecer uma cobertura climática contínua e geoespacializada de alta resiliência, permitindo cruzar anomalias meteorológicas (temperatura, precipitação e radiação) com a perda de vigor vegetativo, quebra de produtividade agrícola e emissões de gases do efeito estufa.
* **URL:** [https://power.larc.nasa.gov/](https://power.larc.nasa.gov/)
* **Método de Acesso:** Extração automatizada e programática via **API REST** utilizando scripts Python.
* **Período de Cobertura:** Dados históricos diários/mensais contínuos de 1980 a 2024.
* **Granularidade:** Diária ou Mensal, baseada em coordenadas geográficas (Latitude e Longitude).
* **Variáveis Disponíveis:** Temperatura do ar (máxima, mínima, média), precipitação (chuva acumulada), umidade relativa, velocidade do vento, radiação solar incidente e evapotranspiração.
* **Licença de Uso:** Dados públicos de domínio público fornecidos pela NASA (NASA Open Data Policy), livres para fins acadêmicos e comerciais.
* **Data de Extração:** Coletado sob demanda em tempo de execução do pipeline.

---

## 3. Kaggle (Agriculture Crop Yield)
* **Objetivo no Projeto:** Atuar como a base de modelagem de produtividade de culturas. Permite correlacionar o rendimento das safras agrícolas com os insumos aplicados,  fatores climáticos coletados e emissões registradas.
* **URL:** [https://www.kaggle.com/datasets/samuelotiattakorah/agriculture-crop-yield](https://www.kaggle.com/datasets/samuelotiattakorah/agriculture-crop-yield)
* **Método de Acesso:** Download direto via interface web ou consumo automatizado através da Kaggle API.
* **Período de Cobertura:** Em média 104 dias
* **Granularidade:** Por talhão/registro de safra ou região produtora (tabular).
* **Variáveis Disponíveis:** Produtividade agrícola, região, tipo de solo, tipo de cultura, volume de chuva, aplicação de fertilizantes, uso de pesticidas, temperatura média, características do manejo do solo, condição climática.
* **Licença de Uso:** CC0 Public Domain.
* **Data de Extração:** 15/06/2026.

---

## 4. SEEG (Sistema de Estimativas de Emissões e Remoções de Gases de Efeito Estufa)
* **Objetivo no Projeto:** Oferecer a verdade fundamental sobre o histórico e a evolução das emissões de gases de efeito estufa ($CO_2e$, $CH_4$, $N_2O$) e uso do solo no território brasileiro. Esta fonte fundamenta a análise de metas ESG e o cálculo de linhas de base para o mercado de Créditos de Carbono.
* **Coleções e Módulos Utilizados:** * Atividade Geral
	* Emissão Total
	* Emissão Total por Bioma
	* Emissão Total por Categoria
	* Emissão Total por Estado
* **URL:** [https://seeg.eco.br/](https://seeg.eco.br/)
* **Método de Acesso:** Extração via download de planilhas e bases consolidadas em formato analítico disponibilizadas pelo Observatório do Clima.
* **Período de Cobertura:** Série histórica de emissões brasileiras cobrindo de 1970 até o inventário anual mais recente publicado (2024).
* **Granularidade:** Anual, com aberturas por Setor Econômico, Atividade/Subatividade, Gás emitido, Estado e Município (conforme o nível da matriz disponível).
* **Setores de Foco do Projeto:** Agropecuária (com ênfase em fermentação entérica e manejo de solos) e Mudança de Uso da Terra e Florestas (MUT).
* **Variáveis Disponíveis:** Emissões brutas e líquidas mensuradas em toneladas de gás específico e convertidas em toneladas de CO₂ equivalente ($tCO_2e$) pelos potenciais de aquecimento global vigentes (GWP/GTP).
* **Licença de Uso:** Creative Commons (Uso livre para análises e aplicações mediante atribuição da iniciativa SEEG / Observatório do Clima).
* **Data de Extração:** 16/06/2026.