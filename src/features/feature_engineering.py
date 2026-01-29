import pandas as pd

def criar_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["comprometimento_renda"] = df["gastos_totais"] / df["renda"]
    
    df["saldo_variacao"] = df["saldo"].diff()

    df["gastos_media_3m"] = df["gastos_totais"].rolling(window=3).mean()

    return df
