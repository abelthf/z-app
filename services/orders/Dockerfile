# imagen base
FROM python:3.7.3-alpine

# nuevo
# instalando sqlite
RUN apk update \
    && apk add sqlite \
    && apk add socat

# estableciendo directorio de trabajo
WORKDIR /usr/src/app

# copiando e instalando requirements
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copiando app
COPY . /usr/src/app

# ejecutar servidor
CMD python manage.py run -h 0.0.0.0
