BEGIN;
--
-- Rename field question_test on question to question_text
--
ALTER TABLE "my_app_question" RENAME COLUMN "question_test" TO "question_text";
COMMIT;
