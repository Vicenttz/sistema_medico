from django.contrib import admin

from intranet import models

# Register your models here.

@admin.register(models.Medico) #Registrando a classe médico no portal do python
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'especialidades', 'ativo')

@admin.register(models.Pacientes)
class PacientesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'ativo')

@admin.register(models.Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('paciente_id', 'id', 'medico_id', 'status',)

