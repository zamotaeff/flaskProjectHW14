import os

from flask import Flask

# Импортируем блюпринт
from app.films.routes import films_api_blueptint

PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

# Создаем экземпляр Flask
app = Flask(__name__)

app.config.from_pyfile('config/development.py')

# регистрируем первый блюпринт
app.register_blueprint(films_api_blueptint)

# Запускаем сервер только, если файл запущен, а не импортирован
if __name__ == "__main__":
    app.run(
        debug=app.config['DEBUG']
    )
