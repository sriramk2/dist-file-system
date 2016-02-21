Python 3.4.3

Distributed File System

Comprises of a client and four servers.

Handles 3 functions:

1. PUT
2. GET
3. LIST

PUT function breaks the file into 4 pieces and stores them in the servers depending on their md5 values. The data is encrypted while using PUT and is decrypted back when using GET.

LIST function lists the files present in the servers.

The program handles subfolders and has traffic optimization as unnecessary data transfer is avoided.

The client and servers match the password and username from dfc.conf and dfs.conf files. The program proceeds only when the username and password matches.

The program is run by specifying the config file alongiwth the function on the command line.