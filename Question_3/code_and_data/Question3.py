# Q3 : What is the relationship between Country and Revenue?

import pandas as pd
import matplotlib.pyplot as plt
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'Q3_Revenue-by-country.csv')

df = pd.read_csv(file_path)
df_total = df.sort_values(by='TotalSale', ascending=False)
df_change = df.sort_values(by='ChangePCT', ascending=False)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle("Sales Performance by Country", fontsize=16, fontweight='bold')

# -------- Total Sales per Country --------
countries = df_total['CountryRegionCode']
sales_last = df_total['SalesLastYear']
sales_ytd = df_total['SalesYTD']

axes[0].bar(countries, sales_last, label='Last Year')
axes[0].bar(countries, sales_ytd, bottom=sales_last, label='YTD')

axes[0].set_title('Total Sales per Country')
axes[0].set_xlabel('Country')
axes[0].set_ylabel('Total Sales')
axes[0].tick_params(axis='x', rotation=45)
axes[0].legend()
axes[0].ticklabel_format(style='plain', axis='y')

# Add value labels 
for i in range(len(countries)):
    total = sales_last.iloc[i] + sales_ytd.iloc[i]
    axes[0].text(i, total, f'{total:,.0f}', ha='center', va='bottom')

# -------- Percentage Change per Country --------
countries = df_change['CountryRegionCode']
change = df_change['ChangePCT']

axes[1].bar(countries, change)

axes[1].set_title('Sales Percentage Change per Country')
axes[1].set_xlabel('Country')
axes[1].set_ylabel('Change (%)')
axes[1].tick_params(axis='x', rotation=45)

# Add value labels
for i in range(len(countries)):
    axes[1].text(i, change.iloc[i], f'{change.iloc[i]:,.0f}', ha='center', va='bottom')

plt.tight_layout()
plt.show()
