from database import get_db
from database.models import User, UserAnswers, Rating
from datetime import datetime

def register_user_db(name: str, phone_number: str) -> int:
    db = next(get_db())
    checker = db.query(User).filter_by(name=name).first()
    if checker:
        return 0
    new_user = User(name=name, phone_number=phone_number,
                    reg_date=datetime.now())
    db.add(new_user)
    db.commit()
    return new_user.id
def get_user_score_db(user_id: int) -> int:
    db = next(get_db())
    try:
        checker = db.query(Rating).order_by(Rating.user_score.desc()).all()
        leaders_list = [user.id for user in checker]
        return leaders_list.index(user_id) + 1
    except:
        return 0
def get_top5_db():
    db = next(get_db())
    checker = db.query(Rating).order_by(Rating.user_score.asc()).all()
    return checker[-1:-6:-1]

def add_user_answer_db(user_id: int, question_id: int,
                       user_answer: int) -> bool:
    db = next(get_db())
    new_answers = UserAnswers(user_id=user_id, question_id=question_id,
                              user_answer=user_answer)
    db.add(new_answers)
    db.commit()
    # сделать проверку, правильно ли ответил юзер на этот вопрос. Если юзер ответил правильно,
    # то нужно обновить его информацию в таблице рейтинга и добавить ему +1 user_score

