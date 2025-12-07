import json
import socket
import nmap
from channels.generic.websocket import AsyncWebsocketConsumer
# from channels.generic.websocket import WebsocketConsumer
import asyncio
from concurrent.futures import ThreadPoolExecutor
import time

thread_pool = ThreadPoolExecutor(max_workers=1000)



class PortScanConsumer(AsyncWebsocketConsumer):

    # def connect(self):
    #     self.accept()

    async def connect(self):
        await self.accept()

    async def disconnect(self,close_code):
        pass

    # def receive(self,text_data):

    async def receive(self, text_data):
        # print("raw data: ",text_data)  
        data = json.loads(text_data)
        # print("parsed json data: ",data)
        ip = data['host']
        # print(f"host: {host}")
        nm = nmap.PortScanner()
        host = socket.gethostbyname(ip)

        loop = asyncio.get_running_loop()

        if data['mode'] == 'single':
            port = str(data['port'])
            
            # nm.scan(hosts=host, ports=port, arguments="-Pn")
            # await asyncio.to_thread(nm.scan, hosts=host, ports=port,  arguments="-Pn")

            if int(port) > 65535:
                await self.send(json.dumps({"error": f"{port} is invalid, please enter between 1-65535."}))
                return 
            await loop.run_in_executor(thread_pool,nm.scan,host,port,'-Pn -sV')

            if host not in nm.all_hosts():
                # self.send(json.dumps({"error": f"{host} is not reachable"}))
                await self.send(json.dumps({"error": f"{host} is not reachable"}))
                return 

            state = nm[host]['tcp'][int(port)]['state']
            service = nm[host]['tcp'][int(port)].get('product','') + " " + nm[host]['tcp'][int(port)].get('version','')
            service = service.strip() if service else 'unknown service'
            
            #adding service detecion feature.

            print(f"host: {host}, port: {port}, status: {state}, 'service':{service}")

            # self.send(json.dumps({
            #     "port":port,
            #     "status": state
            # }))

            await self.send(json.dumps({
                "port":port,
                "status": state,
                'service':service
            }))

        elif data["mode"] == 'all':
            start_time = time.perf_counter()
            # nm.scan(hosts=host, ports=port, arguments="-Pn")

            await loop.run_in_executor(thread_pool,nm.scan,host,'1-65535','-Pn -sV')

            if host not in nm.all_hosts():
                # self.send(json.dumps({"error": f"host {host} is not reachable."}))
                await self.send(json.dumps({"error": f"host {host} is not reachable."}))
                return 

            for port in nm[host]['tcp']:

                state = nm[host]['tcp'][port]["state"]
                version = nm[host]['tcp'][port].get('version', '')
                product = nm[host]['tcp'][port].get('product', '')

                service_info = f"{product} {version}".strip()

                if state == 'open':
                    print(f"host: {host}, port: {port}, status: {state}, service: {service_info}")
                
                # self.send(json.dumps({"port":port,"status":state}))
                await self.send(json.dumps({"port":port,"status":state,
                                            "service":service_info}))

            end_time = time.perf_counter()
            total_time = round(end_time - start_time,3)
            print("total time taken by this port scanner: ",total_time)

            # self.send(json.dumps({"done":True}))
            await self.send(json.dumps({"done":True}))

