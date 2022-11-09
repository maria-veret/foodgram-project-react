## Продуктовый помощник - Foodgram

Foodgram - приложение, на котором пользователи могут публиковать рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов, а также создавать список покупок и выгружать перечень и количество необходимых ингредиентов для рецептов.


### Запуск проекта на локальной машине

Скопируйте проект на свой компьютер:

```
git clone https://github.com/maria-veret/foodgram-project-react.git
```

Cоздайте и активируйте виртуальное окружение для этого проекта:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Перейдите в директорию проекта:

```
cd backend
```

Установите зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
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
docker build -t mari4veret/food_backend:latest .
```

```
docker build -t mari4veret/food_frontend:latest .
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

Создайте суперпользователя:

```
docker compose exec backend python manage.py createsuperuser
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

### Запуск проекта на удаленном сервере

Создайте переменные окружения в репозитории в разделе Secrets > Actions для работы с GitHub Actions:

```
SECRET_KEY              # секретный ключ Django проекта
DOCKER_PASSWORD         # пароль от Docker Hub
DOCKER_USERNAME         # логин Docker Hub
HOST                    # публичный IP сервера
USER                    # имя пользователя на сервере
PASSPHRASE              # *если ssh-ключ защищен паролем
SSH_KEY                 # приватный ssh-ключ
TELEGRAM_TO             # ID телеграм-аккаунта для посылки сообщения
TELEGRAM_TOKEN          # токен бота, посылающего сообщение
DB_ENGINE               # django.db.backends.postgresql
DB_NAME                 # postgres
POSTGRES_USER           # postgres
POSTGRES_PASSWORD       # postgres
DB_HOST                 # db
DB_PORT                 # 5432 (порт по умолчанию)
```

Подключитесь к своему серверу по SSH и обновите индекс пакетов APT:

```
sudo apt update
```

Обновите установленные в системе пакеты и установите обновления безопасности:

```
sudo apt upgrade -y 
```

Проделайте на сервере все необходимые операции для разворачивания Django-проекта:

```
sudo apt install python3-pip python3-venv git -y
```

Скопируйте проект на удаленный сервер:

```
git clone https://github.com/maria-veret/foodgram-project-react.git
```

Создайте и активируйте виртуальное окружение:

```
python -m venv venv
```
```
source venv/bin/activate
```

Установите на сервере Docker, Docker Compose:

```
sudo apt install curl                                   # установка утилиты для скачивания файлов
curl -fsSL https://get.docker.com -o get-docker.sh      # скачать скрипт для установки
sh get-docker.sh                                        # запуск скрипта
sudo apt-get install docker-compose-plugin              # последняя версия docker compose
```

Скопируйте на сервер файлы docker-compose.yml, nginx.conf из папки infra (команды выполнять находясь в папке infra):

```
scp docker-compose.yml nginx.conf username@IP:/home/username/   # username - имя пользователя на сервере
                                                                # IP - публичный IP сервера
```

Создайте и запустите контейнеры Docker:

```
sudo docker compose up -d
```

После успешной сборки выполнить миграции:

```
sudo docker compose exec backend python manage.py migrate
```

Создать суперпользователя:

```
sudo docker compose exec backend python manage.py createsuperuser
```

Собрать статику:

```
sudo docker compose exec backend python manage.py collectstatic --noinput
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
