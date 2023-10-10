import psycopg2


dbname = 'postgres'
user = 'testpostgres'
password = 'testpostgres'
host = 'localhost'


def create_tables():
    try:
        conn = psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host)
        cursor = conn.cursor()

        with open('create_tables.sql', 'r') as file:
            script = file.read()
            cursor.execute(script)
        conn.commit()

    except Exception as e:
        print(f"Connection error: {e}")
    finally:

        if conn:
            cursor.close()
            conn.close()


if __name__ == "__main__":
    create_tables()