CREATE TRIGGER NewArtist
ON Artist AFTER insert
AS
BEGIN
  INSERT INTO Owners
  SELECT ArtistID, 'Artist'
  FROM inserted
END;

GO

CREATE TRIGGER NewCollector
ON Collector AFTER insert
AS
BEGIN
  INSERT INTO Owners
  SELECT CollectorID, 'Collector'
  FROM inserted
END;

GO

CREATE TRIGGER NewVenue
ON Venue AFTER insert
AS
BEGIN
  INSERT INTO Owners
  SELECT VenueID, 'Venue'
  FROM inserted
END;
