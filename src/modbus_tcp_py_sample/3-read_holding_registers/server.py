#!/usr/bin/env python3

"""
Modbus/TCP server
~~~~~~~~~~~~~~~~~

Run this as root to listen on TCP privileged ports (<= 1024).

Add "--host 0.0.0.0" to listen on all available IPv4 addresses of the host.
$ sudo ./server.py --host 0.0.0.0
"""

import argparse
import logging
from pyModbusTCP.server import ModbusServer, DataBank
from random import uniform
from time import sleep

# init logging
logging.basicConfig()
# parse args
parser = argparse.ArgumentParser()
parser.add_argument(
    "-H", "--host", type=str, default="localhost", help="Host (default: localhost)"
)
parser.add_argument(
    "-p", "--port", type=int, default=5020, help="TCP port (default: 502)"
)
parser.add_argument("-d", "--debug", action="store_true", help="set debug mode")
args = parser.parse_args()
# logging setup
if args.debug:
    logging.getLogger("pyModbusTCP.server").setLevel(logging.DEBUG)


# start modbus server
server = ModbusServer(host=args.host, port=args.port, no_block=True)

try:
    print("Start server...")
    server.start()
    print("Server is online")
    state = [0]
    while True:
        # set 10 holding registers values at @0
        server.data_bank.set_holding_registers(
            0, [int(uniform(0, 1000)) for _ in range(10)]
        )
        sleep(0.5)

except:
    print("Shutdown server ...")
    server.stop()
    print("Server is offline")

server.start()
