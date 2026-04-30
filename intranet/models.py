from django.utils import timezone # Importação de modulo timezone que traz datas e horarios

from django.db import models

# Criar um modelo do médico com nome, email, telefone, crm, especialidades

class Medico(models.Model):
    # Atributos = caracteristicas = variaveis
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    email = models.EmailField()
    criacao_data = models.DateTimeField(default=timezone.now)
    telefone = models.CharField(max_length=15)
    crm = models.CharField(max_length=6)
    especialidades = models.CharField(max_length=30)
    ativo = models.BooleanField(default=True)
    mensagem = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='img/%Y/%m', blank=True)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Pacientes(models.Model):
    # Atributos = caracteristicas = variaveis
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=11)
    criacao_data = models.DateTimeField(default=timezone.now)
    mensagem = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='img/%Y/%m', blank=True)


    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Consulta(models.Model):
    paciente_id = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    medico_id = models.ForeignKey(Medico, on_delete=models.CASCADE)
    horario = models.DateTimeField(default=timezone.now)
    observacao = models.TextField(blank=True)
    status = models.CharField(
        default='A',
        max_length=1,
        choices=(
            ('A', 'Agendada'),
            ('X', 'Cancelada'),
            ('C', 'Confirmada'),
            ('R', 'Realizada-')
        )
    )

    def __str__(self):
        return f'consulta {self.status} com sucesso'