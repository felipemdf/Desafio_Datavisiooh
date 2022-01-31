# Desafio_Datavisiooh

## :construction: Status <br/>
🚀 Concluído

## :toolbox: Tecnologias
* [Django](https://www.djangoproject.com)
* [Django Rest Framework](https://www.django-rest-framework.org)
* [SQLite](https://sqlite.org/index.html)

## :hammer_and_wrench: Preparando o ambiente

### Clonando o repositório
```   
# Clone este repositório:
 $ git clone <https://github.com/felipemdf/Desafio_Datavisiooh.git>

# Acesse a pasta do projeto no terminal/cmd 
 $ cd ./Desafio_Datavisiooh/
 
# Inicie o projeto 
 $ python manage.py runserver

# A api vai estar rodando na porta 8000
  <http://localhost:8000>
```

### Utializando a imagem do docker
```   
# De um pull na imagem do projeto:
 $ docker pull felipemdf/desafio_datavisiooh:latest

# Rode a imagem na porta 3000
 $ docker run --rm -p 3000:3000 [id_imagem]

# A api vai estar rodando na porta 3000
  <http://localhost:3000>
```