import telnetlib
import Fuildnc as Fluidnc


class TelnetConnection:
    def __init__(self, Telnet_HOST, Telnet_PORT, TargetPlatform, Timoeout = 5 ):
        print("Telent Connection has been defined")
        self.Telnet_HOST = Telnet_HOST
        self.Telnet_PORT = Telnet_PORT
        self.TargetPlatform = TargetPlatform
        self.Telnet_Connection_Timeout = Timoeout
        self.Telnet_Connected = False
        self.tn = telnetlib.Telnet()
        self.Status_Dict = {"X_M":0,"X_WCO":0, \
            "Y_M":0,"Y_WCO":0, \
            "Z_M":0,"Z_WCO":0, \
            "A_M":0,"A_WCO":0, \
            "B_M":0,"B_WCO":0, \
            "C_M":0,"C_WCO":0, \
            "SpindleSpeed":0.0,\
            "FeedRate":0.0, \
            "X_LimTrig":False, \
            "Y_LimTrig":False, \
            "Z_LimTrig":False, \
            "A_LimTrig":False, \
            "B_LimTrig":False, \
            "C_LimTrig":False, \
            "MSG": 'EMPTY', \
            "Status":'Not Connected' }
        try:
            self.tn = telnetlib.Telnet(self.Telnet_HOST,self.Telnet_PORT,self.Telnet_Connection_Timeout)
            self.Telnet_Connected = True
            print("Telnet Connection has been established")
            self.Status_Dict["Status"] = 'Connected' 
        except:
            print("Telnet Connection failed to connect")
            self.Telnet_Connected = False
            self.Status_Dict["Status"] = 'Disconnected' 
        
    def GetTargetStatus(self):
        try:
            if self.TargetPlatform == "Fluidnc":
                self.Status_Dict["MSG"] = ""
                self.command = "?" + "\n"
                self.tn.write(self.command.encode("ascii"))
                self.Status_Dict = Fluidnc.ParseResponse(str(self.tn.read_until(b"\n", timeout=0.2)))
                self.Status_Dict  = Fluidnc.ParseResponse(str(self.tn.read_until(b"\n", timeout=0.2)))  
            elif self.TargetPlatform == "GRBL":
                print("Connection Not yet implemented")
            elif self.TargetPlatform == "RRF":
                print("Connection Not yet implemented")
            elif self.TargetPlatform == "Marlin":
                print("Connection Not yet implemented") 
        except:
            print("Failed to get Status Command - is dissconnected?")
            self.Status_Dict["Status"] ='Disconnected'
            self.Connection = False

        return self.Status_Dict






#Connection = False
#Status_Dict = {"X_M":0,"X_WCO":0, \
#            "Y_M":0,"Y_WCO":0, \
#            "Z_M":0,"Z_WCO":0, \
#            "A_M":0,"A_WCO":0, \
#            "B_M":0,"B_WCO":0, \
#            "C_M":0,"C_WCO":0, \
#            "SpindleSpeed":0.0,\
#            "FeedRate":0.0, \
#            "X_LimTrig":False, \
#            "Y_LimTrig":False, \
#            "Z_LimTrig":False, \
#            "A_LimTrig":False, \
#            "B_LimTrig":False, \
#            "C_LimTrig":False, \
#            "MSG": 'EMPTY', \
#            "Status":'Not Connected' }






