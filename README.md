# get to post
[Docker Hub](https://hub.docker.com/r/lasergraph/get-to-post)

### GET Request
- Port: 8088
- GET Parameter: message, subject, typ
- Beispiel: `http://alamos.example.com:8088/?message=new Alarm&subject=mysubject&typ=sonderalarm `

### Docker Environment Variable
|Key|Value|Default|
|---|---|--|
|FE2_URL|URL des Alamosserver inkl. Pfad z.B. https://{IP}:{PORT}/rest/external/http/alarm/v2|https://URL:PORT/rest/external/http/position/v2|
|AUTH| 	Geheimnis das in der Externen Schnittstelle bei Gültiger Absender hinterlegt wird um sich gegenüber des FE2 Server zu Authentifizieren|secret|
|ALARM_ADDRESS|address Parameter welcher an den Server übermittelt wird. Diese Einheit wird alarmiert|WagoAlarm|
|ALARM_KEYWORD|keyword Paramerter welcher an den Server übermittelt wird|Fw Magazin|
|ALARM_SENDER|sender Parameter welcher an den Server übermittelt wird|WAGO|
|ALARM_TYPE|TYPE für die Alarmübermittlung sollte normalerweise ALARM sein|ALARM|

### FE2 Parameter
Folgende Parameter werden übermittelt
- type
- timestamp
- sender
- authorization
- keyword 
- subject
- message
- address
- typ (custom Parameter)

