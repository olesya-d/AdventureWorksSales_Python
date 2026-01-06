SELECT 
BusinessEntityID, Name, AnnualRevenue, BusinessType, YearOpened, Specialty, NumberEmployees, (2022-YearOpened) as Duration
FROM Sales.vStoreWithDemographics
