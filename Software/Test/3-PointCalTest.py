import numpy as np
import pickle

# Touchscreen Cal following information from:
# https://www.ti.com/lit/an/slyt277/slyt277.pdf?ts=1659302699138&ref_url=https%253A%252F%252Fwww.google.com%252F

TouchScreenCal =  {"Alpha_X":0, \
            "Beta_X":0, \
            "Delta_X":0, \
            "Alpha_Y":0, \
            "Beta_Y":0, \
            "Delta_Y":0 }

x = [64, 192, 192]
y = [384, 192 ,576]

a = ([[678, 2169, 1],\
    [2807, 1327, 1],\
    [2629, 3367, 1]])




temp = np.matmul(np.linalg.inv(a), np.array(x))
TouchScreenCal["Alpha_X"] = temp[0]
TouchScreenCal["Beta_X"] = temp[1]
TouchScreenCal["Delta_X"] = temp[2]

temp = np.matmul(np.linalg.inv(a), np.array(y))
TouchScreenCal["Alpha_Y"] = temp[0]
TouchScreenCal["Beta_Y"] = temp[1]
TouchScreenCal["Delta_Y"] = temp[2]
print(TouchScreenCal)
pickle.dump( TouchScreenCal, open( "Settings/TouchScreenCal.p", "wb" ) )