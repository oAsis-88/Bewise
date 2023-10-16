import os

import psycopg2.pool
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.abspath(os.curdir), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

postgreSQL_pool = psycopg2.pool.SimpleConnectionPool(
    minconn=1,
    maxconn=20,
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    database=os.getenv('DB_DATABASE')
)
