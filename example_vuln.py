import psycopg2

# Параметры подключения к PostgreSQL (при необходимости измените)
DB_NAME = 'example'
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_HOST = 'localhost'
DB_PORT = '5432'

def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

if __name__ == "__main__":
    user_input = "alice"

    # Уязвимый запрос - строковая конкатенация
    query = f"SELECT username, password FROM users WHERE username = '{user_input}';"
    print("Выполняется запрос:", query)

    try:
        conn = get_connection()
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute(query)

        # Если таблица не будет удалена, а запрос вернётся корректно:
        if cur.description:
            data = cur.fetchall()
            if data:
                for row in data:
                    print(f"Username: {row[0]}, Password: {row[1]}")
            else:
                print("Пользователь не найден или запрос не вернул результатов.")
        else:
            print("Команда выполнена, но данных не возвращено.")

        cur.close()
        conn.close()
    except Exception as e:
        print("Ошибка:", e)
