## COMANDOS DO DJANGO

1. Criando um ambiente virtual -> python -m venv venv
2. Ativando o ambiente virtual -> .\venv\Scripts\activate
3. Instalando o DJANGO -> pip install django
4. Criando o rojeto DJANGO -> django-admin startproject nome_do_projeto . 
5. Subindo o servidor -> python manage.py runserver
6. Criando um novo app -> python manage.py startapp nome_do_app
7. Criando um superusuario -> python manage.py createsuperuser
8. Alterando a senha caso você esqueça -> python manage.py changepassword nome_do_usuario
9. Gerando o pacote de migração -> python manage.py makemigrations
10. Rodando as alterações do pacote de migração -> python manage.py migrate
11. Comando para manipular imagens no django -> python -m pip install Pillow

## Observações 

1. Em Python, só podemos ter mais de um classe por arquivo.

## Tipos de dados do framework ORM

CharField() -> é um campo de texto.
    -max_length -> é o tamanho maximo do campo.
    -choices= -> é a possibilidade definida para aquele campo.

EmailField() -> é um campo que verifica se o email é valido.

DateTimeField() -> é um campo de data e hora.
    -Default -> é o valor padrão.
    -timezone.now -> Data e hora atual(Local).

BoolenField() -> é um campo booleano.
    -Default=True -> é por padrão verdadeiro.

TextField() -> é um campo de texto.
    -blank=True -> permite que o campo seja vazio.

ImageField() -> é um campo de imagem.
    -upload_to -> é o caminho onde a imagem será salva.
    -%y é o ano.
    -%m é o mês.
    -%d é o dia.

-ForeignKeey() -> é um campo de chave estrangeira.
    -on_delete-models.CASCADE -> quando um paciente/medico for deletado a consulta tambem será deletada.
    -verbose_name -> é o nome do campo que será exibido no admin.
