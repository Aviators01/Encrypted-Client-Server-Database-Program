"""
Timothy Queva
CS3130 Lab5
April 4, 2021

This file holds the server functions of rmcommand
"""

import argparse, socket, time,sqlite3,ssl


def parse_command_line(description):
    """Parse command line and return a socket address."""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('host', help='IP or hostname')
    parser.add_argument('-p', metavar='port', type=int, default=1123,
                        help='TCP port (default 1123)')
    parser.add_argument('-a', metavar='cafile', default=None,
                        help='authority: path to CA certificate PEM file')
    parser.add_argument('-s', metavar='certfile', default=None,
                        help='run as server: path to server PEM file')
    args = parser.parse_args()
    address = (args.host, args.p)
    return address

def create_srv_socket(address,certfile, cafile=None):
    purpose = ssl.Purpose.CLIENT_AUTH
    context = ssl.create_default_context(purpose, cafile=cafile)
    context.load_cert_chain(certfile)
    
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind(address)
    listener.listen(64)
    print('Listening at {}'.format(address))
    return listener,context

def setupLogs():
    db = sqlite3.connect('server.lite')
    
    #create table of authorized users
    try:
        db.execute('''create table authorized(
            user char(50) primary key not null,
            password char(20) not null);''')
        db.execute('''insert into authorized(user,password)
            values('tqueva','test'),('fcarlacci','tester');''')
    except:
        pass
    
    #create table to log client requests
    try:
        db.execute('''create table crequests(
            user char(50) primary key not null,
            dtime char(50),
            command char(50);''')
    except:
        pass
    
    #create table of blacklist ip's/port's
    try:
        db.execute('''create table blacklist(
            ip char(15),port int);''')
        db.execute('''insert into blacklist(ip,port)
                   values('127.0.0.1',1060);''')
    except:
        pass
    
    return db

def accept_connections_forever(listener):
    """Forever answer incoming connections on a listening socket."""
    while True:
        raw_sock, address = listener.accept()
        print('Accepted connection from {}'.format(address))
        ssl_sock = listener[1].wrap_socket(raw_sock, server_side=True)
        handle_conversation(ssl_sock, address)

def handle_conversation(sock, address):
    """Converse with a client over `sock` until they are done talking."""
    try:
        handle_request(sock)
    except EOFError:
        print('Client socket to {} has closed'.format(address))
    except Exception as e:
        print('Client {} error: {}'.format(address, e))
    finally:
        sock.close()


def handle_request(sock):
    aphorism = recv_until(sock)
    
    #Check ip address against blacklist
    #Check user against authorized table
    #if validated, log request
    #execute request
    
    #Send confirmation or error
    sock.sendall("Test")

#Receives data until 1024 bytes or client stops (whichever first)
def recv_until(sock):
    data = sock.recv(1024)
    if not data:
        data.decode('utf-8')
        data.strip()
        return data
