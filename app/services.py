
import json
from typing import List, Optional
from app.models import Aluno, AlunoCreate, Especialidade, Local, Agenda, User, AgendaCreate, PresencaRequest, EspecialidadeCompleta, LocalEstudo, AgendaLoteCreate
from datetime import date, timedelta

DATA_DIR = "app/data"

# Funções de autenticação
def get_users() -> List[User]:
    with open(f"{DATA_DIR}/users.json", "r") as f:
        users_data = json.load(f)
    return [User(**user) for user in users_data]

def authenticate_user(email: str, data_nascimento: str) -> Optional[dict]:
    # Primeiro, tentar autenticar como usuário do sistema
    users = get_users()
    try:
        data_obj = date.fromisoformat(data_nascimento)
        for user in users:
            if user.email == email and user.data_nascimento == data_obj:
                return {
                    "id": user.id,
                    "email": user.email,
                    "nome": user.nome,
                    "data_nascimento": user.data_nascimento,
                    "telefone": user.telefone,
                    "role": user.role,
                    "tipo": "usuario"
                }
    except ValueError:
        pass
    
    # Se não encontrou como usuário, tentar como aluno
    alunos = get_alunos()
    try:
        data_obj = date.fromisoformat(data_nascimento)
        for aluno in alunos:
            if aluno.email == email and aluno.data_nascimento == data_obj:
                return {
                    "id": aluno.id,
                    "email": aluno.email,
                    "nome": aluno.nome,
                    "data_nascimento": aluno.data_nascimento,
                    "telefone": aluno.telefone,
                    "role": "aluno",
                    "especialidade_principal": aluno.especialidade_principal,
                    "tipo": "aluno"
                }
    except ValueError:
        pass
    
    return None

# Funções existentes
def get_alunos() -> List[Aluno]:
    with open(f"{DATA_DIR}/alunos.json", "r") as f:
        alunos_data = json.load(f)
    return [Aluno(**aluno) for aluno in alunos_data]

def add_aluno(aluno: AlunoCreate):
    alunos = get_alunos()
    if not any(a.email == aluno.email for a in alunos):
        # Gerar ID único
        if alunos:
            aluno_id = max(a.id for a in alunos) + 1
        else:
            aluno_id = 1
        
        # Criar objeto Aluno completo
        novo_aluno = Aluno(
            id=aluno_id,
            nome=aluno.nome,
            email=aluno.email,
            telefone=aluno.telefone,
            data_nascimento=aluno.data_nascimento,
            especialidade_principal=aluno.especialidade_principal
        )
        
        alunos.append(novo_aluno)
        with open(f"{DATA_DIR}/alunos.json", "w") as f:
            json.dump([a.dict() for a in alunos], f, indent=2, default=str)

def update_aluno(aluno_id: int, aluno_update: Aluno) -> bool:
    alunos = get_alunos()
    for i, aluno in enumerate(alunos):
        if aluno.id == aluno_id:
            # Manter o ID original
            aluno_update.id = aluno_id
            alunos[i] = aluno_update
            with open(f"{DATA_DIR}/alunos.json", "w") as f:
                json.dump([a.dict() for a in alunos], f, indent=2, default=str)
            return True
    return False

def delete_aluno(aluno_id: int) -> bool:
    alunos = get_alunos()
    for i, aluno in enumerate(alunos):
        if aluno.id == aluno_id:
            alunos.pop(i)
            with open(f"{DATA_DIR}/alunos.json", "w") as f:
                json.dump([a.dict() for a in alunos], f, indent=2, default=str)
            return True
    return False

def get_especialidades() -> List[Especialidade]:
    with open(f"{DATA_DIR}/especialidades.json", "r") as f:
        especialidades_data = json.load(f)
    return [Especialidade(**especialidade) for especialidade in especialidades_data]

def add_especialidade(especialidade: Especialidade):
    especialidades = get_especialidades()
    if not any(e.nome == especialidade.nome for e in especialidades):
        # Gerar ID único
        if especialidades:
            especialidade.id = max(e.id for e in especialidades) + 1
        else:
            especialidade.id = 1
        especialidades.append(especialidade)
        with open(f"{DATA_DIR}/especialidades.json", "w") as f:
            json.dump([e.dict() for e in especialidades], f, indent=2, default=str)

