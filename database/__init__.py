from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# подключение к базе данных/создание базы данных
SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
# создание движка бд
engine = create_engine(SQLALCHEMY_DATABASE_URI)
# переменная для создания сессий
SessionLocal = sessionmaker(bind=engine)
# создание шаблока для базы классов бд
Base = declarative_base()

# создание сессий
def get_db():
    db = SessionLocal()
    try:
        # пробуем подключиться к базе данных
        yield db
    except Exception:
        # если не получается откатываем до рабочего состояния
        db.rollback()
        raise
    finally:
        # при любом срабатывании except закрываем сессию
        db.close()
