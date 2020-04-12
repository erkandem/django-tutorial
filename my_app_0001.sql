BEGIN;
--
-- Create model Choice
--
CREATE TABLE "my_app_choice" ("id" serial NOT NULL PRIMARY KEY, "choice_text" varchar(200) NOT NULL, "votes" integer NOT NULL);
--
-- Create model Question
--
CREATE TABLE "my_app_question" ("id" serial NOT NULL PRIMARY KEY, "question_test" varchar(200) NOT NULL, "pub_date" timestamp with time zone NOT NULL);
--
-- Add field question to choice
--
ALTER TABLE "my_app_choice" ADD COLUMN "question_id" integer NOT NULL;
CREATE INDEX "my_app_choice_question_id_3cc54135" ON "my_app_choice" ("question_id");
ALTER TABLE "my_app_choice" ADD CONSTRAINT "my_app_choice_question_id_3cc54135_fk_my_app_question_id" FOREIGN KEY ("question_id") REFERENCES "my_app_question" ("id") DEFERRABLE INITIALLY DEFERRED;
COMMIT;
