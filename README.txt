Timothy Queva
CS3130 Lab5
April 4, 2021

(PROGRAM NOT COMPLETED. SSL needs work)

Description: This program is a client-server program that allows a client to run
program remotely.

Limitations:
1. Only works over the local area network due to NAT (Network Address Translation) preventing
communication beyond a subnet.

Security issues:
1. communication is unencrypted.
2. Database not secured.
3. Message payload not secured against harmful commands

Instructions:
	1. Navigate to the correct folder:
	2. Start the server by typing: python3 rmcommand.py 127.0.0.1 -
	3. (In a different window) start client by typing: python3 rmclient.py 127.0.0.1

Additional tips:
-for help, type: python3 cs_chat.py -h
-127.0.0.1 is just the loopback address. It can be replaced with any valid-according-to-subnet-rules ip address
-To stop the client, one can just type: exit
-to stop the server, press ctrl + c
