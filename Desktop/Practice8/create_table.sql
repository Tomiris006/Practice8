-- Создание таблицы contacts
CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL
);

-- Вставка тестовых данных (можно удалить или заменить)
INSERT INTO contacts (name, phone) VALUES
('Ali', '87001234567'),
('Dana', '87005556677'),
('Amir', '87009998877');