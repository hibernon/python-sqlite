import sqlite3

conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS contatos  (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nome TEXT,
      telefone TEXT
)
""")

cursor.execute("INSERT INTO contatos(nome, telefone) VALUES (?,?)", ("João", "1234-5678"))
cursor.execute("INSERT INTO contatos(nome, telefone) VALUES (?,?)", ("Maria", "9999-8888"))

conexao.commit()

cursor.execute("SELECT * FROM contatos")
for contato in cursor.fetchall():
      print(contato)

conexao.close()