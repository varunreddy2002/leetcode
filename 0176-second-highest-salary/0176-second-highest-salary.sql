select IFNULL(
(select max(salary)
 from Employee 
 where salary<(select max(salary) from employee)), NULL) as "SecondHighestSalary";