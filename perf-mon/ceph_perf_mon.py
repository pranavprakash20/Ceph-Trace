from datetime import datetime, timezone

from docopt import docopt


doc = """
Utility to get Cluster Stats

    Usage:
        cephci/stats.py --cloud-type <CLOUD>
            [--owner <STR>]
            [--report <STR>]
            [--log-level <LOG>]
            [--log-dir <PATH>]

        cephci/provision.py --help

    Options:
        -h --help               Help
        --report <STR>          Report type [hardware|nfs|performance]
        --owner <STR>           Baremetal node owner
        --config <YAML>         Config file with cloud credentials
        --log-level <LOG>       Log level for log utility Default: DEBUG
        --log-dir <PATH>        Log directory for logs
"""

if __name__ == "__main__":
    # Set configs
    cloud_configs, global_configs = {}, []

    # Set user parameters
    args = docopt(doc)

    # Get user parameters
    report = args.get("--report")

