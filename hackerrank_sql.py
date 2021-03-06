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

#Ketty gives Eve a task to generate a report containing three columns: Name, Grade and Mark. 
# Ketty doesn't want the NAMES of those students who received a grade lower than 8. The report 
# must be in descending order by grade -- i.e. higher grades are entered first. If there is more
#  than one student with the same grade (8-10) assigned to them, order those particular students 
# by their name alphabetically. Finally, if the grade is lower than 8, use "NULL" as their name and 
# list them by their grades in descending order. If there is more than one student with the same grade (1-7) assigned to them, order those particular students by their marks in ascending order.
# Write a query to help Eve.

select if (Grade < 8, null, Name), Grade, Marks
from Students s Join Grades g on Marks between Min_Mark and Max_Mark
order by g.Grade desc, s.Name, s.Marks

# Julia just finished conducting a coding contest, and she needs your help 
# assembling the leaderboard! Write a query to print the respective hacker_id 
# and name of hackers who achieved full scores for more than one challenge. 
# Order your output in descending order by the total number of challenges in w
# hich the hacker earned a full score. If more than one hacker received full scores in same number of challenges, 
# then sort them by ascending hacker_id.

select h.hacker_id, h.name
from submissions s
inner join challenges c on s.challenge_id = c. challenge_id
inner join difficulty d on c.difficulty_level = d.difficulty_level
inner join hackers h on s.hacker_id = h.hacker_id
where s.score = d.score and c.difficulty_level = d.difficulty_level
group by s.hacker_id, h.name
having count(s.hacker_id) > 1
order by count(s.hacker_id) desc, s.hacker_id

#Harry Potter and his friends are at Ollivander's with Ron, finally replacing Charlie's old broken wand.
# Hermione decides the best way to choose is by determining the minimum number of gold galleons needed to buy each non-evil wand of high power and age. Write a query to print the id, age, coins_needed, and power of the wands that Ron's interested in, sorted in order of descending power. If more than one wand has same power, sort the result in order of descending age

select w.id, wp.age, s.min_coins_needed, s.power
from (select code, power, min(coins_needed) as min_coins_needed
  from wands
  group by power, code) as s 
left join wands w
  on w.coins_needed = s.min_coins_needed and w.code = s.code and w.power = s.power
left join wands_property as wp 
  on w.code = wp.code 
where wp.is_evil = 0
order by s.power desc, wp.age desc