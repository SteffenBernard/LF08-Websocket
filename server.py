import computer
import socket


class Server(computer.Computer):
    
    _service = "TCP WEB SOCKET Server"
    __sockIP = "0.0.0.0"
    __sockPort = 80 

    def __init__(self,powerSupply,_cpu,_cpuSpeed,_ram,_os,_ip,_service,__sockIP,__sockPort): #__sockIP,__sockPort???
        super().__init__(powerSupply,_cpu,_cpuSpeed,_ram,_os,_ip)
        self._service = _service
        self.__sockIP = __sockIP
        self.__sockPort = __sockPort
        

    def createSocket(self,__sockIP,__sockPort):
        self.__sockIP = __sockIP ##muss mit den Übergabeparameter der Methode übereinstimmen
        self.__sockPort = __sockPort

        
        #####TEST
        #print("Server-IP:" + self.__sockIP)
        #print("Server lauscht auf:" + str(self.__sockPort))
        self.web_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.web_socket.bind((self.__sockIP,self.__sockPort))
        print(self.__sockIP + " " + str(self.__sockPort) +" : Server wartet auf Nachricht vom Client.")



    def runningServer(self,__sockIP, __sockPort):
        ####TEST 
        # print("Server läuft")
        self.web_socket.listen()
        conn, addr = self.web_socket.accept()
        with conn:
            print("Server verbunden mit " + str(addr[0]) + " auf Port " + str(self.__sockport))

        while data.lower != "shutdown": #wenn vom Client ein Shutdown kommt egal welche Schreibweise FALSE
            data = conn.recv(1024)
            steffTalks = data.decode()
            print("empfangen von: " + str(addr[0]) + steffTalks)
        
        self.web_socket.close()


def main():
    
    try:

        steffServer = Server("600 W","Intel i7",3.6, "64 GB", "Windows 10", "TCP-IP", "127.0.0.1")  

        steffServer.createSocket("127.0.0.1",80)
    except Exception as error:
        print("Fehler beim Socketerstellen: "+ str(error))


    try:
        steffServer.runningServer()
    except Exception as error:
        print("Fehler beim Serverstarten: " + str(error))
        steffServer.web_socket.close()
main()