import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 

yearly_deaths=pd.read_csv('yearly_deaths_by_clinic.csv')
monthly_deaths=pd.read_csv('monthly_deaths.csv')


# variables are DX, Sess, and Valence

graph=sns.lineplot(x="births",y="deaths",data=monthly_deaths, estimator="mean",ci=95)
#,hue="DX",style="Sess",estimator="mean", ci=95)
ax=graph.axes
ax.set_xlim(0,0.3)
plt.title('Calcarine', fontsize=18)
plt.xlabel('births', fontsize=14)
plt.ylabel('deaths', fontsize=14)
plt.tick_params(labelsize=13)
#svm = sn.heatmap(df_cm, annot=True,cmap='coolwarm', linecolor='white', linewidths=1)

figure = graph.get_figure()    
#igure.savefig('',format='png', dpi=1000)
#plt.savefig('/home/sepeforrestl2/EmoEvalGraphs/Calcarine_Line_KETPLC.eps',format='eps', dpi=1000)
plt.show()


