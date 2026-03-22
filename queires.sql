
---

# 📄 queries.sql (FINAL)

```sql
-- ===============================
-- PREÇO MÉDIO POR ESTADO
-- ===============================
SELECT 
    estado_sigla,
    ROUND(AVG(valor_venda), 2) AS preco_medio
FROM combustiveis
GROUP BY estado_sigla
ORDER BY preco_medio DESC;


-- ===============================
-- VARIAÇÃO DE PREÇO POR ESTADO
-- ===============================
SELECT 
    estado_sigla,
    ROUND(MAX(valor_venda) - MIN(valor_venda), 2) AS variacao
FROM combustiveis
GROUP BY estado_sigla
ORDER BY variacao DESC;


-- ===============================
-- PREÇO MÉDIO POR PRODUTO
-- ===============================
SELECT 
    produto,
    ROUND(AVG(valor_venda), 2) AS preco_medio
FROM combustiveis
GROUP BY produto
ORDER BY preco_medio DESC;


-- ===============================
-- PREÇO POR ESTADO E PRODUTO
-- ===============================
SELECT 
    estado_sigla,
    produto,
    ROUND(AVG(valor_venda), 2) AS preco_medio
FROM combustiveis
GROUP BY estado_sigla, produto
ORDER BY estado_sigla;


-- ===============================
-- EVOLUÇÃO NO TEMPO
-- ===============================
SELECT 
    data_coleta,
    ROUND(AVG(valor_venda), 2) AS preco_medio
FROM combustiveis
GROUP BY data_coleta
ORDER BY data_coleta;


-- ===============================
-- VALIDAÇÃO DE DADOS (VALOR_COMPRA)
-- ===============================
SELECT 
    COUNT(*) AS total,
    COUNT(valor_compra) AS com_valor_compra
FROM combustiveis;