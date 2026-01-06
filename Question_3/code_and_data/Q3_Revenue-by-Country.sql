SELECT 
	CountryRegionCode, 
	SUM(SalesYTD) as SalesYTD, 
	SUM(SalesLastYear) as SalesLastYear, 
	(SUM(SalesYTD) + SUM(SalesLastYear)) as TotalSale, 
	((SUM(SalesYTD) - SUM(SalesLastYear)) / SUM(SalesLastYear)) * 100 as ChangePCT
FROM Sales.SalesTerritory
GROUP BY CountryRegionCode