-- setup.sql

DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS roles;
DROP TABLE IF EXISTS users;

-- Создать таблицу users
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

-- Создать таблицу roles
CREATE TABLE roles (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    role TEXT NOT NULL
);

-- Создать безвредную таблицу products
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    price NUMERIC NOT NULL
);

-- Вставить начальные данные в users
INSERT INTO users (username, password) VALUES ('alice', 'alice_pass');
INSERT INTO users (username, password) VALUES ('bob', 'bob_pass');
INSERT INTO users (username, password) VALUES ('charlie', 'charlie_pass');

-- Вставить начальные данные в roles
INSERT INTO roles (user_id, role) VALUES (1, 'admin');
INSERT INTO roles (user_id, role) VALUES (2, 'user');
INSERT INTO roles (user_id, role) VALUES (3, 'moderator');

-- Вставить начальные данные в products
INSERT INTO products (name, price) VALUES ('Laptop', 999.99);
INSERT INTO products (name, price) VALUES ('Smartphone', 499.99);
INSERT INTO products (name, price) VALUES ('Headphones', 199.99);

