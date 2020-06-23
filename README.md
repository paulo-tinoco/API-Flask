## Objetivo do projeto

Esse projeto trás as funções básicas do e-commerce.


## Instalação local

 1. Crie uma virtual virtual environment python
 
 `$ python -m venv venv`
 
 2. Ative a environment
 
 `$ source venv/bin/activate`
 
 3. Instale as dependências
 
 `(venv)$ pip install -r requirements.txt`
 
 4. Execute as migrations do projeto
 
 `(venv)$ flask db upgrade`

## Teste

Utilize a classe BasicTestProducts.py para realizar os testes unitários das funções de produtos.

`(venv)$ python BasicTestProducts.py`

Utilize a classe BasicTestUsers.py para realizar os testes unitários das funções de usuários.

`(venv)$ python BasicTestUsers.py`

## Rodando em docker através do Dockerfile

1. Faça o build baseado no Dockerfile
 
 `$ docker build -t restapi:latest .`

2. Inicialize o docker
 
 `$ docker run -d -p 5000:5000 restapi:latest`

## Rodando em docker através do dockerhub

 1. Faça o pull da imagem no dockerhub
 
 `$ docker pull tinoco/restapi`
 
 2. Inicialize o docker
 
 `$ docker run -d -p 5000:5000 tinoco/restapi:latest`
