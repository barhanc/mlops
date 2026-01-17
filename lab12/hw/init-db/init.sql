DROP TABLE IF EXISTS training_results;

CREATE TABLE
    training_results (
        "model_name" TEXT,
        "test_mae" DECIMAL,
        "test_mape" DECIMAL,
        "train_size" INTEGER,
        "train_date" TIMESTAMP
    );