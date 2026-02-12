import mysql.connector
from mysql.connector import MySQLConnection, Error
from config.settings import settings

class DatabaseConnectionError(Exception):
    pass

def get_server_connection() -> MySQLConnection:
    """
    Conecta no servidor MySQL (sem selecionar database).
    Criado caso database não exista.
    """
    try:
        connection = mysql.connector.connect(
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        )

        if not connection.is_connected():
            raise DatabaseConnectionError("Conexão falhou, objeto inválido.")
        
        return connection
    
    except Error as e:
        raise DatabaseConnectionError(
            f"Erro ao conectar no SQL: ({e.errno}): {e.msg}"
        )


def get_db_connection() -> MySQLConnection:
    """
    Conecta já apontando para o database configurado.
    Caso a database exista (ou já foi criado antes).
    """
    return mysql.connector.connect(
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        database=settings.DB_NAME
    )