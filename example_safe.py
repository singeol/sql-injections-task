import psycopg2

# Параметры подключения к PostgreSQL (при необходимости измените)
DB_NAME = 'lab_injections'
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

    # Безопасный параметризованный запрос
    query = "SELECT username, password FROM users WHERE username = %s;"
    print("Выполняется запрос (безопасный):", query, "с параметром:", user_input)

    try:
        conn = get_connection()
        conn.autocommit = True
        cur = conn.cursor()
        # Передаем параметры отдельно, psycopg2 самостоятельно экранирует значения.
        cur.execute(query, (user_input,))

        if cur.description:
            data = cur.fetchall()
            if data:
                for row in data:
                    print(f"Username: {row[0]}, Password: {row[1]}")
            else:
                print("Пользователь не найден.")
        else:
            print("Команда выполнена, но данных не возвращено.")

        cur.close()
        conn.close()
    except Exception as e:
        print("Ошибка:", e)
