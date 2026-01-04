# Q5: What is the relationship between store trading duration and revenue?
##  Data Source and Initial Exploration

I used data from the **AdventureWorks2022** database.  
The information I needed — **Revenue** and **YearOpened** — already existed in the view:

**`[Sales].[vStoreWithDemographics]`**

I exported the resulting table to a **CSV file** and loaded it into pandas for analysis.

---

## Initial EDA

After loading the data:

```python
df.info()
```
Output:

Entries: 701
Null values: None — the dataset has no missing values.

This means the dataset is clean and ready for further analysis without preprocessing for missing data.

## Answer for a question 

I plotted a **scatter plot** to visualize the relationship between **Duration Opened** and **AnnualRevenue** for all stores.  

![Scatter Plot: Duration Opened vs Annual Revenue](images/Rls_Store_tranding_and_revenue.png)  
  *(This plot shows the relationship between store trading duration and revenue, with a trend line added.)*

The scatter plot show that there is **no linear relationship** between the duration a store has been open and its revenue.

I also calculated the **correlation**  between these two variables: **-0.1336**. 

The correlation is very small, which indicates that there is **no meaningful relationship** between store trading duration and revenue. The correlation is very small, which indicates that there is **no meaningful relationship** between store trading duration and revenue.

 ## Analysis by Store Specialty

- Stores were grouped by **`Specialty`**: `['Touring', 'Mountain', 'Road']`.
- Correlations within each specialty:
```
Touring: -0.0728
Mountain: -0.0834
Road: -0.2035
```


- Correlations are low → **no significant relationship** between store age and revenue within these groups.
- Separate scatter plots were created for each specialty to visualize the relationship.

### Graphs by Specialty

![Touring Plot](images/scatter_mountain.png)  

![Mountain Plot](images/scatter_mountain.png)  

![Road Plot](images/scatter_road.png)  

 We can't see any correlation between store trading duration and revenue for different types of store specialties.  
 The scatter plots and low correlation values confirm that **store age does not significantly affect revenue** within each specialty group.

## Analysis by Store Size (SquareFeet)


- Stores were divided into categories:
- To categorize stores by **size (SquareFeet)**, the following bins and labels were used:

```python
bins = [0, 15000, 30000, 50000, 80000]
labels = ['Small', 'Medium', 'Large', 'Very Large']
```

This creates four size categories:
- Small: 0–15,000 sq. ft.
- Medium: 15,001–30,000 sq. ft.
- Large: 30,001–50,000 sq. ft.
- Very Large: 50,001–80,000 sq. ft.

| StoreSizeCategory | Count |
|------------------|-------|
| Medium           | 218   |
| Very Large       | 204   |
| Large            | 192   |
| Small            | 87    |

### Scatter Plots by Store Size Category

 ![Medium Store Plot](images/scatter_medium.png)  
 ![Very Large Store Plot](images/scatter_very_large.png)  
 ![Large Store Plot](images/scatter_large.png)  
 ![Small Store Plot](images/scatter_small.png)  

- Correlation between **Duration Opened** and **AnnualRevenue** for Medium stores: **-0.1865**  
- Correlations for other size categories (`Very Large`, `Large`, `Small`) are **NaN** because **AnnualRevenue is constant within these categories**, making correlation undefined.

---

### Check of Unique Values per Size Category

| Category    | Unique Duration Values | Unique Revenue Values |
|------------|-----------------------|---------------------|
| Very Large | 21                    | 1                   |
| Large      | 23                    | 1                   |
| Medium     | 21                    | 2                   |
| Small      | 11                    | 1                   |

- This explains why correlation cannot be computed for most categories: **no variation in revenue**.

## Conclusion

- Overall, and within specialties or store size categories, **there is no meaningful linear relationship between the duration a store has been open and its revenue**.  
- Scatter plots and correlation calculations confirm this lack of dependence.  
- Most store size categories have **only one revenue value** because the data is **synthetic**, so correlation cannot be calculated.
