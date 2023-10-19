-- creates the database hbtn_0d_2 and the user user_0d_2
-- creates the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create not existed user
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- grant only the select privilige to the user
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
