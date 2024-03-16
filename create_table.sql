DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  location VARCHAR(255),
  gender VARCHAR(255),
  address TEXT,
  postcode VARCHAR(20),
  email VARCHAR(255) UNIQUE NOT NULL,
  username VARCHAR(255) UNIQUE NOT NULL,
  dob DATE,
  registered_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  phone VARCHAR(20),
  picture VARCHAR(255),
  timestamp TIMESTAMP,
  label VARCHAR(255)
);
