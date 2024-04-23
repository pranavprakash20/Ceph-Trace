from ssh.ssh import SSH

class Tracer():
    def __init__(self, conf, reporting_type=None):
       self.conf = conf
       self.reporting_type = reporting_type
       self.ssh_connection = []
    
    def _ssh(self):
        # Estabish ssh connection to all the nodes
        for data in self.conf["nodes"]:
            ip = data["ip"]
            user = data["user"]
            passwd = data["password"]
            try:
                ssh_conn = SSH(ip, user, passwd)
            except Exception as e:
                raise AssertionError(f"Unable to connect to host {ip} {e}")
            self.ssh_connection.append(ssh_conn)
    
    def _upload_trace_script(self, src, dist):
        for node in self.ssh_connection:
            try:
                node.upload(src, dist)
            except Exception as e:
                ip = node.client.get_transport().sock.getpeername()[0]
                raise AssertionError(f"Unable to upload trace script to host {ip} {e}")
    
    def _create_deamon(self,):
        pass

    def reporting(self):
        pass
    
    def start(self):
        # Verify ssh connectione to all nodes
        self._ssh()

        # Add ceph trace tool to nodes
        self._upload_trace_script("scripts/mem_and_cpu_usage.py", "/home/mem_and_cpu_usage.py")

        # Create daemon
        self._create_deamon()

        # start daemon
    
    def stop(self):
        pass

        


        




