import platform


class Computer:
    powerSupply = "800 W"
    _cpuSpeed = 0.0
    _cpu = ""
    _ram = 0
    _os = ""
    _ip = ""
    
    def __init__(self,powerSupply,_cpu,_cpuSpeed,_ram,_os,_ip): #hier müssen keine protected, public gesetzt werden nur Platzhalter
        
        self.powerSupply= powerSupply
        self._cpu = _cpu
        self._cpuSpeed = _cpuSpeed
        self._ram = _ram
        self._os = _os
        self._ip = _ip

    def getInfo(self):
        print("Netzteil:" + self.powerSupply)
        print("CPU:" + self._cpu )
        print("RAM:" + self._ram)
        print("Betriebssystem:" + self._os)
        print("IPAdresse:" + self._ip)
        print()

asusPC = Computer("900 W","Intel i7",3.6, "16 GB", "Windows 10", "192.168.178.231")

asusPC.getInfo()

