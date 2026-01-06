Select e.JobTitle, p.PersonType, e.SickLeaveHours, d.Department, d.GroupName
from HumanResources.Employee e
inner join Person.Person p
on e.BusinessEntityID = p.BusinessEntityID
inner join HumanResources.vEmployeeDepartment as d
on e.BusinessEntityID = d.BusinessEntityID