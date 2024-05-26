import requests
import json
import hmac
import hashlib
import base64
from urllib.parse import urlencode
import time
from loguru import logger 
import asyncio
import websockets


class WS:
	def __init__(self, base_url :str ,
					   ticker : str,
					   public_private_url : str  ,
					   api_config : dict  ):
		self.base_url = base_url
		self.ticker = ticker
		self.public_private_url = public_private_url
		self.privateChannel = 'private' in public_private_url
		self.api_config = api_config

	async def destroy():
		if (self.websocket.open):
			self.websocket.close()  # Terminates any recv() in wait_for_incoming() 
			#await self.incoming_message_task  # keep asyncio happy by awaiting the "background" task

	def get_token(self,api_key,api_secret,api_passphrase):
		base_url = self.base_url

		def get_headers(method):
			now = int(time.time() * 1000)
			str_to_sign = str(now) + method + endpoint
			signature = base64.b64encode(hmac.new(api_secret.encode(), str_to_sign.encode(), hashlib.sha256).digest()).decode()
			passphrase = base64.b64encode(hmac.new(api_secret.encode(), api_passphrase.encode(), hashlib.sha256).digest()).decode()
			return {'KC-API-KEY': api_key,
			        'KC-API-KEY-VERSION': '2',
			        'KC-API-PASSPHRASE': passphrase,
			        'KC-API-SIGN': signature,
			        'KC-API-TIMESTAMP': str(now)}
		logger.info
		req = requests.post(f"{self.base_url}{self.public_private_url}")#,headers=get_headers("POST",self.public_private_url))
		print(req.json())
		return(req.json())
    
	async def start(self):
		try:
			now = str(int(time.time() * 1000))
			data = self.get_token(**self.api_config)['data']
			server = data['instanceServers'][0]
			self.url = f"{server['endpoint']}?token={data['token']}&[connectId={now}]"
			self.websocket = await websockets.connect(self.url)          
			# Get its initial message which describes its full state
			self.initial_message = await self.websocket.recv()
			# Store the initial inventory
			await self.initial_process()
			# Set up a "background" task for further streaming reads of the web socket
			#self.incoming_message_task = asyncio.create_task(self.wait_for_incoming())
			# Done
			return True
		except Exception as e :
			print(e)
		    # Connection failed (or some unexpected error)
			return False

	async def wait_for_incoming(self):
	    while  self.websocket.open:
	        try:
	            return await self.websocket.recv()
	            #print(f'update_message {message}')
	            #asyncio.create_task(self.process_update_message(update_message))
	        except Exception as e :
	        	print(e)
	            # Presumably, socket closure
	            

	async def initial_process(self):
		#params = {"type": "subscribe", "topic": "/market/ticker:BTC-USDT,ETH-USDT", "response": True, "privateChannel":False}
		params = {"type": "subscribe", "topic": f"/market/ticker:{self.ticker}", "response": True, "privateChannel": self.privateChannel}
		await self.websocket.send(json.dumps(params))
        #... Process initial_inventory_message into self.inventory ...
    
	async def process_update_message(self, update_message):
		print(update_message)


async def main():
	websocket = WS('https://api.kucoin.com', 'ETH-USDT')
	if await websocket.start():
		#while True:
		message = await websocket.wait_for_incoming()
		print(message)

	else:
		print('... Connection failed ...')
asyncio.run(main())
       


