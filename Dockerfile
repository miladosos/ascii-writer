FROM python:3.7

ADD . /home/ascii_art/
WORKDIR /home/ascii_art/

ENV ASCII_ART_FONT "standard"

RUN python3 -m pip install -r /home/ascii_art/requirements.txt
EXPOSE 8080

ENTRYPOINT ["python3", "app.py"]