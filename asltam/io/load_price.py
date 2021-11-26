import pandas as pd
from download import download
from asltam.io import url_price, path_price

class load_price :
	def __init__(self, url = url_price, target = path_price):
		download(url, target, replace = False)

	def save_as_price():
		df_price = pd.read_csv(path_price)
		return df_price