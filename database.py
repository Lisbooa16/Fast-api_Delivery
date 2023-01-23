from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine('postgresql://postgres:Postgres2022!@192.168.15.22/postgres',
    echo=True
)

Base = declarative_base()

Session = sessionmaker()