import pandas as pd
import random

def gerar_dados_financeiros(meses: int = 12) -> pd.DataFrame:
    """
    Gera dados financeiros sintéticos para simular comportamento mensal.
    """
    dados = []
    saldo = random.randint(500, 3000)

    for mes in range (1, meses + 1):
        renda = random.randint(2500, 4000)

        gastos_moradia = random.randint(800, 1500)
        gastos_alimentacao = random.randint(400, 500)
        gastos_transporte = random.randint(200, 500)
        gastos_lazer = random.randint(100, 600)

        gastos_totais = (
            gastos_moradia +
            gastos_alimentacao +
            gastos_transporte +
            gastos_lazer
        )

        saldo = saldo + renda - gastos_totais
        
        dados.append({
            "mes": mes,
            "renda": renda,
            "gastos_moradia": gastos_moradia,
            "gastos_alimentacao": gastos_alimentacao,
            "gastos_transporte": gastos_transporte,
            "gastos_lazer": gastos_lazer,
            "gastos_totais": gastos_totais,
            "saldo": saldo
        })

    return pd.DataFrame(dados)
