#!/usr/bin/env python3
"""
Internato Manager - Sistema de Gestão de Estágios Médicos
"""

import uvicorn

if __name__ == "__main__":
    print("🚀 Iniciando Internato Manager...")
    print("📋 Sistema de Gestão de Estágios Médicos")
    print("🌐 Acesse: http://localhost:8001")
    print("👤 Usuários de teste:")
    print("   - admin / admin123")
    print("   - coordenador / coord123")
    print("   - residente / res123")
    print("\n" + "="*50)
    
    uvicorn.run(
        "app.main:app", 
        host="0.0.0.0", 
        port=8001, 
        reload=True,
        log_level="info"
    ) 