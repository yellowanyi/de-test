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

CREATE TABLE car
  (
     id                    INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
     is_new                BOOLEAN NOT NULL DEFAULT true,
     manufacturer          TEXT NOT NULL,
     model_name            TEXT NOT NULL,
     model_variant         TEXT NOT NULL,
     serial_number         TEXT NOT NULL,
     weight                TEXT NOT NULL,
     engine_cubic_capacity TEXT NOT NULL,
     price                 DECIMAL(18, 8) NOT NULL
  );

CREATE TABLE transaction
  (
     id               INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
     salesperson_id   INTEGER,
     customer_id      INTEGER,
     car_id           INTEGER,
     status           TEXT,
     create_timestamp TIMESTAMP NOT NULL DEFAULT Now(),
     CONSTRAINT fk_salesperson FOREIGN KEY (salesperson_id) REFERENCES salesperson (id),
     CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES customer (id),
     CONSTRAINT fk_car FOREIGN KEY (car_id) REFERENCES car (id)
  );
