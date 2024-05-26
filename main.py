from loguru import logger 
import yaml
import datetime as dt
from Code.run import inizialise

config = yaml.safe_load(open("settings.yml"))

def daily_inizialization():
	today = dt.datetime.now().strftime('%d%b%Y')
	logger_name = config['FILE_NAME']['log'].format(today)
	logger.add(f"{config['PATH']['log_path']}/{logger_name}",enqueue=True)


if __name__ == "__main__":
	daily_inizialization()
	logger.info('Starting bot')
	api_config = config['API']
	ws_spot_config = { 'base_url' : config['WEB_SOCKET_URL']['SPOT_BASE'] ,
					   'ticker' : config['TICKER'],
					   'public_private_url' : config['WEB_SOCKET_URL']['API_PUBLIC']  ,
					   'api_config' : api_config }
	ws_futures_config = { 'base_url' : config['WEB_SOCKET_URL']['FUTURES_BASE'] ,
					   'ticker' : config['TICKER'],
					   'public_private_url' : config['WEB_SOCKET_URL']['API_PUBLIC']  ,
					   'api_config' : api_config }
	inizialise(ws_spot_config,ws_futures_config)
