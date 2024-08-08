#!/usr/bin/env python3

""" Minimal code example. """

from pyModbusTCP.client import ModbusClient

# read 3 coils at @0 on localhost server
client = ModbusClient(host="localhost", port=5020, auto_open=True)
print("coils=%s" % client.read_coils(0, 3))
