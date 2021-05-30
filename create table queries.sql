-- Artist Table
CREATE TABLE Artist (
  ArtistID int PRIMARY KEY,
  Name varchar(150) NOT NULL,
  DOB date,
  Addl_Info varchar(MAX),
  CONSTRAINT CHK_ID CHECK (ArtistID>=1000000000 AND ArtistID<=9999999999)
  CONSTRAINT CHK_NAME CHECK (Name<>'')
)

/*
--Good insert
INSERT INTO Artist VALUES (1234567890, 'Pablo Picasso', '1776-07-04', 'pablo picasso was born on this date I think')
--Bad insert
insert into Artist values (3,'Andrew Breton','1000-01-01','Pablo Picasso was born in 1000 AD, trust me')
*/

-- Collector Table
CREATE TABLE Collector (
  CollectorID int PRIMARY KEY,
  Name varchar(150) NOT NULL,
  DOB date,
  CONSTRAINT CHK_ID CHECK (CollectorID>=1000000000 AND CollectorID<=9999999999)
  CONSTRAINT CHK_NAME CHECK (Name<>'')
)

/*
--Good insert
INSERT INTO Collector VALUES (17, 'Scarlett Halima', '1800-12-02')
--Bad insert
INSERT INTO Collector VALUES (1723456890, 'Taylor Eyler', '2020-01-25')
*/

-- Venue Table
CREATE TABLE Venue (
  VenueID int NOT NULL,
  Name varchar (150) NOT NULL,
  Hours varchar(150),
  Location varchar(600) NOT NULL,
  Addl_Info varchar(MAX),
  CONSTRAINT PK_Venue PRIMARY KEY (VenueID, Location)
  CONSTRAINT CHK_NAME CHECK (Name<>'')
  CONSTRAINT CHK_LOCATION CHECK (Location<>'')
)

/*
--Good insert
INSERT INTO Venue VALUES ('1234567890','Seattle Art Museum','9a to 5p mon-fri',
                          '1300 1st Ave, Seattle, WA 98101',
                          'Seattle''s most well-known museum')
--Bad insert
INSERT INTO Venue VALUES ('1234567890','Seattle Art Museum','9a to 5p mon-fri',
                          '','Seattle''s most well-known museum')
*/

-- Exhibit Table
CREATE TABLE Exhibit (
  VenueID int FOREIGN KEY REFERENCES Venue(VenueID) NOT NULL,
  Name varchar(150),
  Description varchar(MAX),
  StartDate date NOT NULL,
  EndDate date NOT NULL,
  CONSTRAINT PK_EXHIBIT PRIMARY KEY (VenueID, Name, StartDate)
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
