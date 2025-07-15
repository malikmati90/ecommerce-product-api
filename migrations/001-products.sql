--! Message: Create products table
--! Previous: 

CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    category TEXT NOT NULL,
    price NUMERIC(10, 2) NOT NULL
);