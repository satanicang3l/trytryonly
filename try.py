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
    except pyodbc.InterfaceError as ie:
        print("Error: Unable to connect to the database. Please check your server and port.")
        print(f"InterfaceError: {ie}")
    except pyodbc.DatabaseError as de:
        print("Error: A database error occurred.")
        print(f"DatabaseError: {de}")
    except pyodbc.Error as e:
        sqlstate = e.args[1]
        if '28000' in sqlstate:
            print("Error: Invalid authorization specification. Please check your username and password.")
        else:
            print("Error: An error occurred while connecting to the database.")
            print(f"Error: {e}")
    except Exception as e:
        print("An unexpected error occurred.")
        print(f"Exception: {e}")
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
