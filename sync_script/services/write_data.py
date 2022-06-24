import psycopg2
from datetime import datetime
from services.connect_Gsheets import _get_data
from config.settings import DATABASE, USER, PASSWORD, HOST, PORT
from exceptions import CantGetData, CantParseCourse, CantWriteDatabase
from services.parse_course import _parse_course


def _update_orders(con: psycopg2) -> None:
    """Service for writing new data from a table"""
    cur = con.cursor()
    cur.execute('DELETE FROM sheet_order')
    _write_new_data(cur)
    con.commit()
    print(f"Record inserted successfully - {datetime.now()}")
    con.close()


def _write_new_data(cur: psycopg2) -> None:
    try:
        data_from_Gsheet = _get_data()
    except CantGetData:
        print('Не могу соединится с Google Sheets')
        exit(1)
    try:
        ruble_exchange_rate = _parse_course()
    except CantParseCourse:
        print('Не могу  получить данные от ЦБ РФ')
        exit(1)
    for element in data_from_Gsheet:
        try:
            cur.execute(
                f"INSERT INTO sheet_order (position_number,order_number,dollar_value,delivery_time,rubles_value) VALUES "
                f"({int(element[0])}, "
                f"{int(element[1])}, {int(element[2])}, '{element[3]}', {round(int(element[2]) * ruble_exchange_rate)})"
            )
        except (psycopg2.errors.UniqueViolation, ValueError, IndexError):
            raise CantWriteDatabase


def _connect_DB() -> psycopg2.connect:
    try:
        con = psycopg2.connect(
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT
        )
        print("[INFO] Подключение с БД установлено")
        return con
    except psycopg2.OperationalError:
        raise CantWriteDatabase
