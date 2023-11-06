from sqlalchemy import create_engine, Column, Integer, String, exc
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    cnpj = Column(String(18), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    senha = Column(String(100), nullable=False)
    endereco = Column(String(200))

class DBConnectionHandler:
    def __init__(self):
        self.__connect_string = 'mysql+mysqldb://root:senha@localhost/banco'
        self.__engine = self.__create_database_engine()
        self.create_table()
        self.session = None

    def get_engine(self):
        return self.__engine

    def __create_database_engine(self):
        try:
            engine = create_engine(self.__connect_string)
            # Testa a conexão
            connection = engine.connect()
            connection.close()
            return engine
        except exc.SQLAlchemyError as e:
            print(f"Erro ao tentar conectar: {e}")
            return None

    def create_table(self):
        if not self.__engine:
            print("Não foi possível criar a tabela devido a um erro de conexão.")
            return

        try:
            Base.metadata.create_all(self.__engine, checkfirst=True)
        except exc.SQLAlchemyError as e:
            print(f"Erro ao tentar criar a tabela: {e}")

    def __enter__(self):
        if not self.__engine:
            print("Erro de conexão. Não foi possível iniciar a sessão.")
            return self

        session_make = sessionmaker(bind=self.__engine)
        print('Abrindo Conexão')
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            print('Encerrando Conexão')
            self.session.close()
