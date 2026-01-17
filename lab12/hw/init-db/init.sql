DROP TABLE IF EXISTS training_results;

CREATE TABLE
    training_results (
        "training_date" DATETIME,
        "model_name" TEXT,
        "test_mae" DECIMAL,
        "training_set_size" INTEGER
    );