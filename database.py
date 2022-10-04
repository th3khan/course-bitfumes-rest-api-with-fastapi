# bitfumes_tutorial_fastapi
import os
from sqlalchemy import create_engine, MetaData

username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
database = os.getenv('DB_DATABASE')

engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

meta = MetaData()

conn = engine.connect()