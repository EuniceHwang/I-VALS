FROM python:3.10.6

RUN sed -i 's@archive.ubuntu.com@mirror.kakao.com@g' /etc/apt/sources.list

RUN apt-get -y update && apt-get -y dist-upgrade

RUN apt-get install -y apt-utils dialog libpq-dev

RUN apt-get install -y libreoffice

RUN apt-get install -y language-selector-gnome fonts-noto-cjk

RUN apt-get install poppler-utils

### python 설치 ###
RUN apt-get install -y python3-pip python3-dev

ENV PYTHONUNBUFFERED=0
ENV PYTHONIOENCODING=utf-8

RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools

### 실행 환경 구축 ###
RUN pip3 install gunicorn

ADD requirements.txt /config/
RUN pip3 install -r /config/requirements.txt

### 작업 디렉토리 ###
RUN mkdir /app
WORKDIR /app

COPY ./ivals/settings.py /app/ivals/settings.py

CMD python3 manage.py collectstatic --no-input && python3 manage.py makemigrations && python3 manage.py migrate && gunicorn I-VALS.wsgi:application -b 0:80
