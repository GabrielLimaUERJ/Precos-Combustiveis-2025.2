import pandas as pd
import mysql.connector

# ==============================
# CONEXÃO
# ==============================
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SUA_SENHA",
    database="combustivel_db"
)

# ==============================
# EXTRAÇÃO
# ==============================
query = "SELECT * FROM combustiveis"
df = pd.read_sql(query, conn)

print("\nTotal de registros:", len(df))

# ==============================
# TRATAMENTO
# ==============================
df['valor_venda'] = pd.to_numeric(df['valor_venda'], errors='coerce')
df['data_coleta'] = pd.to_datetime(df['data_coleta'], errors='coerce')

# ==============================
# ANÁLISE 1
# ==============================
print("\n=== PREÇO MÉDIO POR ESTADO ===")
print(df.groupby('estado_sigla')['valor_venda'].mean().sort_values(ascending=False).head())

# ==============================
# ANÁLISE 2
# ==============================
print("\n=== VARIAÇÃO POR ESTADO ===")
print(df.groupby('estado_sigla')['valor_venda'].agg(lambda x: x.max() - x.min()).sort_values(ascending=False).head())

# ==============================
# ANÁLISE 3
# ==============================
print("\n=== PREÇO POR PRODUTO ===")
print(df.groupby('produto')['valor_venda'].mean().sort_values(ascending=False))

# ==============================
# ANÁLISE 4
# ==============================
print("\n=== ESTADO + PRODUTO ===")
print(df.groupby(['estado_sigla', 'produto'])['valor_venda'].mean().head())

# ==============================
# ANÁLISE 5
# ==============================
print("\n=== EVOLUÇÃO NO TEMPO ===")
print(df.groupby('data_coleta')['valor_venda'].mean().head())

# ==============================
# QUALIDADE DE DADOS
# ==============================
print("\n=== VALOR_COMPRA DISPONÍVEL ===")
print(df['valor_compra'].notna().sum())

conn.close()