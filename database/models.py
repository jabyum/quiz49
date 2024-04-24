from sqlalchemy import (Column, Float, Integer, DateTime,
                        BigInteger, Boolean, String, ForeignKey)
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    # создаем таблицу и даем ей название
    __tablename__ = "users"
    # создаем колонки
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, unique=True)
    phone_number = Column(String)
    reg_date = Column(DateTime)
class Questions(Base):
    __tablename__ = "questions"
    id = Column(Integer, autoincrement=True, primary_key=True)
    q_text = Column(String, nullable=False)
    answer = Column(Integer, nullable=False)
    level = Column(String, nullable=False, default="easy")
    v1 = Column(String, nullable=False)
    v2 = Column(String, nullable=False)
    v3 = Column(String, nullable=True)
    v4 = Column(String, nullable=True)
    reg_date = Column(DateTime)
class UserAnswers(Base):
    __tablename__ = "user_answers"
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    user_answer = Column(Integer)

    user_fk = relationship(User)
    question_fk = relationship(Questions)

class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user_score = Column(Integer, default=0)

    user_fk = relationship(User)

