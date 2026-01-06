SELECT CountryRegionCode, SUM(SalesYTD) as TotalSalesYTD, SUM(SalesLastYear) as TotalSalesLastYear, SUM(SalesYTD + SalesLastYear) as TotalSales
FROM Sales.SalesTerritory
GROUP BY CountryRegionCode
ORDER BY SUM(SalesYTD + SalesLastYear) DESC
