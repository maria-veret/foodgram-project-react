## Продуктовый помощник - Foodgram

Foodgram - приложение, на котором пользователи могут публиковать рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов, а также создавать список покупок и выгружать перечень и количество необходимых ингредиентов для рецептов.


### Запуск проекта на локальной машине

Скопируйте проект на свой компьютер:

```
git clone https://github.com/maria-veret/foodgram-project-react.git
```

Cоздайте и активируйте виртуальное окружение для этого проекта:

```
python -m venv env
```

```
source venv/Scripts/activate
```

Установите зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Перейдите в директорию проекта:

```
cd backend
```

Создайте файл .env в директории backend и заполните его данными по образцу:

```
SECRET_KEY='--'
DB_ENGINE=django.db.backends.postgresql
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

Создайте образ foodgram_backend и foodgram_frontend (текущая директория должна быть backend или frontend соответственно):

```
docker build -t mari4veret/foodgram_backend:latest .
```

```
docker build -t mari4veret/foodgram_frontend:latest .
```

Перейдите в директорию infra:

```
cd ../infra
```

Запустите docker-compose:

```
docker compose up -d
```

Выполните миграции:

```
docker-compose exec -T backend python manage.py migrate
```

Соберите статику:

```
docker-compose exec -T backend python manage.py collectstatic --no-input
```

Запустите проект в браузере.
Введите в адресную строку браузера:

```
http://localhost/
```

### В проекте использованы технологии:
* Python
* React
* Django
* Django REST Framework
* Linux
* Docker
* Docker-compose
* Postgres
* Gunicorn
* Nginx
* Workflow
