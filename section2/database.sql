-- sql to retrieve all registered users in tha last 30 days.
SELECT *
FROM Users
WHERE CreatedDate >= NOW() - INTERVAL 30 DAY;


-- sql to find total number of users with specific domain in their email
SELECT COUNT(*) AS total
FROM Users
WHERE email LIKE '%@example.com';


-- update a user email with specific userId
UPDATE Users
SET email = 'newemail@example.com'
WHERE UserId = 1;