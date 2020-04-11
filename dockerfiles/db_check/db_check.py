"""
establish a connection to preconfigured databases
using an .env file which contains database credentials.
"""
import os
import time
import psycopg2
import psycopg2.extras


class PostgresConfig:
    def __init__(self):
        self.user = os.getenv('POSTGRES_USERNAME') or 'postgres'
        self.pw = os.getenv('POSTGRES_PASSWORD') or 'postgres'
        self.host = os.getenv('POSTGRES_HOST') or 'localhost'
        self.port = os.getenv('POSTGRES_PORT') or 5432
        self.driver = 'psycopg2'
        self.db = 'postgresql'

    def get_uri(self, db_name):
        return f"{self.db}+{self.driver}://{self.user}:{self.pw}@{self.host}:{self.port}/{db_name}"

    def get_uri_simple(self, db_name):
        return f"{self.db}://{self.user}:{self.pw}@{self.host}:{self.port}/{db_name}"


class DbTester:
    def __init__(self):
        self.pgc = PostgresConfig()

    def get_print_and_dispose(self, db_name):
        with psycopg2.connect(self.pgc.get_uri_simple(db_name)) as con:
            cursor = con.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            query = 'SELECT 1 as result;'
            cursor.execute(query)
            data = cursor.fetchall()
        for row in data:
            print(f'{db_name}: {query} {row["result"]}')
        con.close()


def main():
    print('waiting 6 seconds')
    time.sleep(6)
    dbt = DbTester()
    dbt.get_print_and_dispose('postgres')


if __name__ == '__main__':
    main()
