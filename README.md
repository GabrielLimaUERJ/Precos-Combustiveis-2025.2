# ⛽ Análise de Preços de Combustíveis no Brasil no Segundo Semestre de 2025

Projeto de análise de dados utilizando SQL, Python e visualização em dashboard para identificar padrões de preços de combustíveis no Brasil ao longo do tempo.

---

## 🎯 Objetivo

Analisar o comportamento dos preços de combustíveis no Brasil, identificando:

- diferenças regionais
- variação de preços entre estados
- comportamento por tipo de combustível
- evolução temporal dos preços

---

## 🛠️ Tecnologias

- MySQL (armazenamento e consultas)
- Python (Pandas)
- Looker Studio (visualização)
- SQL

---

## 📊 Dataset

Dados públicos de preços de combustíveis contendo:

- localização (estado, município)
- tipo de combustível
- data da coleta
- preço de venda

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

## ▶️ Como executar (Python)

1. Instale as dependências:

```bash
pip install pandas mysql-connector-python
