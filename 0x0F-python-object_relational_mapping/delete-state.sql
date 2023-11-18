-- Delete multiple states from the states table by IDs
USE hbtn_0e_0_usa;

-- Specify the state IDs you want to delete
DELETE FROM states WHERE id IN (6, 7, 8, 11, 12, 13);
