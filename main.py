from data.real_data_loader import carregar_dados_reais
from src.finance.calculator import calcular_indicadores
from src.finance.risk_rules import calcular_risco_financeiro

def main():
    df = carregar_dados_reais("data/raw/meus_dados.csv")
    df = calcular_indicadores(df)

    print("\nResumo Financeiro Atual:")
    print(df[["mes","renda", "gastos_totais", "saldo", "comprometimento_renda"]])

    risco = calcular_risco_financeiro

    print("\nAVALIAÇÃO DE RISCO\n")
    print(f"Score de Risco: {risco['score']}/100")
    print(f"Nivel de Risco: {risco['nivel']}")

    if risco["motivos"]:
        print("Motivos:")
        for m  in risco["motivos"]:
            print(f"- {m}")
    else:
        print("Nenhum sinal relevante de risco detectado.")

if __name__ == "__main__":
    main()