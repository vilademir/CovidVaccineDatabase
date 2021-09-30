use vaccinations;

CREATE TABLE States(
    Entity VARCHAR(150) PRIMARY KEY,
    Code VARCHAR(100),
    DateWeek VARCHAR(100),
    TotalVacci INT,
    Population INT
    );

CREATE TABLE Pfizer(
  Jurisdiction VARCHAR(150) PRIMARY KEY,
  DATE VARCHAR(100),
  First INT,
  Second INT,
  isDeleted INTEGER,
  FOREIGN KEY (Jurisdiction) REFERENCES States(Entity)

);

CREATE TABLE Moderna(
  Jurisdiction VARCHAR(150),
  DATE VARCHAR(100),
  FirstDose INT,
  SecondDose INT,
  isDeleted INTEGER,
  FOREIGN KEY (Jurisdiction) REFERENCES States(Entity)

);

CREATE TABLE Janssen(
  Jurisdiction VARCHAR(150),
  DATE VARCHAR(100),
  FirstD INT,
  isDeleted INTEGER,
  FOREIGN KEY (Jurisdiction) REFERENCES States(Entity)

);

CREATE TABLE US(
    Location VARCHAR(150),
    Cases INT,
    Deaths INT,
    ConfirmedCases INT,
    FOREIGN KEY (Location) REFERENCES States(Entity)
);


drop table Pfizer;
drop table Moderna;
drop table Janssen;
drop table US;
drop table States;

