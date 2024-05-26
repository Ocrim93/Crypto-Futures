from Module.extract_data import  Extract
from loguru import logger
from .plotting_lib import create_figure,plot 
from  .utilities import save

class BackTest():
	def __init__(self, input_path, output_path):
		self.input_path = input_path
		self.output_path = output_path
	


	def run(self):
		logger.info('Extracting data')
		extract_obj = Extract(self.input_path)
		dfs_map = extract_obj.from_excel()

		spot = dfs_map['SPOT']
		del dfs_map['SPOT']
		
		for future, df in dfs_map.items():
			logger.info(f'Starting back test for {future}')

			# Check missing price
			logger.info(f'Spot size {spot.shape[0]}')
			logger.info(f'Future size {df.shape[0]}')
			dataset = spot.merge(df, how = 'inner', on ='Date', suffixes = ('_spot', '_fut'))

			logger.info(f'Size after merging  {dataset.shape[0]}')

			dataset['Diff'] = dataset['Close_spot'] - dataset['Close_fut']
			save(dataset, future)
			fig = create_figure(dataset,f'Spot - {future}', 'Date','Diff', future)
			plot(fig,f'{self.output_path}/{future}')

