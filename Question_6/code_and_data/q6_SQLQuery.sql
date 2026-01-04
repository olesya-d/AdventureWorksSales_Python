select s.Name, a.City, a.StateProvinceName, a.CountryRegionName, s.SalesPersonID, p.FirstName, p.MiddleName, p.LastName
FROM Sales.Store as s
inner join Sales.vStoreWithAddresses as a 
on s.Name = a.Name
inner join Person.Person as p
on s.SalesPersonID = p.BusinessEntityID