def get_locais() -> List[Local]:
    with open(f"{DATA_DIR}/locais.json", "r") as f:
        locais_data = json.load(f)
    return [Local(**local) for local in locais_data]

def add_local(local: Local):
    locais = get_locais()
    if not any(l.nome == local.nome for l in locais):
        # Gerar ID único
        if locais:
            local.id = max(l.id for l in locais) + 1
        else:
            local.id = 1
        locais.append(local)
        with open(f"{DATA_DIR}/locais.json", "w") as f:
            json.dump([l.dict() for l in locais], f, indent=2, default=str)

# Nova função para obter dados completos do dados.json
def get_dados_completos() -> dict:
    with open(f"{DATA_DIR}/dados.json", "r") as f:
        return json.load(f)

def get_especialidades_completas() -> List[EspecialidadeCompleta]:
    dados = get_dados_completos()
    return [EspecialidadeCompleta(**especialidade) for especialidade in dados["especialidades"]]

def get_locais_estudo() -> List[LocalEstudo]:
    especialidades = get_especialidades_completas()
    locais = []
    for especialidade in especialidades:
        for local in especialidade.locais:
            locais.append(local)
    return locais

def get_locais_por_especialidade(especialidade_id: int) -> List[LocalEstudo]:
    especialidades = get_especialidades_completas()
    for especialidade in especialidades:
        if especialidade.especialidade_id == especialidade_id:
            return especialidade.locais
    return []

def get_local_estudo_by_id(local_id: int) -> Optional[LocalEstudo]:
    especialidades = get_especialidades_completas()
    for especialidade in especialidades:
        for local in especialidade.locais:
            if local.local_id == local_id:
                return local
    return None

def get_especialidade_by_id(especialidade_id: int) -> Optional[EspecialidadeCompleta]:
    especialidades = get_especialidades_completas()
    for especialidade in especialidades:
        if especialidade.especialidade_id == especialidade_id:
            return especialidade
    return None

def get_agendas() -> List[Agenda]:
    with open(f"{DATA_DIR}/agendas.json", "r") as f:
        agendas_data = json.load(f)
    return [Agenda(**agenda) for agenda in agendas_data]

def get_agenda_por_aluno(aluno_id: int, data_inicio: date, data_fim: date) -> List[Agenda]:
    agendas = get_agendas()
    return [agenda for agenda in agendas if agenda.aluno_id == aluno_id and data_inicio <= agenda.data <= data_fim]

def add_agenda(agenda: AgendaCreate):
    agendas = get_agendas()
    # Buscar nome do aluno
    alunos = get_alunos()
    aluno = next((a for a in alunos if a.id == agenda.aluno_id), None)
    if not aluno:
        raise ValueError("Aluno não encontrado")
    
    # Buscar dados da especialidade e local de estudo
    especialidade = get_especialidade_by_id(agenda.especialidade_id)
    if not especialidade:
        raise ValueError("Especialidade não encontrada")
    
    local_estudo = get_local_estudo_by_id(agenda.local_estudo_id)
    if not local_estudo:
        raise ValueError("Local de estudo não encontrado")
    
    # Verificar se o local pertence à especialidade
    if local_estudo not in especialidade.locais:
        raise ValueError("Local de estudo não pertence à especialidade")
    
    # Verificar capacidade do local para a data
    agendas_mesmo_local_data = [a for a in agendas 
                               if a.local_estudo_id == agenda.local_estudo_id 
                               and a.data == agenda.data 
                               and a.turno == agenda.turno]
    
    if len(agendas_mesmo_local_data) >= local_estudo.capacidade_alunos:
        raise ValueError(f"Local de estudo já está na capacidade máxima ({local_estudo.capacidade_alunos} alunos)")
    
    # Gerar ID único
    if agendas:
        agenda_id = max(a.id for a in agendas) + 1
    else:
        agenda_id = 1
    
    new_agenda = Agenda(
        id=agenda_id,
        data=agenda.data,
        turno=agenda.turno,
        especialidade=especialidade.nome_especialidade,
        especialidade_id=agenda.especialidade_id,
        local_estudo_id=agenda.local_estudo_id,
        local_estudo_nome=local_estudo.nome_local,
        aluno_id=agenda.aluno_id,
        aluno_nome=aluno.nome,
        responsavel=agenda.responsavel,
        presenca=False,
        carimbo=False,
        observacoes=agenda.observacoes
    )
    agendas.append(new_agenda)
    with open(f"{DATA_DIR}/agendas.json", "w") as f:
        json.dump([a.dict() for a in agendas], f, indent=2, default=str)

