from .ws import WS
import asyncio
from loguru import logger

async def websockets_run( ws_spot_config : dict ,ws_futures_config : dict):
	logger.info('Instanziated spot websocket')
	ws_spot = WS(**ws_spot_config)
	ws_futures =  WS(**ws_futures_config)
	logger.info('Instanziated futures websocket')

	spot_task = asyncio.create_task(ws_spot.start())
	futures_task = asyncio.create_task(ws_futures.start())
	asyncio.gather(spot_task,futures_task)
	if True:
		#while True:
		message = await ws_spot.wait_for_incoming()
		print(message)
		'''
        ... Connection succeeded. Update messages will now be processed 
        in the "background" provided that other users of the event loop 
        yield in some way ...
        '''
	else:
		print('... Connection failed ...')

def inizialise(  ws_spot_config : dict ,ws_futures_config : dict):

	asyncio.run(websockets_run(ws_spot_config,ws_futures_config))