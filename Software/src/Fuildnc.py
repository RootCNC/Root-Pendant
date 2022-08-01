import re

Status_Dict =  {"X_M":0,"X_WCO":0, \
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


def ParseResponse(Msg):
    print("Parsing the returned Mesage = " + Msg)
    if Msg == "b''":
        print("Empty returned Message")
        return
    match = re.findall("(?<=\<)(.*?)(?=\>)", Msg)
    # If-statement after search() tests if it succeeded
    if match:
        for p in match:
            #print('found', p) ## 'found word:cat'
            match2 = re.split("[|]", p)
            for q in range(len(match2)):
                if q ==0:
                    Status_Dict["Status"] = match2[q]
                elif "MPos:" in match2[q]:
                    temp = match2[q].replace("MPos:","")
                    match3 = re.split("[,]",temp)
                    Status_Dict["Mpos_X"] = 0.0
                    Status_Dict["Mpos_Y"] = 0.0
                    Status_Dict["Mpos_Z"] = 0.0
                    Status_Dict["Mpos_A"] = 0.0
                    Status_Dict["Mpos_B"] = 0.0
                    Status_Dict["Mpos_C"] = 0.0
                    for e in range(len(match3)):
                        if e == 0:
                            Status_Dict["Mpos_X"] = float(match3[e])
                        elif e == 1:
                            Status_Dict["Mpos_Y"] = float(match3[e])
                        elif e == 2:
                            Status_Dict["Mpos_Z"] = float(match3[e])
                        elif e == 3:
                            Status_Dict["Mpos_A"] = float(match3[e])
                        elif e == 4:
                            Status_Dict["Mpos_B"] = float(match3[e])
                        elif e == 5:
                            Status_Dict["Mpos_C"] = float(match3[e])
                elif "WCO:" in match2[q]:
                    temp = match2[q].replace("WCO:","")
                    match3 = re.split("[,]",temp)
                    Status_Dict["WCO_X"] = 0.0
                    Status_Dict["WCO_Y"] = 0.0
                    Status_Dict["WCO_Z"] = 0.0
                    Status_Dict["WCO_A"] = 0.0
                    Status_Dict["WCO_B"] = 0.0
                    Status_Dict["WCO_C"] = 0.0
                    for e in range(len(match3)):
                        if e == 0:
                            Status_Dict["WCO_X"] = float(match3[e])
                        elif e == 1:
                            Status_Dict["WCO_Y"] = float(match3[e])
                        elif e == 2:
                            Status_Dict["WCO_Z"] = float(match3[e])
                        elif e == 3:
                            Status_Dict["WCO_A"] = float(match3[e])
                        elif e == 4:
                            Status_Dict["WCO_B"] = float(match3[e])
                        elif e == 5:
                            Status_Dict["WCO_C"] = float(match3[e])
                elif "FS:" in match2[q]:
                    temp = match2[q].replace("FS:","")
                    match3 = re.split("[,]",temp)
                    Status_Dict["FeedRate"] = 0.0
                    Status_Dict["SpindleSpeed"] = 0.0
                    for e in range(len(match3)):
                        if e == 0:
                            Status_Dict["FeedRate"] = float(match3[e])
                        elif e == 1:
                            Status_Dict["SpindleSpeed"] = float(match3[e])
                elif "Pn:" in match2[q]:
                    temp = match2[q].replace("Pn:","")
                    match3 = re.split("[,]",temp)
                    Status_Dict["X_LimTrig"] = False
                    Status_Dict["Y_LimTrig"] = False
                    Status_Dict["Z_LimTrig"] = False
                    Status_Dict["A_LimTrig"] = False
                    Status_Dict["B_LimTrig"] = False
                    Status_Dict["C_LimTrig"] = False
                    for e in range(len(match3)):
                        if match3[e] == "X":
                            Status_Dict["X_LimTrig"] = True
                        elif match3[e] == "Y":
                            Status_Dict["Y_LimTrig"] = True
                        elif match3[e] == "Z":
                            Status_Dict["Z_LimTrig"] = True
                        elif match3[e] == "A":
                            Status_Dict["A_LimTrig"] = True
                        elif match3[e] == "B":
                            Status_Dict["B_LimTrig"] = True
                        elif match3[e] == "C":
                            Status_Dict["C_LimTrig"] = True
    else:
        Status_Dict["MSG"] = Msg.replace("\\r\\n","")
    return Status_Dict