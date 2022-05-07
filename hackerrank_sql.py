# Given the table schemas below, write a query to print the company_code, 
# founder name, total number of lead managers, total number of senior managers,
#  total number of managers, and total number of employees. Order your output by ascending company_code.

#1st attempt
select c.company_code, 
        c.founder, 
        count(DISTINCT l.lead_manager_code), 
        count(DISTINCT s.senior_manager_code), 
        count(DISTINCT m.manager_code), 
        count(DISTINCT e.employee_code)
from Company c, Lead_Manager l, Senior_Manager s, Manager m, Employee e
where c.company_code = l.company_code
    and l.lead_manager_code = s.lead_manager_code,
    and s.senior_manager_code = m.senior_manager_code,
    and m.manager_code = e.manager_code
group by c.company_code
order by c.company_code

#2nd attempt (answer)
select c.company_code, 
    c.founder, 
    count(DISTINCT e.lead_manager_code), 
    count(DISTINCT e.senior_manager_code), 
    count(DISTINCT e.manager_code), 
    count(DISTINCT e.employee_code)
from Company c
    inner join Employee e on c.company_code = e.company_code
group by c.company_code, c.founder
order by c.company_code

# Query the following two values from the STATION table:
# The sum of all values in LAT_N rounded to a scale of  decimal places.
# The sum of all values in LONG_W rounded to a scale of  decimal places 

select round(sum(LAT_N), 2), 
    round(sum(LONG_W), 2)
from STATION

# Query the sum of Northern Latitudes (LAT_N) f
# From STATION having values greater than  and less than . Truncate your answer to  decimal places.

select round(sum(LAT_N), 4)
from STATION
where LAT_N < 137.2345 and LAT_N > 38.7880;

# Query the greatest value of the Northern Latitudes 
# (LAT_N) from STATION that is less than . Truncate your answer to  decimal places.

select round(max(LAT_N), 4)
from STATION
where LAT_N < 137.2345;

#Query the Western Longitude (LONG_W) for the largest 
# Northern Latitude (LAT_N) in STATION that is less than . 
# Round your answer to  decimal places.

select round(LONG_W, 4)
from STATION
where LAT_N = (select max(LAT_N) from STATION where LAT_N < 137.2345);

#Query the smallest Northern Latitude (LAT_N) from 
# STATION that is greater than . Round your answer to  decimal places.

select round(min(LAT_N), 4)
from STATION
where LAT_N > 38.7780;

# Query the Western Longitude (LONG_W)where the smallest 
# Northern Latitude (LAT_N) in STATION is greater than . Round your answer to  decimal places.

select round(LONG_W, 4)
from STATION
where LAT_N = (select min(LAT_N) from STATION where LAT_N > 38.7780);

#Consider  and  to be two points on a 2D plane.

 #happens to equal the minimum value in Northern Latitude (LAT_N in STATION).
 #happens to equal the minimum value in Western Longitude (LONG_W in STATION).
 #happens to equal the maximum value in Northern Latitude (LAT_N in STATION).
 #happens to equal the maximum value in Western Longitude (LONG_W in STATION).
#Query the Manhattan Distance between points  and  and round it to a scale of  decimal places.

select round((max(LAT_N)-min(LAT_N)) + (max(LONG_W)-min(LONG_W)), 4)
from STATION