import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import os
import dataframe_image as dfi

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'Q6_ShopsvsSize.csv')
df = pd.read_csv(file_path)

file_path = os.path.join(script_dir, 'Q6_ShopvsSize_extra.csv')
df_extra = pd.read_csv(file_path)

#print(df.head(5))
#print(df.info())
# print(len(df))
# print(df.AnnualRevenue.value_counts())
# print(df.SquareFeet.value_counts())
# print(df.NumberEmployees.value_counts())

rev_group = sorted(df['AnnualRevenue'].unique())
df['rev_per_empl'] = df['AnnualRevenue']/df['NumberEmployees']
df['rev_per_empl'] = df['rev_per_empl'].round(2)

corr = df[['AnnualRevenue', 'SquareFeet', 'NumberEmployees', 'rev_per_empl']].corr()

plt.figure()
sns.heatmap(corr, annot=True, fmt='.3f', cmap='coolwarm', linewidths=0.5, square=True)
plt.title("Correlation Heatmap")  
    
# -------- Shopsize by Revenue boxplot--------
fig, ax = plt.subplots()
sns.boxplot(data=df, x='AnnualRevenue', y='SquareFeet')

plt.title('Shop Size Distribution by Revenue Category', fontsize=16)
plt.xlabel('Annual Revenue(thousands)', fontsize=12)
plt.ylabel('Square Feet(thousands)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Annotate min, max
stats_df = df.groupby('AnnualRevenue')['SquareFeet'].agg(['min', 'max']).reset_index()
for i in range(len(stats_df)):
    min = stats_df.loc[i,'min']
    max = stats_df.loc[i,'max']
    ax.text(i, min, f'min: {int(min/1000)}', ha='center', va='top', fontsize=9)
    ax.text(i, max, f'max: {int(max/1000)}', ha='center', va='bottom', fontsize=9) 

# Format X axis
ticks_x = range(len(rev_group))
labels_x = [f"{int(t/1000)}k" for t in rev_group]
ax.set_xticks(ticks_x)
ax.set_xticklabels(labels_x)

# Format Y axis
ticks_y = ax.get_yticks()
labels_y = [f"{int(t/1000)}k" for t in ticks_y]
ax.set_yticks(ticks_y)
ax.set_yticklabels(labels_y)

# -------- Revenue by Size regplot--------
fig, ax = plt.subplots()
sns.regplot(data=df, x='SquareFeet', y='AnnualRevenue',  line_kws={'color': 'red'})

plt.title('Correlation between  Revenue and Shop Size', fontsize=16)
plt.ylabel('Annual Revenue(thousand)', fontsize=12)
plt.xlabel('Square Feet (thousands)', fontsize=12)
plt.xlim(5000, None)
plt.grid(linestyle='--', alpha=0.5)
# Format X axis
ticks_x = sorted(set(stats_df["min"].to_list() + stats_df["max"].to_list()))
labels_x = [f"{int(t/1000)}k" for t in ticks_x]
idx = ticks_x.index(23000)
labels_x[idx] = ""
ax.set_xticks(ticks_x)
ax.set_xticklabels(labels_x)
# Format Y axis
labels_y = [f"{int(t/1000)}k" for t in rev_group]
ticks_y = rev_group
ax.set_yticks(ticks_y)
ax.set_yticklabels(labels_y)

# -------- Employee by Revenue boxplot--------

fig, ax = plt.subplots()
sns.boxplot(data=df, x='AnnualRevenue', y='NumberEmployees')

plt.title('Number of Employees Distribution by Revenue Category', fontsize=16)
plt.xlabel('Annual Revenue(thousands)', fontsize=12)
plt.ylabel('Number of Employees', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Annotate min, max
stats_df = df.groupby('AnnualRevenue')['NumberEmployees'].agg(['min', 'max']).reset_index()
for i in range(len(stats_df)):
    min = stats_df.loc[i,'min']
    max = stats_df.loc[i,'max']
    ax.text(i, min, f'min: {int(min)}', ha='center', va='top', fontsize=9)
    ax.text(i, max, f'max: {int(max)}', ha='center', va='bottom', fontsize=9)

# Format X axis
ticks_x = range(len(rev_group))
labels_x = [f"{int(t/1000)}k" for t in rev_group]
ax.set_xticks(ticks_x)
ax.set_xticklabels(labels_x)

# -------- Revenue by Employee regplot--------
fig, ax = plt.subplots()
sns.regplot(data=df, x='NumberEmployees', y='AnnualRevenue', line_kws={'color': 'red'})
plt.title('Correlation between  Revenue and Number of Employees', fontsize=16)
plt.ylabel('Annual Revenue(thousand)', fontsize=12)
plt.xlabel('NumberEmployees', fontsize=12)
plt.grid(linestyle='--', alpha=0.5)
# Format X axis
ticks_x = sorted(set(stats_df["min"].to_list() + stats_df["max"].to_list()))
labels_x = [f"{int(t)}" for t in ticks_x]
indexes_hide = [1, 3, 5]
for i in indexes_hide:
    labels_x[i] = ""
ax.set_xticks(ticks_x)
ax.set_xticklabels(labels_x)
# Format Y axis
labels_y = [f"{int(t/1000)}k" for t in rev_group]
ticks_y = rev_group
ax.set_yticks(ticks_y)
ax.set_yticklabels(labels_y)

# -------- Revenue per Employee vs ShopSize regplot --------
fig, ax = plt.subplots()
sns.regplot(data=df, y='rev_per_empl', x='SquareFeet', line_kws={'color': 'red'})

plt.title('Correlation between Revenue per Employee and Shop Size', fontsize=16)
plt.ylabel('Revenue per Employee (thousand)', fontsize=12)
plt.xlabel('Square Feet (thousands)', fontsize=12)
plt.grid(linestyle='--', alpha=0.5)
# Format X axis
ticks_x = ax.get_xticks()
labels_x = [f"{int(t/1000)}k" for t in ticks_x] 
ax.set_xticks(ticks_x)
ax.set_xticklabels(labels_x)
# Format Y axis
ticks_y = ax.get_yticks()
labels_y = [f"{int(t/1000)}k" for t in ticks_y] 
ax.set_yticks(ticks_y)
ax.set_yticklabels(labels_y)

plt.show()

top10 = df.nlargest(10, 'rev_per_empl')[['Name']]
bottom10 = df.nsmallest(10, 'rev_per_empl')[['Name']]


df_extra = df_extra.merge(df[['Name','rev_per_empl']], on='Name')
df_extra['full_name'] =  df_extra['FirstName'] + ' ' + df_extra['LastName']
df_extra['address'] = df_extra['CountryRegionName'] + ", " + df_extra['City']

cols = ['Name', 'address', 'full_name', 'rev_per_empl']
top_table = df_extra.nlargest(10, 'rev_per_empl')[cols]
bottom_table = df_extra.nsmallest(10, 'rev_per_empl')[cols]

script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, '..', 'images')
output_path1 = os.path.join(images_dir, 'tabletop.png')
output_path2 = os.path.join(images_dir, 'tablebottom.png')

dfi.export(top_table, output_path1)
dfi.export(bottom_table, output_path2)

