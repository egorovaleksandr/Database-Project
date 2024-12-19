CREATE TABLE IF NOT EXISTS customer
(
  customer_id INTEGER NOT NULL PRIMARY KEY,
  full_name TEXT NOT NULL,
  phone_number VARCHAR(20) NOT NULL UNIQUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS seller
(
  seller_id INTEGER NOT NULL PRIMARY KEY,
  full_name TEXT NOT NULL,
  phone_number VARCHAR(20) NOT NULL UNIQUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS payment
(
  pay_id INTEGER NOT NULL PRIMARY KEY,
  pay_method TEXT NOT NULL,
  pay_date DATE NOT NULL,
  account_number TEXT NOT NULL,
  receipt_size REAL CHECK(receipt_size >= 0)
);

CREATE TABLE IF NOT EXISTS maker
(
  maker_id INTEGER NOT NULL PRIMARY KEY,
  company TEXT NOT NULL UNIQUE,
  country TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS model
(
  model_id INTEGER NOT NULL PRIMARY KEY,
  model_name TEXT NOT NULL,
  color TEXT NOT NULL,
  number_of_seats INTEGER CHECK(number_of_seats > 0 AND number_of_seats < 10),
  engine TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS price
(
  model_id INTEGER NOT NULL,
  price REAL NOT NULL CHECK(price > 0),
  date_from DATE NOT NULL,
  date_to DATE,
  PRIMARY KEY (model_id, date_from),
  FOREIGN KEY (model_id) REFERENCES model(model_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS automobile
(
  automobile_id INTEGER NOT NULL PRIMARY KEY,
  car_brand TEXT NOT NULL,
  maker_id INTEGER NOT NULL,
  model_id INTEGER NOT NULL,
  FOREIGN KEY (maker_id) REFERENCES maker(maker_id) ON DELETE CASCADE,
  FOREIGN KEY (model_id) REFERENCES model(model_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS service_info
(
  service_id INTEGER PRIMARY KEY NOT NULL,
  seller_id INTEGER NOT NULL,
  automobile_id INTEGER NOT NULL,
  service_date DATE NOT NULL,
  pay_id INTEGER NOT NULL,
  FOREIGN KEY (seller_id) REFERENCES seller(seller_id) ON DELETE CASCADE,
  FOREIGN KEY (automobile_id) REFERENCES automobile(automobile_id) ON DELETE CASCADE,
  FOREIGN KEY (pay_id) REFERENCES payment(pay_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS service
(
  customer_id INTEGER NOT NULL,
  service_id INTEGER NOT NULL,
  automobile_id INTEGER NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES customer(customer_id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES service_info(service_id) ON DELETE CASCADE,
  FOREIGN KEY (automobile_id) REFERENCES automobile(automobile_id) ON DELETE CASCADE,
  PRIMARY KEY (customer_id, service_id, automobile_id)
);

CREATE INDEX IF NOT EXISTS idx_customer_phone ON customer(phone_number);

CREATE INDEX IF NOT EXISTS idx_seller_phone ON seller(phone_number);

CREATE INDEX IF NOT EXISTS idx_price_model ON price(model_id);

CREATE INDEX IF NOT EXISTS idx_automobile_model ON automobile(model_id);