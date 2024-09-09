FROM python:3
RUN useradd -r  Nilewa

WORKDIR /usr/app
COPY codigoBasico2.py /usr/app

RUN apt update && apt upgrade

USER Nilewa
CMD ["python3","codigoBasico2.py"]   


