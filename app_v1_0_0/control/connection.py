import sqlite3

class banco():
    def __init__(self):
        super().__init__()

        self.criarBanco()

    def criarBanco(self):
        conexao = sqlite3.connect('convertai.db')
        cursor = conexao.cursor()
        cursor.execute('''
            
            CREATE TABLE IF NOT EXISTS company(
            id INTEGER PRIMARY KEY,
            name TEXT,
            cnpj TEXT,
            password TEXT,
            choice TEXT
            )
        ''')

        conexao.commit()
        conexao.close()

    def cadastrar_usuario(self, name, cnpj, password, choice):
        if self.usuario_existente(cnpj):
            return False
        conexao = sqlite3.connect('convertai.db')
        cursor = conexao.cursor()
        cursor.execute('''
            INSERT INTO company (name, cnpj, password, choice) VALUES (?, ?, ?, ?)        
        ''', (name, cnpj, password, choice))

        conexao.commit()
        conexao.close()
        return True

    def usuario_existente(self, cnpj):
        conexao = sqlite3.connect('convertai.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM company WHERE cnpj = ?', (cnpj))
        user = cursor.fetchone()
        conexao.close()
        return user is not None

    def realizar_login(self, cnpj, password):
        conexao = sqlite3.connect('convertai.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM company WHERE cnpj = ? AND password = ?', (cnpj,password))
        user = cursor.fetchone()
        conexao.close()
        return user

    def obter_choice(self, cnpj):
        conexao = sqlite3.connect('convertai.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT choice FROM company WHERE cnpj = ?', (cnpj))
        choice = cursor.fetchone()
        conexao.close()
        return choice[0] if choice else None