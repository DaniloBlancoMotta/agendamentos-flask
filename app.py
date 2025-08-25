# app.py

from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
DB_FILE = 'agendamentos.db'

def get_db_connection():
    """Cria uma conexão com o banco de dados."""
    conn = sqlite3.connect(DB_FILE)
    # Isso permite acessar as colunas pelo nome (ex: lead['nome_lead'])
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def pagina_inicial():
    """Renderiza a página inicial."""
    return "&lt;h1&gt;Olá! Nosso servidor de agendamentos está no ar.&lt;/h1&gt;&lt;a href='/agendamentos'&gt;Ver Agendamentos&lt;/a&gt;"

@app.route('/agendamentos')
def exibir_agendamentos():
    """Busca os dados no banco e renderiza a página de agendamentos."""
    conn = get_db_connection()
    # Busca todos os agendamentos, ordenados pelo mais recente
    agendamentos_do_banco = conn.execute('SELECT * FROM agendamentos ORDER BY data_criacao DESC').fetchall()
    conn.close()
    
    # render_template vai procurar o arquivo 'agendamentos.html' na pasta 'templates'
    # e vai passar a variável 'agendamentos' para o HTML.
    return render_template('agendamentos.html', agendamentos=agendamentos_do_banco)

if __name__ == '__main__':
    app.run(port=5001, debug=True)