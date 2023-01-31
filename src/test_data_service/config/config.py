from dataclasses import dataclass
from environs import Env


@dataclass
class DBConfig:
    name: str
    user: str
    password: str
    host: str
    port: str


@dataclass
class Config:
    db: DBConfig
    csrf_enabled: bool = True
    session_cookie_secure: bool = True


def load_config(path: str = None) -> Config:
    env = Env()
    env.read_env(path)

    return Config(
        db=DBConfig(
            name=env.str('APP_POSTGRESQL_NAME'),
            user=env.str('APP_POSTGRESQL_USER'),
            password=env.str('APP_POSTGRESQL_PASSWORD'),
            host=env.str('APP_POSTGRESQL_HOST'),
            port=env.str('APP_POSTGRESQL_PORT')
        ),
        csrf_enabled=env.str('CSRF_ENABLED'),
        session_cookie_secure=env.str('SESSION_COOKIE_SECURE')
    )


settings = load_config('.env')