def add_agenda_lote(agenda_lote: AgendaLoteCreate):
    """Criar agendas em lote para múltiplos alunos"""
    agendas_criadas = []
    erros = []
    
    # Verificar dados básicos
    especialidade = get_especialidade_by_id(agenda_lote.especialidade_id)
    if not especialidade:
        raise ValueError("Especialidade não encontrada")
    
    local_estudo = get_local_estudo_by_id(agenda_lote.local_estudo_id)
    if not local_estudo:
        raise ValueError("Local de estudo não encontrado")
    
    # Verificar se o local pertence à especialidade
    if local_estudo not in especialidade.locais:
        raise ValueError("Local de estudo não pertence à especialidade")
    
    # Buscar alunos
    alunos = get_alunos()
    alunos_ids = [a.id for a in alunos]
    
    # Verificar se todos os alunos existem
    for aluno_id in agenda_lote.alunos_ids:
        if aluno_id not in alunos_ids:
            erros.append(f"Aluno ID {aluno_id} não encontrado")
    
    if erros:
        raise ValueError(f"Erros encontrados: {'; '.join(erros)}")
    
    # Criar agendas para cada data e aluno
    from datetime import timedelta
    current_date = agenda_lote.data_inicio
    agendas = get_agendas()
    
    while current_date <= agenda_lote.data_fim:
        # Pular finais de semana (sábado=5, domingo=6)
        if current_date.weekday() < 5:  # Segunda a sexta
            for aluno_id in agenda_lote.alunos_ids:
                # Verificar se já existe agenda para este aluno nesta data/turno
                agenda_existente = next((a for a in agendas 
                                       if a.aluno_id == aluno_id 
                                       and a.data == current_date 
                                       and a.turno == agenda_lote.turno), None)
                
                if agenda_existente:
                    erros.append(f"Aluno {aluno_id} já tem agenda para {current_date} - {agenda_lote.turno}")
                    continue
                
                # Verificar capacidade do local
                agendas_mesmo_local_data = [a for a in agendas 
                                           if a.local_estudo_id == agenda_lote.local_estudo_id 
                                           and a.data == current_date 
                                           and a.turno == agenda_lote.turno]
                
                if len(agendas_mesmo_local_data) >= local_estudo.capacidade_alunos:
                    erros.append(f"Local {local_estudo.nome_local} já está na capacidade máxima para {current_date} - {agenda_lote.turno}")
                    continue
                
                # Buscar nome do aluno
                aluno = next((a for a in alunos if a.id == aluno_id), None)
                
                # Gerar ID único
                if agendas:
                    agenda_id = max(a.id for a in agendas) + 1
                else:
                    agenda_id = 1
                
                new_agenda = Agenda(
                    id=agenda_id,
                    data=current_date,
                    turno=agenda_lote.turno,
                    especialidade=especialidade.nome_especialidade,
                    especialidade_id=agenda_lote.especialidade_id,
                    local_estudo_id=agenda_lote.local_estudo_id,
                    local_estudo_nome=local_estudo.nome_local,
                    aluno_id=aluno_id,
                    aluno_nome=aluno.nome,
                    responsavel=agenda_lote.responsavel,
                    presenca=False,
                    carimbo=False,
                    observacoes=agenda_lote.observacoes
                )
                agendas.append(new_agenda)
                agendas_criadas.append(new_agenda)
        
        current_date += timedelta(days=1)
    
    # Salvar todas as agendas
    with open(f"{DATA_DIR}/agendas.json", "w") as f:
        json.dump([a.dict() for a in agendas], f, indent=2, default=str)
    
    return {
        "agendas_criadas": len(agendas_criadas),
        "erros": erros,
        "agendas": agendas_criadas
    }

