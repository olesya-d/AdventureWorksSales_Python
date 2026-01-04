
# Overview Q3 (What is the relationship between Country and Revenue?)

This part of the project aims to analyze and visualize the relationship between Country and Revenue. The data is sourced from Microsoft Learn website.

## Dataset

The dataset used in this project is the AdventureWorks2022 database. This is one of the sample databases originally published by Microsoft and is widely used for learning and demonstration purposes.

## Database  

Required information such as **AnnualRevenue** and **CountryRegionName** was already in two separate views:

**`[Sales].[vStoreWithDemographics]`**

**`[Sales].[vStoreWithAddresses]`**

## SQL Queries

To gather the necessary information into a single table, SQL was used as a robust and efficient way to query and manipulate the data:

[Q3_Revenue-by-Country.sql](https://github.com/KristinaScgen/Group-Task_2/blob/main/Question_3/Data/Q3_Revenue-by-Country.sql)

As a result of utilizing SQL, a **CSV file** containing the necessary results for analysis was generated:

[Q3_Revenue-by-country.csv](https://github.com/KristinaScgen/Group-Task_2/blob/main/Question_3/Data/Q3_Revenue-by-country.csv)

## Python scripts

Data has been checked on missing values. Were found 701 entries with no Null data. Data was ready wor further analysis without additional processing.

For answering the question was used **Python** code:

[Q3.py - For Bar Chart](https://github.com/KristinaScgen/Group-Task_2/blob/main/Question_3/Script/Q3.py)
[Q3-addon.py - For Scatter Plot](https://github.com/KristinaScgen/Group-Task_2/blob/main/Question_3/Script/Q3-addon.py)

# Answer for a question

## Bar Chart

A **bar chart** was plotted to clearly illustrate the relationship between **Revenue** and **Country**, providing a direct comparison of performance across all markets.  

![Bar Chart: Revenue by Countries](https://github.com/KristinaScgen/Group-Task_2/blob/main/Question_3/Images/Revenue_by_countries.png)
  
This chart visualizes the total aggregated Revenue across key international markets, revealing the concentration of sales within the primary geographical areas.

### Key Observations:

**Market Dominance:** The United States is the overwhelmingly dominant market, generating over $65,000,000 in revenue.

**Second-Tier Market:** Canada stands as the second-largest market, contributing nearly $20,000,000.

**Comparable Low Contributors:** The remaining four regions (Australia, France, Germany, and the United Kingdom) show relatively similar and low revenue totals, all falling below the $10,000,000 mark.

### Conclusion:

The chart shows that the U.S. drives most of our sales, which is typical given its size and economy. However, we shouldn"t rely only on these absolute numbers. To truly see how effective we are, we need to calculate Revenue per Capita (revenue divided by population). This will show if smaller markets like Canada or Germany are actually generating revenue more efficiently relative to their size, informing future strategic decisions.

## Scatter Plot
To better address this question and deepen the analysis, an additional plot was considered.
A **scatter plot** was used to test the hypothesis that **Total Revenue** is positively correlated with the **Number of Stores per Country**, offering a visual comparison of market scale and output.

![The generated table shows the Store Count and Total Revenue by Country](https://github.com/KristinaScgen/Group-Task_2/blob/main/Question_3/Images/Number_of_stores_by_country.png)

![Relationship between Number of stores and Total Revenue by Country](https://github.com/KristinaScgen/Group-Task_2/blob/main/Question_3/Images/Number_of_stores_vs_Revenue_by_Country.png)

Relationship Analysis: Store Count vs. Revenue
To further explore the factors driving high revenue concentration, a scatter plot was used to test the relationship between the Number of Stores per Country and the Total Revenue.

### Key Observations:
**Strong Positive Correlation:** The plot clearly demonstrates a strong, linear correlation between the number of stores and the generated revenue. Markets with more established physical presence tend to generate higher total sales.

The calculated Pearson correlation coefficient is:

![Pearson_Correlation](https://github.com/KristinaScgen/Group-Task_2/blob/main/Question_3/Images/Pearson_correlation.png)

**Outlier Status:** The United States acts as a significant outlier, reinforcing its absolute market dominance by possessing the highest store count (427) and the highest revenue (over $67 million).

**Linear Tiering:** Canada follows the same linear trend but operates in a clear second tier (approx. 114 stores). The remaining markets cluster tightly in the low-end quadrant, characterized by a low store count (around 40) and low revenue.

**Strategic Synthesis:** From Absolute to Efficient Growth
The initial analysis confirms that the U.S. is the primary revenue driver, consistent with its economic size, and that total sales strongly correlates with the physical store count.

However, the high reliance on absolute numbers demands a pivot to strategic evaluation:

# Final Conclusion and Next Steps:
The current revenue distribution is highly skewed. To truly see how effective markets are, we need to calculate Revenue per Capita (revenue divided by population). This relative metric will show if smaller markets like Canada or Germany are actually generating revenue more efficiently relative to their size, informing future strategic decisions regarding store expansion and capital allocation. This is essential for unlocking hidden market potential and mitigating the risk associated with over-reliance on the primary market.


