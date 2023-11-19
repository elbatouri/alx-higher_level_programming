-- Delete multiple states from the states table by IDs
USE hbtn_0e_6_usa;

-- Specify the state IDs you want to delete
DELETE FROM states WHERE id IN (7, 8, 9, 10);
