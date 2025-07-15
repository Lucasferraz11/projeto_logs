# 🛠️  Analisador de Logs com MySQL e Relatórios

Este projeto carrega arquivos CSV contendo registros de erros do sistema, armazena os dados em um banco MySQL e gera indicadores consolidados em um relatório Excel.

---

## 💾 Tecnologias Utilizadas

- Python
- MySQL
- pandas
- openpyxl
- dotenv

---

## 📁 Estrutura de Arquivos

- `logs/`: pasta com arquivos `.csv` contendo os logs
- `carregar_logs.py`: script que lê todos os arquivos da pasta e insere no banco
- `relatorios.py`: gera relatório consolidado com indicadores
- `db.py`: conexão com o banco MySQL
- `.env`: credenciais (não versionadas)
- `README.md`: este arquivo

---

## 🗃️ Estrutura do Banco

```sql
CREATE DATABASE analisador_logs;

CREATE TABLE erros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data_erro DATE,
    codigo_erro INT,
    tipo_erro VARCHAR(100),
    descricao TEXT
);

▶️ Como usar
Clone o repositório:

git clone https://github.com/seu-usuario/projeto_logs.git
cd projeto_logs
Crie o .env com as variáveis de conexão:

DB_HOST=localhost
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_NAME=analisador_logs

Instale as dependências:

pip install -r requirements.txt
Adicione arquivos .csv na pasta logs/

Carregue os logs:

python carregar_logs.py
Gere os indicadores:

python relatorios.py
📊 Indicadores Gerados
Total de erros por tipo

Dia com mais erros

Código de erro mais frequente

Total de erros por código

Intervalo de datas dos erros