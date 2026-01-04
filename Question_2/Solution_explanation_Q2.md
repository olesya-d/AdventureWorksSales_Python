
# Solution explanation #

## **Q2: What is the relationship between annual leave taken and bonus?** ## 

### **Data Source and Initial Exploration** ###

I used data from the AdventureWorks2022 database.

The required information was present in the tables:

[Sales.SalesPerson] and [HumanResources.Employee]

A SQL query extracted employees'IDs, bonus and annual leave data. 

I exported the resulting table to a CSV file and loaded it into pandas for analysis.

### **Answer to the question** ###

I calculated correlation between annual leave and bonus. The correlation was very low, 0.38, indicating that there was no strong correlation between the 2 variables.

I plotted a scatter plot to visualize the relationship. [Figure_3_Q1](images/Figure_1_Q2.png)

**Conclusion:**

As you can see from the scatter plot, there is no strong correlation between the annual leave taken and bonus earned. However, the data does seem to suggest that 3 out of 4 people who have taken the shortest time of annual leave have also not earned any bonus, which might indicate that employees perform their best when given a chance to recuperate.
