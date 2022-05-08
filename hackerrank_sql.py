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

#Consider  and  to be two points on a 2D plane where  are the respective minimum and maximum values of Northern Latitude (LAT_N) and  are the respective minimum and maximum values of Western Longitude (LONG_W) in STATION.
# Query the Euclidean Distance between points  and  and format your answer to display  decimal digits.

select round(
    sqrt(
    power(max(LAT_N)-min(LAT_N), 2) + 
    power(max(LONG_W)-min(LONG_W), 2)
    ), 4)
from STATION;

# A median is defined as a number separating the 
# higher half of a data set from the lower half. 
# Query the median of the Northern Latitudes (LAT_N) from STATION and round your answer to  decimal places.

select LAT_N
from (select LAT_N, ROW_NUMBER() OVER(ORDER BY LAT_N) AS RowNum
      from STATION) as temptable
where temptable.RowNum = ((count(LAT_N)/2) + ((count(LAT_N)/2)+1))/2

select round(LAT_N, 4)
from (select ROW_NUMBER() OVER(ORDER BY LAT_N) AS RowNum, LAT_N
      from STATION) as t
where t.RowNum = 250