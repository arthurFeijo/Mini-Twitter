# Mini-Twitter API

Mini-Twitter é uma API RESTful construída com Django e Django REST Framework. Ela permite que usuários se registrem, façam login via JWT, criem posts e visualizem uma timeline paginada.

## Tecnologias

- Python 3.13
- Django 5.2
- Django REST Framework
- PostgreSQL
- JWT Authentication (via SimpleJWT)

# Instruções de Instalação

1. Clone o repositório
2. Crie e ative um ambiente virtual
3. Instale as dependências com `pip install -r requirements.txt`
4. Configure seu banco de dados PostgreSQL em `settings.py`
5. Rode as migrações com `python manage.py migrate`
6. Crie um superusuário com `python manage.py createsuperuser`
7. Inicie o servidor com `python manage.py runserver`

# Rotas Principais

- POST /api/register/           → Criar usuário
- POST /api/token/              → Obter tokens (JWT)
- POST /api/token/refresh/      → Renovar token
- GET /api/posts/               → Ver posts
- POST /api/posts/              → Criar post (autenticado)

## 📄 Documentação da API

Para visualizar a documentação interativa da API:

1. Certifique-se de ter o pacote instalado:
pip install drf-yasg

2. Inicie o servidor local:
python manage.py runserver

3. Acesse:
- Swagger: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- ReDoc: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)
