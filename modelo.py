import sqlite3

banco = sqlite3.connect('usuarios.db')

cursor = banco.cursor()

cursor.execute("""
               CREATE TABLE pessoas (
                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL, 
                   senha TEXT NOT NULL
                   );
""")

cursor.execute("""
               INSERT INTO  pessoas (nome,senha)
               VALUES(?,?)
""", ('zaqui','123'))

banco.commit()
banco.close()
