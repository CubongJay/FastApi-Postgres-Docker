import urllib.parse
import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm


my_password = urllib.parse.quote_plus("p@ssword1")

# DATABASE_URL = f'postgresql+psycopg2://admin:{password}@localhost/fastapi_db'
DATABASE_URL = "postgresql://myuser:password@localhost:5416/fastapi_db"

engine = _sql.create_engine(DATABASE_URL)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = _declarative.declarative_base()