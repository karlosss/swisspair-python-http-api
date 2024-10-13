FROM archlinux:latest
LABEL authors="karlosss"

WORKDIR /app

RUN pacman -Syu --noconfirm &&  \
    pacman -S --noconfirm python python-pip gcc make cmake git pybind11

COPY . .

RUN pip install --break-system-packages --root-user-action=ignore -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "app.py"]
