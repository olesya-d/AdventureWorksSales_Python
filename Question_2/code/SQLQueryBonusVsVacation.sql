SELECT Sales.SalesPerson.BusinessEntityID,Bonus, HumanResources.Employee.VacationHours
FROM Sales.SalesPerson
LEFT JOIN HumanResources.Employee ON (Sales.SalesPerson.BusinessEntityID = HumanResources.Employee.BusinessEntityID)
ORDER BY Bonus
