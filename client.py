
import socket
from computer import Computer
import platform
class Client(Computer):
    __remoteIP = "" #Localhost
    __remotePort = 0 #Lausche am Port xyz
    
    #def __init__(self,powerSupply,_cpu,_cpuSpeed,_ram,_os,_ip,__remoteIP,__remotePort):
    #    super().__init__(powerSupply,_cpu,_cpuSpeed,_ram,_os,_ip) #Danke Julian für die super()
    #    self.__remoteIP = str(__remoteIP)
    #    self.__remotePort = int(__remotePort)
       

    #def createSocket(self,__remoteIP, __remotePort):
        #####TEST
        # 
        #print("IP-Adresse:" + self.__remoteIP)
        #print("Lauscht am Port:" + self.__remotePort)# 
        
    def createSocket(self,__remoteIP,__remotePort):
        
        try:
            self.__remoteIP = __remoteIP
            self.__remotePort = __remotePort
            self.web_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print(f"Remote-IP: {self.__remoteIP}\nRemote-Port: {self.__remotePort}")                                
        except Exception as error:
            print("Es ist ein Fehler beim Versenden der Daten entstanden."+ error)

    def sendData(self): 
        ###TEST
        #print("Hier soll eine Eingabe zum Senden erfolgen") 
        # 
        # #
        #steffTalks == "" in string umbenennen 
   
        try: #DANKE Patrick für den Try-Exceptions Tipps
            string = ""
            self.web_socket.connect((self.__remoteIP, self.__remotePort))
            print(f"\nErfolgreich verbunden mit {self.__remoteIP}:{self.__remotePort}")
            while string != "shutdown":
                string = input("Nachricht senden >>")
                self.web_socket.sendall(string.encode())
                data = self.web_socket.recv(1024)
                print(data.decode())
                if(string.lower == "shutdown"):    
                    print("Server wird heruntergefahren.")
                    self.web_socket.close()
                elif(string.lower == "exit"):
                    print("Server wird beendet. Auf Wiedersehen")
                    self.web_socket.close()
                    break
        except Exception as error:
            print(f"Fehler bei Serverausführung: {error}]")

        '''
        print("Nachricht senden starten...")
        self.client_socket.connect((self.__remoteIP,self.__remotePort))
        print(self.__remoteIP + " auf Port " + str(self.__remotePort) +": Bitte Nachricht eingeben.")

        while True:  #while steffTalks.lower != "shutdown": funktionierte nicht
            steffTalks = input(">>")
            self.web_socket.sendall(steffTalks.encode())#ENCODE???--DECODE???? UTF-8 unnötig
         ######TEST keine Fehlermeldung und aber auch keine Ausgabe???
            data = self.web_socket.recv(1024)
            print(data.decode())
            if steffTalks.lower == "shutdown":
                break
        self.web_socket.close()
        print("Server wird heruntergefahren. Auf Wiedersehen.")
         # #
         # #
         # #
         #    
'''

if __name__ == '__main__': #Danke Julian
    #def main():
    #try:  #besser in Funktionen Fehler abfangen   
    steffClient = Client("900 W",platform.processor(),3.6, "16 GB", "Windows 10", "192.168.178.231")
    steffClient.createSocket("127.0.0.1",2022)
    steffClient.getInfo()
    steffClient.sendData() 

    #except Exception as error:
    #print("Es ist ein Fehler beim Versenden der Daten entstanden."+ error)
    #main