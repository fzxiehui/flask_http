FROM python:3.9-slim

ARG http_proxy
ARG https_proxy
ARG no_proxy

ENV http_proxy=${http_proxy}
ENV https_proxy=${https_proxy}
ENV no_proxy=${no_proxy}

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD sh -c "\
    flask db init || echo 'flask db init already done'; \
    flask db migrate -m 'init tables' || echo 'No changes to migrate'; \
    flask db upgrade; \
    python main.py"
