import socket
 
host = '192.168.137.220'
port = 50008
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print("Connected to "+(host)+" on port "+str(port))
a=input()
s.sendall(a.encode('ASCII'))
 
while True:
 data = s.recv(1024)
 d=data.decode('ASCII')
 print("Recieved: "+(d))
 response = input("Reply: ")
 if response == "exit":
     #break
  s.sendall(response)
s.close()
