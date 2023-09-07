# Import socket module
import socket
 
def main():
   # Local host IP '127.0.0.1'
   host = '127.0.0.1'
 
   # Define the server port to connect with
   port = 5009
 
   server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
   # Connect to server on local computer
   server.connect((host,port))
 
   # String you want to send to server
 
   while True:
 
       # Message sent to server
       message = input("Enter numbers with space to add : ")
       server.send(message.encode())
 
       # Message received from server
       data = server.recv(1001)
 
       # Print the received message from server
       print('Addition :',str(data.decode()))
 
       cont= input('\nDo you want to continue(y/n) :')
       if cont== 'y':
           continue
       else:
           break
   # Close the connection
   server.close()
 
if __name__ == '__main__':
   main()