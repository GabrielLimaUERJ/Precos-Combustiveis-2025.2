# ⛽ Análise de Preços de Combustíveis no Brasil no Segundo Semestre de 2025

Projeto de análise de dados utilizando SQL e Python, com desenvolvimento de um dashboard interativo em Streamlit para exploração dos dados.

---

## 🎯 Objetivo

Analisar o comportamento dos preços de combustíveis no Brasil, identificando:

- diferenças regionais
- variação de preços entre estados
- comportamento por tipo de combustível
- evolução temporal dos preços

---

## 📊 Dashboard Interativo

O projeto conta com um dashboard desenvolvido em Streamlit, permitindo:

- filtragem por estado
- filtragem por tipo de combustível
- visualização dinâmica de métricas
- análise interativa dos dados

---

## 🛠️ Tecnologias

- MySQL (armazenamento e consultas)
- Python (Pandas)
- SQL
- Streamlit (dashboard interativo)
- Matplotlib

---

## 📊 Dataset

Dados públicos de preços de combustíveis contendo:

- localização (estado, município)
- tipo de combustível
- data da coleta
- preço de venda

O dataset utilizado neste projeto é público e pode ser obtido em:

[dados.gov.br - Série histórica de preços de combustíveis](https://dados.gov.br/dados/conjuntos-dados/serie-historica-de-precos-de-combustiveis-e-de-glp)

Por questões de tamanho, o arquivo completo não foi incluído no repositório.

---

## 📈 Principais Análises

- Preço médio por estado
- Variação de preços por estado (máx - mín)
- Preço médio por tipo de combustível
- Análise cruzada (estado + produto)
- Evolução dos preços ao longo do tempo
- Validação da qualidade dos dados

---

## 💡 Principais Insights

- Estados da região Norte apresentam os maiores preços médios de combustíveis.
- O Sudeste apresenta preços mais baixos, especialmente para etanol.
- A gasolina aditivada é consistentemente o combustível mais caro.
- Estados com maior atividade econômica apresentam maior variação de preços, indicando maior concorrência.
- Os preços se mantêm relativamente estáveis ao longo do tempo, com picos pontuais.
- Foi identificada ausência de dados confiáveis na variável de valor de compra, impossibilitando análise de margem.

---

## ⚠️ Limitações dos Dados

- A coluna `valor_compra` não possui dados válidos suficientes.
- Possível presença de outliers em datas específicas.
- Diferenças de preço podem ser influenciadas por fatores externos não presentes no dataset.

---

## ▶️ Como executar

1. Clone o repositório:

```bash
git clone https://github.com/GabrielLimaUERJ/Precos-Combustiveis-2025.2.git
cd Precos-Combustiveis-2025.2
pip install -r requirements.txt
streamlit run app.py
