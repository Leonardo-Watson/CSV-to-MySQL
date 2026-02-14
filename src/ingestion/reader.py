from pathlib import Path
import pandas as pd

def choose_chunksize(path: str) -> int | None:
    size_mb = Path(path).stat().st_size / (1024 * 1024)

    if size_mb < 10:
        return None
    elif size_mb < 30:
        return 20000
    else:
        return 50000

def csv_reader():
    BASE_DIR = Path(__file__).resolve().parents[2]
    data_path = BASE_DIR / 'data'

    for file in data_path.glob("*.csv"):
        print(f"Processando o arquivo: {file.name}")
        chunksize = choose_chunksize(file)

        if chunksize is None:
            df = pd.read_csv(file)
            yield file.name, df
        else:
            for chunk in pd.read_csv(file, chunksize=chunksize):
                print(f"Chunk do arquivo {file.name} processado: {chunk.shape}")
                yield file.name, chunk
