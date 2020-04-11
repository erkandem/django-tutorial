"""
establish a connection to preconfigured databases
using an .env file which contains database credentials.
"""
import os
import time
import psycopg2
import dotenv

dotenv.load_dotenv(
    dotenv.find_dotenv(
        raise_error_if_not_found=True
    )
)


class PostgresConfig:
    def __init__(self):
        self.user = os.getenv('POSTGRES_USERNAME') or 'postgres'
        self.pw = os.getenv('POSTGRES_PASSWORD') or 'postgres'
        self.host = os.getenv('POSTGRES_HOST') or 'localhost'
        self.port = os.getenv('POSTGRES_PORT') or 5432
        self.driver = 'psycopg2'
        self.db = 'postgresql'

    def get_uri(self, db_name):
        return f"{self.db}://{self.user}:{self.pw}@{self.host}:{self.port}/{db_name}"


class DbTester:
    def __init__(self):
        self.succeeded = False
        self.attempts = 5
        self.sleep_time = 5
        self.pgc = PostgresConfig()

    def get_print_and_dispose(self, db_name):
        with psycopg2.connect(self.pgc.get_uri_simple(db_name)) as con:
            cursor = con.cursor()
            query = 'SELECT 1;'
            cursor.execute(query)
            data = cursor.fetchall()
            for row in data:
                print(f'{db_name}: {query} {row[0]}')

    def test_loop(self):
        while not self.succeeded and self.attempts > 0:
            try:
                self.get_print_and_dispose('postgres')
                self.succeeded = True
            except psycopg2.OperationalError:
                print('connection failed')
                print(f'sleeping {self.sleep_time} seconds')
                time.sleep(self.sleep_time)
            self.attempts = self.attempts - 1


def main():
    dbt = DbTester()
    dbt.test_loop()


if __name__ == '__main__':
    main()
