import socket,os
import json
from data_parse import data_parse
from time import strftime, localtime

server = socket.socket()
server.bind(("192.168.1.105",8889))
server.listen(5)
str2=('73657276657241000000000000000000000000000041fefe')
while True:
    conn,addr = server.accept()
    print("new addr:",addr)
    print(conn)
    allData={}
    # path='C:\\Users\\Administrator\\Desktop\\wifi版睡眠带\\zzgs.txt'
    # f=open(path,'a')
    i=0
    str1=('73657276657241000000000000000000000000000041fefe')
    while True:
        str=conn.recv(1024)
        send_time=strftime("%Y-%m-%d %H:%M:%S", localtime())
        data=str.hex()
        allData[send_time]=data
        js=json.dumps(allData)
        # f.write(js)
        # f.flush()
        s=[]
        for x in range(len(data)//2):
            s.append(data[2*x:2*x+2])
        data_parse(s)
        i=i+1
        b=bytes.fromhex(str2)
        conn.send(b)
        
            
    
    
# f.close()
server.close()