from sqlalchemy import create_engine
from sqlalchemy import insert, select, delete, update
from database.database_creator import Users, Bots
import config_checker
import datetime


class DataBase:

    def __init__(self, table):
        self.DATABASE_URL = "sqlite:///" + config_checker.get_data_for_web_bot()["data_base_path"]
        self.engine = create_engine(self.DATABASE_URL)
        self.conn = self.engine.connect()
        self.table = table

    def add_to_database(self, data: dict | list):
        if data is dict:
            request = insert(self.table).values(**data)
        elif data is list:
            request = insert(self.table).values(*data)
        else:
            raise TypeError()

        return self.commit(request)

    def delete_from_database(self, user_id):
        request = delete(self.table).where(self.table.id == f"{user_id}")
        return self.commit(request)

    def update_database(self, user_id, user_data):
        request = update(self.table).where(self.table.id == f"{user_id}").values(**user_data)
        return self.commit(request)

    def select_all_from_database(self):
        table_data = self.conn.execute(select(self.table)).all()
        return table_data

    def commit(self, request):
        self.conn.execute(request)
        self.conn.commit()
        return True