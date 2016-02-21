import socket
import os
import sys
from _thread import *
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Server 4")
x = open('dfs.conf', 'r')
r = x.read()

e = r.splitlines()[0]
password = e.split()[1]
name = e.split()[0]
if not os.path.exists('DFS4'):
        os.mkdir('DFS4')

b = e.split()[0]
s.bind(('127.0.0.1',10004))
s.listen(20)
conn, addr = s.accept()
pw = conn.recv(9)
# print(pw)
if pw != password.encode('utf8') or str(b) != name:
    print("Invalid username/password")
    sys.exit()
data00 = conn.recv(1024)
req = data00.decode('utf8')
if req == 'LIST':
    
    #file4 = []
    dirs = os.listdir('DFS4/' + str(b) + '/')
    for f4 in dirs:
        print(f4)
        conn.send(bytes(f4,'utf8'))
        conn.recv(1024)

if req == 'LISTS':
    
    #file4 = []
    s = conn.recv(1024)
    sub = s.decode('utf8').split('/')[1]
    dirs = os.listdir('DFS4/' + str(b) + '/' + str(sub) + '/')
    for f4 in dirs:
        print(f4)
        conn.send(bytes(f4,'utf8'))
        conn.recv(1024)


# print(b)
elif req == 'PUT':
    if not os.path.exists('DFS4/' + str(b)):
        os.mkdir('DFS4/' + str(b))
    
    conn.send(bytes(str(1),'utf8'))
    data0 = conn.recv(1024)
    file = data0.decode('utf8')
    conn.send(bytes(str(1),'utf8'))
    data = conn.recv(1024)
    mod = data.decode('utf8')
    if mod == 'm0':
        f = open('DFS4/' + str(b) + '/' + '.' + str(file) + '.4', 'wb')
        f1= open('DFS4/' + str(b) + '/' + '.' + str(file) + '.1', 'wb')
    elif mod == 'm1':
        f = open('DFS4/' + str(b) + '/' + '.' + str(file) + '.3', 'wb')
        f1= open('DFS4/' + str(b) + '/' + '.' + str(file) + '.4', 'wb')
    elif mod == 'm2':
        f = open('DFS4/' + str(b) + '/' + '.' + str(file) + '.2', 'wb')
        f1= open('DFS4/' + str(b) + '/' + '.' + str(file) + '.3', 'wb')
    elif mod == 'm3':
        f = open('DFS4/' + str(b) + '/' + '.' + str(file) + '.1', 'wb')
        f1= open('DFS4/' + str(b) + '/' + '.' + str(file) + '.2', 'wb')
    
    conn.send(bytes(str(1),'utf8'))
    while 1:
        data1 = conn.recv(1024)
        size1 = data1.decode('utf8')
    #     print(size1)
        conn.send(bytes(str(1),'utf8'))
        data2 = conn.recv(1024)
        size2 = data2.decode('utf8')
    #     print(size2)
        conn.send(bytes(str(1),'utf8'))
        for x in range(0, int(size1)):
            data3 = conn.recv(1024)
            f.write(data3)
    #         print(len(data3))
        conn.send(bytes(str(1),'utf8'))
        f.close()
        
        for x in range(0, int(size2)):
            data4 = conn.recv(1024)
            f1.write(data4)
    #         print(len(data4))
        f1.close()
        break
    
    
    
elif req == 'PUTS':
    
    if not os.path.exists('DFS4/' + str(b)):
        os.mkdir('DFS4/' + str(b))
    
    conn.send(bytes(str(1),'utf8'))
    data0 = conn.recv(1024)
    f = data0.decode('utf8')
    sub = f.split('/')[1]
    file = f.split('/')[0]
    if not os.path.exists('DFS4/' + str(b) + '/' + str(sub)):
        os.mkdir('DFS4/' + str(b) + '/' + str(sub))
    conn.send(bytes(str(1),'utf8'))
    data = conn.recv(1024)
    mod = data.decode('utf8')
    if mod == 'm0':
        f = open('DFS4/' + str(b) + '/' + str(sub) + '/' + '.' + str(file) + '.4', 'wb')
        f1= open('DFS4/' + str(b) + '/' + str(sub) + '/' + '.' + str(file) + '.1', 'wb')
    elif mod == 'm1':
        f = open('DFS4/' + str(b) + '/' + str(sub) + '/' + '.' + str(file) + '.3', 'wb')
        f1= open('DFS4/' + str(b) + '/' + str(sub) + '/' + '.' + str(file) + '.4', 'wb')
    elif mod == 'm2':
        f = open('DFS4/' + str(b) + '/' + str(sub) + '/' + '.' + str(file) + '.2', 'wb')
        f1= open('DFS4/' + str(b) + '/' + str(sub) + '/' + '.' + str(file) + '.3', 'wb')
    elif mod == 'm3':
        f = open('DFS4/' + str(b) + '/' + str(sub) + '/' + '.' + str(file) + '.1', 'wb')
        f1= open('DFS4/' + str(b) + '/' + str(sub) + '/' + '.' + str(file) + '.2', 'wb')

    
    
    conn.send(bytes(str(1),'utf8'))
    while 1:
        data1 = conn.recv(1024)
        size1 = data1.decode('utf8')
    #     print(size1)
        conn.send(bytes(str(1),'utf8'))
        data2 = conn.recv(1024)
        size2 = data2.decode('utf8')
    #     print(size2)
        conn.send(bytes(str(1),'utf8'))
        for x in range(0, int(size1)):
            data3 = conn.recv(1024)
            f.write(data3)
    #         print(len(data3))
        conn.send(bytes(str(1),'utf8'))
        f.close()
        
        for x in range(0, int(size2)):
            data4 = conn.recv(1024)
            f1.write(data4)
    #         print(len(data4))
        f1.close()
        break
    
    
    
    
    
    
    
    
