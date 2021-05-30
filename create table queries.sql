-- Artist Table
CREATE TABLE Artist (
  ArtistID int NOT NULL,
  Name varchar(150) NOT NULL,
  DOB date,
  Addl_Info varchar(MAX),
  CONSTRAINT CHK_ID CHECK (ArtistID>=1000000000 AND ArtistID<=9999999999)
)

/*
--Good insert
INSERT INTO Artist VALUES (1234567890, 'Pablo Picasso', '1776-07-04', 'pablo picasso was born on this date I think')
--Bad insert
insert into Artist values (3,'Pablo Picasso','1000-01-01','Pablo Picasso was born in 1000 AD, trust me')
*/

-- TABLENAME Table
CREATE TABLE Collector (

)

/*
--Good insert

--Bad insert

*/

-- TABLENAME Table
CREATE TABLE Venue (

)

/*
--Good insert

--Bad insert

*/

-- TABLENAME Table
CREATE TABLE Exhibit (

)

/*
--Good insert

--Bad insert

*/

-- TABLENAME Table
CREATE TABLE Art_Style (

)

/*
--Good insert

--Bad insert

*/

-- TABLENAME Table
CREATE TABLE Artwork (

)

/*
--Good insert

--Bad insert

*/

-- TABLENAME Table
CREATE TABLE Artwork_Creation (

)

/*
--Good insert

--Bad insert

*/

-- TABLENAME Table
CREATE TABLE Art_Ownership (

)

/*
--Good insert

--Bad insert

*/

-- TABLENAME Table
CREATE TABLE Exhibit_Contents (

)

/*
--Good insert

--Bad insert

*/
