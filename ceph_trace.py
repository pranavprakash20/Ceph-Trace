from trace.tracer import Tracer

import docopt
import yaml

# Set doc description
doc = """
This script fetches all the options require for ceph trace
    Usage:
        ceph_trace.py (--conf <conf>)
            [--reporting <reporting>]
            [--end-trace <end-tace>]

        ceph_trace.py --help

    Options:
        -h --help               Shows the command usage.
        -c --conf <str>         ceph trace config file
        -r --reporting <str>    Reporting type [csv | db]
        -e --end-trace          End trace
"""

if __name__ == "__main__":
    # Get args with docopt
    args = docopt.docopt(doc)

    # Get parameters from args
    conf = args.get("--conf").lower()
    # Load conf file
    conf_data = yaml.safe_load(open(conf, "r"))
    end_trace = args.get("--end-trace")
    if end_trace:
        Tracer(conf_data).stop()
    else:
        reporting_type = args.get("--reporting").lower()
        # Run ceph trace
        Tracer(conf_data, reporting_type).start()
