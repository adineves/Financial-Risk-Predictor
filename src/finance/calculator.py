import pandas as pd
from typing import List

def calcular_indicadores(df: pd.DataFrame) -> pd.DataFrame:
    gastos_cols: List[str] = [
        "aluguel",
        "agua",
        "internet",
        "mercado",
        "cartao",
        "luz"
    ]

    for col in gastos_cols + ["renda"]:
        df[col] =(
            df[col]
            .astype(str)
            .str.replace(",", ".", regex=False)
            .str.replace(r"[^\d\.]", "", regex=True)
            .astype(float)
        )
    df["gastos_totais"] = df[gastos_cols].sum(axis=1)
    df["saldo"] = df["renda"] - df["gastos_totais"]
    df["comprometimento_renda"] = (df["gastos_totais"] / df["renda"]).round(2)
    df["saldo_variacao"] = df["saldo"].diff()

    return df