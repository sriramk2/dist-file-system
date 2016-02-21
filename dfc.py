import socket
import sys
import os
import hashlib
# import crypto.cipher
zz = sys.argv[1]

x = open(zz, 'r')
r = x.read()
a = r.splitlines()[0]
b = r.splitlines()[1]
c = r.splitlines()[2]
d = r.splitlines()[3]
g = r.splitlines()[4]
e = r.splitlines()[5]
password = e.split()[1]
username = g.split()[1]
#print(username.encode('utf8'))

p1 = a.split()[2]
port1 = p1.split(':')[1]
host1 = p1.split(':')[0]
p2 = b.split()[2]
port2 = p2.split(':')[1]
host2 = p1.split(':')[0]
p3 = c.split()[2]
port3 = p3.split(':')[1]
host3 = p1.split(':')[0]
p4 = d.split()[2]
port4 = p4.split(':')[1]
host4 = p1.split(':')[0]
try:
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s1.connect((host1, int(port1)))
    s1.send(password.encode('utf8'))
except:
    print("Server 1 down")
try:
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.connect((host2, int(port2)))
    s2.send(password.encode('utf8'))
except:
    print("Server 2 down")
try:
    s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s3.connect((host3, int(port3)))
    s3.send(password.encode('utf8'))
except:
    print("Server 3 down")
try:
    s4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s4.connect((host4, int(port4)))
    s4.send(password.encode('utf8'))
except:
    print("Server 4 down")
file1 = []
file2 = []
file3 = []
file4 = []
if sys.argv[2] == 'LIST':
    #print("yes")
    server1 = 1
    server2 = 1
    server3 = 1
    server4 = 1
    
    if len(sys.argv) == 3:
        l = 'LIST'
    elif len(sys.argv) == 4:    
        l = 'LISTS'
    try:
        s1.send(bytes(l,'utf8'))
    except:
        server1 = 0    
    try:
        s2.send(bytes(l,'utf8'))
    except:
        server2 = 0
    try:        
        s3.send(bytes(l,'utf8'))
    except:
        server3 = 0    
    try:    
        s4.send(bytes(l,'utf8'))
    except:
        server4 = 0
    try:
        if l == 'LISTS':
                s1.send(bytes(sys.argv[3],'utf8'))
        while 1:
            
            data1 = s1.recv(1024).decode('utf8')
#             print("HMMM")
            file1.append(data1)
#             print(data1)
            s1.send(bytes(str(1),'utf8'))
            if len(data1) == 0:
                break
#         print(file1)
#         print("WTF")
        f11 = []
        f111 = []
        for x in range(0,len(file1) - 1):
            #print(file1[x])
            fl1 = file1[x].split('.')[1]
            fl1_1 = file1[x].split('.')[2]
            co1 = str(fl1) + '.' + str(fl1_1)
    #         fl11 = fl1.split('.')[0]
    #         print(fl1)
            f11.append(co1)
            f111.append(file1[x])
#             print(f11)
    except:
        pass
#     print(f11)
#     print(f111)
    try:
        if l == 'LISTS':
                s2.send(bytes(sys.argv[3],'utf8'))
        while 1:
            
            data2 = s2.recv(1024).decode('utf8')
            file2.append(data2)
            s2.send(bytes(str(1),'utf8'))
            if len(data2) == 0:
                break
        #print(file2)
        f22 = []
        f222 = []
        for x in range(0,len(file2) - 1):
            #print(file2[x])
            fl2 = file2[x].split('.')[1]
            fl2_1 = file2[x].split('.')[2]
            co2 = str(fl2) + '.' + str(fl2_1)
    #         print(fl2)
            #fl22 = fl2.split('.')[0]
            f222.append(file2[x])
            f22.append(co2)
#         print(f22)
    except:
        pass
