import pandas as pd
from src.ingestion.reader import csv_reader

def transformer_data():
    for arquivo, data in csv_reader():
        print(f'Iniciando transformação de: {arquivo}')
        data = normalize_column(data)
        print(data.columns)

def normalize_column(data: pd.DataFrame) -> pd.DataFrame:

    # Trata moedas
    data.columns = (
        data.columns
        .str.replace("R$", " BRL ", regex=False)
        .str.replace("€", " EUR ", regex=False)
        .str.replace("$", " USD ", regex=False)
    )

    # Normalização geral
    data.columns = (
        data.columns
        .str.strip()
        .str.normalize('NFD')
        .str.encode('ascii', errors='ignore')
        .str.decode('utf-8')
        .str.replace(r"[^a-zA-Z0-9_]", "_", regex=True)
        .str.replace(r"_+", "_", regex=True)
        .str.strip("_")
        .str.lower()
    )
    return data

# def normalize_rows(data: pd.DataFrame) -> pd.DataFrame:
#     print(data)

if __name__ == "__main__":
    transformer_data()