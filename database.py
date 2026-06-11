from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# mudar usuario e senha (root) na url abaixo? tirar postgresql?
DATABASE_URL = "postgresql://'postgresql':'postgresql'@localhost/tasks"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