#     print(f22)
#     print(f222)
    try:
        if l == 'LISTS':
                s3.send(bytes(sys.argv[3],'utf8'))
        while 1:
            
            data3 = s3.recv(1024).decode('utf8')
            file3.append(data3)
            s3.send(bytes(str(1),'utf8'))
            if len(data3) == 0:
                break
        #print(file3)
        f33 = []
        f333 = []
        for x in range(0,len(file3) - 1):
            #print(file3[x])
            fl3 = file3[x].split('.')[1]
            fl3_1 = file3[x].split('.')[2]
            co3 = str(fl3) + '.' + str(fl3_1)
            #print(fl3)
            #fl33 = fl3.split('.')[0]
            f33.append(co3)
            f333.append(file3[x])
    except:
        pass
#     print(f33)
#     print(f333)
    try:
        if l == 'LISTS':
                s4.send(bytes(sys.argv[3],'utf8'))
        while 1:
            
            data4 = s4.recv(1024).decode('utf8')
            file4.append(data4)
            s4.send(bytes(str(1),'utf8'))
            if len(data4) == 0:
                break
        #print(file4)
        f44 = []
        f444 = []
        for x in range(0,len(file4) - 1):
            #print(file4[x])
            fl4 = file4[x].split('.')[1]
            fl4_1 = file4[x].split('.')[2]
            co4 = str(fl4) + '.' + str(fl4_1)
            #fl44 = fl4.split('.')[0]
            #print(fl4)
            f44.append(co4)
            f444.append(file4[x])
    except:
        pass
#     print(f44)
#     print(f444)
    main_list = []
    #for x in range(0,len(f44) - 1):
        
    a = 0
    b = 1
    
    
    if server1 == 0:
        main_list = f22 + f33 + f44
        
        if server2 == 0:
            main_list = f33 + f44
            
            if server3 == 0:
                main_list = f44
                
                if server4 == 0:
                    print("No data")
                
    if server2 == 0:
        main_list = f11 + f33 + f44
        
        if server1 == 0:
            main_list = f33 + f44
            
            if server3 == 0:
                main_list = f44
                if server4 == 0:
                    print("No data")
                
    if server3 == 0:
        main_list = f22 + f11 + f44
        
        if server2 == 0:
            main_list = f11 + f44
            
            if server1 == 0:
                main_list = f44
                if server4 == 0:
                    print("No data")
    
    if server4 == 0:
        main_list = f22 + f11 + f33
        
        if server2 == 0:
            main_list = f11 + f33
            
            if server1 == 0:
                main_list = f33
                if server3 == 0:
                    print("No data")
                    
    if server1 != 0 and server2 != 0 and server3 != 0 and server4 != 0:
        main_list = f11 + f22 + f33 + f44
                    
#     print("DAMN")
    
    try:
        while 1:
        
            if main_list.count(main_list[0]) >=  6 :
                print(main_list[0])
                main_list = [x for x in main_list if x != main_list[0]]
            elif main_list.count(main_list[0]) <  6 :
                print(main_list[0] + " [Incomplete]")
                main_list = [x for x in main_list if x != main_list[0]]
            elif len(main_list) == 0:
                break
    except:
        pass
