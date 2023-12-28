import pandas as pd
from facebookpostpredictions.logger import logging
from facebookpostpredictions.exception import customexception

import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    raw_data_path: str
    train_data_path: str
    test_data_path: str

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.ingestion_config = config

    def initiate_data_ingestion(self, dataset_path: str):
        logging.info("Data ingestion started")

        try:
            # Read dataset
            data = pd.read_csv(Path(dataset_path))
            logging.info("Dataset read as a DataFrame")

            # Save raw dataset
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Raw dataset saved in the artifacts folder")

            # Train-test split
            logging.info("Performing train-test split")
            train_data, test_data = train_test_split(data, test_size=0.25)
            logging.info("Train-test split completed")

            # Save train and test datasets
            train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False)

            logging.info("Data ingestion completed")

            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path

        except Exception as e:
            logging.error("Exception occurred during data ingestion")
            raise customexception(e, sys)

# Example usage:
config = DataIngestionConfig(
    raw_data_path=os.path.join("artifacts", "raw.csv"),
    train_data_path=os.path.join("artifacts", "train.csv"),
    test_data_path=os.path.join("artifacts", "test.csv")
)

data_ingestion = DataIngestion(config)
train_data_path, test_data_path = data_ingestion.initiate_data_ingestion(dataset_path="notebooks/data/dataset1.csv")
