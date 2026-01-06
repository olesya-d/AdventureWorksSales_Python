# Q3 : What is the relationship between Country and Revenue?

import pandas as pd
import matplotlib.pyplot as plt
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'Q3_Revenue-by-country.csv')

df = pd.read_csv(file_path)

# -------- Total Sales per Country --------
df_total = df.sort_values(by='TotalSale', ascending=False)

countries = df_total['CountryRegionCode']
sales_last = df_total['SalesLastYear']
sales_ytd = df_total['SalesYTD']

plt.figure()

bars_last = plt.bar(countries, sales_last, label='Last Year')
bars_ytd = plt.bar(countries, sales_ytd, bottom=sales_last, label='YTD')

plt.xlabel('Country')
plt.ylabel('Total Sales')
plt.title('Total Sales per Country')
plt.xticks(rotation=45)
plt.legend()
plt.ticklabel_format(style='plain', axis='y')

# Add value labels 
for i in range(len(countries)):
    total = sales_last.iloc[i] + sales_ytd.iloc[i]
    plt.text(i, total, f'{total:,.0f}', ha='center', va='bottom')

plt.tight_layout()
plt.show()

# -------- Percentage Change per Country --------
df_change = df.sort_values(by='ChangePCT', ascending=False)
countries = df_change['CountryRegionCode']
change = df_change['ChangePCT']

plt.figure()

bars = plt.bar(countries, change)

plt.xlabel('Country')
plt.ylabel('Change (%)')
plt.title('Sales Percentage Change per Country')
plt.xticks(rotation=45)

# Add value labels
for i in range(len(countries)):
    plt.text(i, change.iloc[i], f'{change.iloc[i]:,.0f}', ha='center', va='bottom')
plt.tight_layout()
plt.show()
