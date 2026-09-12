CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    done BOOLEAN NOT NULL DEFAULT FALSE
);

INSERT INTO tasks (title, done)
SELECT 'Learn FastAPI', FALSE
WHERE NOT EXISTS (SELECT 1 FROM tasks);

INSERT INTO tasks (title, done)
SELECT 'Buy milk', TRUE
WHERE NOT EXISTS (
    SELECT 1 FROM tasks WHERE title = 'Buy milk'
);

INSERT INTO tasks (title, done)
SELECT 'Finish assignment', FALSE
WHERE NOT EXISTS (
    SELECT 1 FROM tasks WHERE title = 'Finish assignment'
);