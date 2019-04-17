import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np 

#read in year cvs file and define 
yearly_deaths=pd.read_csv('yearly_deaths_by_clinic.csv',dtype={'year': 'str', 'births': 'int','deaths': 'int'}, parse_dates=['year'])
monthly_deaths=pd.read_csv('monthly_deaths.csv')
print(yearly_deaths.columns)
print(yearly_deaths.dtypes)

#check datatypes 
yearly_deaths.describe()


yearly_deaths.groupby('year').mean().deaths.plot.bar()
height=yearly_deaths.groupby('year').mean().deaths
plt.xlabel('year', fontsize=14)
plt.ylabel('deaths', fontsize=14)
plt.xticks(np.arange(6),('1841', '1842', '1843', '1844', '1845','1846'), rotation=20)
years=['1841', '1842', '1843', '1844', '1845','1846']
#barlist=plt.bar([yearly_deaths], [year], color='b')
#plt.bar(yearly_deaths, height, color=(0.1, 0.2, 0.3, 0.4))
#plt.bar(years, deaths, color=(0.2, 0.4, 0.3, 0.5))

plt.show()