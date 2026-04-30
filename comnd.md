# class Bolo(models.Model):
#     tema = models.CharField(max_length=40)
#     tipo = models.CharField(max_length=40)
#     mesa = models.CharField(max_length=2)

#     def __str__(self):
#          return f'{self.tema}'

    
# class Evento(models.Model):
#      nome = models.CharField(max_length=40)
#      localizacao = models.CharField(max_length=40)
#      data = models.DateField()

#      def __str__(self):
#          return f'{self.nome}'
     
# class Patrocinadores(models.Model):
#      empresa = models.CharField(max_length=40)

#      def __str__(self):
#          return f'{self.empresa}'
     
# class Formulario(models.Model):
#      nome = models.CharField(max_length=40)
#      email = models.EmailField()
#      telefone = models.CharField(max_length=15)
#      cpf = models.CharField(max_length=11)

#      def __str__(self):
#          return f'{self.nome}'

------------------------------------------------

@admin.register(models.Bolo)
class BoloAdmin(admin.ModelAdmin):
    list_display = ('id', 'tema', 'tipo', 'mesa')

@admin.register(models.Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'localizacao', 'data')

@admin.register(models.Patrocinadores)
class PatrocinadoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'empresa')

@admin.register(models.Formulario)
class FormularioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'cpf')

