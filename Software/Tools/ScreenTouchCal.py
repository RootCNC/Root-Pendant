from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ScreenCal_UI import Ui_ScreenCal_UI
import sys
import time
import RPi.GPIO as GPIO
import board
import time
import src.adafruit_tsc2007 

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
i2c = board.I2C()

irq_dio = None  # don't use an irq pin by default
# uncomment for optional irq input pin so we don't continuously poll the I2C for touches
# irq_dio = digitalio.DigitalInOut(board.A0)


class ScreenCal_UI(QMainWindow):


    def __init__(self):
        super().__init__()
        self.ui = Ui_ScreenCal_UI()
        self.ui.setupUi(self)
        #self.ui.MenuBtn.clicked.connect(self.SlideLeftMenu)
        #self.ui.FilesBtn.clicked.connect(self.FilesRightMenu)
        #self.ui.RootBtn.clicked.connect(self.Close)
        #flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        #self.setWindowFlags(flags)
        self.StartMainWorkerThread()

    def StartMainWorkerThread(self):
        self.worker = WorkerThread()
        self.worker.start()
        self.worker.finished.connect(self.MainWorker_Finished)
        self.worker.Update_Status.connect(self.MainWorker_Update)

    def MainWorker_Finished(self):
        QMessageBox.information(self,"DONE!", "This shouldnt normally happen!")

    def MainWorker_Update(self,val):
        self.ui.X_Val.setProperty("value", format(val["X"]))
        self.ui.Y_Val.setProperty("value", format(val["Y"]))
        self.ui.Z_Val.setProperty("value", format(val["Z"]))
        if val["Step"] == 1:
            self.ui.Step_1.setEnabled(True)
            self.ui.Step_2.setEnabled(False)
            self.ui.Step_3.setEnabled(False)
            print("step 1")
        elif val["Step"] == 2:
            self.ui.Step_1.setEnabled(False)
            self.ui.Step_2.setEnabled(True)
            self.ui.Step_3.setEnabled(False)
            print("step 2")
        elif val["Step"] == 3:
            self.ui.Step_1.setEnabled(False)
            self.ui.Step_2.setEnabled(False)
            self.ui.Step_3.setEnabled(True)
            print("step 3")
        print("Done")

class WorkerThread(QThread):
    tsc = src.adafruit_tsc2007.TSC2007(i2c, irq=irq_dio)
    Update_Status = pyqtSignal(dict)
    Status_Dict = {"X":0,"Y":0,"Z":0,"Step":1}
    def run(self):
        while(1):       
            if self.tsc.touched:
                point = self.tsc.touch
                self.Status_Dict["X"] = point["x"]
                self.Status_Dict["Y"] = point["y"]
                self.Status_Dict["Z"] = point["z"]
                print("Touchpoint: (%d, %d, %d)" % (point["x"], point["y"], point["pressure"]))
                if (time.time() - self.NoTouchTime) > 10:
                    self.Status_Dict["Step"] = self.Status_Dict["Step"] + 1
                self.Update_Status.emit(self.Status_Dict)
            else:
                self.NoTouchTime = time.time()
            time.sleep(.2)
            #self.Update_Status.emit(self.Status_Dict)

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        w = ScreenCal_UI()
        w.show()
        app.exec()
    except KeyboardInterrupt:
        print('interrupted!')
        app.quit()