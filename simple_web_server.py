from socket import *

HOST,PORT = '',8000

ss = socket(AF_INET,SOCK_STREAM)

# Allow to resume same address
ss.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
ss.bind((HOST,PORT))
ss.listen(1)
print("Server HTTP on port {}".format(PORT))

num = 0
while True:
    cs,addr = ss.accept()
    request = cs.recv(1024)
    num += 1
    print (num)
    print(request.decode('utf-8'))

    http_response = b"""\
    HTTP/1.1 200 OK
    Content-Type: text/html; charset=utf-8

    <h1>hello,It is a simple server!</h1>
    """

    cs.sendall(http_response)
    cs.close()

