# Class that handles the creation of perf-mon daemon

class Daemon:

    def __init(self, name):
        self.name = name

    def create(self, service_content, node):
        """
        Creates the daemon
        """
        path = r"/etc/systemd/system"
        _file = f"{path}/{self.name}.service"
        cmd = f'echo "{service_content}" >> {_file}'
        node.exec_command(cmd)

    def start(self, node):
        """
        Starts the daemon
        """
        cmd = f"systemctl start {self.name}"
        node.exec_command(cmd)

    def status(self, node):
        """
        Returns status of the daemon
        """
        cmd = f"systemctl status {self.name}"
        node.exec_command(cmd)

    def stop(self, node):
        """
        Stops the daemon
        """
        cmd = f"systemctl stop {self.name}"
        node.exec_command(cmd)
