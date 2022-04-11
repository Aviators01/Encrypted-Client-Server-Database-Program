"""
Timothy Queva
CS3130 Lab5
April 4, 2021

This program spawns threads which accept connections, verify the user
using sqlite3 databases, log requests, deny commands/close connection
if user ip address blacklisted, and then execute the user's command.
A code is sent back to client to indicate success/failure of command.
"""

import servefunct
from threading import Thread

def start_threads(listener, workers=4):
    t = (listener,)
    for i in range(workers):
        Thread(target=servefunct.accept_connections_forever, args=t).start()

if __name__ == '__main__':
    address = servefunct.parse_command_line('This multi-threaded server '+
                                            'allows running of programs'+
                                            'remotely.')
    listener = servefunct.create_srv_socket(address)
    db = servefunct.setupLogs()
    start_threads(listener)