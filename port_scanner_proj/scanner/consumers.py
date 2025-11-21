import json
import socket
import nmap
from channels.generic.websocket import WebsocketConsumer

class PortScanConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        self.send("connected sockets")

    def receive(self, text_data):
        # print("raw data: ",text_data)  
        data = json.loads(text_data)
        # print("parsed json data: ",data)
        host = data['host']
        # print(f"host: {host}")
        nm = nmap.PortScanner()

        if data['mode'] == 'single':
            port = str(data['port'])
            nm.scan(hosts=host, ports=port, arguments="-Pn")

            if host not in nm.all_hosts():
                self.send(json.dumps({"error": f"{host} is not reachable"}))
                return 

            state = nm[host]['tcp'][int(port)]['state']

            print(f"host: {host}, port: {port}, status: {state}")

            self.send(json.dumps({
                "port":port,
                "status": state
            }))

        elif data["mode"] == 'all':
            nm.scan(hosts=host,ports='1-65535',arguments="-Pn")

            if host not in nm.all_hosts():
                self.send(json.dumps({"error": f"host {host} is not reachable."}))
                return 

            for port in nm[host]['tcp']:
                state = nm[host]['tcp'][port]["state"]

                if state == 'open':
                    print(f"host: {host}, port: {port}, status: {state}")
                self.send(json.dumps({"port":port,"status":state}))

            self.send(json.dumps({"done":True}))
