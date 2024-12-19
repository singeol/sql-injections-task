from flask import Flask, request, render_template
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os

app = Flask(__name__)

# Параметры подключения к PostgreSQL
DB_NAME = 'lab_injections' 
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_HOST = 'localhost'
DB_PORT = '5432'

def get_connection():
    """Функция для установления соединения с базой данных."""
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

@app.route('/')
def index():
    return render_template(
        "index.html",
        title="Выберите вариант",
        note="Перейдите по ссылкам выше, чтобы увидеть уязвимую или безопасную версию."
    )

@app.route('/vulnerable', methods=['GET', 'POST'])
def vulnerable():
    results = ""
    if request.method == 'POST':
        user_input = request.form.get('username', '')
        # Уязвимый запрос - строковая конкатенация без параметров
        query = f"SELECT username, password FROM users WHERE username = '{user_input}';"
        
        try:
            conn = get_connection()
            conn.autocommit = True

            # YOUR CODE HERE
            # Подсказки:
            # 1. Получите курсор: cur = conn.cursor()
            # 2. Выполните запрос: cur.execute(query)
            # 3. Получите данные: data = cur.fetchall()
            # 4. Обработайте результаты и сохраните их в переменную results
            
            # Не забудьте закрыть курсор и соединение
            # cur.close()
            # conn.close()

        except Exception as e:
            results = f"Ошибка: {e}"
    return render_template(
        "vulnerable.html",
        title="Уязвимый запрос",
        results=results
    )

@app.route('/safe', methods=['GET', 'POST'])
def safe():
    results = ""
    if request.method == 'POST':
        user_input = request.form.get('username', '')
        # Безопасный параметризованный запрос
        query = "SELECT username, password FROM users WHERE username = %s;"

        try:
            conn = get_connection()
            conn.autocommit = True

            # YOUR CODE HERE
            # Подсказки:
            # 1. Получите курсор: cur = conn.cursor()
            # 2. Выполните запрос с параметром: cur.execute(query, (user_input,))
            # 3. Получите данные: data = cur.fetchall()
            # 4. Обработайте результаты и сохраните их в переменную results
            
            # Не забудьте закрыть курсор и соединение
            # cur.close()
            # conn.close()

        except Exception as e:
            results = f"Ошибка: {e}"
    return render_template(
        "safe.html",
        title="Безопасный запрос",
        results=results
    )

if __name__ == "__main__":
    app.run(debug=True)
