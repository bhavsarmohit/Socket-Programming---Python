import socket

def runSocket():
    while (True):
        result = ''
        try:
            # next create a socket object
            s = socket.socket()
            print("Socket successfully created")

            # reserve a port on your computer in our
            # case it is 12345 but it can be anything
            port = 6000

            # Next bind to the port
            # we have not typed any ip in the ip field
            # instead we have inputted an empty string
            # this makes the server listen to requests
            # coming from other computers on the network
            # catch exception when android device disconnected

            s.bind(('192.168.1.30', port))
            # s.bind(('', port))
            # =======
            # hostname = socket.gethostname()
            # IPAddr = socket.gethostbyname(hostname)
            # s.bind((IPAddr, port))
            # print("IPADD::"+IPAddr)
            # =======

            # print("socket binded to %s" % (port))

            # put the socket into listening mode
            s.listen(5)
            print("socket is listening")

            # a forever loop until we interrupt it or
            # an error occurs
            while result=='':
                # Establish connection with client.
                c, addr = s.accept()
                print('Got connection from', addr)

                result = c.recv(1024).decode("utf-8")

                print(result)

                # send a thank you message to the client.
                # c.send('Thank you for connecting')
                print(c)

                # Close the connection with the client
                c.close()
                return result


        except Exception as e:
            # Exception is also occur when port 6000 is busy

            print(e)
            print("Check your Connection")
            print("System port is not available at this time")

result=runSocket()
print(result)