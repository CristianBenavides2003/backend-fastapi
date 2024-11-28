import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# Cargar las variables de entorno desde el archivo .env
# Leer DATABASE_URL desde las variables de entorno

DATABASE_URL = "mysql+pymysql://root:@localhost:3306/dbusers"
print(DATABASE_URL)
# Configurar SQLAlchemy
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()