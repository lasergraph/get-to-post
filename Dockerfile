FROM python:alpine3.18

#Ordner erstellen
RUN mkdir /opt/scripts

#Python Pakete installieren
RUN pip3 install http3 urllib3 datetime requests pytz

#Dateien kopieren
COPY main.py /opt/scripts/

#env
ENV FE2_URL="https://URL:PORT/rest/external/http/position/v2"
ENV AUTH="secret"
ENV ALARM_TYPE="ALARM"
ENV ALARM_SENDER="WAGO"
ENV ALARM_KEYWORD="Fw Magazin"
ENV ALARM_ADDRESS="WagoAlarm"

#Port für Webook
EXPOSE 8088

ENTRYPOINT python3 /opt/scripts/main.py
