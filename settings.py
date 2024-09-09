from email.policy import default

from envparse import Env

env = Env()

REAL_DATABASE_URL = env.str(
    'REAL_DATABASE_URL',
    default='postgresql+asyncpg://postgres:root@0.0.0.0:5432/postgres'
)