elif sys.argv[2] == 'PUT':
    print("yesssssss")
    if len(sys.argv) == 4:
        p = 'PUT'
        z = str(sys.argv[3])
        f1 = open(z,'rb')
    elif len(sys.argv) == 5:
        p = 'PUTS'
        z = str(sys.argv[3]) + str(sys.argv[4]) 
        f1 = open(str(sys.argv[3]),'rb')
    print(z)
    r11 = f1.read()
    hash1 = hashlib.sha256()
    hash1.update(r11)
    md5 = int(hash1.hexdigest(),16)
    # print(md5)
    print(len(r11))
    fsize = len(r11)
    if fsize % 4 == 2:
        print("2")
        sz1 = int(((fsize - 2)/4) + 1)
        sz2 = int(((fsize - 2)/4) + 1)
        sz3 = int((fsize - 2)/4)
        sz4 = int((fsize - 2)/4)
    elif fsize % 4 == 3:
        print("3")
        sz1 = int(((fsize - 3)/4) + 1)
        sz2 = int(((fsize - 3)/4) + 1)
        sz3 = int(((fsize - 3)/4) + 1)
        sz4 = int((fsize - 3)/4)
    elif fsize % 4 == 1:
        print("1")
        sz1 = int(((fsize - 1)/4) + 1)
        sz2 = int((fsize - 1)/4)
        sz3 = int((fsize - 1)/4)
        sz4 = int((fsize - 1)/4)
    elif fsize % 4 == 0:
        print("0")
        sz1 = int((fsize)/4)
        sz2 = int((fsize)/4)
        sz3 = int((fsize)/4)
        sz4 = int((fsize)/4)
    i11 = sz1/1024
    i22 = sz2/1024
    i33 = sz3/1024
    i44 = sz4/1024
    if sz1 % 1024 == 0:
        i1 = int(i11)
        
    else:
        i1 = int(i11) + 1
    if sz2 % 1024 == 0:
        i2 = int(i22)
    else:
        i2 = int(i22) + 1
    if sz3 % 1024 == 0:
        i3 = int(i33)
    else:
        i3 = int(i33) + 1
    if sz1 % 1024 == 0:
        i4 = int(i44)
    else:
        i4 = int(i44) + 1
#     print(sz1)
#     print(sz2)
#     print(sz3)
#     print(sz4)
    f2 = open(str(sys.argv[3]),'rb')
    
    rp11 = f2.read(sz1)
    rp1111 = hashlib.sha256()
    rp1111.update(username.encode('utf8'))
    rp111 = rp1111.hexdigest()
    rp1 = b''.join([rp11,rp111.encode('utf8')])
    print(len(rp1))
    rp22 = f2.read(sz2)
    rp2222 = hashlib.sha256()
    rp2222.update(username.encode('utf8'))
    rp222 = rp2222.hexdigest()
    rp2 = b''.join([rp22,rp222.encode('utf8')])
    print(len(rp2))
    rp33 = f2.read(sz3)
    rp3333 = hashlib.sha256()
    rp3333.update(username.encode('utf8'))
    rp333 = rp3333.hexdigest()
    rp3 = b''.join([rp33,rp333.encode('utf8')])
    print(len(rp3))
    rp44 = f2.read(sz4)
    rp4444 = hashlib.sha256()
    rp4444.update(username.encode('utf8'))
    rp444 = rp4444.hexdigest()
    rp4 = b''.join([rp44,rp444.encode('utf8')])
    print(len(rp4))
    # MATTER IS HERE !!!!!
    
    o1 = sz1 / 1024
    if sz1 % 1024 == 0:
        it1 = int(o1)
    else:
        it1 = int(o1) + 1
    print(it1)
    
    o2 = sz2 / 1024
    if sz2 % 1024 == 0:
        it2 = int(o2)
    else:
        it2 = int(o2) + 1
    print(it2)
    
    o3 = sz3 / 1024
    if sz3 % 1024 == 0:
        it3 = int(o3)
    else:
        it3 = int(o3) + 1
    print(it3)
    
    o4 = sz4 / 1024
    if sz4 % 1024 == 0:
        it4 = int(o4)
    else:
        it4 = int(o4) + 1
    print(it4)
    
    if md5 % 4 == 0:
        m = 'm0'
        print("m0")
        #try:
        s1.settimeout(1)
        s1.send(bytes(p,'utf8'))
        s1.recv(1024)
        s1.send(z.encode('utf8'))
        s1.recv(1024)
        s1.send(bytes(m,'utf8'))
        s1.recv(1024)
        s1.send(bytes(str(it1),'utf8'))
        s1.recv(1024)
        s1.send(bytes(str(it2),'utf8'))
        s1.recv(1024)
        s1.send(rp1)
        s1.recv(1024)
        s1.send(rp2)
