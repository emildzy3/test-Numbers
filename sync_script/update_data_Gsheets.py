from __future__ import print_function, annotations


from exceptions import CantWriteDatabase, CantGetData, CantParseCourse
from services.write_data import _connect_DB, _update_orders


def write_data_to_db() -> None:
    """Service for writing data from Google sheets to the database"""
    try:
        con = _connect_DB()
    except CantWriteDatabase:
        print('Ошибка с соединением с БД')
        exit(1)
    _update_orders(con)


if __name__ == '__main__':
    while True:
        try:
            write_data_to_db()
        except (CantWriteDatabase, CantGetData, CantParseCourse):
            print("Ошибка получения данных. Повторная попытка...")
            continue
