
from fastapi import APIRouter, HTTPException
from typing import List
from app import services
from app.models import Aluno, AlunoCreate, Especialidade, Local, Agenda, AgendaCreate, PresencaRequest, EspecialidadeCompleta, LocalEstudo, AgendaLoteCreate
from datetime import date

router = APIRouter()

@router.get("/alunos", response_model=List[Aluno])
def get_alunos():
    return services.get_alunos()

@router.get("/alunos/{aluno_id}", response_model=Aluno)
def get_aluno(aluno_id: int):
    aluno = services.get_aluno_by_id(aluno_id)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno

@router.post("/alunos")
def add_aluno(aluno: AlunoCreate):
    services.add_aluno(aluno)
    return {"message": "Aluno adicionado com sucesso"}

@router.put("/alunos/{aluno_id}")
def update_aluno(aluno_id: int, aluno: Aluno):
    if services.update_aluno(aluno_id, aluno):
        return {"message": "Aluno atualizado com sucesso"}
    raise HTTPException(status_code=404, detail="Aluno não encontrado")

@router.delete("/alunos/{aluno_id}")
def delete_aluno(aluno_id: int):
    if services.delete_aluno(aluno_id):
        return {"message": "Aluno excluído com sucesso"}
    raise HTTPException(status_code=404, detail="Aluno não encontrado")

@router.get("/especialidades", response_model=List[Especialidade])
def get_especialidades():
    return services.get_especialidades()

@router.post("/especialidades")
def add_especialidade(especialidade: Especialidade):
    services.add_especialidade(especialidade)
    return {"message": "Especialidade adicionada com sucesso"}

@router.get("/especialidades-completas", response_model=List[EspecialidadeCompleta])
def get_especialidades_completas():
    return services.get_especialidades_completas()

@router.get("/locais", response_model=List[Local])
def get_locais():
    return services.get_locais()

@router.post("/locais")
def add_local(local: Local):
    services.add_local(local)
    return {"message": "Local adicionado com sucesso"}

@router.get("/locais-estudo", response_model=List[LocalEstudo])
def get_locais_estudo():
    return services.get_locais_estudo()

@router.get("/locais-estudo/{especialidade_id}", response_model=List[LocalEstudo])
def get_locais_por_especialidade(especialidade_id: int):
    return services.get_locais_por_especialidade(especialidade_id)

@router.get("/agendas", response_model=List[Agenda])
def get_agendas():
    return services.get_agendas()

@router.get("/agendas/periodo", response_model=List[Agenda])
def get_agendas_por_periodo(data_inicio: date, data_fim: date):
    """Buscar agendas por período específico"""
    agendas = services.get_agendas()
    return [agenda for agenda in agendas if data_inicio <= agenda.data <= data_fim]

@router.get("/agendas/{aluno_id}", response_model=List[Agenda])
def get_agenda_por_aluno(aluno_id: int, data_inicio: date, data_fim: date):
    return services.get_agenda_por_aluno(aluno_id, data_inicio, data_fim)

@router.post("/agendas")
def add_agenda(agenda: AgendaCreate):
    try:
        services.add_agenda(agenda)
        return {"message": "Agenda adicionada com sucesso"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/agendas/lote")
def add_agenda_lote(agenda_lote: AgendaLoteCreate):
    try:
        result = services.add_agenda_lote(agenda_lote)
        return {
            "message": f"Agendas criadas em lote: {result['agendas_criadas']} criadas",
            "agendas_criadas": result["agendas_criadas"],
            "erros": result["erros"]
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/agendas/lote")
def delete_agendas_lote(agenda_ids: List[int]):
    """Excluir múltiplas agendas por IDs"""
    try:
        result = services.delete_agendas_lote(agenda_ids)
        return {
            "message": f"Exclusão em lote concluída: {result['excluidas']} agendas excluídas",
            "excluidas": result["excluidas"],
            "erros": result["erros"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao excluir agendas em lote: {str(e)}")

@router.delete("/agendas/{agenda_id}")
def delete_agenda_by_id(agenda_id: int):
    """Excluir agenda por ID"""
    try:
        if services.delete_agenda(agenda_id):
            return {"message": "Agenda excluída com sucesso"}
        else:
            raise HTTPException(status_code=404, detail="Agenda não encontrada")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao excluir agenda: {str(e)}")

@router.delete("/agendas/{aluno_id}/{data}")
def delete_agenda(aluno_id: int, data: str):
    """Excluir agenda por aluno e data (mantido para compatibilidade)"""
    try:
        data_obj = date.fromisoformat(data)
        if services.delete_agenda_by_aluno_data(aluno_id, data_obj):
            return {"message": "Agenda excluída com sucesso"}
        else:
            raise HTTPException(status_code=404, detail="Agenda não encontrada")
    except ValueError:
        raise HTTPException(status_code=400, detail="Data inválida")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao excluir agenda: {str(e)}")

@router.post("/presenca/{aluno_id}/{data}")
def registrar_presenca(aluno_id: int, data: str, presenca: PresencaRequest):
    try:
        data_obj = date.fromisoformat(data)
        services.registrar_presenca_completa(aluno_id, data_obj, presenca)
        return {"message": "Presença registrada com sucesso"}
    except ValueError:
        raise HTTPException(status_code=400, detail="Data inválida")

@router.get("/dashboard")
def get_dashboard():
    return services.get_dashboard_data()
