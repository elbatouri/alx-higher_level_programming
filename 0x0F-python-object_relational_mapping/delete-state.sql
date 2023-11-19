-- Delete multiple states from the states table by IDs
USE hbtn_0e_6_usa;

-- Specify the state IDs you want to delete
DELETE FROM states WHERE id IN (1, 2, 3, 4, 5);
