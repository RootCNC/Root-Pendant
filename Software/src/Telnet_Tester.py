import time
import TelnetConnection
print("Starting Telnet Demo")

Connection = TelnetConnection.TelnetConnection("192.168.0.67","23","Fluidnc",5)

#Connection.Connect
for x in range(100):
    time.sleep(.2)
    temp = Connection.GetTargetStatus()
    print(temp)
    