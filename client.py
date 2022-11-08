import socket
from telnetlib import SE
import time
import json
from fileinput import close

def Get():
    global data, addr, s,jData
    data, addr = s.recvfrom(1024)
    data = data.decode('utf-8')
    jData = json.loads(data)

def Write(jData):
    with open ("deneme.json" ,'w') as f:
        json.dump(jData,f)
    close()

def Read():
    with open("deneme.json" , 'r') as f:
       global deneme
       deneme = json.load(f)
    close()
    
def Control():
    print

def Security():
    print

def Send():
    global deneme, s, server
    deneme["name"] = "Hakan"
    message = json.dumps(deneme)
    s.sendto(message.encode('utf-8'), server)        

def Term():
    global host, port, server, s, i
    host='192.168.43.61' #client ip
    port = 4005
    
    server = ('192.168.43.66', 4000)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))
    i = 0
    
def Print():
    global i, jData
    i=i+1
    print("\nServer: " + jData["name"] + "\n",i)

def Writed():
    print    
    
while True:

    try:
        while True:
            Term()              #Bağlantı Kurma
            Read()              #Dosya okuma
            Send()              #Veri yollama
            Get()               #Veri alma
            Writed()            #Database yazma
            Write(jData)        #Dosyaya yazma
                                       

            time.sleep(1)
        s.close()
    except socket.error:
        print("[Server aktif değil.] Mesaj:")
