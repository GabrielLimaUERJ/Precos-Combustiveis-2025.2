# ==============================
# 📦 IMPORTS
# ==============================
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# ==============================
# 🔌 CONEXÃO COM BANCO
# ==============================
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sua_Senha",
    database="combustivel_db"
)

# ==============================
# 📥 EXTRAÇÃO DOS DADOS
# ==============================
print("\n🔄 Carregando dados...")

query = "SELECT * FROM combustiveis"
df = pd.read_sql(query, conn)

print(f"\n✅ Total de registros: {len(df)}")

# ==============================
# 🧹 TRATAMENTO
# ==============================
df['valor_venda'] = pd.to_numeric(df['valor_venda'], errors='coerce')
df['data_coleta'] = pd.to_datetime(df['data_coleta'], errors='coerce')

# ==============================
# 📊 ANÁLISE 1 — PREÇO POR ESTADO
# ==============================
print("\n📊 === TOP 5 ESTADOS MAIS CAROS ===")
preco_estado = df.groupby('estado_sigla')['valor_venda'].mean().sort_values(ascending=False)
print(preco_estado.head(5))

# ==============================
# 📊 ANÁLISE 2 — VARIAÇÃO POR ESTADO
# ==============================
print("\n📊 === TOP 5 MAIOR VARIAÇÃO DE PREÇO ===")
variacao_estado = df.groupby('estado_sigla')['valor_venda'].agg(lambda x: x.max() - x.min()).sort_values(ascending=False)
print(variacao_estado.head(5))

# ==============================
# 📊 ANÁLISE 3 — PREÇO POR PRODUTO
# ==============================
print("\n⛽ === PREÇO MÉDIO POR PRODUTO ===")
preco_produto = df.groupby('produto')['valor_venda'].mean().sort_values(ascending=False)
print(preco_produto)

# ==============================
# 📊 ANÁLISE 4 — ESTADO + PRODUTO
# ==============================
print("\n🌎 === PREÇO POR ESTADO E PRODUTO (EXEMPLO AC) ===")
estado_produto = df.groupby(['estado_sigla', 'produto'])['valor_venda'].mean()
print(estado_produto.loc['AC'])

# ==============================
# 📊 ANÁLISE 5 — EVOLUÇÃO NO TEMPO
# ==============================
print("\n📈 === EVOLUÇÃO DOS PREÇOS ===")
evolucao = df.groupby('data_coleta')['valor_venda'].mean()
print(evolucao.head())

# ==============================
# ⚠️ QUALIDADE DE DADOS
# ==============================
print("\n⚠️ === VALOR_COMPRA DISPONÍVEL ===")
valor_compra_validos = df['valor_compra'].notna().sum()
print(valor_compra_validos)

# ==============================
# 📊 VISUALIZAÇÕES
# ==============================

# 🔹 Evolução no tempo
plt.figure()
evolucao.plot()
plt.title("Evolução dos preços de combustíveis")
plt.xlabel("Data")
plt.ylabel("Preço médio")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 🔹 Top 5 estados mais caros
plt.figure()
preco_estado.head(5).plot(kind='bar')
plt.title("Top 5 estados com maior preço médio")
plt.xlabel("Estado")
plt.ylabel("Preço médio")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 🔹 Variação de preços
plt.figure()
variacao_estado.head(5).plot(kind='bar')
plt.title("Estados com maior variação de preços")
plt.xlabel("Estado")
plt.ylabel("Variação (R$)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 🔹 Preço por produto
plt.figure()
preco_produto.plot(kind='bar')
plt.title("Preço médio por tipo de combustível")
plt.xlabel("Produto")
plt.ylabel("Preço médio")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==============================
# 🔚 FINALIZAÇÃO
# ==============================
conn.close()
print("\n✅ Análise finalizada com sucesso!")