#         except:
#             print("Server 1 timed out")
        try:
            s2.settimeout(1)
            s2.send(bytes(p,'utf8'))
            s2.recv(1024)
            s2.send(z.encode('utf8'))
            s2.recv(1024)
            s2.send(bytes(m,'utf8'))
            s2.recv(1024)
            s2.send(bytes(str(it2),'utf8'))
            s2.recv(1024)
            s2.send(bytes(str(it3),'utf8'))
            s2.recv(1024)
            s2.send(rp2)
            s2.recv(1024)
            s2.send(rp3)
        except:
            print("Server 2 timed out")
        try:
            s3.settimeout(1)    
            s3.send(bytes(p,'utf8'))
            s3.recv(1024)
            s3.send(z.encode('utf8'))
            s3.recv(1024)
            s3.send(bytes(m,'utf8'))
            s3.recv(1024)
            s3.send(bytes(str(it3),'utf8'))
            s3.recv(1024)
            s3.send(bytes(str(it4),'utf8'))
            s3.recv(1024)
            s3.send(rp3)
            s3.recv(1024)
            s3.send(rp4)
        except:
            print("Server 3 timed out")
        try:
            s4.settimeout(1)
            s4.send(bytes(p,'utf8'))
            s4.recv(1024)
            s4.send(z.encode('utf8'))
            s4.recv(1024)
            s4.send(bytes(m,'utf8'))
            s4.recv(1024)
            s4.send(bytes(str(it4),'utf8'))
            s4.recv(1024)
            s4.send(bytes(str(it1),'utf8'))
            s4.recv(1024)
            s4.send(rp4)
            s4.recv(1024)
            s4.send(rp1)
        except:
            print("Server 4 timed out")
    elif md5 % 4 == 1:
        m = 'm1'
        print(m)
        try:
            s1.settimeout(1)
            s1.send(bytes(p,'utf8'))
            s1.recv(1024)
            s1.send(bytes(z,'utf8'))
            s1.recv(1024)
            s1.send(bytes(m,'utf8'))
            s1.recv(1024)
            s1.send(bytes(str(it4),'utf8'))
            s1.recv(1024)
            s1.send(bytes(str(it1),'utf8'))
            s1.recv(1024)
            s1.send(rp4)
            s1.recv(1024)
            s1.send(rp1)
        except:
            print("Server 1 timed out")
        try:
            s2.settimeout(1)
            s2.send(bytes(p,'utf8'))
            s2.recv(1024)
            s2.send(bytes(z,'utf8'))
            s2.recv(1024)
            s2.send(bytes(m,'utf8'))
            s2.recv(1024)
            s2.send(bytes(str(it1),'utf8'))
            s2.recv(1024)
            s2.send(bytes(str(it2),'utf8'))
            s2.recv(1024)
            s2.send(rp1)
            s2.recv(1024)
            s2.send(rp2)
        except:
            print("Server 2 timed out")
        try:
            s3.settimeout(1)
            s3.send(bytes(p,'utf8'))
            s3.recv(1024)
            s3.send(bytes(z,'utf8'))
            s3.recv(1024)
            s3.send(bytes(m,'utf8'))
            s3.recv(1024)
            s3.send(bytes(str(it2),'utf8'))
            s3.recv(1024)
            s3.send(bytes(str(it3),'utf8'))
            s3.recv(1024)
            s3.send(rp2)
            s3.recv(1024)
            s3.send(rp3)
        except:
            print("Server 3 timed out")
        try:
            s4.settimeout(1)
            s4.send(bytes(p,'utf8'))
            s4.recv(1024)
            s4.send(bytes(z,'utf8'))
            s4.recv(1024)
            s4.send(bytes(m,'utf8'))
            s4.recv(1024)
            s4.send(bytes(str(it3),'utf8'))
            s4.recv(1024)
            s4.send(bytes(str(it4),'utf8'))
            s4.recv(1024)
            s4.send(rp3)
            s4.recv(1024)
            s4.send(rp4)
        except:
            print("Server 4 timed out")
    elif md5 % 4 == 2:
        m = 'm2'
        print(m)
        try:
            s1.settimeout(1)
            s1.send(bytes(p,'utf8'))
            s1.recv(1024)
            s1.send(bytes(z,'utf8'))
            s1.recv(1024)
            s1.send(bytes(m,'utf8'))
            s1.recv(1024)
            s1.send(bytes(str(it3),'utf8'))
            s1.recv(1024)
            s1.send(bytes(str(it4),'utf8'))
            s1.recv(1024)
            s1.send(rp3)
            s1.recv(1024)
            s1.send(rp4)
        except:
            print("Server 1 timed out")
        try:
            s2.settimeout(1)
            s2.send(bytes(p,'utf8'))
            s2.recv(1024)
            s2.send(bytes(z,'utf8'))
            s2.recv(1024)
            s2.send(bytes(m,'utf8'))
            s2.recv(1024)
            s2.send(bytes(str(it4),'utf8'))
            s2.recv(1024)
            s2.send(bytes(str(it1),'utf8'))
            s2.recv(1024)
            s2.send(rp4)
            s2.recv(1024)
            s2.send(rp1)
        except:
            print("Server 2 timed out")
        try:
            s3.settimeout(1)
            s3.send(bytes(p,'utf8'))
            s3.recv(1024)
            s3.send(bytes(z,'utf8'))
            s3.recv(1024)
            s3.send(bytes(m,'utf8'))
            s3.recv(1024)
            s3.send(bytes(str(it1),'utf8'))
            s3.recv(1024)
            s3.send(bytes(str(it2),'utf8'))
            s3.recv(1024)
            s3.send(rp1)
            s3.recv(1024)
            s3.send(rp2)
        except:
            print("Server 3 timed out")
        try:
            s4.settimeout(1)
            s4.send(bytes(p,'utf8'))
            s4.recv(1024)
            s4.send(bytes(z,'utf8'))
            s4.recv(1024)
            s4.send(bytes(m,'utf8'))
            s4.recv(1024)
            s4.send(bytes(str(it2),'utf8'))
            s4.recv(1024)
            s4.send(bytes(str(it3),'utf8'))
            s4.recv(1024)
            s4.send(rp2)
            s4.recv(1024)
            s4.send(rp3)
        except:
            print("Server 4 timed out")
    elif md5 % 4 == 3:
        m = 'm3'
        print(m)
        try:
            s1.settimeout(1)
            s1.send(bytes(p,'utf8'))
            s1.recv(1024)
            s1.send(bytes(z,'utf8'))
            s1.recv(1024)
            s1.send(bytes(m,'utf8'))
            s1.recv(1024)
            s1.send(bytes(str(it2),'utf8'))
            s1.recv(1024)
            s1.send(bytes(str(it3),'utf8'))
            s1.recv(1024)
            s1.send(rp2)
            s1.recv(1024)
            s1.send(rp3)
        except:
            print("Server 1 timed out")
        try:
            s2.settimeout(1)
            s2.send(bytes(p,'utf8'))
            s2.recv(1024)
            s2.send(bytes(z,'utf8'))
            s2.recv(1024)
            s2.send(bytes(m,'utf8'))
            s2.recv(1024)
            s2.send(bytes(str(it3),'utf8'))
            s2.recv(1024)
            s2.send(bytes(str(it4),'utf8'))
            s2.recv(1024)
            s2.send(rp3)
            s2.recv(1024)
            s2.send(rp4)
        except:
            print("server 2 timed out")
        try:
            s3.settimeout(1)
            s3.send(bytes(p,'utf8'))
            s3.recv(1024)
            s3.send(bytes(z,'utf8'))
            s3.recv(1024)
            s3.send(bytes(m,'utf8'))
            s3.recv(1024)
            s3.send(bytes(str(it4),'utf8'))
            s3.recv(1024)
            s3.send(bytes(str(it1),'utf8'))
            s3.recv(1024)
            s3.send(rp4)
            s3.recv(1024)
            s3.send(rp1)
        except:
            print("Server 3 timed out")
        try:
            s4.settimeout(1)
            s4.send(bytes(p,'utf8'))
            s4.recv(1024)
            s4.send(bytes(z,'utf8'))
            s4.recv(1024)
            s4.send(bytes(m,'utf8'))
            s4.recv(1024)
            s4.send(bytes(str(it1),'utf8'))
            s4.recv(1024)
            s4.send(bytes(str(it2),'utf8'))
            s4.recv(1024)
            s4.send(rp1)
            s4.recv(1024)
            s4.send(rp2)
        except:
            print("Server 4 timed out")
