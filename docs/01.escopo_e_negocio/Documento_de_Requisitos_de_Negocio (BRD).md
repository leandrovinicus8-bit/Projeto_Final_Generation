### Perguntas de Negócio que o Projeto Responde
1. Qual é o comportamento histórico das emissões na região e como ele se correlaciona com as séries temporais de precipitação?
2. Existem zonas ou períodos críticos onde a falta de chuva potencializou a poluição ou o risco climático na safra?
3. A adoção de práticas agrícolas sustentáveis específicas mitigou quantitativamente os poluentes e emissões ao longo dos ciclos produtivos?

### KPIs Esperados
* **Redução Percentual de Emissões:** Variação anual da estimativa de toneladas de $CO_2$ equivalente ($tCO_2e$) por hectare.
* **Eficiência de Insumos:** Identificação de margem para redução de custos com fertilizantes nitrogenados (via Fixação Biológica de $N_2$, por exemplo).
* **Elegibilidade para Certificados:** Índice de conformidade da base histórica com os requisitos das metodologias globais (Adicionalidade e Mensurabilidade).

### Requisitos Funcionais (Dashboard e Data App)
* Visualização da evolução histórica das emissões sobreposta a indicadores climáticos.
* Filtros dinâmicos por período temporal (safras/anos) e localização geográfica.
* Destaque visual para anomalias ou períodos de seca extrema.

### Requisitos Não-Funcionais
* Garantia de reprodutibilidade total do ambiente de dados (virtualenv e sementes de código fixadas).
* Rastreabilidade completa: do dado bruto (Bronze) ao painel final (*Gold*).

---

