#!/usr/bin/env python3
"""
Script para gerar distribuição ideal das agendas
Período: 04/08/2025 a 05/10/2025
"""

import json
from datetime import date, timedelta
from typing import List, Dict
import random

# Configurações
DATA_INICIO = date(2025, 8, 4)
DATA_FIM = date(2025, 10, 5)

# Carregar dados
def carregar_dados():
    with open("app/data/alunos.json", "r") as f:
        alunos = json.load(f)
    
    with open("app/data/dados.json", "r") as f:
        dados = json.load(f)
    
    return alunos, dados

def gerar_distribuicao_ideal():
    alunos, dados = carregar_dados()
    
    # Estrutura para armazenar agendas
    agendas = []
    agenda_id = 1
    
    # Mapear especialidades e locais
    especialidades_locais = {}
    for especialidade in dados["especialidades"]:
        especialidades_locais[especialidade["especialidade_id"]] = {
            "nome": especialidade["nome_especialidade"],
            "locais": especialidade["locais"]
        }
    
    # Distribuir alunos por especialidades (rotação)
    alunos_por_especialidade = {}
    for i, aluno in enumerate(alunos):
        # Rotacionar especialidades: 1, 2, 3, 4, 1, 2, 3, 4...
        esp_id = (i % 4) + 1  # 1=Enfermaria, 2=Ortopedia, 3=Cirurgia Geral, 4=GO
        if esp_id not in alunos_por_especialidade:
            alunos_por_especialidade[esp_id] = []
        alunos_por_especialidade[esp_id].append(aluno)
    
    # Calcular datas úteis (segunda a sexta)
    datas_uteis = []
    current_date = DATA_INICIO
    while current_date <= DATA_FIM:
        if current_date.weekday() < 5:  # Segunda a sexta
            datas_uteis.append(current_date)
        current_date += timedelta(days=1)
    
    # Distribuição por semana
    semanas = []
    for i in range(0, len(datas_uteis), 5):
        semana = datas_uteis[i:i+5]
        if semana:
            semanas.append(semana)
    
    # Gerar agendas para cada semana
    for semana_idx, semana in enumerate(semanas):
        print(f"Gerando semana {semana_idx + 1}: {semana[0]} a {semana[-1]}")
        
        # Distribuir especialidades por dia da semana
        especialidades_dia = {
            0: [1, 3, 4],  # Segunda: Enfermaria, Cirurgia Geral, GO
            1: [2, 6, 8],  # Terça: Ortopedia, Vascular, Urologia
            2: [1, 3, 5],  # Quarta: Enfermaria, Cirurgia Geral, Otorrino
            3: [2, 4, 7],  # Quinta: Ortopedia, GO, Pediátrica
            4: [1, 3, 6]   # Sexta: Enfermaria, Cirurgia Geral, Vascular
        }
        
        for dia_idx, data in enumerate(semana):
            if dia_idx not in especialidades_dia:
                continue
                
            especialidades_do_dia = especialidades_dia[dia_idx]
            
            for especialidade_id in especialidades_do_dia:
                if especialidade_id not in especialidades_locais:
                    continue
                    
                especialidade = especialidades_locais[especialidade_id]
                locais_disponiveis = especialidade["locais"]
                
                # Distribuir alunos da especialidade
                alunos_especialidade = alunos_por_especialidade.get(especialidade_id, [])
                
                for local in locais_disponiveis:
                    capacidade = local["capacidade_alunos"]
                    
                    # Selecionar alunos para este local
                    alunos_local = []
                    for aluno in alunos_especialidade:
                        if len(alunos_local) < capacidade:
                            # Verificar se aluno já tem agenda neste dia
                            ja_tem_agenda = any(
                                a["aluno_id"] == aluno["id"] and a["data"] == data.isoformat()
                                for a in agendas
                            )
                            
                            if not ja_tem_agenda:
                                alunos_local.append(aluno)
                    
                    # Criar agendas para os alunos selecionados
                    for i, aluno in enumerate(alunos_local):
                        # Alternar entre manhã e tarde
                        turno = "Manhã" if i % 2 == 0 else "Tarde"
                        
                        agenda = {
                            "id": agenda_id,
                            "data": data.isoformat(),
                            "turno": turno,
                            "especialidade": especialidade["nome"],
                            "especialidade_id": especialidade_id,
                            "local_estudo_id": local["local_id"],
                            "local_estudo_nome": local["nome_local"],
                            "aluno_id": aluno["id"],
                            "aluno_nome": aluno["nome"],
                            "responsavel": local["medico_responsavel"]["nome"],
                            "presenca": False,
                            "carimbo": False,
                            "observacoes": ""
                        }
                        
                        agendas.append(agenda)
                        agenda_id += 1
    
    # Adicionar algumas agendas extras para garantir que todos os alunos tenham pelo menos algumas agendas
    for aluno in alunos:
        # Verificar se o aluno tem poucas agendas
        agendas_aluno = [a for a in agendas if a["aluno_id"] == aluno["id"]]
        if len(agendas_aluno) < 3:  # Se tem menos de 3 agendas
            # Adicionar algumas agendas extras
            for i in range(3 - len(agendas_aluno)):
                # Escolher uma data aleatória no período
                dias_aleatorios = random.randint(0, len(datas_uteis) - 1)
                data_aleatoria = datas_uteis[dias_aleatorios]
                
                # Escolher uma especialidade aleatória
                esp_id = random.randint(1, 4)
                if esp_id in especialidades_locais:
                    especialidade = especialidades_locais[esp_id]
                    local = random.choice(especialidade["locais"])
                    
                    # Verificar se não há conflito
                    ja_tem_agenda = any(
                        a["aluno_id"] == aluno["id"] and a["data"] == data_aleatoria.isoformat()
                        for a in agendas
                    )
                    
                    if not ja_tem_agenda:
                        agenda = {
                            "id": agenda_id,
                            "data": data_aleatoria.isoformat(),
                            "turno": "Manhã" if i % 2 == 0 else "Tarde",
                            "especialidade": especialidade["nome"],
                            "especialidade_id": esp_id,
                            "local_estudo_id": local["local_id"],
                            "local_estudo_nome": local["nome_local"],
                            "aluno_id": aluno["id"],
                            "aluno_nome": aluno["nome"],
                            "responsavel": local["medico_responsavel"]["nome"],
                            "presenca": False,
                            "carimbo": False,
                            "observacoes": ""
                        }
                        
                        agendas.append(agenda)
                        agenda_id += 1
    
    # Salvar agendas
    with open("app/data/agendas.json", "w") as f:
        json.dump(agendas, f, indent=2, default=str)
    
    print(f"\n✅ Distribuição concluída!")
    print(f"📊 Total de agendas geradas: {len(agendas)}")
    print(f"📅 Período: {DATA_INICIO} a {DATA_FIM}")
    print(f"👥 Alunos distribuídos: {len(alunos)}")
    
    # Estatísticas por especialidade
    print("\n📈 Estatísticas por Especialidade:")
    stats = {}
    for agenda in agendas:
        esp = agenda["especialidade"]
        if esp not in stats:
            stats[esp] = 0
        stats[esp] += 1
    
    for esp, count in sorted(stats.items()):
        print(f"  • {esp}: {count} agendas")
    
    # Estatísticas por aluno
    print("\n👥 Estatísticas por Aluno:")
    for aluno in alunos:
        agendas_aluno = [a for a in agendas if a["aluno_id"] == aluno["id"]]
        print(f"  • {aluno['nome']}: {len(agendas_aluno)} agendas")

if __name__ == "__main__":
    gerar_distribuicao_ideal() 