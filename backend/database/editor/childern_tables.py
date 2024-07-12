from sqlalchemy import create_engine
from sqlalchemy import insert, select, delete, update
from database.database_creator import Users, Bots
from main_table import Table
from creator import Users, Products, ProductsCard, Sessions


class UsersTable(Table):
    def __init__(self):
        super().__init__(Users)

    def check_user_data(self, login: str, password: str):
        is_user = self.table.login == login and self.table.password == password
        table_data = self.conn.execute(select(self.table).where(is_user)).first()
        return table_data


class ProductsTable(Table):
    def __init__(self):
        super().__init__(Products)

    def add_count(self, added_count: int, product_id: int):
        count = self.conn.execute(select(self.table.count).where(self.table.id == product_id)).first()
        count += added_count
        self.update_database({"count": count})


class CardTable(Table):
    def __init__(self):
        super().__init__(ProductsCard)


class SessionTable(Table):
    def __init__(self):
        super().__init__(Sessions)