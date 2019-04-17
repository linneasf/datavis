import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

#read in year cvs file and define 
yearly_deaths=pd.read_csv('yearly_deaths_by_clinic.csv',dtype={'year': 'str', 'births': 'int','deaths': 'int'}, parse_dates=['year'])
monthly_deaths=pd.read_csv('monthly_deaths.csv')
print(yearly_deaths.columns)
print(yearly_deaths.dtypes)

#check datatypes 
yearly_deaths.describe()


yearly_deaths.groupby('year').mean().deaths.plot.bar()