elif sys.argv[2] == 'GET':
#     s2.close()
#     s3.close()
#     s4.close()
    serv1 = []
    serv2 = []
    serv3 = []
    serv4 = []
    
    if len(sys.argv) == 4:
        g = 'GET'
        z = sys.argv[3]
    if len(sys.argv) == 5:
        g = 'GETS'
        z = str(sys.argv[3]) + str(sys.argv[4])
    #print(g.encode('utf8'))
    try:
        print("ERR")
        s1.send(g.encode('utf8'))
        s1.send(z.encode('utf8'))
        serv1 = []
        n1 = s1.recv(1024)
        s1.send(b'1')
        no1 = n1.decode('utf8')
        for x in range(0,int(no1)):
            f1 = s1.recv(1024)
            
            serv1.append(f1.decode('utf8'))
        print("server 1:" + format(serv1))
    except:
        serv1 = ['']
        pass
    try:
        s2.send(g.encode('utf8'))
        s2.send(z.encode('utf8'))
        serv2 = []
        n2 = s2.recv(1024)
        s2.send(b'1')
        no2 = n2.decode('utf8')
        for x in range(0,int(no2)):
            f2 = s2.recv(1024)
            
            serv2.append(f2.decode('utf8'))
        print("server 2:" + format(serv2))
    except:
        serv2 = ['']
        pass
    
    try:
        s3.send(g.encode('utf8'))
        s3.send(z.encode('utf8'))
        serv3 = []
        n3 = s3.recv(1024)
        s3.send(b'1')
        no3 = n3.decode('utf8')
        for x in range(0,int(no3)):
            f3 = s3.recv(1024)
            
            serv3.append(f3.decode('utf8'))
        print("server 3:" + format(serv3))
    except:
        serv3 = ['']
        pass
    
    try:
        s4.send(g.encode('utf8'))
        s4.send(z.encode('utf8'))
        serv4 = []
        n4 = s4.recv(1024)
        s4.send(b'1')
        no4 = n4.decode('utf8')
        for x in range(0,int(no4)):
            f4 = s4.recv(1024)
            
            serv4.append(f4.decode('utf8'))
        print("server 4:" + format(serv4))
    except:
        serv4 = ['']
        pass
    
    
    #print(main)
    
    if str('.' + sys.argv[3] + '.1') in serv1:
        re1 = 1
    elif str('.' + sys.argv[3] + '.1') in serv2:
        re1 = 2
    elif str('.' + sys.argv[3] + '.1') in serv3:
        re1 = 3
    elif str('.' + sys.argv[3] + '.1') in serv4:
        re1 = 4
    else:
        re1 = 0   
    
    if str('.' + sys.argv[3] + '.2') in serv1:
        re2 = 1
    elif str('.' + sys.argv[3] + '.2') in serv2:
        re2 = 2
    elif str('.' + sys.argv[3] + '.2') in serv3:
        re2 = 3
    elif str('.' + sys.argv[3] + '.2') in serv4:
        re2 = 4
    else:
        re2 = 0
        
    if str('.' + sys.argv[3] + '.3') in serv1:
        re3 = 1
    elif str('.' + sys.argv[3] + '.3') in serv2:
        re3 = 2
    elif str('.' + sys.argv[3] + '.3') in serv3:
        re3 = 3
    elif str('.' + sys.argv[3] + '.3') in serv4:
        re3 = 4
    else:
        re3 = 0
        
    if str('.' + sys.argv[3] + '.4') in serv1:
        re4 = 1
    elif str('.' + sys.argv[3] + '.4') in serv2:
        re4 = 2
    elif str('.' + sys.argv[3] + '.4') in serv3:
        re4 = 3
    elif str('.' + sys.argv[3] + '.4') in serv4:
        re4 = 4
    else:
        re4 = 0
    
    
    print(re1)
    print(re2)
    print(re3)
    print(re4)
    
    if re1 == 0 or re2 ==0 or re3 == 0 or re4 == 0:
        print("File is incomplete")
    
   
    if re1 == 3:
        f1 = open('file1.txt','wb')
        s3.send(b'1')
        it1 = s3.recv(10)
        for x in range(0,int(it1)):
            d1 = s3.recv(1024)
            f1.write(d1)
        op1 = open('file1.txt','rb')
        
        #print(len(f1))
        f1.close()
        fe1 = op1.read(os.path.getsize('file1.txt') - 64)
        
    if re2 == 3:
        f2 = open('file2.txt','wb')
        s3.send(b'2')
        it2 = s3.recv(10)
        for x in range(0,int(it2)):
            d2 = s3.recv(1024)
            f2.write(d2)
        op2 = open('file2.txt','rb')
        
        #print(len(f2))
        f2.close()    
        fe2 = op2.read(os.path.getsize('file2.txt') - 64)
    
    if re3 == 3:
        f3 = open('file3.txt','wb')
        s3.send(b'3')
        it3 = s3.recv(10)
        for x in range(0,int(it3)):
            d3 = s3.recv(1024)
            f3.write(d3)
        op3 = open('file3.txt','rb')
        
        #print(len(f3))
        f3.close()
        fe3 = op3.read(os.path.getsize('file3.txt') - 64)
    
    if re4 == 3:
        f4 = open('file4.txt','wb')
        s3.send(b'1')
        it4 = s3.recv(10)
        for x in range(0,int(it4)):
            d4 = s3.recv(1024)
            f4.write(d4)
        op4 = open('file4.txt','rb')
        
        #print(len(f4))
        f4.close()
        fe4 = op4.read(os.path.getsize('file4.txt') - 64)
    
    if re1 == 2:
        f1 = open('file1.txt','wb')
        s2.send(b'1')
        it1 = s2.recv(10)
        for x in range(0,int(it1)):
            d1 = s2.recv(1024)
            f1.write(d1)
        op1 = open('file1.txt','rb')
        
        #print(len(f1))
        f1.close()
        fe1 = op1.read(os.path.getsize('file1.txt') - 64)
    

    
    
    if re4 == 2:
        f4 = open('file4.txt','wb')
        s2.send(b'4')
        it4 = s2.recv(10)
        for x in range(0,int(it4)):
            d4 = s2.recv(1024)
            f4.write(d4)
        op4 = open('file4.txt','rb')
        
        #print(len(f4))
        f4.close()
        fe4 = op4.read(os.path.getsize('file4.txt') - 64)
    
    
    if re1 == 1:
        f1 = open('file1.txt','wb')
        s1.send(b'1')
        it1 = s1.recv(10)
        for x in range(0,int(it1)):
            d1 = s1.recv(1024)
            f1.write(d1)
        
        op1 = open('file1.txt','rb')
        
        #print(len(fe1))
        f1.close()
        fe1 = op1.read(os.path.getsize('file1.txt') - 64)
    
    
      
    if re2 == 1:
        f2 = open('file2.txt','wb')
        s1.send(b'2')
        it2 = s1.recv(10)
        for x in range(0,int(it2)):
            d2 = s1.recv(1024)
            f2.write(d2)
        
        op2 = open('file2.txt','rb')
        
        #print(len(fe2))
        f2.close()
        fe2 = op2.read(os.path.getsize('file2.txt') - 64)
        
    if re3 == 1:
        f3 = open('file3.txt','wb')
        s1.send(b'3')
        it3 = s1.recv(10)
        #print(it3)
        for x in range(0,int(it3)):
            d3 = s1.recv(1024)
            #print(len(d3))
            f3.write(d3)
        
        op3 = open('file3.txt','rb')
        
        
        f3.close()
        fe3 = op3.read(os.path.getsize('file3.txt') - 64)
        #print(len(fe3))
    
    if re4 == 1:
        f4 = open('file4.txt','wb')
        s1.send(b'4')
        it4 = s1.recv(10)
        for x in range(0,int(it4)):
            d4 = s1.recv(1024)
            f4.write(d4)
        
        op4 = open('file4.txt','rb')
        
        #print(len(fe4))
        f4.close()
        fe4 = op4.read(os.path.getsize('file4.txt') - 64)
        
    
    
    if re2 == 2:
        f2 = open('file2.txt','wb')
        s2.send(b'2')
        it2 = s2.recv(10)
        #print(it3)
        for x in range(0,int(it2)):
            d2 = s2.recv(1024)
            #print(len(d4))
            f2.write(d2)
        
        op2 = open('file2.txt','rb')
        
        #print(len(fe2))
        f2.close()
        fe2 = op2.read(os.path.getsize('file2.txt') - 64)
