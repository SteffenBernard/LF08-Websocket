import computer
import socket


class Server(computer.Computer):
    
    _service = "TCP"
    __sockIP = "172.16.16.1"
    __sockPort = "80" 

    def __init__(self,powerSupply,_cpu,_cpuSpeed,_ram,_os,_ip,_service): #__sockIP,__sockPort???
        super().__init__(powerSupply,_cpu,_cpuSpeed,_ram,_os,_ip)
        self._service = _service
        

    def createSocket(self,__sockIP,__sockPort):
        self.__sockIP = __sockIP
        self.__sockPort = __sockPort
        
        print("Server-IP:" + self.__sockIP)
        print("Server lauscht auf:" + self.__sockPort)


        #HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
        #PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.__sockIP, self.__sockPort))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    
                    data = conn.recv(1024)
                    if data.lower == "shutdown":
                        print("Server wird beendet.")
                        break
                    conn.sendall(data)



    def runningServer(self):
        print("Server läuft")





asusPC = Server("600 W","Intel i9",3.6, "64 GB", "Windows 10", "TCP-IP", "192.168.178.231")  

asusPC.createSocket("192.16.16.16","80")

asusPC.runningServer()

