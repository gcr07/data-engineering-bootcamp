#!/usr/bin/python3

import pandas as pd



size = 1000000

df = pd.read_csv('all_data.csv', chunksize=size)


header=True

for chunk in df:
	chunk_filter= chunk['cadenaComercial']
	#print(chunk_filter.unique())
	chunk_filter.to_csv('out.csv', header=header, mode='a',index=False)
	header= False
