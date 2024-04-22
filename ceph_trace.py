import docopt
import yaml
from trace.main_ceph_trace import mainCephTrace

# Set doc description
doc = """
This script fetches all the options require for ceph trace
    Usage:
        ceph_trace.py (--conf <conf>)
            (--reporting <reporting>)

        ceph_trace.py --help

    Options:
        -h --help               Shows the command usage.
        -c --conf <str>         ceph trace config file
        -r --reporting <str>    Reporting type [csv | db]
"""

if __name__ == "__main__":
    # Get args with docopt
    args = docopt.docopt(doc)

    # Get parameters from args
    conf = args.get("--conf").lower()
    # Load conf file
    conf_data = yaml.safe_load(open(conf,'r'))
    reporting_type = args.get("--reporting").lower()

    # Run ceph trace
    mainCephTrace(conf_data,reporting_type).run_ceph_trace()
