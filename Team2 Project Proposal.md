# Team 2  
## Data Analytics Interim Project Proposal

### Overview
The team used **SQL** to query the relevant data from the Adventure Works database.  

The following **Python libraries** were used in the analysis:  
- **pandas** – for data manipulation, joining, filtering, and grouping  
- **seaborn** – for boxplots, regression plots, and correlation visualizations  
- **matplotlib** – for customizing labels, grids, ticks, and plots  

| Proposed by | Team 2<br>Kristina Schogol<br>Nataliia Biliuk<br>Oksana Karpenko<br>Olesya Drozhzhina |
|-------------|----------------|
| Timeframe   | Completion by 20.11<br>Presentation on 20.11 |

---

### Objectives and Steps
Using the Adventure Works dataset, we aimed to answer the following questions:

---

#### 1. What is the regional sales in the best performing country?

**Steps taken:**  
1. Queried data from the table `Sales.SalesTerritory` with attributes: `CountryRegionCode`, `SalesYTD`, `SalesLastYear`.  
2. Identified the best performing country by total sales (**US**) and extracted its regions.  
3. Created tables with attributes: `CountryCode` & `Sales`, and `RegionName` & `Sales`.

**Analysis:**  
- Pie chart showing the percentage of sales per region.  
- **South West** region had the highest sales over the two years.

---

#### 2. What is the relationship between annual leave taken and bonus?

**Steps taken:**  
1. Joined `Sales.SalesPerson` and `HumanResources.Employee` tables to obtain: `BusinessEntityID`, `Bonus`, `VacationHours`.  
2. Calculated correlation between bonus and vacation hours.

**Analysis:**  
- No discernible correlation was found.  
- Scatter plot visualized the absence of correlation between vacation taken and bonus.

---

#### 3. What is the relationship between Country and Revenue?  

**Steps taken:**  
1. Constructed dataset by joining the views:  
   - `Sales.vStoreWithDemographics`  
   - 'Sales.vStoreWithAddresses`  
2. Resulting table included: 'AnnualRevenue' and 'CountryName' 

**Analysis:**  
- Created Pivot table calculating and grouping revenue by country.  
- **Bar chart** showed the revenue in the US significantly exceeded the revenue in the other countries, which was to be expected based on the difference in the number of stores across the countries.

--- 

#### 4. What is the relationship between sick leave and Job Title?

**Steps taken:**  
1. Constructed dataset by joining:  
   - `HumanResources.Employee`  
   - `Person.Person`  
   - `HumanResources.vEmployeeDepartment`  
2. Resulting table included: `JobTitle`, `PersonType`, `SickLeaveHours`, `Department`, `GroupName`.

**Analysis:**  
- Only two values for `PersonType` and 67 unique `JobTitle` values.  
- **Boxplot** showed Sales Persons take fewer sick leave hours than other employees.  
- Explored extremes for `JobTitle` using dual horizontal bar charts (top 10 and bottom 10 by average sick leave).  
  - Roles with highest average leave: operational and physical labor roles (e.g., Stocker, Janitor).  
  - Roles with lowest average leave: highly specialized technical and senior management jobs (e.g., CFO, VP of Engineering).  
- Department-wise sick leave analysis did not reveal significant insights.

---

#### 5. What is the relationship between store trading duration and revenue?

**Steps taken:**  
Retrieved data from `Sales.vStoreWithDemographics` with attributes: `Revenue` and `YearOpened`.  

**Analysis:**  
- Scatter plot showed **no linear relationship** between duration a store has been open and revenue.  
- Correlation calculations confirmed minimal relationship.  
- Grouped stores by **Speciality** (Touring, Mountain, Road) and **Size**, analyzed correlations.  
- Separate scatter plots per speciality showed no significant relationship.  
- Synthetic nature of data (most store size categories have constant revenue) limited correlation calculations.

---

#### 6. What is the relationship between store size, number of employees, and revenue?

**Steps taken:**  
 Data from `Sales.vStoreWithDemographics` with attributes: `Name`, `AnnualRevenue`, `SquareFeet`, `NumberEmployees`.  

**Analysis:**  
- Initial correlation analysis confirmed: larger stores with more employees tend to generate higher revenue.  
- Introduced **RevenuePerEmployee = AnnualRevenue / NumberEmployees** to measure efficiency.  
- Identified top 10 most efficient and bottom 10 least efficient stores.  
- Combined data from `Sales.Store`, `Sales.vStoreWithAddresses`, and `Person.Person` to provide store name, location, and sales representative details.
