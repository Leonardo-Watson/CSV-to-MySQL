import pandas as pd
from db.connection import get_server_connection, get_db_connection, DatabaseConnectionError

def main():
    try:
        server_connection = get_server_connection()
        print("Conectado com sucesso.")
        server_connection.close()
    except DatabaseConnectionError as e:
        print(e)
        exit(1)

if __name__ == "__main__":
    main()