def registrar_presenca(aluno_id: int, data: date):
    agendas = get_agendas()
    for agenda in agendas:
        if agenda.aluno_id == aluno_id and agenda.data == data:
            agenda.presenca = True
            agenda.carimbo = True
            break
    with open(f"{DATA_DIR}/agendas.json", "w") as f:
        json.dump([a.dict() for a in agendas], f, indent=2, default=str)

def registrar_presenca_completa(aluno_id: int, data: date, presenca: PresencaRequest):
    agendas = get_agendas()
    for agenda in agendas:
        if agenda.aluno_id == aluno_id and agenda.data == data:
            agenda.presenca = True
            agenda.carimbo = True
            # Atualizar observações com as informações da presença
            agenda.observacoes = f"PRESENÇA REGISTRADA - {presenca.observacoes} | Horas: {presenca.horas}h | Tipo: {presenca.tipo}"
            break
    with open(f"{DATA_DIR}/agendas.json", "w") as f:
        json.dump([a.dict() for a in agendas], f, indent=2, default=str)

def get_dashboard_data():
    agendas = get_agendas()
    alunos = get_alunos()
    
    # Alunos por especialidade hoje
    alunos_por_especialidade = {}
    for agenda in agendas:
        if agenda.data == date.today():
            if agenda.especialidade not in alunos_por_especialidade:
                alunos_por_especialidade[agenda.especialidade] = []
            if agenda.aluno_nome not in alunos_por_especialidade[agenda.especialidade]:
                alunos_por_especialidade[agenda.especialidade].append(agenda.aluno_nome)
    
    # Alunos com menos de 6 carimbos na semana
    from datetime import timedelta
    inicio_semana = date.today() - timedelta(days=date.today().weekday())
    fim_semana = inicio_semana + timedelta(days=6)
    
    alunos_sem_carimbo = []
    for aluno in alunos:
        agendas_aluno = [agenda for agenda in agendas 
                        if agenda.aluno_id == aluno.id 
                        and inicio_semana <= agenda.data <= fim_semana]
        carimbos = sum(1 for agenda in agendas_aluno if agenda.carimbo)
        if carimbos < 6:
            alunos_sem_carimbo.append({
                "nome": aluno.nome,
                "carimbos": carimbos
            })
    
    return {
        "alunos_por_especialidade_hoje": alunos_por_especialidade,
        "alunos_com_menos_de_6_carimbos": alunos_sem_carimbo,
        "total_alunos": len(alunos),
        "total_agendas_hoje": len([a for a in agendas if a.data == date.today()])
    }

def get_aluno_by_email(email: str) -> Optional[Aluno]:
    alunos = get_alunos()
    return next((aluno for aluno in alunos if aluno.email == email), None)

def get_aluno_by_id(aluno_id: int) -> Optional[Aluno]:
    alunos = get_alunos()
    return next((aluno for aluno in alunos if aluno.id == aluno_id), None)

def get_colegas_agenda(aluno_id: int, data: str, especialidade_id: int, local_id: int) -> List[dict]:
    """Busca colegas que estão na mesma agenda (mesmo local, mesma data, mesma especialidade)"""
    agendas = get_agendas()
    colegas = []
    
    for agenda in agendas:
        if (agenda.aluno_id != aluno_id and 
            agenda.data.isoformat() == data and 
            agenda.especialidade_id == especialidade_id and 
            agenda.local_estudo_id == local_id):
            
            colegas.append({
                "id": agenda.aluno_id,
                "nome": agenda.aluno_nome,
                "turno": agenda.turno
            })
    
    return colegas

