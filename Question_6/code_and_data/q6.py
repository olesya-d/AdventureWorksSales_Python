import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_csv("q6_Shops.csv")

#print(df.head(5))
#print(df.info())

# print(len(df))
# print(df.AnnualRevenue.value_counts())
# print(df.SquareFeet.value_counts())
# print(df.NumberEmployees.value_counts())

df['rev_per_empl'] = df['AnnualRevenue']/df['NumberEmployees']

corr = df[['AnnualRevenue', 'SquareFeet', 'NumberEmployees', 'rev_per_empl']].corr()

plt.figure()
sns.heatmap(corr, annot=True, fmt='.3f', cmap='coolwarm', linewidths=0.5, square=True)
plt.title("Correlation Heatmap")


plt.figure()
sns.boxplot(data=df, x='AnnualRevenue', y='SquareFeet')

plt.title('Shop Size Distribution by Revenue Category', fontsize=16)
plt.xlabel('Annual Revenue(thousands)', fontsize=12)
plt.ylabel('Square Feet(thousands)', fontsize=12)

ax = plt.gca()

groups = df.groupby('AnnualRevenue')['SquareFeet']
for i, (rev, g) in enumerate(groups):
    stats = g.describe() 
    ax.text(i, stats['min'], f"min: {int(stats['min']/1000)}", ha='center', va='top', fontsize=9)
    ax.text(i, stats['max'], f"max: {int(stats['max']/1000)}", ha='center', va='bottom', fontsize=9)

rev_group = sorted(df['AnnualRevenue'].unique())
ticks_x = range(len(rev_group))
labels_x = [f"{int(t/1000)}k" for t in rev_group]

ticks_y = ax.get_yticks()
labels_y = [f"{int(t/1000)}k" for t in ticks_y] 

ax.set_xticks(ticks_x)
ax.set_xticklabels(labels_x)
ax.set_yticks(ticks_y)
ax.set_yticklabels(labels_y)

plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.figure()
sns.regplot(data=df, x='SquareFeet', y='AnnualRevenue',  line_kws={'color': 'red'})

plt.title('Correlation between  Revenue and Shop Size', fontsize=16)
plt.ylabel('Annual Revenue(thousand)', fontsize=12)
plt.xlabel('Square Feet (thousands)', fontsize=12)

ax = plt.gca()
grouped = df.groupby("AnnualRevenue")["SquareFeet"].agg(["min", "max"]).reset_index()
ticks_x = sorted(set(grouped["min"].to_list() + grouped["max"].to_list()))
labels_x = [f"{int(t/1000)}k" for t in ticks_x]
idx = ticks_x.index(23000)
labels_x[idx] = ""

labels_y = [f"{int(t/1000)}k" for t in rev_group]
ticks_y = rev_group

ax.set_yticks(ticks_y)
ax.set_yticklabels(labels_y)
ax.set_xticks(ticks_x)
ax.set_xticklabels(labels_x)
plt.xlim(5000, None)
plt.grid(linestyle='--', alpha=0.5)


#--------------------------------------

plt.figure()
sns.boxplot(data=df, x='AnnualRevenue', y='NumberEmployees')

plt.title('Number of Employees Distribution by Revenue Category', fontsize=16)
plt.xlabel('Annual Revenue(thousands)', fontsize=12)
plt.ylabel('Number of Employees', fontsize=12)

ax = plt.gca()

groups = df.groupby('AnnualRevenue')['NumberEmployees']
for i, (rev, g) in enumerate(groups):
    stats = g.describe() 

    ax.text(i, stats['min'], f"min: {int(stats['min'])}", ha='center', va='top', fontsize=9)
    ax.text(i, stats['max'], f"max: {int(stats['max'])}", ha='center', va='bottom', fontsize=9)

#rev_group = sorted(df['AnnualRevenue'].unique())
labels_x = [f"{int(t/1000)}k" for t in rev_group]
ticks_x = range(len(rev_group))
ax.set_xticks(ticks_x)
ax.set_xticklabels(labels_x)

plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.figure()
sns.regplot(data=df, x='NumberEmployees', y='AnnualRevenue', line_kws={'color': 'red'})

plt.title('Correlation between  Revenue and Number of Employees', fontsize=16)
plt.ylabel('Annual Revenue(thousand)', fontsize=12)
plt.xlabel('NumberEmployees', fontsize=12)

ax = plt.gca()
grouped = df.groupby("AnnualRevenue")["NumberEmployees"].agg(["min", "max"]).reset_index()
ticks_x = sorted(set(grouped["min"].to_list() + grouped["max"].to_list()))
labels_x = [f"{int(t)}" for t in ticks_x]
indexes_hide = [1, 3, 5]
for i in indexes_hide:
    labels_x[i] = ""

labels_y = [f"{int(t/1000)}k" for t in rev_group]
ticks_y = rev_group

ax.set_yticks(ticks_y)
ax.set_yticklabels(labels_y)
ax.set_xticks(ticks_x)
ax.set_xticklabels(labels_x)
plt.grid(linestyle='--', alpha=0.5)

plt.figure()
sns.regplot(data=df, y='rev_per_empl', x='SquareFeet', line_kws={'color': 'red'})

plt.title('Correlation between  Revenue per Employee and Shop Size', fontsize=16)
plt.ylabel('Revenue per Employee (thousand)', fontsize=12)
plt.xlabel('Square Feet (thousands)', fontsize=12)

ax = plt.gca()
ticks_x = ax.get_xticks()
labels_x = [f"{int(t/1000)}k" for t in ticks_x] 
ticks_y = ax.get_yticks()
labels_y = [f"{int(t/1000)}k" for t in ticks_y] 
ax.set_xticks(ticks_x)
ax.set_xticklabels(labels_x)
ax.set_yticks(ticks_y)
ax.set_yticklabels(labels_y)
plt.grid(linestyle='--', alpha=0.5)

plt.show()
df["rev_per_empl"] = df["rev_per_empl"].round(2)

top10_shop = df.sort_values('rev_per_empl', ascending = False).head(10)['Name']
bottom10_shop = df.sort_values('rev_per_empl').head(10)['Name']

df4 = pd.read_csv('q6_extra.csv')
df4 = df4.merge(df[['Name','rev_per_empl']], on='Name')
df4['full_name'] =  df4['FirstName'] + ' ' + df4['LastName']
df4['address'] = df4['CountryRegionName'] + ", " + df4['City']

top_table = df4.sort_values('rev_per_empl', ascending = False).head(10)[['Name','address', 'full_name','rev_per_empl']]
bottom_table = df4.sort_values('rev_per_empl').head(10)[['Name','address','full_name','rev_per_empl']]
# print('top10:')

# print(top_table)
# print('\nbottom10:')

# print(bottom_table)

import dataframe_image as dfi

dfi.export(top_table, "tabletop.png")
dfi.export(bottom_table, "tablebottom.png")
