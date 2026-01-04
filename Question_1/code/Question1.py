import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
reg_sales=pd.read_csv(r"C:\Users\natal\OneDrive\Documents\python\Visualization task\Question1\Regional sales.csv")
reg_sales['salesTotal']=reg_sales['SalesYTD']+reg_sales['SalesLastYear']
regions=reg_sales.iloc[:,0]
totalSales=reg_sales.iloc[:,3]
plt.pie(totalSales, labels=regions, autopct='%1.1f%%')
plt.title('Total Sales by region')
plt.show()
