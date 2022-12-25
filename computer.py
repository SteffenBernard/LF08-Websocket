import platform


class Computer:
    powerSupply = "0 W" #string
    _cpuSpeed = 0.0 #double
    _cpu = "" #string
    _ram = 0 #int
    _os = ""#str
    _ip = ""#str
    
    def __init__(self,powerSupply,_cpu,_cpuSpeed,_ram,_os,_ip): #hier müssen keine protected, public gesetzt werden nur Platzhalter
        
        self.powerSupply= powerSupply
        self._cpu = _cpu
        self._cpuSpeed = _cpuSpeed
        self._ram = _ram
        self._os = _os
        self._ip = _ip

    def getInfo(self):
        print("Netzteil:" + str(self.powerSupply))
        print("CPU:" + str(self._cpu))
        print("RAM:" + str(self._ram))
        print("Betriebssystem:" + str(self._os))
        print("IPAdresse:" + str(self._ip))
        print() #Leerzeile


if __name__== "__main__": #Danke Julian
    #####TEST
    #steffPC = Computer("900 W","INTEL i7",3.6, "16 GB", "Windows 10", "192.168.178.231")
    steffPC = Computer("900 W",platform.machine(),3.6, "16 GB", platform.system(), platform.node())#module platform
    steffPC.getInfo()

