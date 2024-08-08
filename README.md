```
Установка необходимых модулей:
python -m pip install django pytz pillow

Импорт данных в базу данных:
python manage.py load_doctors
python manage.py load_services
python manage.py load_procedures

Запуск приложения:
python manage.py runserver 7000
```

```
cosmetology_site/
│
├── manage.py
├── cosmetology_site/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── cosmetology/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── management/
│   │   ├── __init__.py
│   │   └── commands/
│   │       └── load_procedures.py
│   └── static/
│       ├── images/
│       │   ├── doctor_1.jpg
│       │   ├── procedure_1.jpg
│       │   └── service_1.jpg
│       └── css/
│           └── styles.css
│   └── templates/
│       └── cosmetology/
│           ├── base.html
│           ├── doctors.html
│           ├── procedures.html
│           └── services.html
│
└── staticfiles/  # Создается после выполнения команды `collectstatic`
```

```
Описание файлов и папок
manage.py: Скрипт для управления проектом (например, запуск сервера, выполнение миграций).

cosmetology_site/: Основная директория проекта Django.

__init__.py: Пустой файл, чтобы Python рассматривал эту директорию как модуль.
asgi.py: Конфигурация для ASGI.
settings.py: Конфигурационный файл Django для вашего проекта.
urls.py: Файл маршрутизации URL-адресов проекта.
wsgi.py: Конфигурация для WSGI.
cosmetology/: Директория для вашего приложения.

__init__.py: Пустой файл, чтобы Python рассматривал эту директорию как модуль.
admin.py: Настройка админки Django.
apps.py: Конфигурация приложения.
models.py: Модели данных приложения.
tests.py: Тесты для приложения.
views.py: Представления для обработки запросов и возврата ответов.
migrations/: Хранит файлы миграций для модели.
management/:
commands/: Пользовательские команды управления, например, load_procedures.py.
static/:
images/: Директория для хранения изображений.
css/: Директория для хранения CSS-файлов.
templates/:
cosmetology/: Директория для хранения HTML-шаблонов приложения.
base.html: Основной шаблон для общего оформления.
doctors.html: Шаблон для отображения информации о врачах.
procedures.html: Шаблон для отображения информации о процедурах.
services.html: Шаблон для отображения информации о услугах.
staticfiles/: Директория, создаваемая после выполнения команды collectstatic, содержит собранные статические файлы для развертывания.
```

#### Автор: Михаил
#### Дата: 05.08.2024
