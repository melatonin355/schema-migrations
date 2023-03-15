-- +goose Up
-- +goose StatementBegin
CREATE TABLE pets (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  type VARCHAR(255) NOT NULL,
  owner_id INT NOT NULL,
  PRIMARY KEY (id),
);
-- +goose StatementEnd

-- +goose Down
-- +goose StatementBegin
DROP TABLE IF EXISTS pets;
-- +goose StatementEnd
