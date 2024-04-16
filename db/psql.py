import psycopg


class Psql:

    def __init__(self, conf):
        self.db_name = conf["db_name"]
        self.db_user = conf["db_user"]
        self.db_pwd = conf["db_pwd"]
        self.db_host = conf["db_host"]
        self.db_port = conf["db_port"]
        self.db_conn = self._establish_db_conn()

    def _establish_db_conn(self):
        return psycopg.connect(
            dbname=self.db_name,
            user=self.db_user,
            password=self.db_pwd,
            host=self.db_host,
            port=self.db_port,
        )
        self.db_conn.autocommit = True

    def close(self):
        self.db_conn.close()

    def insert(self, table, cols, data):
        insert_query = f"""INSERT INTO {table} ({cols}) VALUES ({data})"""
        self._execute(insert_query)

    def update(self, table, cols, data):
        pass

    def delete(self, table, value):
        pass

    def _execute(self, cmd):
        self.db_conn.cursor().execute(cmd)
        self.db_conn.commit()
