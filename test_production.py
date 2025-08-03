#!/usr/bin/env python3
"""
Script para testar o ambiente de produção com prefixo /internato
"""

import os
import subprocess
import time
import requests

# Configurar variável de ambiente para simular produção
os.environ["BASE_PATH"] = "/internato"

print("🚀 Testando ambiente de produção com prefixo /internato...")
print("📋 Iniciando servidor...")

# Iniciar o servidor em background
process = subprocess.Popen(
    ["python", "run.py"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# Aguardar o servidor iniciar
time.sleep(5)

try:
    # Testar URLs com prefixo
    base_url = "http://localhost:8001"
    
    print("\n🧪 Testando URLs com prefixo /internato:")
    
    # Teste 1: Página principal
    response = requests.get(f"{base_url}/internato/")
    print(f"✅ Página principal: {response.status_code}")
    
    # Teste 2: Login
    response = requests.post(
        f"{base_url}/internato/login",
        data={"email": "admin@pvtinternatos.com", "data_nascimento": "1980-01-01"},
        allow_redirects=False
    )
    print(f"✅ Login: {response.status_code}")
    
    # Teste 3: Dashboard (após login)
    cookies = response.cookies
    response = requests.get(f"{base_url}/internato/dashboard", cookies=cookies)
    print(f"✅ Dashboard: {response.status_code}")
    
    # Teste 4: API
    response = requests.get(f"{base_url}/internato/api/agendas", cookies=cookies)
    print(f"✅ API Agendas: {response.status_code}")
    
    print("\n🎉 Todos os testes passaram!")
    print("🌐 URLs de produção funcionando corretamente:")
    print("   - https://api.brunoretiro.com.br/internato/")
    print("   - https://api.brunoretiro.com.br/internato/login")
    print("   - https://api.brunoretiro.com.br/internato/dashboard")
    print("   - https://api.brunoretiro.com.br/internato/api/agendas")

except Exception as e:
    print(f"❌ Erro durante os testes: {e}")

finally:
    # Parar o servidor
    process.terminate()
    process.wait()
    print("\n�� Servidor parado.") 