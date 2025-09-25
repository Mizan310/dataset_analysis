# installed pandas
# installed pandas-profiling

import pandas as pd
from pandas_profiling import ProfileReport 

df = pd.read_csv('housing.csv')
print(df)