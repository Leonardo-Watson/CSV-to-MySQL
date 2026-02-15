from pathlib import Path
import pandas as pd

def choose_chunksize(path: str) -> int | None:
    """
    Define o tamanho do chunk com base no tamanho do arquivo.
    Retorna None para leitura completa ou um inteiro para leitura em partes.
    """
    size_mb = Path(path).stat().st_size / (1024 * 1024)

    if size_mb < 10:
        return None
    elif size_mb < 30:
        return 20000
    else:
        return 50000
    
def _decoder_csv(file: Path, chunksize=None, **kwargs):
    """
    Tenta ler CSV com UTF-8 e faz fallback para encodings comuns no Brasil.
    Retorna o resultado do pd.read_csv (DataFrame ou TextFileReader).
    """
    encodings_to_try = ["utf-8", "utf-8-sig", "cp1252", "latin1"]

    last_err = None
    for encode in encodings_to_try:
        try:
            return pd.read_csv(file, encoding=encode, chunksize=chunksize, **kwargs)
        except UnicodeDecodeError as e:
            last_err = e

    raise last_err

def csv_reader():
    """
    Percorre os arquivos CSV do diretório data, aplica leitura com
    definição automática de chunksize e fallback de encoding.
    Retorna os dados utilizando generator (yield).
    """
    BASE_DIR = Path(__file__).resolve().parents[2]
    data_path = BASE_DIR / 'data'

    for file in data_path.glob("*.csv"):
        print(f"Processando o arquivo: {file.name}")
        chunksize = choose_chunksize(file)

        if chunksize is None:
            df = _decoder_csv(file)
            yield file.name, df
        else:
            reader = _decoder_csv(file, chunksize=chunksize)
            for chunk in reader:
                print(f"Chunk do arquivo {file.name} processado: {chunk.shape}")
                yield file.name, chunk

