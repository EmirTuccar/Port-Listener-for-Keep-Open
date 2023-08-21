# Port-Listener-for-Keep-Open
This is a program for port listening which will help to keep open specific ports.

I write this program for listen port and ip for keep open port.
When we try to nmap scan our ports sometimes they might be closed because no one listen that port. This program solves that issue and listen forever until you cancel.
Porgram shows that the connections of that port. Foer example when you start the program and after that you want to access that port from another computer, program shows informations of that computer which is trying to connect our port.

!!!Problems!!!
When you tried to scan with scanner program (nmap, netstat) listener program connection resets from peer. 

