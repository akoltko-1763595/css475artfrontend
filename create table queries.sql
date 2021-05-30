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

-- TABLENAME Table: Scarlett
CREATE TABLE Exhibit (
  Name varchar(150) NOT NULL,
  Description varchar(MAX),
  StartDate date,
  EndDate date,
  VenueID int FOREIGN KEY REFERENCES Venue(VenueID) NOT NULL
  CONSTRAINT PK_Exhibit PRIMARY KEY (VenueID, Name, StartDate)
)

/*
--Good insert

--Bad insert

*/

-- TABLENAME Table
CREATE TABLE Art_Style (
  Name varchar(150) NOT NULL,
  Period varchar(MAX),
  Addl_Info varchar(MAX)
  CONSTRAINT PK_Art_Style PRIMARY KEY (Name, Period)
)

/*
--Good insert

--Bad insert

*/

-- TABLENAME Table
CREATE TABLE Artwork (
  Title varchar(150) NOT NULL,
  CreationDate Date NOT NULL,
  ArtworkValue int NOT NULL,
  CONSTRAINT ARTWORK_VALUE_CHK_ID CHECK (ArtworkValue>=0),
  ArtistID int FOREIGN KEY REFERENCES Artist(ArtistID) NOT NULL,
  Addl_Info varchar(MAX),
  VenueID int FOREIGN KEY REFERENCES Venue(VenueID) NOT NULL,
  StyleName varchar(150) FOREIGN KEY REFERENCES Art_Style(Name),
  Period varchar(MAX) FOREIGN KEY REFERENCES Art_Style(Table)
  CONSTRAINT PK_Artwork PRIMARY KEY (Title, CreationDate, ArtistID)
)

/*
--Good insert

--Bad insert

*/

-- TABLENAME Table
CREATE TABLE Artwork_Creation (
  ArtistID int FOREIGN KEY REFERENCES Artist(ArtistID) NOT NULL,
  Title varchar(150) FOREIGN KEY REFERENCES Artwork(Title) NOT NULL,
  CreationDate Date FOREIGN KEY REFERENCES Artwork(CreationDate) NOT NULL
  CONSTRAINT PK_Artwork_Creation PRIMARY KEY (ArtistID, Title, CreationDate)
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
  VenueID int FOREIGN KEY REFERENCES Venue(VenueID) NOT NULL,
  Name varchar(150) FOREIGN KEY REFERENCES Exhibit(Name) NOT NULL,
  StartDate Date FOREIGN KEY REFERENCES Exhibit(StartDate) NOT NULL,
  Title varchar(150) FOREIGN KEY REFERENCES Artwork(Title) NOT NULL,
  CreationDate Date FOREIGN KEY REFERENCES Artwork(CreationDate) NOT NULL,
  ArtistID int FOREIGN KEY REFERENCES Artist(ArtistID) NOT NULL,
  CONSTRAINT PK_Exhibit_Contents PRIMARY KEY (VenueID, Name, StartDate, Title, CreationDate, ArtistID)
)

/*
--Good insert

--Bad insert

*/
