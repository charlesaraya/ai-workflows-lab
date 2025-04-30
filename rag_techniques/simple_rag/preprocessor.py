import os

from langchain_community.document_loaders.csv_loader import CSVLoader

def preprocess_csv(path):
    base_path = os.path.dirname(__file__)
    filepath = os.path.join(base_path, path)

    loader = CSVLoader(file_path=filepath)
    return loader.load_and_split()