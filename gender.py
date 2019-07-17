def gender():
	import pandas as pd
	from flask import jsonify
	df_csv = pd.read_csv('/home/ganesh/Downloads/adult_dataset.csv')
	dic={}
	df = pd.DataFrame(df_csv)
	
	df1=df.groupby("sex").size().to_dict()
	df1 = {x.replace(' ', ''): v  
     for x, v in df1.items()} 
	df2=df.groupby("relationship").size().to_dict()
	df2 = {x.replace(' ', ''): v  
     for x, v in df2.items()} 
	print(df2)
	dic['gender'] = df1
	dic['relation']=df2
	return dic