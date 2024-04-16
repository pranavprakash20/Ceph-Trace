from psql import Psql


class BackendStorage:

    def __init__(self, storage_type, conf):
        self.db = None
        if storage_type == "psql":
            self.db = Psql(conf)

    def list_available_backend_storage(self):
        pass
