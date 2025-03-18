USE Multiverz_AI_Chat;
ALTER TABLE chat ADD COLUMN user_name VARCHAR(255) NOT NULL;
INSERT INTO chat (user_name, user_message, ai_response)
SHOW tables;
SELECT * FROM chat LIMIT 10;
