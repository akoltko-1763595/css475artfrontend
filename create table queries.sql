-- Artist Table
CREATE TABLE Artist (
  ArtistID bigint PRIMARY KEY,
  Name varchar(150) NOT NULL,
  DOB date,
  Addl_Info varchar(MAX),
  CONSTRAINT CHK_ARTIST_ID CHECK (ArtistID>=1000000000 AND ArtistID<=9999999999),
  CONSTRAINT CHK_ARTIST_NAME CHECK (Name<>'')
)

--Collector Table
CREATE TABLE Collector (
  CollectorID bigint PRIMARY KEY,
  Name varchar(150) NOT NULL,
  DOB date,
  CONSTRAINT CHK_COLLECTOR_ID CHECK (CollectorID>=1000000000 AND CollectorID<=9999999999),
  CONSTRAINT CHK_COLLECTOR_NAME CHECK (Name<>'')
)

--Venue Table
CREATE TABLE Venue (
  VenueID bigint NOT NULL PRIMARY KEY,
  Name varchar (150) NOT NULL,
  Hours varchar(150),
  Location varchar(600) NOT NULL,
  Addl_Info varchar(MAX),
  CONSTRAINT CHK_VENUE_ID CHECK (VenueID>=1000000000 AND VenueID<=9999999999),
  CONSTRAINT CHK_VENUE_NAME CHECK (Name<>''),
  CONSTRAINT CHK_VENUE_LOCATION CHECK (Location<>'')
)

--Exhibit Table
CREATE TABLE Exhibit (
 Name varchar(150) NOT NULL,
 Description varchar(MAX),
 StartDate date,
 EndDate date,
 VenueID bigint FOREIGN KEY REFERENCES Venue(VenueID) NOT NULL,
 CONSTRAINT PK_Exhibit PRIMARY KEY (VenueID, Name, StartDate),
 CONSTRAINT CHK_EXHIBIT_NAME CHECK (Name<>''),
 CONSTRAINT CHK_START_END_DATES CHECK (StartDate<=EndDate)
)

--Art Style Table
CREATE TABLE Art_Style (
 Name varchar(150) NOT NULL,
 Period varchar(150) NOT NULL,
 Addl_Info varchar(MAX),
 CONSTRAINT PK_Art_Style PRIMARY KEY (Name, Period),
 CONSTRAINT CHK_ART_STYLE_NAME CHECK (Name<>'')
)

--Artwork Table
CREATE TABLE Artwork (
  Title varchar(150) NOT NULL,
  CreationDate date NOT NULL,
  ArtworkValue int,
  ArtistID bigint NOT NULL FOREIGN KEY REFERENCES Artist(ArtistID),
  ArtworkSize varchar(MAX),
  Material varchar(MAX),
  Addl_Info varchar(MAX),
  VenueID bigint  NOT NULL FOREIGN KEY REFERENCES Venue(VenueID),
  StyleName varchar(150) NOT NULL,
  Period varchar(150) NOT NULL,
  CONSTRAINT PK_Artwork PRIMARY KEY (TItle, CreationDate, ArtistID),
  CONSTRAINT CHK_TITLE CHECK (Title<>''),
  CONSTRAINT CHK_VALUE CHECK (ArtworkValue is NULL or ArtworkValue>0),
  CONSTRAINT CHK_ID CHECK (ArtistID>=1000000000 AND ArtistID<=9999999999),
  CONSTRAINT CHK_ARTWORKSIZE CHECK (ArtworkSize<>''),
  CONSTRAINT CHK_MATERIAL CHECK (Material<>''),
  CONSTRAINT FK_ARTSTYLE FOREIGN KEY (StyleName, Period) REFERENCES   Art_Style(Name, Period)
)

--Owners Table
CREATE TABLE Owners (
  OwnerID bigint PRIMARY KEY NOT NULL,
  OwnerType varchar(9) NOT NULL,
  CONSTRAINT CHK_TYPE CHECK (OwnerType in ('Collector', 'Artist', 'Venue'))
)

--Art Ownership Table
CREATE TABLE Art_Ownership (
  OwnerID bigint NOT NULL FOREIGN KEY REFERENCES Owners(OwnerID),
  ArtTitle varchar(150) NOT NULL,
  ArtCreationDate date NOT NULL,
  ArtistID bigint NOT NULL,
  CONSTRAINT FK_OWNERS FOREIGN KEY (ArtTitle, ArtCreationDate, ArtistID) REFERENCES Artwork(Title, CreationDate, ArtistID)
)

--Exhibit Contents Table
CREATE TABLE Exhibit_Contents (
 VenueID bigint NOT NULL,
 Name varchar(150) NOT NULL,
 StartDate Date NOT NULL,
 Title varchar(150) NOT NULL,
 CreationDate Date NOT NULL,
 ArtistID bigint NOT NULL,
 CONSTRAINT PK_Exhibit_Contents PRIMARY KEY (VenueID, Name, StartDate, Title, CreationDate, ArtistID),
 CONSTRAINT FK_Exhibit FOREIGN KEY (VenueID, Name, StartDate) REFERENCES Exhibit(VenueID, Name, StartDate),
 CONSTRAINT FK_Artwork FOREIGN KEY (Title, CreationDate, ArtistID) REFERENCES Artwork(Title, CreationDate, ArtistID)
)
