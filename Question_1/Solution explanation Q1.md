
# Solution explanation #

## **Q1: What are the regional sales in the best performing country?** ## 

### **Data Source and Initial Exploration** ###

I used data from the AdventureWorks2022 database.

The required information was present in the table:

[Sales].[SalesTerritory]

In order to define the best performing country , a SQL query extracted the country names, and summed up the sales for the current year, last year and total sales for 2 years. 

Having identified the US to be the best performing country, another SQL query selected the regions of the US with their sales numbers.

I exported the resulting table to a CSV file and loaded it into pandas for analysis.

### **Answer to the question** ###

I plotted a pie chart to visualize the percentage of sales for each region in the US. [Figure_3_Q1](images/Figure_3_Q1.png)

**Conclusion:**

As seen from the table "Best performing country" [Best Performing country.csv](tables/Best Performing Country.csv), the US has remained the leader in sales for 2 years in a row.
As for the regional sales in the US, South West has been the reqion with most sales, further improving its performance this year in comparison with last year sales.
