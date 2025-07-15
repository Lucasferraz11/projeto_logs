import os
import glob
import pandas as pd
from db import conectar

def carregar_logs():
    pasta_logs = "logs/"
    arquivos_csv = glob.glob(os.path.join(pasta_logs, "*.csv"))

    if not arquivos_csv:
        print("[AVISO] Nenhum arquivo CSV encontrado em /logs.")
        return

    conexao = conectar()
    cursor = conexao.cursor()

    for arquivo in arquivos_csv:
        print(f"[INFO] Lendo arquivo: {arquivo}")
        try:
            df = pd.read_csv(arquivo)
        except Exception as e:
            print(f"[ERRO] Falha ao ler {arquivo}: {e}")
            continue

        for _, linha in df.iterrows():
            query = """
                INSERT INTO erros (data_erro, codigo_erro, tipo_erro, descricao)
                VALUES (%s, %s, %s, %s)
            """
            valores = (
                linha["data_erro"],
                int(linha["codigo_erro"]),
                linha["tipo_erro"],
                linha["descricao"]
            )

            try:
                cursor.execute(query, valores)
            except Exception as e:
                print(f"[ERRO] Falha ao inserir linha: {e}")

        conexao.commit()
        print(f"[OK] Dados do arquivo {arquivo} inseridos com sucesso.")

    cursor.close()
    conexao.close()

if __name__ == "__main__":
    carregar_logs()
