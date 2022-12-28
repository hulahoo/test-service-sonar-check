# test-data-service

Веб-сервис для предоставления тестовых данных


## Информаци о ENV-параметрах
Имеющиеся env-параметры в проекте:
```
APP_POSTGRESQL_NAME=test_name
APP_POSTGRESQL_USER=user
APP_POSTGRESQL_PASSWORD=password
APP_POSTGRESQL_HOST=localhost
APP_POSTGRESQL_PORT=5432
```

### Запуск сервиса

1. Создайте виртуальное окружение

```
python3 -m venv venv
```

2. Активировать виртуальное окружение: 

```
source venv/bin/activate
```

3. Установить зависимости: 

```
python setup.py install
```

4. Запустите сервер
```
test-data-service
```