# Nova função para obter dados do dashboard do aluno
def get_aluno_dashboard_data(aluno_id: int):
    agendas = get_agendas()
    alunos = get_alunos()
    aluno = next((a for a in alunos if a.id == aluno_id), None)
    
    if not aluno:
        return None
    
    # Agendas do aluno
    agendas_aluno = [a for a in agendas if a.aluno_id == aluno_id]
    
    # Estatísticas da semana
    inicio_semana = date.today() - timedelta(days=date.today().weekday())
    fim_semana = inicio_semana + timedelta(days=6)
    
    agendas_semana = [a for a in agendas_aluno if inicio_semana <= a.data <= fim_semana]
    carimbos_semana = sum(1 for a in agendas_semana if a.carimbo)
    
    # Próximas agendas com informações de colegas
    hoje = date.today()
    proximas_agendas = [a for a in agendas_aluno if a.data >= hoje]
    proximas_agendas.sort(key=lambda x: x.data)
    
    # Para cada agenda próxima, buscar colegas no mesmo local e data
    agendas_com_colegas = []
    for agenda in proximas_agendas:
        colegas = []
        for a in agendas:
            if (a.aluno_id != aluno_id and 
                a.data == agenda.data and 
                a.local_estudo_id == agenda.local_estudo_id and
                a.turno == agenda.turno):
                colega = next((al for al in alunos if al.id == a.aluno_id), None)
                if colega:
                    colegas.append({
                        "nome": colega.nome,
                        "email": colega.email
                    })
        
        # Criar dicionário com dados da agenda e colegas
        agenda_dict = agenda.dict()
        agenda_dict["colegas"] = colegas
        agendas_com_colegas.append(agenda_dict)
    
    return {
        "aluno": aluno,
        "total_agendas": len(agendas_aluno),
        "carimbos_semana": carimbos_semana,
        "proximas_agendas": agendas_com_colegas[:5],  # Próximas 5 agendas
        "agendas_semana": agendas_semana
    }

def get_distribuicao_carga_horaria():
    """Gera dados para visualização da distribuição de carga horária"""
    agendas = get_agendas()
    alunos = get_alunos()
    especialidades = get_especialidades_completas()
    
    # Estatísticas gerais
    hoje = date.today()
    inicio_semana = hoje - timedelta(days=hoje.weekday())
    fim_semana = inicio_semana + timedelta(days=6)
    
    agendas_semana = [a for a in agendas if inicio_semana <= a.data <= fim_semana]
    total_agendas_semana = len(agendas_semana)
    
    # Calcular carimbos por aluno
    carimbos_por_aluno = {}
    for aluno in alunos:
        agendas_aluno_semana = [a for a in agendas_semana if a.aluno_id == aluno.id]
        carimbos = sum(1 for a in agendas_aluno_semana if a.carimbo)
        carimbos_por_aluno[aluno.id] = carimbos
    
    media_carimbos = sum(carimbos_por_aluno.values()) / len(alunos) if alunos else 0
    alunos_em_risco = sum(1 for carimbos in carimbos_por_aluno.values() if carimbos < 4)
    
    # Distribuição por especialidade
    distribuicao_especialidades = []
    for especialidade in especialidades:
        agendas_especialidade = [a for a in agendas_semana if a.especialidade_id == especialidade.especialidade_id]
        alunos_especialidade = list(set([a.aluno_id for a in agendas_especialidade]))
        
        if alunos_especialidade:
            carimbos_especialidade = [carimbos_por_aluno.get(aluno_id, 0) for aluno_id in alunos_especialidade]
            media_carimbos_esp = sum(carimbos_especialidade) / len(carimbos_especialidade)
        else:
            media_carimbos_esp = 0
        
        distribuicao_especialidades.append({
            "nome": especialidade.nome_especialidade,
            "cor": especialidade.cor_interface,
            "total_alunos": len(alunos_especialidade),
            "total_agendas": len(agendas_especialidade),
            "media_carimbos": media_carimbos_esp
        })
    
    # Distribuição por aluno
    distribuicao_alunos = []
    for aluno in alunos:
        agendas_aluno_semana = [a for a in agendas_semana if a.aluno_id == aluno.id]
        especialidades_aluno = list(set([a.especialidade for a in agendas_aluno_semana]))
        
        distribuicao_alunos.append({
            "nome": aluno.nome,
            "email": aluno.email,
            "carimbos_semana": carimbos_por_aluno.get(aluno.id, 0),
            "especialidades": especialidades_aluno
        })
    
    # Distribuição semanal
    dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    distribuicao_semanal = []
    
    for i, dia_nome in enumerate(dias_semana):
        dia_data = inicio_semana + timedelta(days=i)
        agendas_dia = [a for a in agendas_semana if a.data == dia_data]
        especialidades_dia = list(set([a.especialidade for a in agendas_dia]))
        
        distribuicao_semanal.append({
            "nome": dia_nome,
            "data": dia_data,
            "total_agendas": len(agendas_dia),
            "especialidades": especialidades_dia
        })
    
    # Capacidade dos locais de estudo
    locais_estudo = []
    for especialidade in especialidades:
        for local in especialidade.locais:
            agendas_local_hoje = [a for a in agendas if a.local_estudo_id == local.local_id and a.data == hoje]
            ocupacao = (len(agendas_local_hoje) / local.capacidade_alunos) * 100 if local.capacidade_alunos > 0 else 0
            
            locais_estudo.append({
                "nome_local": local.nome_local,
                "especialidade": especialidade.nome_especialidade,
                "capacidade": local.capacidade_alunos,
                "agendas_hoje": len(agendas_local_hoje),
                "ocupacao": ocupacao
            })
    
    return {
        "total_alunos": len(alunos),
        "total_agendas_semana": total_agendas_semana,
        "media_carimbos_semana": round(media_carimbos, 1),
        "alunos_em_risco": alunos_em_risco,
        "distribuicao_especialidades": distribuicao_especialidades,
        "distribuicao_alunos": distribuicao_alunos,
        "distribuicao_semanal": distribuicao_semanal,
        "locais_estudo": locais_estudo,
        "especialidades": especialidades
    }

