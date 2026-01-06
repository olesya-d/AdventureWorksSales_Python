#Q5 : What is the relationship between store trading duration and revenue?

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'Q5_years_open.csv')

df = pd.read_csv(file_path)

# df.head()
# df.info()
# df.describe()
# df.notnull().sum()

df = df.sort_values(by='Duration')

#calculate correlation between Duration opened and AnnualRevenue
correlation = df['Duration'].corr(df['AnnualRevenue'])
print(f'Correlation between Duration Opened and Revenue: {correlation}')

rev_group = sorted(df['AnnualRevenue'].unique())

fig, ax = plt.subplots()

sns.boxplot(data=df, x='AnnualRevenue', y='Duration')
ax.set_title('Store Duration by Revenue Category',fontsize=16)
plt.xlabel('Annual Revenue(thousands)', fontsize=12)
plt.ylabel('Duration(years)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Annotate min, max
stats_df = df.groupby('AnnualRevenue')['Duration'].agg(['min', 'median', 'max']).reset_index()
for i in range(len(stats_df)):
    min = stats_df.loc[i,'min']
    median = stats_df.loc[i,'median']
    max = stats_df.loc[i,'max']
    ax.text(i, min, f'min: {int(min)}', ha='center', va='top', fontsize=9)
    ax.text(i, median, f'median: {int(median)}', ha='center', va='top', fontsize=9)
    ax.text(i, max, f'max: {int(max)}', ha='center', va='bottom', fontsize=9) 

# Format X axis
ticks_x = range(len(rev_group))
labels_x = [f"{int(t/1000)}k" for t in rev_group]
ax.set_xticks(ticks_x)
ax.set_xticklabels(labels_x)

plt.show()