# 🏥 Internato 2.0 - PVT Internatos

Sistema de Gerenciamento de Internatos com foco em organização de rodízios cirúrgicos e controle de estágios médicos.

## 🎨 Nova Identidade Visual

- **Marca**: PVT Internatos
- **Cor Principal**: #0369a1 (Azul profissional)
- **Design**: Interface moderna e responsiva
- **Logo**: Integrado em todas as páginas

## 📋 Funcionalidades Implementadas

### ✅ Sistema Completo
- [x] **Sistema de Login** - Autenticação por e-mail e data de nascimento
- [x] **Dashboard Moderno** - Estatísticas em tempo real com design profissional
- [x] **Gestão de Alunos** - Cadastro completo com ID, nome, e-mail, telefone, data de nascimento
- [x] **Gestão de Especialidades** - Cadastro com IDs e descrições
- [x] **Gestão de Locais** - Locais com endereços, especialidades e responsáveis
- [x] **Gestão de Agendas** - Sistema completo de alocações
- [x] **Registro de Presença** - Controle de presença e carimbos
- [x] **Perfil do Usuário** - Página personalizada com informações do aluno
- [x] **Interface Web Moderna** - Design responsivo com Bootstrap 5

### 🎯 Funcionalidades Principais

#### Sistema de Autenticação
- Login por e-mail e data de nascimento
- Sessões seguras
- Perfil personalizado para cada usuário

#### Dashboard Profissional
- Cards de estatísticas com design moderno
- Alunos por especialidade no dia
- Alunos com menos de 6 carimbos da semana
- Informações sobre o sistema

#### Gestão Completa de Alunos
- ID único para cada aluno
- Nome completo
- E-mail para login
- Telefone para contato
- Data de nascimento
- Especialidade principal
- Estatísticas de agendas e carimbos

#### Gestão de Especialidades
- ID único para cada especialidade
- Nome da especialidade
- Descrição detalhada
- Contagem de alunos e agendas

#### Gestão de Locais
- ID único para cada local
- Nome do local
- Endereço completo
- Lista de especialidades disponíveis
- Responsável pelo local

#### Sistema de Agendas
- ID único para cada agenda
- Data e turno
- Especialidade e local
- Aluno vinculado
- Responsável pela agenda
- Observações
- Controle de presença e carimbos

#### Perfil do Usuário
- Informações pessoais completas
- Estatísticas de agendas e carimbos
- Histórico de agendas recentes
- Status de progresso

## 🤖 Funcionalidades de IA (Em Desenvolvimento)

### 🧠 Lógica de Distribuição com IA

#### Sistema Inteligente de Rodízios
- **Sugestão automática** de rodízios equilibrados para cada aluno durante o semestre
- **IA evita repetições** - alunos não repetem a mesma especialidade em semanas consecutivas
- **Distribuição balanceada** - atribui alunos a blocos e ambulatórios de forma equilibrada

#### Critérios da IA
- **Capacidade de cada local** - respeita limites de ocupação
- **Especialidades obrigatórias** - garante cobertura mínima por aluno
- **Restrições do aluno** - considera limitações individuais
- **Histórico de alocação** - evita padrões repetitivos
- **Cobertura semanal** - garante 6 carimbos por aluno

#### Algoritmo de Distribuição
```
Gere um algoritmo de distribuição de alunos por semana considerando:
- Cada aluno deve passar por todas especialidades disponíveis
- Um aluno por bloco cirúrgico por turno
- Vários alunos em ambulatórios conforme capacidade
- Garantir 6 carimbos semanais por aluno
- Evitar repetir mesma especialidade 2x na semana
- Respeitar restrições de aluno e local
```

### 🎯 Inteligência de Rodízio (IA)

#### Sugestões Automáticas
- **Geração automática** de agendas por semana
- **Alerta inteligente** para alunos com repetição de setor
- **Cobertura garantida** de especialidades por aluno
- **Rodízios balanceados** gerados automaticamente

#### Controle Administrativo
- **Revisão e aprovação** das sugestões da IA pelo administrador
- **Ajustes manuais** quando necessário
- **Validação** de distribuições antes da implementação
- **Histórico** de sugestões e aprovações

#### Benefícios da IA
- **Otimização de tempo** - reduz trabalho manual de distribuição
- **Equidade** - garante acesso igual a todas especialidades
- **Flexibilidade** - permite ajustes conforme necessidades
- **Transparência** - critérios claros e auditáveis

## 🚀 Como Executar

### 1. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 2. Executar o Sistema
```bash
python run.py
```

### 3. Acessar o Sistema
Abra o navegador e acesse: **http://localhost:8000**

## 👤 Usuários de Teste

| E-mail | Data de Nascimento | Função |
|---------|-------------------|--------|
| admin@pvtinternatos.com | 1980-01-01 | Administrador |
| farley@pvtinternatos.com | 1985-05-15 | Coordenador (Farley) |
| residente@pvtinternatos.com | 1990-08-20 | Residente |

