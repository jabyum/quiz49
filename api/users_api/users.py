from fastapi import APIRouter
# создаем роутер(блюпринт/компонент)
user_router = APIRouter(prefix="/user",
                        tags=["Пользователи"])
# регистрация юзера/вход
@user_router.post("/register")
async def register_user(name: str, phone_number: str):
    pass
# получить таблицу лидеров
@user_router.get("/leaders")
async def get_5_leaders():
    pass
# запись результата
@user_router.post("/done")
async def test_finished(user_id: int):
    pass

