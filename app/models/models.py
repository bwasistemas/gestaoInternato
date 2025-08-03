from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database import Base

class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    matricula = Column(String(20), unique=True, nullable=False)
    email = Column(String(100))
    telefone = Column(String(20))
    created_at = Column(TIMESTAMP, server_default=func.now())

    escalas = relationship("Escala", back_populates="aluno")

class Especialidade(Base):
    __tablename__ = "especialidades"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    codigo = Column(String(10))
    capacidade_maxima = Column(Integer)
    created_at = Column(TIMESTAMP, server_default=func.now())

    medicos = relationship("Medico", back_populates="especialidade")
    escalas = relationship("Escala", back_populates="especialidade")

class Medico(Base):
    __tablename__ = "medicos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    especialidade_id = Column(Integer, ForeignKey("especialidades.id"))
    tipo_atividade = Column(String(50))

    especialidade = relationship("Especialidade", back_populates="medicos")
    escalas = relationship("Escala", back_populates="medico")

class Periodo(Base):
    __tablename__ = "periodos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50))
    data_inicio = Column(Date)
    data_fim = Column(Date)
    ativo = Column(Boolean, default=True)

    escalas = relationship("Escala", back_populates="periodo")

class Escala(Base):
    __tablename__ = "escalas"

    id = Column(Integer, primary_key=True, index=True)
    aluno_id = Column(Integer, ForeignKey("alunos.id"))
    especialidade_id = Column(Integer, ForeignKey("especialidades.id"))
    medico_id = Column(Integer, ForeignKey("medicos.id"))
    periodo_id = Column(Integer, ForeignKey("periodos.id"))
    tipo_atividade = Column(String(50))

    aluno = relationship("Aluno", back_populates="escalas")
    especialidade = relationship("Especialidade", back_populates="escalas")
    medico = relationship("Medico", back_populates="escalas")
    periodo = relationship("Periodo", back_populates="escalas")
    frequencia = relationship("Frequencia", back_populates="escala")

class Frequencia(Base):
    __tablename__ = "frequencia"

    id = Column(Integer, primary_key=True, index=True)
    escala_id = Column(Integer, ForeignKey("escalas.id"))
    data = Column(Date)
    presente = Column(Boolean)
    observacoes = Column(String)

    escala = relationship("Escala", back_populates="frequencia")
