import telnetlib
import time

HOST = "192.168.0.165"

print("Start")
tn = telnetlib.Telnet(HOST,"23")
command = "$SD/Status" + "\n"
#tn.write(command.encode("ascii"))
TermCommand = "\r\n"
t_end = time.time() + 60 * 0.01
while time.time() < t_end:
    print(tn.read_eager())


command = "$SD/List" + "\n"
tn.write(command.encode("ascii"))
print(tn.expect("",3))
#print(tn.read_until(TermCommand.encode("ascii"),4))
#print(tn.read_until(TermCommand.encode("ascii"),4))
#print(tn.read_until(TermCommand.encode("ascii"),4))
#print(tn.read_until(TermCommand.encode("ascii"),4))
print("Exit")
