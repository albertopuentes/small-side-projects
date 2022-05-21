Question: Find the total number of downloads for paying and non-paying users by date. Include only records where non-paying customers have more downloads than paying customers. The output should be sorted by earliest date first and contain 3 columns date, non-paying downloads, paying downloads.

SELECT date,
non_paying,
paying
FROM
(SELECT date, SUM(CASE
WHEN paying_customer = 'yes' THEN downloads
END) AS paying,
SUM(CASE
WHEN paying_customer = 'no' THEN downloads
END) AS non_paying
FROM ms_user_dimension a
INNER JOIN ms_acc_dimension b ON a.acc_id = b.acc_id
INNER JOIN ms_download_facts c ON a.user_id=c.user_id
GROUP BY date
ORDER BY date) t
WHERE (non_paying - paying) > 0
ORDER BY t.date ASC;

#Question: Find all number pairs whose first number is smaller than the second one and the product of two numbers is larger than 11.
#Output both numbers in the combination.

SELECT DISTINCT n1.number AS num1, n2.number AS num2
FROM transportation_numbers n1
INNER JOIN transportation_numbers n2 ON n1.index <> n2.index
WHERE n1.number < n2.number
AND n1.number * n2.number > 11;