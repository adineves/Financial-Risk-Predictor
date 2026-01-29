from src.data.data_generator import gerar_dados_financeiros
from src.features.feature_engineering import criar_features
from finance.risk_rules import calcular_score_risco

df = gerar_dados_financeiros(meses=12)
df = criar_features(df)

score = calcular_score_risco(df)

print(df)
print(f"\n Score de risco financiero: {score}/100")
print(df.columns)
print(df[[
    "mes",
    "renda",
    "gastos_totais",
    "comprometimento_renda",
    "saldo_variacao",
    "gastos_media_3m"
]])