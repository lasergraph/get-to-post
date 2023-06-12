from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import requests
import datetime
import pytz

get_data = {}
#request_url = "http://localhost:8090"
request_url = 'https://httpbin.org/post'
auth = 'testTRIO1'
now = datetime.datetime.now(pytz.timezone('Europe/Zurich'))
timestamp = now.strftime('%Y-%m-%dT%H:%M:%S%z')


class GP(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def do_HEAD(self):
        self._set_headers()
    def do_GET(self):
        self._set_headers()
        print(parse_qs(self.path[2:]))
        get_data = parse_qs(self.path[2:])

        typ = ''
        message = ''
        subject = ''
        
        for i in get_data:
            if i == 'typ':
                typ = get_data['typ'][0]
            elif i == 'message':
                message = get_data['message'][0]
            elif i == 'subject':
                subject = get_data['subject'][0]
            else:
                print('key nicht bekannt')

        if  len(typ) > 1:
        
            print(typ)
            print(message)
            print(subject)

            #POST Request
            request_data = { 
                'type': 'ALARM',
                'timestamp': timestamp,
                'sender': 'WAGO',
                'authorization': auth,
                'data': { 
                    'keyword': 'Fw Magazin',
                    'subject' : subject,
                    'message': [
                        message
                    ],
                    'units': [
                      {
                        'address': 'WagoAlarm'
                      }  
                    ],
                    "custom": {
                        "typ": typ
                    }

                }
            }
            r = requests.post(request_url, json = request_data)
            print(r.text)
            if r.status_code == 200:
                status = 'OK'
            else:
                status = "Not OK"        
        else:
            status = 'No Typ'
        
        self.wfile.write(status.encode('ascii'))


#HTTP-Server for GET Listening
def run(server_class=HTTPServer, handler_class=GP, port=8088):
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print("Server running at localhost:8088...")
    httpd.serve_forever()

run()