
***

<h2>Бэкенд-часть SPA веб-приложения</h2>

***

<h3>Описание:</h3>

<h4>Контекст:</h4>
 - В 2018 году Джеймс Клир написал книгу «Атомные привычки», 
    которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек. 
    Заказчик прочитал книгу, впечатлился и обратился к вам с запросом реализовать трекер полезных привычек.

<h4>Решенные задачи:</h4>

 - Настроен CORS.  
 - Настроена интеграция с Telegram.  
 - Реализована пагинация.  
 - Все необходимые эндпоинты реализованы.  
 - Настроены все необходимые валидаторы.  
 - Описаны права доступа.  
 - Настроена отложенная задача через Celery.

***

<h3>Стек технологий:</h3>

 - celery==5.3.4
 - coverage==7.3.2
 - Django==4.2.7
 - django-celery-beat==2.5.0
 - django-cors-headers==4.3.0
 - django-filter==23.3
 - djangorestframework==3.14.0
 - djangorestframework-simplejwt==5.3.0
 - drf-spectacular==0.26.5
 - drf-yasg==1.21.7
 - eventlet==0.33.3
 - psycopg2==2.9.9
 - python-dotenv==1.0.0
 - redis==5.0.1
 - requests==2.31.0

***

<h3>Для запуска необходимо:</h3>

 - Клонировать проект на собственный диск в новом каталоге
 - Создать виртуальное окружение
 - Установить зависимости командой: pip install -r requirements.txt
 - Прописать переменные окружения в файле .env.sample
 - Создать базу данных (в данной работе используется PostgreSQL)
<br> psql -U postgres
<br> create database habits;
<br> \q
 - Установить Redis
 - В терминале выполнить команды:
<br> python manage.py migrate
<br> python manage.py csu

***

<h3>Работа с Телеграм:</h3>

 - Для создания Telegram-бота найдите в чате самого главного бота: BotFather.
 - Далее следуйте инструкциям и по завершении создания бота вам будет выдан токен. 
Его необходимо перенести в файл .env в поле TELEGRAM_API_TOKEN. 
Токен будет использован ботом для обращения к API Telegram-сервисов.
 - В терминале выполнить команду:
<br> python manage.py get_chat_id

***

<h3>Работа с проектом с использованием Docker выполняется с помощью последовательности команд</h3>

- docker-compose build - происходит сборка образа контейнера согласно инструкции в файле Dockerfile
- docker-compose up - происходит последовательный запуск всех контейнеров согласно инструкции в файле docker-compose.yaml

***

<h3>Завершение работы с использованием Docker:</h3>

 - Ctrl+C

***

<h2>Хорошего настроения!</h2>
