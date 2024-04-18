from paramiko.client import SSHClient
from paramiko import AutoAddPolicy


class SSH:
    """
    E.g:
        conn = SSH('ip_addr', 'root', 'pwd<keep empty if passwdless>')
        conn.connect()
        out = conn.exec_command("ls ")
        print(out)
        conn.close()
    """

    def __init__(self, host, username, passwd):
        self.host = host
        self.username = username
        self.passwd = passwd
        self.client = SSHClient()
        self.client.set_missing_host_key_policy(AutoAddPolicy())

    def connect(self):
        self.client.connect(self.host,
                            username=self.username,
                            password=self.passwd)

    def exec_command(self, cmd):
        _stdin, _stdout, _stderr = self.client.exec_command(command=cmd)
        return _stdout.read().decode()

    def close(self):
        self.client.close()

