FROM python:alpine3.18

#Ordner erstellen
RUN mkdir /opt/scripts && mkdir /opt/scripts

#Python Pakete installieren
RUN pip3 install http3 urllib3 datetime requests pytz

#Dateien kopieren
COPY main.py /opt/scripts/

#env
ENV FE2_URL="https://URL:PORT/rest/external/http/position/v2"
ENV AUTH="secret"

#Port für Webook
EXPOSE 8080

ENTRYPOINT python3 /opt/scripts/main.py
