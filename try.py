import pyodbc

def connect_to_mssql(server, port, database, user, password):
    connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server},{port};"
        f"DATABASE={database};"
        f"UID={user};"
        f"PWD={password}"
    )
    try:
        conn = pyodbc.connect(connection_string)
        print("Connected to the database")
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

def get_tables(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
        tables = [row.TABLE_NAME for row in cursor.fetchall()]
        return tables
    except Exception as e:
        print(f"Error retrieving tables: {e}")
        return []

def main():
    server = 'your_server'
    port = 'your_port'
    database = 'your_database'
    user = 'your_username'
    password = 'your_password'

    conn = connect_to_mssql(server, port, database, user, password)
    if conn:
        tables = get_tables(conn)
        print("Tables in the database:")
        for table in tables:
            print(table)
        conn.close()
        print("Connection closed")

if __name__ == "__main__":
    main()
