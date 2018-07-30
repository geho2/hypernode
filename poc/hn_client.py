"""
****************
HyperNode Client
****************

Run from the command line with the instance index from common .py

Example:

.. code-block:: text

  python3 hn_client.py -i 0 --action status

Basic Command line arguments
============================

Prefer long params to short ones to avoid lower/upper case mismatch.

``-V`` , ``--version`` (optional, default=False)
------------------------------------------------
Report client version, does not connect.


``-i`` , ``--index`` (optional, default=0)
------------------------------------------
Instance index to connect to.

``-I`` , ``--ip`` (optional, default=127.0.0.1)
-----------------------------------------------
Hypernode Host to connect to.

``-p`` , ``--port`` (optional, default=6969)
--------------------------------------------
Hypernode port to connect to.

``-v`` , ``--verbose`` (optional, default=False)
------------------------------------------------
Be verbose.

Commands
========

Commands are issued via ``--action`` and ``--param`` command line switches.

``--param`` is an optional input parameter to the action command

``--action=hello``
------------------

``--action=ping``
-----------------

``--action=status``
-------------------
Returns full Hypernode status as a Json string,
as well as client version in a dedicated "client" section.

Sample output:

``{"config": {"address": "BLYkQwGZmwjsh7DY6HmuNBpTbqoRqX14ne", "ip": "127.0.0.1", "port": 6969, "verbose": 1},
"instance": {"version": "0.0.51", "hn_version": "0.0.75", "statustime": 1532851042, "localtime": 1532851046.703249},
"chain": {"block_height": 3631, "Genesis": "BLYkQwGZmwjsh7DY6HmuNBpTbqoRqX14ne", "height": 3631, "round": 6420, "sir": 1, "block_hash": "a7a4b32406584b54bd30bacbe0457583a2d84492", "uniques": 4, "uniques_round": 0, "forgers": 4, "forgers_round": 2},
"mempool": {"NB": 0, "SENDERS": 0, "RECIPIENTS": 0},
"peers": {"connected_count": 1, "outbound": ["127.0.0.1:06971"], "inbound": ["127.0.0.1:06971"],
"net_height": {"height": 3631, "round": 6420, "sir": 1, "block_hash": "a7a4b32406584b54bd30bacbe0457583a2d84492", "uniques": 0, "uniques_round": 0, "forgers": 4, "forgers_round": 2, "count": 1, "peers": ["127.0.0.1:06971"]}},
"state": {"state": "START", "round": 8693, "sir": 1, "forger": "BHbbLpbTAVKrJ1XDLMM48Qa6xJuCGofCuH"},
"client": {"version": "0.0.51", "lib_version": "0.0.33", "localtime": 1532851046.7035139}}``

``--action=block --param=block_height``
---------------------------------------
Returns block info and list of transactions for given height

.. code-block:: text

  python3 hn_client.py --action=block --param=53

Sample output:

``{"txs": [["8bdc804328d9e8ac0...53a53f0dffe1f", 53, 1528381933,
"BLYkQwGZmwjsh7DY6HmuNBpTbqoRqX14ne", "BHbbLpbTAVKrJ1XDLMM48Qa6xJuCGofCuH",
0, "", 1, "2275e088ef7dde5972...72e7da47b2967", 1532772325]], "height": 53,
"round": 4969, "sir": 1, "timestamp": 1528382103,
"previous_hash": "7b12101dcb088170285b5d5cad68e7e79e4cb6b4", "msg_count": 1,
"unique_sources": 0, "signature": "d0feb58827e614f76...74f84282c39f87",
"block_hash": "ae27f98d0fc513778ce78c22287214bbbe702db3", "received_by": "",
"forger": "BMSMNNzB9qdDp1vudRZoge4BUZ1gCUC3CV"}``


``--action=address_txs --param=block_height``
---------------------------------------------
Returns list of transactions both issued AND received by the given address.
Param is the address, and an optional extra param after a comma
`--param=address,extra`

extra can be

  - omitted: will send back 100 latest tx
  - a block height: will send back at most 100 tx from the given height
  - a transaction signature: will send back at most 100 tx following the signature (to be detailed, do not use yet)

.. code-block:: text

  python3 hn_client.py --action=address_txs --param=BLYkQwGZmwjsh7DY6HmuNBpTbqoRqX14ne

.. code-block:: text

  python3 hn_client.py --action=address_txs --param=BLYkQwGZmwjsh7DY6HmuNBpTbqoRqX14ne,2

.. code-block:: text

  python3 hn_client.py --action=address_txs --param=BLYkQwGZmwjsh7DY6HmuNBpTbqoRqX14ne,34371d12bb699e97...67987b1589c0522

Sample output:

``[["8bdc804328d9e8ac097fb2b2f...053a53f0dffe1f", 53, 1528381933, "BLYkQwGZmwjsh7DY6HmuNBpTbqoRqX14ne", "BHbbLpbTAVKrJ1XDLMM48Qa6xJuCGofCuH",
0, "", 1, "2275e088ef7dde5972...dc72e7da47b2967", 1532850901],
["34371d12bb6c249e899e97...ca74987b1589c0522", 54, 1528382155, "BLYkQwGZmwjsh7DY6HmuNBpTbqoRqX14ne", "BHbbLpbTAVKrJ1XDLMM48Qa6xJuCGofCuH",
0, "", 1, "2275e088ef7dde5972...dc72e7da47b2967", 1532850901]]``

``--action=tx --param=tx_signature``
---------------------------------------
Returns full detail of transaction matching the signature.
(the signature is the transaction id)
Returns `false` if the signature was not found.

.. code-block:: text

  python3 hn_client.py --action=tx --param=8bdc804328d9e8ac097fb2b2f53ca5902e28f21423f1db87f4ab39a970176c6d4bb33e24b75200438a49f8308e4f6addf471b6e6591c091da5053a53f0dffe1f

Sample output:

``[["8bdc804328d9...da5053a53f0dffe1f", 53, 1528381933, "BLYkQwGZmwjsh7DY6HmuNBpTbqoRqX14ne", "BHbbLpbTAVKrJ1XDLMM48Qa6xJuCGofCuH", 0, "", 1, "2275e088ef7dde597279cde...7da47b2967", 1532854630]]``

*FR:* add ,dict to get as a dict() and not a list() , or convert to dict client side
*FR:* also returns details of the block it's in

``--action=address``
--------------------
TODO - Info and stats about a PoS address


``--action=mempool``
--------------------
Returns current mempool content as json.


``--action=headers``
--------------------
Returns the latest `common.BLOCK_SYNC_COUNT` block headers (block info, without tx info).
'tx' key will be there but always an empty list.
`--param` is an optional string and can be:

- start,count : count headers from start, ex `--param=50,2` will send headers 50 and 51
- ,count : return the latest "count" headers ex: `--param=,10` will send latest 10 headers

Sample output:

``[{"txs": [], "previous_hash": "7b12101dcb088170285b5d5cad68e7e79e4cb6b4", "signature": "d0feb58827e614f768e97fe9e9981e4bdf91be9251066a6a0938aa8e26fd66c5aad410da2304b022a5b8e0f2672da2a28b6856727d17e8868074f84282c39f87", "block_hash": "ae27f98d0fc513778ce78c22287214bbbe702db3"},
{"txs": [], "previous_hash": "ae27f98d0fc513778ce78c22287214bbbe702db3", "signature": "a9254987127c1cc8313218a97ff700193ccd16af6b535d1f143f0ecc78dc1148c7c23a8ad549c93ebfdbfbb2f8c579619ee3d65961b98cf00afce4891afe9f57", "block_hash": "28b828f717e4d04cad8c1b48f5d4b61a85203415"}]``


``--action=txtest``
-------------------
Emits a test transaction.


``--action=blocksync --param=block_height``
-------------------------------------------
Returns the latest `common.BLOCK_SYNC_COUNT` full blocks starting from block_height as a json list of dict.




"""

