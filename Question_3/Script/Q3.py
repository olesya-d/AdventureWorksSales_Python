# Q3 : What is the relationship between Country and Revenue?

# Import neccessery libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Module for disabling automatic scaling
from matplotlib.ticker import StrMethodFormatter

# 1. Data Preparation - Load the dataset

df = pd.read_csv('Group_Project_1\Data\Q3_Revenue-by-country.csv')

# print(df.head())

# Revenue grouped by with Pivot table by country as revenue_by_country
revenue_by_country = df.pivot_table(
    index="Country",
    values="Revenue",
    aggfunc="sum")

# print(revenue_by_country.head())

# 2. Plotting and Configuration

# 2.1. Create Figure and Axes for charts (plt library)
fig, ax = plt.subplots(figsize=(10, 6))

# 2.2. Plotting onto the 'ax' object
revenue_by_country.plot(
    kind='bar',
    y='Revenue',   # Name column as an axis y
    title='Revenue by Countries',
    legend=False,
    rot=0,         # Label's horisontal position for an axis x
    ax=ax          # Give our grap to 'ax'
)

# 2.3. Asis Y formatting: Disable automatic scaling
formatter = StrMethodFormatter('{x:,.0f}')
ax.yaxis.set_major_formatter(formatter)

# 2.4. Setting the Axis Labels and Gridlines
ax.set_xlabel("Country")
ax.set_ylabel("Revenue")
ax.grid(axis='y', linestyle='--', alpha=0.6)

# 2.5. Displaying the bar chart
plt.show()
