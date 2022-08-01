from operator import contains
import re

from regex import P

TestStr = "bbbb<Alarm|MPos:10.000,20.000,30.000|FS:35,45|WCO:1.100,2.200,3.300>\r\n'jj"
match = re.findall("(?<=\<)(.*?)(?=\>)", TestStr)
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
                Mpos_X = 0.0
                Mpos_Y = 0.0
                Mpos_Z = 0.0
                Mpos_A = 0.0
                Mpos_B = 0.0
                Mpos_C = 0.0
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
                WCO_X = 0.0
                WCO_Y = 0.0
                WCO_Z = 0.0
                WCO_A = 0.0
                WCO_B = 0.0
                WCO_C = 0.0
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
            elif "Pn:" in match2[q]:
                temp = match2[q].replace("Pn:","")
                match3 = re.split("[,]",temp)
                X_LimTrig = False
                Y_LimTrig = False
                Z_LimTrig = False
                A_LimTrig = False
                B_LimTrig = False
                C_LimTrig = False
                for e in range(len(match3)):
                    if match3[e] == "X":
                        X_LimTrig = True
                    elif match3[e] == "Y":
                        Y_LimTrig = True
                    elif match3[e] == "Z":
                        Z_LimTrig = True
                    elif match3[e] == "A":
                        A_LimTrig = True
                    elif match3[e] == "B":
                        B_LimTrig = True
                    elif match3[e] == "C":
                        C_LimTrig = True
else:
    print('did not find')
print("end")