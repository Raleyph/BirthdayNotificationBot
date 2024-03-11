import os
import dotenv

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from .repository import Base

dotenv.load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), os.path.pardir, ".env"))

USERNAME = str(os.getenv("PG_USERNAME"))
PASSWORD = str(os.getenv("PG_PASSWORD"))
HOST = str(os.getenv("PG_HOST"))
DATABASE = str(os.getenv("DATABASE"))

engine = create_engine(f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}")

if not database_exists(engine.url):
    create_database(engine.url)

Base.metadata.create_all(engine)
engine.connect()
