FROM ubuntu:latest
LABEL authors="karlosss"

WORKDIR /app

RUN apt-get update -y &&  \
    apt-get install -y python3 python3-pip gcc make cmake git libgmp-dev

COPY . .

RUN pip install --break-system-packages --root-user-action=ignore --extra-index-url https://test.pypi.org/simple/ -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "app.py"]
