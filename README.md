- [Финальный проект на Django==4.2.18](#финальный-проект-на-django4218)
  - [Чтобы запустить проект, нужно:](#чтобы-запустить-проект-нужно)
# Финальный проект на Django==4.2.18

## Чтобы запустить проект, нужно:
1. Установить виртуальное окружение - `python -m venv venv`
2. Установить зависимости - `pip install -r requirements.txt`
3. Принять зависимости - `python manage.py migrate`
4. Создать файл - `.env` c такими переменными как
   - `NAME=""`
   - `USER=""`
   - `PASSWORD=""`
   - `HOST=""`
   - `PORT=""`
   - `API_YANDEX_MAPS`
5. Запустить проект - `python manage.py runserver`
