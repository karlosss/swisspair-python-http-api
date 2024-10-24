FROM python:latest
LABEL authors="karlosss"

WORKDIR /app

COPY . .

RUN pip install --break-system-packages --root-user-action=ignore -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]
