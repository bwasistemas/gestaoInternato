from app.database import SessionLocal, en_engine
from app.models import models

def seed_data():
    db = SessionLocal()

    # Add specialties
    specialties = [
        models.Especialidade(nome="Cirurgia Geral", codigo="CG", capacidade_maxima=5),
        models.Especialidade(nome="Ortopedia", codigo="ORT", capacidade_maxima=3),
        models.Especialidade(nome="Ginecologia/Obstetrícia", codigo="GO", capacidade_maxima=3),
        models.Especialidade(nome="Otorrinolaringologia", codigo="OTR", capacidade_maxima=2),
        models.Especialidade(nome="Urologia", codigo="URO", capacidade_maxima=2),
    ]
    db.add_all(specialties)
    db.commit()

    # Add students
    students = [
        models.Aluno(nome="João da Silva", matricula="2024001", email="joao.silva@email.com", telefone="(11) 99999-0001"),
        models.Aluno(nome="Maria Oliveira", matricula="2024002", email="maria.oliveira@email.com", telefone="(11) 99999-0002"),
        models.Aluno(nome="Pedro Santos", matricula="2024003", email="pedro.santos@email.com", telefone="(11) 99999-0003"),
        models.Aluno(nome="Ana Souza", matricula="2024004", email="ana.souza@email.com", telefone="(11) 99999-0004"),
        models.Aluno(nome="Carlos Pereira", matricula="2024005", email="carlos.pereira@email.com", telefone="(11) 99999-0005"),
        models.Aluno(nome="Mariana Costa", matricula="2024006", email="mariana.costa@email.com", telefone="(11) 99999-0006"),
        models.Aluno(nome="José Almeida", matricula="2024007", email="jose.almeida@email.com", telefone="(11) 99999-0007"),
        models.Aluno(nome="Fernanda Lima", matricula="2024008", email="fernanda.lima@email.com", telefone="(11) 99999-0008"),
        models.Aluno(nome="Ricardo Gomes", matricula="2024009", email="ricardo.gomes@email.com", telefone="(11) 99999-0009"),
        models.Aluno(nome="Patrícia Rocha", matricula="2024010", email="patricia.rocha@email.com", telefone="(11) 99999-0010"),
        models.Aluno(nome="Lucas Martins", matricula="2024011", email="lucas.martins@email.com", telefone="(11) 99999-0011"),
        models.Aluno(nome="Sandra Barbosa", matricula="2024012", email="sandra.barbosa@email.com", telefone="(11) 99999-0012"),
        models.Aluno(nome="Bruno Carvalho", matricula="2024013", email="bruno.carvalho@email.com", telefone="(11) 99999-0013"),
        models.Aluno(nome="Juliana Ribeiro", matricula="2024014", email="juliana.ribeiro@email.com", telefone="(11) 99999-0014"),
        models.Aluno(nome="Felipe Dias", matricula="2024015", email="felipe.dias@email.com", telefone="(11) 99999-0015"),
    ]
    db.add_all(students)
    db.commit()

    db.close()

if __name__ == "__main__":
    models.Base.metadata.create_all(bind=en_engine)
    seed_data()
