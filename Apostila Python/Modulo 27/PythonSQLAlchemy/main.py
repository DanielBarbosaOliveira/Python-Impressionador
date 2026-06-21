from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=db)
session = Session()


Base = declarative_base()

# as tabelas
class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column("id_usuario", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo =Column("ativo", Boolean)
    
    def __init__(self, nome, email, senha, ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo


class Livro(Base):
    __tablename__ = "livros"
    
    id = Column("id_livro", Integer, primary_key=True, autoincrement=True)
    titulo = Column("titulo", String)
    qtde_paginas = Column("qtde_paginas", Integer)
    dono = Column("dono", ForeignKey("usuarios.id_usuario"))
    
    def __init__(self, titulo, qtde_paginas, dono):
        self.titulo = titulo
        self.qtde_paginas = qtde_paginas
        self.dono = dono

Base.metadata.create_all(bind=db)

# CRUD
#Create
""" usuario = Usuario(nome="takeiro", email="takeiro@gmail.com", senha="12345")
session.add(usuario)
session.commit() """

# READ
# lista_usuarios = session.query(Usuario).all()
#usuario_dan = session.query(Usuario).filter_by(email="dandan@dasod").first()


""" livro = Livro(titulo="O Hobbit", qtde_paginas=350, dono=usuario_dan.id)
session.add(livro)
session.commit() """

# Update
""" usuario_dan.nome = "Daniel"
session.add(usuario_dan)
session.commit() """

# Delete
usuario_takeiro = session.query(Usuario).filter_by(email="takeiro@gmail.com").first()
session.delete(usuario_takeiro)
session.commit()