## 📁 Estrutura do Projeto

```
21 - INTERNATO/
├── app/
│   ├── data/                 # Arquivos JSON de dados
│   │   ├── alunos.json       # Alunos com dados completos
│   │   ├── especialidades.json # Especialidades com IDs
│   │   ├── locais.json       # Locais com endereços e responsáveis
│   │   ├── agendas.json      # Agendas com observações
│   │   └── users.json        # Usuários do sistema
│   ├── templates/            # Templates HTML
│   │   ├── base.html         # Template base com nova identidade
│   │   ├── login.html        # Login por e-mail/data nascimento
│   │   ├── dashboard.html    # Dashboard moderno
│   │   ├── alunos.html       # Gestão de alunos
│   │   ├── especialidades.html # Gestão de especialidades
│   │   ├── locais.html       # Gestão de locais
│   │   ├── agendas.html      # Gestão de agendas
│   │   ├── presenca.html     # Registro de presença
│   │   └── perfil.html       # Perfil do usuário
│   ├── static/               # Arquivos estáticos
│   │   └── pvt.png          # Logo PVT Internatos
│   ├── main.py              # Aplicação principal
│   ├── controllers.py       # Rotas da API
│   ├── services.py          # Lógica de negócio
│   └── models.py            # Modelos de dados
├── run.py                   # Script de execução
├── requirements.txt         # Dependências Python
└── README.md               # Documentação
```

## 🔧 Tecnologias Utilizadas

- **Backend**: FastAPI (Python)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Autenticação**: Sistema de sessões com e-mail/data nascimento
- **Armazenamento**: Arquivos JSON estruturados
- **Templates**: Jinja2
- **Design**: Identidade visual PVT Internatos
- **IA**: Algoritmos de distribuição inteligente (em desenvolvimento)

## 📊 Funcionalidades do Dashboard

### Estatísticas em Tempo Real
- Total de alunos cadastrados
- Agendas para hoje
- Especialidades ativas
- Alunos com menos de 6 carimbos

### Alunos por Especialidade (Hoje)
- Lista organizada por especialidade
- Visualização em cards modernos
- Contagem de alunos por área

### Alunos com Menos de 6 Carimbos
- Lista de alunos que precisam de atenção
- Status de carimbos da semana atual
- Indicadores visuais de urgência

## 🎨 Interface Moderna

### Design Profissional
- Interface responsiva
- Cor principal #0369a1
- Gradientes e animações
- Ícones Font Awesome
- Cards organizados
- Modais para ações

### Navegação Intuitiva
- Sidebar com logo PVT Internatos
- Menu principal organizado
- Breadcrumbs para navegação
- Botões de ação rápida
- Feedback visual para ações

## 🔐 Segurança

### Autenticação Moderna
- Login por e-mail e data de nascimento
- Sistema de sessões seguras
- Proteção de rotas
- Logout automático
- Cookies seguros

### Validação de Dados
- Validação de formulários
- Sanitização de inputs
- Tratamento de erros
- Feedback ao usuário

## 📈 Próximas Melhorias

### 🚀 Funcionalidades de IA
- [ ] **Sistema de Sugestão de Rodízios** - IA para distribuição automática
- [ ] **Algoritmo de Distribuição** - Lógica inteligente de alocação
- [ ] **Controle de Aprovação** - Interface para revisar sugestões da IA
- [ ] **Alertas Inteligentes** - Notificações sobre repetições e desequilíbrios
- [ ] **Otimização de Horários** - IA para melhor aproveitamento de recursos

### 🔧 Melhorias Técnicas
- [ ] Banco de dados SQLite/PostgreSQL
- [ ] Sistema de relatórios em PDF
- [ ] Exportação de dados para Excel
- [ ] Notificações em tempo real
- [ ] API REST completa
- [ ] Sistema de backup automático
- [ ] Logs de auditoria
- [ ] Múltiplos usuários com permissões
- [ ] Sistema de mensagens internas
- [ ] Calendário integrado

### 🎯 Funcionalidades Avançadas
- [ ] **Dashboard de IA** - Métricas de distribuição inteligente
- [ ] **Relatórios de Eficiência** - Análise de cobertura por especialidade
- [ ] **Sistema de Restrições** - Configuração de limitações por aluno
- [ ] **Histórico de Distribuições** - Comparação de rodízios anteriores
- [ ] **Exportação de Rodízios** - Geração de planilhas com distribuições

## 🤝 Contribuição

Para contribuir com o projeto:

1. Faça um fork do repositório
2. Crie uma branch para sua feature
3. Implemente as mudanças
4. Teste todas as funcionalidades
5. Envie um pull request

## 📞 Suporte

Para dúvidas ou problemas:

- Abra uma issue no repositório
- Consulte a documentação da API
- Verifique os logs do sistema

---

**Desenvolvido com ❤️ pela PVT Internatos para facilitar a gestão de estágios médicos**

*Internato 2.0 - Sistema de Gerenciamento de Internatos com IA* # gestaoInternato
