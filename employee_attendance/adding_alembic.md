- `pip install alembic`
- `alembic init alembic`

- modify the `alembic.ini` file and env.py

- `alembic revision --autogenerate -m "initial"`
    - to create a new migration

- `alembic upgrade head`
    - to upgrade the database

- `alembic downgrade base`
    - to downgrade the database
- `alembic current`
- to downgrade one or more migrations
    - `alembic downgrade -n 1` for one
    - `alembic downgrade -n 2` for two