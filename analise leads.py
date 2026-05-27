import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

# Gera os dados falsos
def gerar_base_leads():
    dados = {
        "nome": [
            "Carlos Souza", "Ana Lima", "Roberto Pinto", "Fernanda Alves",
            "Marcos Ferreira", "Julia Costa", "Paulo Menezes", "Tatiane Rocha",
            "Diego Nunes", "Camila Teixeira", "Bruno Martins", "Leticia Borges",
            "Thiago Carvalho", "Renata Vieira", "Felipe Santos"
        ],
        "origem": [
            "Instagram", "OLX", "Indicação", "Site", "WhatsApp",
            "Instagram", "OLX", "Indicação", "Site", "Instagram",
            "WhatsApp", "OLX", "Indicação", "Site", "WhatsApp"
        ],
        "interesse": [
            "Compra", "Locação", "Compra", "Compra", "Locação",
            "Compra", "Locação", "Compra", "Locação", "Compra",
            "Compra", "Locação", "Compra", "Locação", "Compra"
        ],
        "status": [
            "Convertido", "Em andamento", "Perdido", "Convertido", "Em andamento",
            "Convertido", "Perdido", "Em andamento", "Convertido", "Perdido",
            "Em andamento", "Convertido", "Perdido", "Em andamento", "Convertido"
        ],
        "valor_imovel": [
            320000, 1800, 450000, 280000, 2200,
            510000, 1500, 390000, 2500, 620000,
            340000, 1700, 480000, 2100, 295000
        ],
        "data_entrada": [
            "2024-01-05", "2024-01-12", "2024-01-18", "2024-02-03", "2024-02-10",
            "2024-02-20", "2024-03-01", "2024-03-08", "2024-03-15", "2024-03-22",
            "2024-04-02", "2024-04-10", "2024-04-18", "2024-04-25", "2024-05-03"
        ]
    }
    return pd.DataFrame(dados)

def analisar_leads(df):
    print("=" * 50)
    print("RELATÓRIO DE ANÁLISE DE LEADS")
    print(f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print("=" * 50)

    total = len(df)
    convertidos = len(df[df["status"] == "Convertido"])
    taxa_conversao = (convertidos / total) * 100

    print(f"\nTotal de leads: {total}")
    print(f"Convertidos: {convertidos}")
    print(f"Taxa de conversão: {taxa_conversao:.1f}%")

    print("\n--- Leads por origem ---")
    por_origem = df["origem"].value_counts()
    for origem, qtd in por_origem.items():
        print(f"  {origem}: {qtd} leads")

    print("\n--- Status por tipo de interesse ---")
    tabela = pd.crosstab(df["interesse"], df["status"])
    print(tabela)

    return taxa_conversao

def gerar_graficos(df):
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle("Análise de Leads - Imobiliária", fontsize=14, fontweight="bold")

    # Gráfico 1: leads por origem
    origem_counts = df["origem"].value_counts()
    axs[0].bar(origem_counts.index, origem_counts.values, color="#4C72B0")
    axs[0].set_title("Leads por Origem")
    axs[0].set_xlabel("Canal")
    axs[0].set_ylabel("Quantidade")
    axs[0].tick_params(axis="x", rotation=15)

    # Gráfico 2: status geral
    status_counts = df["status"].value_counts()
    cores = ["#4CAF50", "#FF9800", "#F44336"]
    axs[1].pie(status_counts.values, labels=status_counts.index, autopct="%1.1f%%", colors=cores)
    axs[1].set_title("Distribuição por Status")

    plt.tight_layout()

    os.makedirs("outputs", exist_ok=True)
    plt.savefig("outputs/grafico_leads.png", dpi=150)
    print("\nGráfico salvo em: outputs/grafico_leads.png")
    plt.show()

def exportar_excel(df):
    os.makedirs("outputs", exist_ok=True)
    caminho = "outputs/relatorio_leads.xlsx"

    with pd.ExcelWriter(caminho, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Base de Leads", index=False)

        resumo = df.groupby("origem").agg(
            total_leads=("nome", "count"),
            convertidos=("status", lambda x: (x == "Convertido").sum())
        ).reset_index()
        resumo["taxa_%"] = (resumo["convertidos"] / resumo["total_leads"] * 100).round(1)
        resumo.to_excel(writer, sheet_name="Resumo por Origem", index=False)

    print(f"Relatório Excel salvo em: {caminho}")

if __name__ == "__main__":
    df = gerar_base_leads()
    analisar_leads(df)
    gerar_graficos(df)
    exportar_excel(df)
