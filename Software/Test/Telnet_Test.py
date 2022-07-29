import telnetlib
import time
import re

HOST = "192.168.0.67"

print("Start")
tn = telnetlib.Telnet(HOST,"23")
#command = "$SD/Status" + "\n"
##tn.write(command.encode("ascii"))
#TermCommand = "\r\n"
#t_end = time.time() + 60 * 0.01
#while time.time() < t_end:
#    print(tn.read_eager())
#
#
#command = "$SD/List" + "\n"
#tn.write(command.encode("ascii"))
#print(tn.expect("",3))
##print(tn.read_until(TermCommand.encode("ascii"),4))
##print(tn.read_until(TermCommand.encode("ascii"),4))
##print(tn.read_until(TermCommand.encode("ascii"),4))
##print(tn.read_until(TermCommand.encode("ascii"),4))
command = "?" + "\n"
for x in range(20):
    tn.write(command.encode("ascii"))
    temp = str(tn.read_until(b"\n", timeout=2))
    match = re.findall("(?<=\<)(.*?)(?=\>)", temp)
    # If-statement after search() tests if it succeeded
    if match:
        for p in match:
            print('found', p) ## 'found word:cat'
            match2 = re.split("[|]", p)
            for q in range(len(match2)):
                if q ==0:
                    Status = match2[q]
                elif "MPos:" in match2[q]:
                    temp = match2[q].replace("MPos:","")
                    match3 = re.split("[,]",temp)
                    for e in range(len(match3)):
                        if e == 0:
                            Mpos_X = float(match3[e])
                        elif e == 1:
                            Mpos_Y = float(match3[e])
                        elif e == 2:
                            Mpos_Z = float(match3[e])
                        elif e == 3:
                            Mpos_A = float(match3[e])
                        elif e == 4:
                            Mpos_B = float(match3[e])
                        elif e == 5:
                            Mpos_C = float(match3[e])
                elif "WCO:" in match2[q]:
                    temp = match2[q].replace("WCO:","")
                    match3 = re.split("[,]",temp)
                    for e in range(len(match3)):
                        if e == 0:
                            WCO_X = float(match3[e])
                        elif e == 1:
                            WCO_Y = float(match3[e])
                        elif e == 2:
                            WCO_Z = float(match3[e])
                        elif e == 3:
                            WCO_A = float(match3[e])
                        elif e == 4:
                            WCO_B = float(match3[e])
                        elif e == 5:
                            WCO_C = float(match3[e])
                elif "FS:" in match2[q]:
                    temp = match2[q].replace("FS:","")
                    match3 = re.split("[,]",temp)
                    for e in range(len(match3)):
                        if e == 0:
                            FeedRate = float(match3[e])
                        elif e == 1:
                            SpindleSpeed = float(match3[e])
                
    else:
        print('did not find')
    print("end")
print("Exit")
