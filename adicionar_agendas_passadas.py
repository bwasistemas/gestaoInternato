#!/usr/bin/env python3
"""
Script para adicionar agendas passadas para testar as ações
"""

import json
from datetime import date, timedelta

# Carregar agendas existentes
with open("app/data/agendas.json", "r") as f:
    agendas = json.load(f)

# Adicionar algumas agendas passadas para o aluno Farley (ID 2)
aluno_id = 2
datas_passadas = [
    "2025-07-28",  # Segunda-feira passada
    "2025-07-29",  # Terça-feira passada
    "2025-07-30",  # Quarta-feira passada
    "2025-07-31",  # Quinta-feira passada
    "2025-08-01",  # Sexta-feira passada
    "2025-08-02",  # Sábado passado
]

novas_agendas = []
for i, data_str in enumerate(datas_passadas):
    data_obj = date.fromisoformat(data_str)
    
    # Alternar entre especialidades
    especialidade_id = (i % 4) + 1
    especialidades = {
        1: "Enfermaria Cirúrgica",
        2: "Ortopedia", 
        3: "Cirurgia Geral",
        4: "Ginecologia/Obstetrícia"
    }
    
    # Alternar turnos
    turno = "Manhã" if i % 2 == 0 else "Tarde"
    
    nova_agenda = {
        "id": len(agendas) + i + 1,
        "data": data_str,
        "turno": turno,
        "especialidade": especialidades[especialidade_id],
        "especialidade_id": especialidade_id,
        "local_estudo_id": 1,
        "local_estudo_nome": f"{especialidades[especialidade_id]} ID: 1",
        "aluno_id": aluno_id,
        "aluno_nome": "Farley Eleandro Costa",
        "responsavel": f"Dr. Responsável {especialidades[especialidade_id]}",
        "presenca": False,
        "carimbo": False,
        "observacoes": None
    }
    
    novas_agendas.append(nova_agenda)

# Adicionar às agendas existentes
agendas.extend(novas_agendas)

# Salvar
with open("app/data/agendas.json", "w") as f:
    json.dump(agendas, f, indent=2, default=str)

print(f"✅ Adicionadas {len(novas_agendas)} agendas passadas para o aluno Farley (ID {aluno_id})")
print("📅 Datas adicionadas:")
for agenda in novas_agendas:
    print(f"  • {agenda['data']} - {agenda['turno']} - {agenda['especialidade']}") 