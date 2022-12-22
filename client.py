import socket
import computer

class Client(computer.Computer):
    __remoteIP = "127.0.0.1" #Localhost
    __remotePort = 0 #Lausche am Port 80

    def __init__(self,powerSupply,_cpu,_cpuSpeed,_ram,_os,_ip,__remoteIP,__remotePort):
        super().__init__(powerSupply,_cpu,_cpuSpeed,_ram,_os,_ip) 
        self.__remoteIP = __remoteIP
        self.__remotePort = __remotePort
        

    def createSocket(self,__remoteIP, __remotePort):
        #####TEST
        # 
        #print("IP-Adresse:" + self.__remoteIP)
        #print("Lauscht am Port:" + self.__remotePort)# 
        #
        #      
        self.__remoteIP = __remoteIP
        self.__remotePort = __remotePort
        self.web_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print("Remote IP: "+ self.__remoteIP)
        print("Remote Port: " + str(self.__remotePort))


    def sendData(self):

        ###TEST
        #print("Hier soll eine Eingabe zum Senden erfolgen") 
        # 
        # #
        steffTalks = ""
        print("Nachricht senden starten...")
        self.web_socket.connect((self.__remoteIP,self.__remotePort))
        print(self.__remoteIP + " auf Port " + str(self.__remotePort) +": Bitte Nachricht eingeben.")

        while steffTalks.lower != "shutdown":
            steffTalks = input(">>")
            self.web_socket.sendall(steffTalks.encode())#ENCODE???--DECODE???? UTF-8 unnötig
         ######TEST keine Fehlermeldung und auch  keine Ausgabe???
            data = self.web_socket.recv(1024)
            print(data.decode())

        self.web_socket.close()
        print("Auf Wiedersehen.")
         # #
         # #
         # #
         #    
def main():
    try:    
        steffClient = Client("900 W","Intel i7",3.6, "16 GB", "Windows 10", "192.168.178.231","127.0.0.1", "80")

        steffClient.createSocket("127.0.0.1",80)
        steffClient.getInfo()
        
    except:
        print("Es ist ein Fehler beim Erstellen des Client-Sockets entstanden.")
    
    try:
        steffClient.sendData()  #GETINFO SENDEN!!!!!  
    except Exception as error:
        print("Es ist ein Fehler beim Versenden der Daten entstanden."+ error)
main()