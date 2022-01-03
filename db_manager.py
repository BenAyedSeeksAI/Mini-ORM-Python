import sqlite3 as sql3
import datetime


class ConnectionSqliteManager:
    def __init__(self,filename):
        self.filename = filename

    def __enter__(self):
        print("Connection started ...")
        self.connection = sql3.connect(self.filename)
        self.cursor = self.connection.cursor()
        return self

    def commit(operation):
        def wrapper(self, tablename, fields):
            operation(self, tablename, fields)
            self.connection.commit()
            print(f"{datetime.datetime.now()}: Commit is successful!!")
        return wrapper

    @commit
    def create_table(self, tablename, fields):
        fields = list(fields)
        fields = " text, ".join(fields) +" text"
        drop_command = f"DROP TABLE IF EXISTS {tablename}"
        create_command = f"CREATE TABLE {tablename} ({fields})"
        try:
            self.cursor.execute(drop_command)
            self.cursor.execute(create_command)
        except sql3.Error as er:
            print(f"SQLite error: {' '.join(er.args)}")
        finally:
            print(f"{tablename}: created successfully!")

    def alter_table(self, ):
        pass

    @property
    def show_tables(self):
        command = "SELECT * FROM sqlite_master WHERE type='table';"
        return self.cursor.execute(command)

    def __exit__(self, type, value, traceback):
        print("Connection ended ...")
        self.connection.close()
