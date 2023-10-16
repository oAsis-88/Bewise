CREATE TABLE IF NOT EXISTS questions_info
(
    id bigserial,
    question_id bigint unique not null,
    question_text text not null,
    question_answer text not null,
    question_created_at timestamp not null,

    create_date timestamp not null,
    update_date timestamp
);