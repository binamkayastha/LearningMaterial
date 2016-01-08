import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SOCK_STREM gives the secure connection
print (s)

server = 'pythonprogramming.net'
port = 80

server_ip = socket.gethostbyname(server)
print(server_ip)
#Or get ip of server by pinging it

request = "GET / HTTP/1.1\nHost: "+server+"\n\n"
s.connect((server,port))
s.send(request.encode())
result = s.recv(4096) #Buffer

#print(result)

while (len(result) > 0):
    print(result)
    result = s.recv(1024)
