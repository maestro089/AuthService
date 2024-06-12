# AuthService

## Миграции

* Создаем миграции

alembic revision --autogenerate -m 'upgrade models'

* Загружаем в БД

alembic upgrade head
