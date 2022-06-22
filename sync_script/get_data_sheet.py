from __future__ import print_function, annotations

import time

import psycopg2
from datetime import datetime
from connect_Gsheets import _get_data
from config.settings import DATABASE, USER, PASSWORD, HOST, PORT
from parse_course import parse_course


def write_data_to_db() -> None:
    con = _connect_DB()
    cur = con.cursor()

    cur.execute('DELETE FROM sheet_order')
    data_from_Gsheet = _get_data()
    ruble_exchange_rate = parse_course()
    for element in data_from_Gsheet:
        cur.execute(
            f"INSERT INTO sheet_order (position_number,order_number,dollar_value,delivery_time,rubles_value) VALUES "
            f"({int(element[0])}, "
            f"{int(element[1])}, {int(element[2])}, '{element[3]}', {round(int(element[2]) * ruble_exchange_rate)})"
        )

    con.commit()
    print(f"Record inserted successfully - {datetime.now()}")
    con.close()


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
    except:
        print("[INFO] Нет соединения с БД")


if __name__ == '__main__':
    while True:
        try:
            write_data_to_db()
        except (psycopg2.errors.UniqueViolation, ValueError, IndexError):
            print("Ошибка ")
            continue
