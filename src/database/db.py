from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

CONNECTION_STRING = "sqlite:///./freqtrade-api.db"
engine = create_engine(CONNECTION_STRING, connect_args={"check_same_thread": False})

Session = sessionmaker(bind=engine)
session = Session()
