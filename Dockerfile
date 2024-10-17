FROM ubuntu:latest
LABEL authors="karlosss"

WORKDIR /app

RUN apt-get update -y &&  \
    apt-get install -y python3 python3-pip

COPY . .

RUN pip install --break-system-packages --root-user-action=ignore -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]
