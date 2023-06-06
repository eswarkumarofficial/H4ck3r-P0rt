import socket
import threading
import pyfiglet
from datetime import datetime 

ascii_banner = pyfiglet.figlet_format("H4ck3r - P0rt") 
print(ascii_banner)
print("                                                by Eswar H4ck3r\n")

print("-" * 50) 
print("Scanning started at: " + str(datetime.now())) 
print("-" * 50)

host=input("\n" + "Enter host : ")
start_port = int(input("\n" + "Enter the start port : "))
end_port = int(input("\n" + "Enter the end port : "))
open_ports = []

def scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    try:
        con = s.connect((host, port))
        open_ports.append(port)
        print(f"port {port} is open")
        con.close()
    except:
        pass

for port in range(start_port, end_port+1):
    t = threading.Thread(target=scan, args=(port,))
    t.start()

print("open ports:",open_ports)