def delete_agenda(agenda_id: int) -> bool:
    """Excluir agenda por ID"""
    agendas = get_agendas()
    for i, agenda in enumerate(agendas):
        if agenda.id == agenda_id:
            agendas.pop(i)
            with open(f"{DATA_DIR}/agendas.json", "w") as f:
                json.dump([a.dict() for a in agendas], f, indent=2, default=str)
            return True
    return False

def delete_agenda_by_aluno_data(aluno_id: int, data: date) -> bool:
    """Excluir agenda por aluno e data"""
    agendas = get_agendas()
    for i, agenda in enumerate(agendas):
        if agenda.aluno_id == aluno_id and agenda.data == data:
            agendas.pop(i)
            with open(f"{DATA_DIR}/agendas.json", "w") as f:
                json.dump([a.dict() for a in agendas], f, indent=2, default=str)
            return True
    return False

def delete_agendas_lote(agenda_ids: List[int]) -> dict:
    """Excluir múltiplas agendas por IDs"""
    agendas = get_agendas()
    excluidas = 0
    erros = []
    
    # Criar um conjunto de IDs para busca mais eficiente
    ids_to_delete = set(agenda_ids)
    
    # Filtrar agendas que devem ser excluídas
    agendas_restantes = []
    for agenda in agendas:
        if agenda.id in ids_to_delete:
            excluidas += 1
        else:
            agendas_restantes.append(agenda)
    
    # Verificar se todos os IDs foram encontrados
    ids_encontrados = set(agenda.id for agenda in agendas if agenda.id in ids_to_delete)
    ids_nao_encontrados = ids_to_delete - ids_encontrados
    
    if ids_nao_encontrados:
        erros.append(f"IDs não encontrados: {list(ids_nao_encontrados)}")
    
    # Salvar agendas restantes
    with open(f"{DATA_DIR}/agendas.json", "w") as f:
        json.dump([a.dict() for a in agendas_restantes], f, indent=2, default=str)
    
    return {
        "excluidas": excluidas,
        "erros": erros
    }
