import psycopg2
import constants

connection = None


def get_connection():
    global connection

    if connection is None:
        connection = psycopg2.connect(dbname=constants.DBNAME, user=constants.USER,
                                      password=constants.PASSWORD,
                                      host=constants.HOST, port=constants.PORT)
        connection.autocommit = True

    return connection


def get_all():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {constants.TARGET_TABLE}")

    return cursor.fetchall()
