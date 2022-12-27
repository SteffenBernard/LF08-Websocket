from computer import Computer #von computer.py die Computer Parent-Klasse importieren
import socket
import platform

class Server(Computer): # Vererbung
    
    _service = ""
    __sockIP = "0.0.0.0"
    __sockPort = 0 

    def __init__(self,powerSupply,_cpu,_cpuSpeed,_ram,_os,_ip,_service,__sockIP,__sockPort):#???
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



    def runningServer(self):
        ####TEST 
        # print("Server läuft")
        steffTalks = ""

        self.web_socket.listen()
        conn, addr = self.web_socket.accept()
        with conn: # einrücken nicht vergessen Danke Simon
            print("Server verbunden mit " + str(addr[0]) + " auf Port " + str(self.__sockPort))

            while data.lower != "shutdown": #wenn vom Client ein Shutdown kommt--- lower: egal welche Schreibweise FALSE
                data = conn.recv(1024)
                steffTalks = data.decode()
                print("empfangen von: " + str(addr[0]) + " " + steffTalks)
                conn.sendall(("empfangen von: " + str(addr[0]) + " " + steffTalks).encode())
            self.web_socket.close()


if __name__== "__main__":
    steffServer = Server("900 W",platform.machine(),3.6, "16 GB", platform.system(),platform.node(), platform.system(),"127.0.0.1",2022)  
    #("900 W",platform.machine(),3.6, "16 GB", platform.system(), platform.node())#module platform und Computer Klasse plus ServerIP u. Port
    #try: try except besser in Methoden() verwenden 
    steffServer.createSocket("127.0.0.1",2022)
    
    #print("Fehler beim Socketerstellen: "+ str(error))
    steffServer.runningServer() #self.sockPort falsche Schreibweise Fehler Danke Simon
    #except Exception as error:
    #print("Fehler beim Serverstarten: " + str(error))
    #steffServer.web_socket.close()
