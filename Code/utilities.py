from loguru import logger 
import os
from settings import PATH



def create_folder(output_folder : str = None):
	# ---------- Create folder -----------
	for folder in  list(PATH):
		if not os.path.exists(folder.value):
			os.mkdir(folder.value)
			logger.info(f'Create folder {folder.value}')
	if output_folder != None:
		if not os.path.exists(f'{PATH.Output.value}/{output_folder}'):
			os.makedirs(f'{PATH.Output.value}/{output_folder}')
			logger.info(f'Create folder {output_folder}')
	return  f'{PATH.Output.value}/{output_folder}'

def save(dataset, filename : str):
	folder_path = create_folder(filename)
	logger.info(f'Saving {filename}.csv')
	dataset.to_csv(f'{folder_path}/{filename}.csv')

def formatting_output_ws(message : str)  -> dict :
	pass