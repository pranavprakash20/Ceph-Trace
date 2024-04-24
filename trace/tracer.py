from daemon.daemon import Daemon
from ssh.ssh import SSH


class Tracer:
    def __init__(self, conf, reporting_type=None):
        self.conf = conf
        self.reporting_type = reporting_type
        self.ssh_connection = {}
        self.trace_script_path = "scripts/mem_and_cpu_usage.py"
        self.trace_dst_path = "/home"
        self.trace_dst_file_name = "mem_and_cpu_usage.py"

    def start(self):
        # Verify ssh connectione to all nodes
        self._ssh()
        #
        # Add ceph trace tool to nodes
        self._upload_trace_script()

        # Create daemon
        self._create_deamon()

        # start daemon
        # self._start_daemon()

    def stop(self):
        # Verify ssh connectione to all nodes
        self._ssh()

        # Stop the daemons
        self._stop_daemon()

    def _ssh(self):
        # Estabish ssh connection to all the nodes
        for data in self.conf["nodes"]:
            ip = data["ip"]
            user = data["user"]
            passwd = data["password"]
            try:
                print(f"Establishing conection to {ip} as {user} user")
                ssh_conn = SSH(ip, user, passwd)
                print("Connection successful.")
            except Exception as e:
                raise AssertionError(f"Unable to connect to host {ip} {e}")
            self.ssh_connection[ip] = ssh_conn

    def _upload_trace_script(self):
        for ip, node in self.ssh_connection.items():
            try:
                print(f"Uploading trace script to {ip}")
                node.upload(
                    self.trace_script_path,
                    f"{self.trace_dst_path}/{self.trace_dst_file_name}",
                )
                print("Trace script upload successful")
            except Exception as e:
                raise AssertionError(f"Unable to upload trace script to host {ip} {e}")

    def _create_deamon(self):
        daemon = Daemon()
        with open("daemon/daemon-service.template", "r") as f:
            service_content_template = f.read()
        service_content = service_content_template.format(
            script_directory=f"{self.trace_dst_path}",
            script_run_cmd=f"{self.trace_dst_file_name}",
        )
        for node in self.conf["nodes"]:
            node = self.ssh_connection[node["ip"]]
            daemon.create(service_content, node)
            print(f"Daemon created successfully. Daemon name : {daemon.name}")

    def _start_daemon(self):
        daemon = Daemon()
        for node in self.conf["nodes"]:
            node = self.ssh_connection[node["ip"]]
            daemon.start(node)

    def _stop_daemon(self):
        daemon = Daemon()
        for node in self.conf["nodes"]:
            node = self.ssh_connection[node["ip"]]
            daemon.stop(node)
