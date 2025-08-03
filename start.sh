#!/bin/bash

echo "🏥 Internato Manager - Sistema de Gestão de Estágios Médicos"
echo "=========================================================="
echo ""

# Verificar se o ambiente virtual existe
if [ ! -d "venv" ]; then
    echo "📦 Criando ambiente virtual..."
    python3 -m venv venv
fi

# Ativar ambiente virtual
echo "🔧 Ativando ambiente virtual..."
source venv/bin/activate

# Instalar dependências se necessário
echo "📥 Verificando dependências..."
pip install -r requirements.txt > /dev/null 2>&1

# Executar o sistema
echo "🚀 Iniciando o sistema..."
echo ""
echo "📋 Informações importantes:"
echo "   🌐 URL: http://localhost:8000"
echo "   👤 Usuários de teste:"
echo "      - admin / admin123"
echo "      - coordenador / coord123"
echo "      - residente / res123"
echo ""
echo "🛑 Para parar o sistema, pressione Ctrl+C"
echo ""

python run.py 