#     print(len(fe2))
    
    if re3 == 2:
        f3 = open('file3.txt','wb')
        s3.send(b'3')
        it3 = s2.recv(10)
        #print(it3)
        for x in range(0,int(it3)):
            d3 = s2.recv(1024)
            #print(len(d4))
            f3.write(d3)
        
        op3 = open('file3.txt','rb')
        
        #print(len(fe3))
        f3.close()
        fe3 = op3.read(os.path.getsize('file3.txt') - 64)
    
    if re1 == 4:
        f1 = open('file1.txt','wb')
        s4.send(b'1')
        it1 = s4.recv(10)
        for x in range(0,int(it1)):
            d1 = s4.recv(1024)
            f1.write(d1)
        op1 = open('file1.txt','rb')
        
        #print(len(f1))
        f1.close()
        fe1 = op1.read(os.path.getsize('file1.txt') - 64)
        
    if re2 == 4:
        f2 = open('file2.txt','wb')
        s4.send(b'2')
        it2 = s4.recv(10)
        for x in range(0,int(it2)):
            d2 = s4.recv(1024)
            f2.write(d2)
        op2 = open('file2.txt','rb')
        
        #print(len(f2))
        f2.close()    
        fe2 = op2.read(os.path.getsize('file2.txt') - 64)
    
    if re3 == 4:
        f3 = open('file3.txt','wb')
        s4.send(b'3')
        it3 = s4.recv(10)
        for x in range(0,int(it3)):
            d3 = s4.recv(1024)
            f3.write(d3)
        op3 = open('file3.txt','rb')
        
        #print(len(f3))
        f3.close()
        fe3 = op3.read(os.path.getsize('file3.txt') - 64)
    
    if re4 == 4:
        f4 = open('file4.txt','wb')
        s4.send(b'1')
        it4 = s4.recv(10)
        for x in range(0,int(it4)):
            d4 = s4.recv(1024)
            f4.write(d4)
        op4 = open('file4.txt','rb')
        
        #print(len(f4))
        f4.close()
        fe4 = op4.read(os.path.getsize('file4.txt') - 64)

    
    try:    
        
      
        file = b''.join([fe1,fe2,fe3,fe4])
        print(len(file))
        f = open("Received-" + str(sys.argv[3]),'wb')
        f.write(file)
    except:
        pass