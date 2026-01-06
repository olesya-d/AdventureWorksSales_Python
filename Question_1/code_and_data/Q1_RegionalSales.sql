SELECT Name, SalesYTD, SalesLastYear, (SalesYTD + SalesLastYear) as TotalSale
FROM Sales.SalesTerritory
WHERE CountryRegionCode='US';
