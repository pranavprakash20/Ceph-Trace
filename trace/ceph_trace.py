from datetime import datetime, timezone
import os
import sys
sys.path.insert(1, os.getcwd())
from ssh.ssh import SSH
from docopt import docopt


doc = """
Utility to get Cluster Stats

    Usage:
        trace/ceph_trace.py 

    Options:
        -h --help               Help
"""

if __name__ == "__main__":

    # Set user parameters
    args = docopt(doc)





