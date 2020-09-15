import socket,os
from testdemo1 import *
def dataParse(data):
    print(data[0:2])
    if data[0:2]==['ff', 'ff']:
        header=[data[0:2]]
        mac= data[2:8]
        print('设备mac地址为：',mac)
        data_style=data[8]
        print('数据类型为：',data_style)
        data_lenth=int(data[11]+data[12],16)
        print(data_lenth)
        if data_lenth==16:
            dataParse_16(data[13:29])
        else:
            dataParse_20(data[13:],data_lenth)

"""
解析16字节长度数据
"""
def dataParse_16(data_16):
    if data_16[0]=='41':
        print('设备当前时间为：',
        data_16[1],'年',
        data_16[2],'月',
        data_16[3],'日',
        data_16[4],':',data_16[5],':',data_16[6])
    else:
        print(data_16)

"""
解析20字节长度存储数据
"""
def dataParse_20(data_20,data_lenth):
    for x in range(data_lenth//20):
        s=data_20[x*20:(x+1)*20]
        if s[0:2]==['88','ff']:
            flag1.setflag(False)
        print(s)
    
"""
数据接收是否完成状态
"""


addr='192.168.1.104'
port=8889
server=socket.socket()
server.bind((addr,port))
server.listen(5)
flag1=data_isok_status()
while True:
    client_conn,client_addr=server.accept()
    print('客户端连接：',client_addr,'已连接')
    client_conn.send(
        bytes.fromhex('73657276657211010000000000000000000000000012fefe')
        )
    while True:
        # 接收数据
        data=client_conn.recv(1024).hex()
        if len(data)>0:
            s=[]
            for x in range(len(data)//2):
                s.append(data[x*2:(x+1)*2])
        #调用数据解析函数       
            dataParse(s)  
              
        print(flag1.flag)  
        if flag1.flag==False:
            del_data=('73657276657212888800000000000000000000000022fefe')
            senddata=bytes.fromhex(del_data)
            client_conn.send(senddata)
            flag1.flag=True
            print('已发送清除历史数据指令')

        print('接收数据已完成')




        