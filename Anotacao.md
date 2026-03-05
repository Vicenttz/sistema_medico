# PRINCIPAIS COMANDOS DO GIT - Enviando a primeira versão 

1. git init -> Inicializar a pasta como repositório local 
2. git branch -M main -> Altera a branch para main
3. git add . -> Adiciona os arquivos para o repositorio local
4. git commit -m "Primeira versão do sistema" 
5. git remote add origin https://github.com/Vicenttz/sistema_medico.git
6. git push -u origin main

## Enviando as proximas versões

1. git add . -> Adiciona os arquivos para o repositorio local
2. git commit -m "Segunda Versão do sistema"
3. git push

## CONFIGURAÇÃO DE GIT

git config --global user.name "Davi Barreto"
git config --global user.email "vicennttzz@gmail.com"

## Sites

https://docs.djangoproject.com/en/6.0/

## Comandos do ambiente virtual

1. python -m venv venv  -> gera um abiente virtual do tipo venv
2. ./venv/Scripts/activate -> Atva o ambiente virtual
3. pip install django -> Instala o django
4. django-admin startproject sistema .
5. python manage.py runserver