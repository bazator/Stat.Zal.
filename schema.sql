DROP TABLE IF EXISTS person_name;

CREATE TABLE person_name (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL,
  gender TEXT NOT NULL
);