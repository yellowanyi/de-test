CREATE TABLE salesperson
  (
     id   INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
     name TEXT
  );

CREATE TABLE customer
  (
     id    INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
     name  TEXT NOT NULL,
     phone TEXT NOT NULL
  );

CREATE TABLE manufacturer
  (
     id   INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
     name TEXT
  );

CREATE TABLE car
  (
     id                    INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
     is_new                BOOLEAN NOT NULL DEFAULT true,
     manufacturer_id       INTEGER,
     model_name            TEXT NOT NULL,
     model_variant         TEXT NOT NULL,
     serial_number         TEXT NOT NULL,
     weight                TEXT NOT NULL,
     engine_cubic_capacity TEXT NOT NULL,
     price                 DECIMAL(18, 8) NOT NULL,
     CONSTRAINT fk_manufacturer FOREIGN KEY (manufacturer_id) REFERENCES manufacturer (id)
  );

CREATE TABLE transaction
  (
     salesperson_id   INTEGER,
     car_id           INTEGER,
     PRIMARY KEY      (salesperson_id, car_id),
     customer_id      INTEGER,
     create_timestamp TIMESTAMP NOT NULL DEFAULT Now(),
     CONSTRAINT fk_salesperson FOREIGN KEY (salesperson_id) REFERENCES salesperson (id),
     CONSTRAINT fk_car FOREIGN KEY (car_id) REFERENCES car (id),
     CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES customer (id)
  );
