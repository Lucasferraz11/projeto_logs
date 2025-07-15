import pandas as pd
from db import conectar

def gerar_relatorio_indicadores():
    conn = conectar()

    relatorios = {
        "total_por_tipo": """
            SELECT tipo_erro, COUNT(*) AS total
            FROM erros
            GROUP BY tipo_erro
            ORDER BY total DESC
        """,

        "dia_com_mais_erros": """
            SELECT data_erro, COUNT(*) AS total
            FROM erros
            GROUP BY data_erro
            ORDER BY total DESC
            LIMIT 1
        """,

        "erro_mais_comum": """
            SELECT codigo_erro, COUNT(*) AS total
            FROM erros
            GROUP BY codigo_erro
            ORDER BY total DESC
            LIMIT 1
        """,

        "total_por_codigo": """
            SELECT codigo_erro, COUNT(*) AS total
            FROM erros
            GROUP BY codigo_erro
            ORDER BY total DESC
        """,

        "intervalo_datas": """
            SELECT MIN(data_erro) AS primeira_data, MAX(data_erro) AS ultima_data
            FROM erros
        """
    }

    with pd.ExcelWriter("relatorio_indicadores.xlsx", engine="openpyxl") as writer:
        for nome, sql in relatorios.items():
            df = pd.read_sql(sql, conn)
            df.to_excel(writer, sheet_name=nome, index=False)

    conn.close()
    print("[OK] Relatório gerado: relatorio_indicadores.xlsx")

if __name__ == "__main__":
    gerar_relatorio_indicadores()
