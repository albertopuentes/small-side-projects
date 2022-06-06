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