-- task_4.sql
-- Script to print the full description of the 'books' table
-- without using DESCRIBE or EXPLAIN

SELECT 
    COLUMN_NAME AS FIELD,
    COLUMN_TYPE AS TYPE,
    IS_NULLABLE AS 'NULL',
    COLUMN_KEY AS 'KEY',
    COLUMN_DEFAULT AS 'DEFAULT',
    EXTRA AS EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME = 'books';
