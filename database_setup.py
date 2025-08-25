
# database_setup.py

import sqlite3 # A biblioteca para interagir com o SQLite, já vem com o Python!

def criar_banco_de_dados():
    """
    Esta função se conecta ao banco de dados (ou o cria, se não existir)
    e cria a nossa tabela 'agendamentos'.
    """
    # Conecta-se ao arquivo do banco de dados.
    # Se o arquivo 'agendamentos.db' не existir, ele será criado.
    conn = sqlite3.connect('agendamentos.db')
    
    # 'cursor' é o objeto que usamos para executar comandos SQL.
    cursor = conn.cursor()
    
    print("Conexão com o banco de dados estabelecida.")

    # Comando SQL para criar a tabela, adaptado para SQLite.
    # A sintaxe é muito parecida com as anteriores.
    sql_command = """
    CREATE TABLE IF NOT EXISTS agendamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_lead TEXT NOT NULL,
        telefone_lead TEXT NOT NULL UNIQUE,
        status TEXT NOT NULL DEFAULT 'NOVO',
        data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
        data_agendamento DATETIME,
        id_evento_google TEXT
    );
    """

    # Executa o comando SQL.
    cursor.execute(sql_command)
    
    # 'commit' salva as alterações no banco de dados.
    conn.commit()
    
    # Fecha a conexão com o banco. É uma boa prática sempre fechar.
    conn.close()
    
    print("Tabela 'agendamentos' criada com sucesso!")
    print("Banco de dados 'agendamentos.db' está pronto para uso.")


# --- Execução do Script ---
# Este bloco de código verifica se o script está sendo executado diretamente
# (e não importado em outro arquivo) e chama a nossa função.
if __name__ == '__main__':
    criar_banco_de_dados()
