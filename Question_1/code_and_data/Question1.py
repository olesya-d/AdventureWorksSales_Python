# 1.	What are the regional sales in the best-performing country?
import pandas as pd
import matplotlib.pyplot as plt
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'Q1_Regional sales.csv')

df = pd.read_csv(file_path)

regions = df['Name']
TotalSales = df['TotalSale']

#function to add total values to the slices
def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        value = int(round(pct * total / 100.0))
        return f'{pct:.1f}%\n({value:,})'
    return my_format

plt.pie(TotalSales, labels=regions, autopct=autopct_format(TotalSales), 
        wedgeprops={'edgecolor': 'black','linewidth': 0.5})

plt.title('Total Sales by region')
plt.show()
