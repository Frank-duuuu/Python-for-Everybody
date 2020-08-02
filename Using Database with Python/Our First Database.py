# Input these lines into your SQLite Browser
# Remember to delete previous execution before every step

CREATE TABLE Ages (
  name VARCHAR(128),
  age INTEGER
)

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Mali', 13);
INSERT INTO Ages (name, age) VALUES ('Karmen', 23);
INSERT INTO Ages (name, age) VALUES ('Sanfur', 19);
INSERT INTO Ages (name, age) VALUES ('Jez', 18);

SELECT hex(name || age) AS X FROM Ages ORDER BY X
