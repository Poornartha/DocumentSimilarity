
import pandas as pd
from fuzzywuzzy import fuzz


def similarity_check(file1, file2, tar1, tar2, ft1, ft2):
	if ft1 == "1":
		df1 = pd.read_csv(file1)
	else:
		df1 = pd.read_excel(file1)

	if ft2 == "1":
		df2 = pd.read_csv(file2)
	else:
		df2 = pd.read_excel(file2)

	df1.dropna()
	df2.dropna()
	
	return fuzz.ratio(df1[tar1].tolist(), df2[tar2].tolist())
