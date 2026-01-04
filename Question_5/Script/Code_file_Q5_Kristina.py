#Q5 : What is the relationship between store trading duration and revenue?

#import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

#load the data
df = pd.read_csv('Data/data for Q5.csv')
df.head()

#EDA
df.info()
df.describe()

df.notnull().sum()

#create new columns 'Duration opened in years' when we know only YearOpened
current_year = datetime.now().year
df['Duration_opened_in_years'] = current_year - df['YearOpened']
df.head()

df = df.sort_values(by='Duration_opened_in_years')

#plot relationship between store trading duration and revenue
plt.scatter(df['Duration_opened_in_years'], df['AnnualRevenue'])
plt.xlabel('Duration Opened (years)')
plt.ylabel('Revenue')
trendline = np.polyfit(df['Duration_opened_in_years'], df['AnnualRevenue'], 1)
plt.plot(df['Duration_opened_in_years'], np.polyval(trendline, df['Duration_opened_in_years']), color='red', linestyle='-', label='Trendline')
plt.title('Relationship between Store Trading Duration and Revenue')
plt.show()

#calculate correlation between Duration opened and AnnualRevenue
correlation = df['Duration_opened_in_years'].corr(df['AnnualRevenue'])
print(f'Correlation between Duration Opened and Revenue: {correlation}')

#try to group by Duration_opened_in_years by Specialty and plot result for each Specialty
specialties = df['Specialty'].unique()
print(specialties)
for specialty in specialties:
    specialty_data = df[df['Specialty'] == specialty]
    correlation = specialty_data['Duration_opened_in_years'].corr(specialty_data['AnnualRevenue'])
    plt.scatter(specialty_data['Duration_opened_in_years'], specialty_data['AnnualRevenue'], label=specialty)
    plt.text(x=60, y=50000, s=f'Correlation ={correlation:.2f}', fontsize=12, color='red')
    trendline = np.polyfit(specialty_data['Duration_opened_in_years'], specialty_data['AnnualRevenue'], 1)
    plt.plot(specialty_data['Duration_opened_in_years'], np.polyval(trendline, specialty_data['Duration_opened_in_years']), color='red')
    plt.xlabel('Duration Opened (years)')
    plt.ylabel('Revenue')
    plt.title(f'Relationship between Store Trading Duration and Revenue for {specialty}')
    plt.legend()
    plt.show()

    print(f'Correlation between Duration Opened and Revenue for {specialty}: {correlation}')


# i devided data by size of store(SquareFeet collumn) and want to see correlation between Duration opened and AnnualRevenue for each size
bins = [0, 15000, 30000, 50000, 80000]
labels = ['Small', 'Medium', 'Large', 'Very Large']
df['StoreSizeCategory'] = pd.cut(df['SquareFeet'], bins=bins, labels=labels)


categories = df['StoreSizeCategory'].unique()

for cat in categories:
    cat_data = df[df['StoreSizeCategory'] == cat]

    plt.figure(figsize=(6,4))
    plt.scatter(cat_data['Duration_opened_in_years'], cat_data['AnnualRevenue'])
    plt.title(f'Scatter: Duration vs Revenue ({cat})')
    plt.xlabel('Duration Opened (years)')
    plt.ylabel('Annual Revenue')
    plt.trendline = np.polyfit(cat_data['Duration_opened_in_years'], cat_data['AnnualRevenue'], 1)
    
    plt.plot(specialty_data['Duration_opened_in_years'], np.polyval(plt.trendline, specialty_data['Duration_opened_in_years']), color='red')
    plt.show()
    correlation = cat_data['Duration_opened_in_years'].corr(cat_data['AnnualRevenue'])
    print(f'Correlation between Duration Opened and Revenue for {cat} stores: {correlation}')

df['StoreSizeCategory'].value_counts()

#check how many unique values in Duration_opened_in_years and AnnualRevenue for Very Large, large, medium and small stores
for category in ['Very Large', 'Large', 'Medium', 'Small']:
    duration_unique = df[df['StoreSizeCategory'] == category]['Duration_opened_in_years'].nunique()
    revenue_unique = df[df['StoreSizeCategory'] == category]['AnnualRevenue'].nunique()

    print(f"Category: {category}")
    print(f"  Unique 'Duration_opened_in_years' values: {duration_unique}")
    print(f"  Unique 'AnnualRevenue' values: {revenue_unique}")
    print("-" * 50)



    
# The correlation is very small, which indicates that there is **no meaningful relationship** between store trading duration and revenue.   