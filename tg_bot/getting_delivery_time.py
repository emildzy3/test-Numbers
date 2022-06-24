from dataclasses import dataclass
from datetime import datetime
from typing import Any
import psycopg2
from exceptions import CantGetData, CantConvertDataToDB
from settings import DATABASE, USER, PASSWORD, HOST, PORT


@dataclass(slots=True, frozen=True)
class Order:
    position_number: int
    order_number: int
    dollar_value: int
    delivery_time: int
    rubles_value: int


def delivery_time_check() -> tuple[Order]:
    """Service for receiving and converting the delivery time from the database"""
    try:
        list_orders = _get_tuple_orders()
        return list_orders
    except CantGetData:
        print("Ошибка при попытке получить данные.")
        exit(1)


def _get_tuple_orders() -> tuple[Order]:
    try:
        con = _connect_DB()
    except psycopg2.OperationalError:
        raise CantGetData
    raw_data = _get_raw_data(con)
    con.close()
    try:
        return tuple(_convert_data_from_db(raw_data))
    except CantConvertDataToDB:
        print('Не могу конвертировать данные из БД')
        exit(1)


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
        print("[INFO] Нет соединения с БД")


def _get_raw_data(con: psycopg2) -> tuple[tuple[Any, ...], ...]:
    cur = con.cursor()
    now_date = datetime.today().strftime("%Y-%m-%d")
    cur.execute(
        f"SELECT * FROM sheet_order WHERE delivery_time < '{now_date}'"
    )
    return tuple(cur.fetchall())


def _convert_data_from_db(raw_data: tuple[tuple[Any, ...], ...]) -> list[Order]:
    list_orders = []
    for values in raw_data:
        try:
            list_orders.append(Order(
                position_number=values[0],
                order_number=values[1],
                dollar_value=values[2],
                delivery_time=values[3],
                rubles_value=values[4],
            ))
            return list_orders
        except (psycopg2.errors.UniqueViolation, ValueError, IndexError):
            raise CantConvertDataToDB


if __name__ == '__main__':
    delivery_time_check()
