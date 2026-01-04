-- Joining two views to get country and revenue
SELECT ssa.CountryRegionName AS Country, 
	ssa.Name AS StoreName,
	ssd.AnnualRevenue AS StoreRevenue

FROM Sales.vStoreWithDemographics ssd
INNER JOIN Sales.vStoreWithAddresses ssa
	ON ssd.BusinessEntityID = ssa.BusinessEntityID

GROUP BY 
    ssa.CountryRegionName, ssa.Name, ssd.AnnualRevenue

ORDER BY
    ssa.CountryRegionName, StoreRevenue DESC;
