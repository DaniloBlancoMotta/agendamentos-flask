# gerenciar_leads.py

import sqlite3

# O nome do arquivo do nosso banco de dados.
DB_FILE = 'agendamentos.db'

def inserir_lead(nome, telefone):
    """
    Função para inserir um novo lead na tabela agendamentos.
    O status padrão será 'NOVO', como definido na criação da tabela.
    """
    try:
        # Conecta ao banco de dados
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Comando SQL para inserir dados.
        # Usamos '?' para evitar um tipo de ataque chamado SQL Injection.
        # É uma prática de segurança muito importante!
        sql_command = "INSERT INTO agendamentos (nome_lead, telefone_lead) VALUES (?, ?)"
        
        # Executa o comando, passando os valores em uma tupla
        cursor.execute(sql_command, (nome, telefone))
        
        # Salva (commit) as alterações
        conn.commit()
        
        print(f"Lead '{nome}' inserido com sucesso!")

    except sqlite3.IntegrityError:
        # Este erro acontece se tentarmos inserir um telefone que já existe.
        print(f"Erro: O telefone '{telefone}' já existe no banco de dados.")
    
    except Exception as e:
        print(f"Ocorreu um erro ao inserir o lead: {e}")

    finally:
        # Garante que a conexão seja sempre fechada, mesmo se ocorrer um erro.
        if conn:
            conn.close()


def listar_leads():
    """

    Função para buscar e exibir todos os leads da tabela.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        # conn.row_factory = sqlite3.Row nos permite acessar os dados por nome da coluna.
        conn.row_factory = sqlite3.Row 
        cursor = conn.cursor()

        sql_command = "SELECT * FROM agendamentos"
        cursor.execute(sql_command)
        
        # fetchall() busca todos os resultados da consulta.
        todos_os_leads = cursor.fetchall()

        if not todos_os_leads:
            print("Nenhum lead encontrado no banco de dados.")
            return

        print("\n--- LISTA DE LEADS NO BANCO DE DADOS ---")
        for lead in todos_os_leads:
            # Imprime os dados de forma organizada
            print(f"ID: {lead['id']}, Nome: {lead['nome_lead']}, Telefone: {lead['telefone_lead']}, Status: {lead['status']}")
        print("----------------------------------------")

    except Exception as e:
        print(f"Ocorreu um erro ao listar os leads: {e}")

    finally:
        if conn:
            conn.close()


# --- Execução do Script para Teste ---
if __name__ == '__main__':
    print(">>>> Testando a inserção de um novo lead...")
    # Dados do nosso primeiro lead de teste
    inserir_lead("Ana Silva", "5511987654321")
    
    print("\n>>>> Testando a listagem de leads...")
    # Lista todos os leads para confirmar que a Ana foi inserida
    listar_leads()
