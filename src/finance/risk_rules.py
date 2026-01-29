import pandas as pd
from typing import Dict, List

def calcular_risco_financeiro(df: pd.DataFrame) -> Dict[str, object]:
    score = 0 
    motivos: List[str] = []

    ultimo = df.iloc[-1]

    if ultimo["comprometimento_rendaa"] >= 1:
        score += 50
        motivos.append("100% ou mais da renda comprometida.")

    if ultimo["comprometimento_rendaa"] >= 0.8:
        score += 30
        motivos.append("Comprometimento da renda alto.")

    if ultimo["comprometimento_rendaa"] >= 2:
        score += 20
        motivos.append("Quedas frequentes de saldo.")

    score = min(score, 100)

    if score >= 70:
        nivel = "ALTO"
    elif score >= 40:
        nivel = "MEDIO"
    else:
        nivel = "BAIXO"

    return {
        "score": score,
        "nivel": nivel, 
        "motivos": motivos,
    }