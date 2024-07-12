from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String
import config_checker
from sqlalchemy.orm import relationship, mapped_column


DATABASE_URL = "sqlite:///" + config_checker.get_data_for_web_bot()["data_base_path"]
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    login = Column(String, nullable=False)
    password = Column(String, nullable=False)
    sessions = relationship("Sessions", cascade='save-update, merge, delete')
    product_cards = relationship("Products", cascade='save-update, merge, delete')


class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    discription = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    count = Column(Integer, nullable=False)
    product_cards = relationship("ProductsCard", cascade='save-update, merge, delete')


class Sessions(Base):
    __tablename__ = 'session'
    id = Column(Integer, primary_key=True)
    user_id = mapped_column(Integer, ForeignKey("Users.id"))
    ip_address = Column(String)


class ProductsCard(Base):
    __tablename__ = 'products_card'
    id = Column(Integer, primary_key=True)
    user_id = mapped_column(Integer, ForeignKey("Users.id"))
    product_id = mapped_column(Integer, ForeignKey("Products.id"))
    count = Column(Integer)


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Database Created!")