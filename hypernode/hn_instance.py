"""
#####################
HyperNode Instance
#####################

Run from the command line with the instance index from config.py

Example:

.. code-block:: text

  python3 hn_instance.py -i 0 -v

"""

import argparse
import os
import sys
import time

# custom modules
sys.path.append('../modules')
import com_helpers
import config
from poshn import Poshn
from poschain import SqlitePosChain
import poscrypto
import poshelpers

__version__ = '0.0.53'


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Bismuth Proof of concept PoS HyperNode')
    parser.add_argument("-i", "--index", type=int, default = -1, help='Demo address index [0-4]')
    parser.add_argument("-I", "--ip", type=str, default = '', help="IP to listen on ('ALL' for all interfaces)")
    parser.add_argument("-v", "--verbose", action="count", default=False, help='Be verbose.')
    parser.add_argument("--action", type=str, default=None, help='Specific action. ')
    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit()
    try:
        if args.action == 'genesis':
            # Displays genesis block info for db insert
            poscrypto.load_keys("hn_temp/mn0.json")
            pos_chain = SqlitePosChain(verbose=True)
            # genesis = pos_chain.genesis_dict()
            print("TODO")
        else:
            # If we are updating, let our previous instance close.
            time.sleep(1)
            if args.index >= 0:
                if len(config.POC_HYPER_NODES_LIST) <= 0:
                    poshelpers.load_hn_temp()
                my_info = config.POC_HYPER_NODES_LIST[args.index]
                ip = my_info[1]
                port = my_info[2]
                address = my_info[0]
                wallet_name = "hn_temp/mn{}.json".format(args.index)
                # allows to run several HN on the same machine - debug/dev only
                datadir = "./data{}".format(args.index)
                if not os.path.exists(datadir):
                    os.makedirs(datadir)
                suffix = str(args.index)
            else:
                wallet_name = "poswallet.json"
                datadir = "./data"
                if len(config.POC_HYPER_NODES_LIST) <= 0:
                    config.POC_HYPER_NODES_LIST = config.POC_HYPER_NODES_LIST_0
                my_info = config.POC_HYPER_NODES_LIST[args.index]
                ip = args.ip if args.ip else None
                port = config.DEFAULT_PORT
                suffix=''
            if args.ip == 'ALL':
                ip = None
            peers = config.POC_HYPER_NODES_LIST
            com_helpers.MY_NODE = Poshn(ip, port, peers=peers, verbose = args.verbose,
                                        wallet=wallet_name, datadir=datadir, suffix=suffix, version=__version__)
            com_helpers.MY_NODE.serve()
            # only ctrl-c will stop it
    except Exception as e:
        print(e)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)