import sys
import argparse
import time
import asyncio

# custom modules
sys.path.append('../modules')
# import common
import posclient
import com_helpers


__version__ = '0.0.52'

DESC = 'Bismuth Hypernode client'


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=DESC)
    parser.add_argument("-i", "--index", type=int, default = 0, help='Demo address index [0-4]')
    parser.add_argument("-I", "--ip", type=str, default = '127.0.0.1', help='HN Host to connect to (127.0.0.1)')
    parser.add_argument("-p", "--port", type=str, default = 6969, help='HN port (6969)')
    parser.add_argument("-v", "--verbose", action="count", default=False, help='Be verbose.')

    parser.add_argument("-V", "--version", action="count", default=False, help='Show version')

    parser.add_argument("--action", type=str, default=None,
                        help='Specific action. hello, ping, status, block, tx, address_txs, mempool, blocksync, '
                             'headers, txtest.')
    parser.add_argument("--param", type=str, default=None, help='Input param from block and tx command.')
    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit()
    if args.version:
        print(DESC)
        print("Client version {}".format(__version__))
        print("Client Lib version {}".format(posclient.__version__))
        sys.exit()
    if args.verbose:
        print("Client version {}".format(__version__))
        print("Client Lib version {}".format(posclient.__version__))
    try:
        com_helpers.MY_NODE = posclient.Posclient(args.ip, args.port, wallet="mn_temp/mn{}.json".format(args.index),
                                                  verbose=args.verbose, version=__version__)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(com_helpers.MY_NODE.action(args.action, args.param))

    except Exception as e:
        print(e)
