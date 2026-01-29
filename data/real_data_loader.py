import pandas as pd

def carregar_dados_reais(caminho_csv):
    df = pd.read_csv(caminho_csv, sep=",")
    print("COLUNAS LIDAS PELO PANDAS:", list(df.columns))
    return df

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.normalize("NFKD")
        .str.encode("ascii", errors="ignore")
        .str.decode("utf-8")
    )

    df = df.rename(columns={
        "mes": "mes",
        "renda": "renda",
        "aluguel": "aluguel",
        "mercado": "mercado",
        "internet": "internet",
        "agua": "agua",
        "luz": "energia",
        "cartao": "cartao",
    })

    return df