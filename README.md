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

### Локальный запуск

Для запуска приложения локально нужно:

1. Создать виртуальное окружение:
```bash
python3 -m venv venv
```

2. Активировать виртуальное окружение:
```bash
source venv/bin/activate
```

3. Установить зависимости:
```bash
pip3 install -r requirements.txt
```

4. Собрать приложение как модуль:
```bash
python3 -m pip install .
```

5. Запустить приложение:
```bash
test-data-service
```

### Запуск с помощью докера
1. Dockerfile:
```dockerfile
FROM python:3.11.1-slim as deps
WORKDIR /app
COPY . ./
RUN apt-get update -y && apt-get -y install gcc
RUN pip --no-cache-dir install -r requirements.txt 
RUN pip --no-cache-dir install -r requirements.setup.txt 
RUN pip install -e .

FROM deps as build
ARG ARTIFACT_VERSION=local
RUN python setup.py sdist bdist_wheel
RUN ls -ll /app/
RUN ls -ll /app/dist/


FROM python:3.11.1-slim as runtime
COPY --from=build /app/dist/*.whl /app/
RUN apt-get update -y && apt-get -y install gcc
RUN pip --no-cache-dir install /app/*.whl
ENTRYPOINT ["test-data-service"]
```

2. docker-compose.yml
```yaml
version: '3'


services:
  db:
    image: db_image:staging

  worker:
    restart: always
    build: ./
    ports:
    - "8080:8080"
    environment:
      APP_POSTGRESQL_USER: dbuser
      APP_POSTGRESQL_PASSWORD: test
      APP_POSTGRESQL_NAME: db
      APP_POSTGRESQL_HOST: db
      APP_POSTGRESQL_PORT: 5432
    depends_on:
      - db

 
networks:
    external:
      name: kafka_net
```

3. Запуск контейнеров:
```bash
docker-compose up --build
```
