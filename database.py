import sqlite3

class Data_base():
    
    def __init__(self, name= 'system.db') -> None:
        self.name = name
        self.connection = name

    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        
        except:
            pass
    
    def criare_tabela_perguntas(self):
        cursor= self.connection.cursor()

        cursor.execute("""

                       CREATE TABLE IF NOT EXISTS Perguntas(
                       
                       ID INTEGER NOT NULL,
                       pergunta text,
                       nivel text,
                       resposta1 text,
                       resposta2 text,
                       resposta3 text,
                       resposta4 text,
                       respostaCerta text,

                       PRIMARY KEY ("ID" AUTOINCREMENT)

                       );

                       
                       """)
    
    def cadastrar_pergunta(self, pergunta):
        campos_tabela = ('pergunta', 'nivel','resposta1','resposta2',
                         'resposta3','resposta4','respostaCerta')
        
        qntd=("?,?,?,?,?,?,?")

        try:
            cursor = self.connection.cursor()
            cursor.execute(f"""INSERT INTO Perguntas {campos_tabela} VALUES ({qntd}) """, pergunta)
            self.connection.commit()

            return "OK"
        except Exception as e:
            print(e)
            return e
        
    def selecionar_pergunta(self, nivel):

        self.connect()

        try:
            cursor=self.connection.cursor()
            cursor.execute(f"SELECT * FROM Perguntas WHERE  nivel= '{nivel}'")
            perguntas=cursor.fetchall()
            self.close_connection()
            return perguntas
        except Exception as e:
            print(e)
            self.connection()
            return e