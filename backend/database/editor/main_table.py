from sqlalchemy import create_engine
from sqlalchemy import insert, select, delete, update
from database.database_creator import Users, Bots, Base
import config_checker


class Table:
    def __init__(self, table: Base):
        self.DATABASE_URL = "sqlite:///" + config_checker.get_data_for_web_bot()["data_base_path"]
        self.engine = create_engine(self.DATABASE_URL)
        self.conn = self.engine.connect()
        self.table = table

    def add_to_database(self, data: dict):
        request = insert(self.table).values(**data)
        self.commit(request)

    def delete_from_database(self, id: int):
        request = delete(self.table).where(self.table.id == f"{id}")
        self.commit(request)

    def update_database(self, id: int, new_data: dict):
        request = update(self.table).where(self.table.id == f"{id}").values(**new_data)
        self.commit(request)

    def select_all_from_database(self):
        table_data = self.conn.execute(select(self.table)).all()
        return table_data

    def select_from_database_by_id(self, id: int):
        table_data = self.conn.execute(select(self.table).where(self.table.id == id)).first()
        return table_data

    def commit(self, request):
        self.conn.execute(request)
        self.conn.commit()