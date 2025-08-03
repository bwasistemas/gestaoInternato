
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import date

class User(BaseModel):
    id: int
    email: EmailStr
    nome: str
    data_nascimento: date
    telefone: str
    role: str

class LoginRequest(BaseModel):
    email: EmailStr
    data_nascimento: date

class Aluno(BaseModel):
    id: int
    nome: str
    email: EmailStr
    telefone: str
    data_nascimento: date
    especialidade_principal: Optional[str] = None
    # Campos dinâmicos para estatísticas
    agendas_count: Optional[int] = 0
    carimbos_semana: Optional[int] = 0

class AlunoCreate(BaseModel):
    nome: str
    email: EmailStr
    telefone: str
    data_nascimento: date
    especialidade_principal: Optional[str] = None

class Especialidade(BaseModel):
    id: int
    nome: str
    descricao: Optional[str] = None
    # Campos dinâmicos para estatísticas
    alunos_count: Optional[int] = 0
    agendas_count: Optional[int] = 0

class Local(BaseModel):
    id: int
    nome: str
    endereco: str
    especialidades: List[str] = []
    responsavel: str
    # Campos dinâmicos para estatísticas
    agendas_count: Optional[int] = 0
    especialidades_count: Optional[int] = 0

class MedicoResponsavel(BaseModel):
    nome: str
    crm: Optional[str] = None
    titulo: Optional[str] = None

class Restricao(BaseModel):
    descricao: str

class LocalEstudo(BaseModel):
    local_id: int
    nome_local: str
    tipo_local: str
    medico_responsavel: MedicoResponsavel
    endereco: str
    capacidade_alunos: int
    restricoes: List[str]

class EspecialidadeCompleta(BaseModel):
    especialidade_id: int
    nome_especialidade: str
    codigo_especialidade: str
    cor_interface: str
    descricao: str
    ativo: bool
    locais: List[LocalEstudo]

class Agenda(BaseModel):
    id: int
    data: date
    turno: str
    especialidade: str
    especialidade_id: int
    local_estudo_id: int
    local_estudo_nome: str
    aluno_id: int
    aluno_nome: str
    responsavel: str
    presenca: bool = False
    carimbo: bool = False
    observacoes: Optional[str] = None

class AgendaCreate(BaseModel):
    data: date
    turno: str
    especialidade_id: int
    local_estudo_id: int
    aluno_id: int
    responsavel: str
    observacoes: Optional[str] = None

class AgendaLoteCreate(BaseModel):
    data_inicio: date
    data_fim: date
    turno: str
    especialidade_id: int
    local_estudo_id: int
    alunos_ids: List[int]
    responsavel: str
    observacoes: Optional[str] = None

class PresencaRequest(BaseModel):
    aluno_id: int
    data: date
    observacoes: str
    horas: int
    tipo: str

class PresencaResponse(BaseModel):
    message: str
    presenca: dict

class LocalEspecialidade(BaseModel):
    local_id: int
    especialidade_id: int
    responsavel: str
