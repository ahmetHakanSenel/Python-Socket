from email import message
from fileinput import close
import socket
import json
import time


def Write(readed):
    with open("data.json","w") as f:
        json.dump(readed,f)
        close()
        
def Read():
    with open("data.json","r") as f:
        global readed
        readed = json.load(f)
        close()
        
def Get():
    global data, addr, s
    data, addr = s.recvfrom(1024)
    data = data.decode('utf-8')
    data = json.loads(data)
    
def Send():
    global message, s, addr
    message = json.dumps(readed)
    s.sendto(message.encode('utf-8'), addr)

def Print():
    global i, data
    print(i)
    print("Client: " + data["name"])
    i = i+1

def Control():
    print

def Security():
    print
    
def Term():
    global s, addr, data,i,host,port
    host = '192.168.43.66' #Server ip
    port = 4000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    s.bind((host, port))
    print("Server Started")
    i = 0
    


def Main():
    
    Term()                      #Bağlantı Kurma

    try:
        Get()
        while True:
            Control()
            Read()              #Okuma
            Write(data)         #Yazma
            Send()              #Gönderme
            Write(readed)       #Yazma
            Print()             #Verileri Görme
            Get()               #Alma
            time.sleep(1)
            
        
        c.close()
    except socket.error as msg:
            print("[Server aktif değil.] Mesaj:", msg)

if __name__=='__main__':
    Main()