elif req == 'GET':
    print("GET")
    file6 = []
    dirs = os.listdir('DFS4/' + str(b) + '/')
    for f1 in dirs:
        print(f1)
        file6.append(f1)
    data7 = conn.recv(1024)
    print(data7.decode('utf8'))
    l = len(file6)
    conn.send(bytes(str(l),'utf8'))
    conn.recv(1024)
    for x in range(0,l):
        conn.send(file6[x].encode('utf8'))
    
    
    try:
        while 1:
            ree = conn.recv(1024)
            if ree == b'1':
                f1 = open('DFS4/' + str(b) + '/.' + data7.decode('utf8') + '.1','rb')
                s1 = os.path.getsize('DFS4/' + str(b) + '/.' + data7.decode('utf8') + '.1')
                print(s1)
                it1 = int((s1/1024)) + 1
                conn.send(bytes(str(it1),'utf8'))
                r1 = f1.read(s1)
                conn.send(r1)
                
                
            #ree = conn.recv(1024)
            if ree == b'2':
                print("p2")
                f2 = open('DFS4/' + str(b) + '/.' + data7.decode('utf8') + '.2','rb')
                s2 = os.path.getsize('DFS4/' + str(b) + '/.' + data7.decode('utf8') + '.2')
                print(s2)
                it2 = int((s2/1024)) + 1
                conn.send(bytes(str(it2),'utf8'))
                r2 = f2.read(s2)
                conn.send(r2)
                
            if ree == b'3':
                print("p3")
                f3 = open('DFS4/' + str(b) + '/.' + data7.decode('utf8') + '.3','rb')
                s3 = os.path.getsize('DFS4/' + str(b) + '/.' + data7.decode('utf8') + '.3')
                print(s3)
                it3 = int((s3/1024)) + 1
                conn.send(bytes(str(it3),'utf8'))
                r3 = f3.read(s3)
                conn.send(r3)
                
            if ree == b'4':
                print("p4")
                f4 = open('DFS4/' + str(b) + '/.' + data7.decode('utf8') + '.4','rb')
                s4 = os.path.getsize('DFS4/' + str(b) + '/.' + data7.decode('utf8') + '.4')
                print(s4)
                it4 = int((s4/1024)) + 1
                conn.send(bytes(str(it4),'utf8'))
                r4 = f4.read(s4)
                conn.send(r4)
                
            if len(ree) == 0:
                break   
    except:
        conn.close()
        print("LOL")
    


elif req == 'GETS':
    print("GETS")
    file6 = []
    dataz = conn.recv(1024)
    print(dataz)
    data77 = dataz.decode('utf8')
    subs = data77.split('/')[1]
    sub = subs.encode('utf8')
    fl = data77.split('/')[0]
    data7 = fl.encode('utf8')
    dirs = os.listdir('DFS4/' + str(b) + '/' + sub.decode('utf8') + '/')
    for f1 in dirs:
        print(f1)
        file6.append(f1)
    
    print(data7.decode('utf8'))
    l = len(file6)
    conn.send(bytes(str(l),'utf8'))
    conn.recv(1024)
    for x in range(0,l):
        conn.send(file6[x].encode('utf8'))
    
    
    try:
        while 1:
            ree = conn.recv(1024)
            if ree == b'1':
                f1 = open('DFS4/' + str(b) + '/' + sub.decode('utf8') + '/.' + data7.decode('utf8') + '.1','rb')
                s1 = os.path.getsize('DFS4/' + str(b) + '/' + sub.decode('utf8') + '/.' + data7.decode('utf8') + '.1')
                print(s1)
                it1 = int((s1/1024)) + 1
                conn.send(bytes(str(it1),'utf8'))
                r1 = f1.read(s1)
                conn.send(r1)
                
                
            #ree = conn.recv(1024)
            if ree == b'2':
                print("p2")
                f2 = open('DFS4/' + str(b) + '/' + sub.decode('utf8') + '/.' + data7.decode('utf8') + '.2','rb')
                s2 = os.path.getsize('DFS4/' + str(b) + '/' + sub.decode('utf8') + '/.' + data7.decode('utf8') + '.2')
                print(s2)
                it2 = int((s2/1024)) + 1
                conn.send(bytes(str(it2),'utf8'))
                r2 = f2.read(s2)
                conn.send(r2)
                
            if ree == b'3':
                print("p3")
                f3 = open('DFS4/' + str(b) + '/' + sub.decode('utf8') + '/.' + data7.decode('utf8') + '.3','rb')
                s3 = os.path.getsize('DFS4/' + str(b) + '/' + sub.decode('utf8') + '/.' + data7.decode('utf8') + '.3')
                print(s3)
                it3 = int((s3/1024)) + 1
                conn.send(bytes(str(it3),'utf8'))
                r3 = f3.read(s3)
                conn.send(r3)
                
            if ree == b'4':
                print("p4")
                f4 = open('DFS4/' + str(b) + '/' + sub.decode('utf8') + '/.' + data7.decode('utf8') + '.4','rb')
                s4 = os.path.getsize('DFS4/' + str(b) + '/' + sub.decode('utf8') + '/.' + data7.decode('utf8') + '.4')
                print(s4)
                it4 = int((s4/1024)) + 1
                conn.send(bytes(str(it4),'utf8'))
                r4 = f4.read(s4)
                conn.send(r4)
                
            if len(ree) == 0:
                break   
    except:
        conn.close()
        print("LOL")
    
    
    