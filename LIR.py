import pandas as pd
import numpy as np

# LIR generator
t = range(0,1201)
cf = pd.DataFrame(data=t, columns=['t'])
cf['GOC_ID'] = "LOB_1_2312"
['SPCODE','GOC_ID','cf_bom','cf_mom','cf_eom']
data= np.array([1111,"LOB_1_2312",100,100,100])
cf_df = pd.DataFrame(columns=['SPCODE','GOC_ID','cf_bom','cf_mom','cf_eom'],data=data)