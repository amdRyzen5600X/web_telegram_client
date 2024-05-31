FROM ubuntu:22.04

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -yqq --no-install-recommends libreoffice python3.11 python3-pip tzdata default-jre libreoffice-java-common && \
    pip3 install -r requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


WORKDIR /web_telegram_client
COPY . /web_telegram_client

EXPOSE 42069

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /web_telegram_client
USER appuser

CMD ["fastapi", "run", "main.py", "--port", "42069"]
