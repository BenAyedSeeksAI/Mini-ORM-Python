from db_manager import ConnectionSqliteManager
from base import model_list

import argparse

class Migrate:
    def __init__(self, model_list):
        pass

    def migrate(self):
        print("Begin database Migration ...")
        for element in model_list:
            print()
            Elem = element()
            print(f"{Elem.tablename} Migration")
            with ConnectionSqliteManager("example.db") as Connection:
                Connection.create_table(tablename=Elem.tablename , fields=Elem.fields)
            print()

class MigrateCommand:

    def __init__(self):

        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("migrate",type=str,help="Migrate all models in base.py to database")
        self.args = self.parser.parse_args()

    @property
    def get_args(self):
        return self.args

    def migrate(self):
        if self.get_args.migrate =="migrate":
            mig = Migrate(model_list)
            mig.migrate()
        elif self.get_args.migrate == "show-what-to-migrate":
            print(model_list)





Command = MigrateCommand()
Command.migrate()
