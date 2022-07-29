from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from test_1 import Ui_RootPendant_Main
import sys
import time


class RootPendant_Main(QMainWindow):


    def __init__(self):
        super().__init__()
        self.ui = Ui_RootPendant_Main()
        self.ui.setupUi(self)
        self.ui.MenuBtn.clicked.connect(self.SlideLeftMenu)
        self.ui.FilesBtn.clicked.connect(self.FilesRightMenu)
        self.ui.RootBtn.clicked.connect(self.Close)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.StartMainWorkerThread()

    def Close(self):
        self.close()

    def SlideLeftMenu(self):
        Duration=0
        pos = self.ui.SettingsFrame.pos()
        NewPos = pos
        if pos.x() < -50:
            NewPos.setX(0)
        else:
            NewPos.setX(-240)

        #if self.FilesRightMenu_IsShown(self): self.FilesRightMenu(self)
        
        print("OlD ", pos.x(),"Files Menu New Pos", NewPos.x())
        if Duration == 0: Duration=300

        self.animation = QPropertyAnimation(self.ui.SettingsFrame, b"pos")
        self.animation.setDuration(Duration)
        #   self.animation.setStartValue(pos)
        self.animation.setEndValue(NewPos)
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.start()

    def FilesRightMenu_IsShown(self):
        pos = self.ui.FileFrame.pos()
        if pos.x() > 50:
            print("Right Menu is NOT Shown")
            return False
        else:
            print("Right Menu is Shown")
            self.FilesRightMenuClose()
            return True

    def SettingsFrame_IsShown(self):
        if self.ui.SettingsFrame.width() > 50:
            return True
        else:
            return False

    def FilesRightMenu(self):
        Duration=0
        pos = self.ui.FileFrame.pos()
        NewPos = pos
        if pos.x() > 50:
            NewPos.setX(0)
        else:
            NewPos.setX(240)
        
        print("OlD ", pos.x(),"Files Menu New Pos", NewPos.x())
        if Duration == 0: Duration=300

        self.animation = QPropertyAnimation(self.ui.FileFrame, b"pos")
        self.animation.setDuration(Duration)
        #   self.animation.setStartValue(pos)
        self.animation.setEndValue(NewPos)
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.start()

    def StartMainWorkerThread(self):
        self.worker = WorkerThread()
        self.worker.start()
        self.worker.finished.connect(self.MainWorker_Finished)
        self.worker.Update_Status.connect(self.MainWorker_Update)

    def MainWorker_Finished(self):
        QMessageBox.information(self,"DONE!", "This shouldnt normally happen!")

    def MainWorker_Update(self,val):
        self.ui.DRO_X_M.setProperty("value", format(val["X_M"]))
        self.ui.DRO_X_WCO.setProperty("value", format(val["X_WCO"]))
        self.ui.DRO_Y_M.setProperty("value", format(val["Y_M"]))
        self.ui.DRO_Y_WCO.setProperty("value", format(val["Y_WCO"]))
        self.ui.DRO_Z_M.setProperty("value", format(val["Z_M"]))
        self.ui.DRO_Z_WCO.setProperty("value", format(val["Z_WCO"]))
        self.ui.DRO_A_M.setProperty("value", format(val["A_M"]))
        self.ui.DRO_A_WCO.setProperty("value", format(val["A_WCO"]))
        self.ui.DRO_B_M.setProperty("value", format(val["B_M"]))
        self.ui.DRO_B_WCO.setProperty("value", format(val["B_WCO"]))
        self.ui.DRO_C_M.setProperty("value", format(val["C_M"]))
        self.ui.DRO_C_WCO.setProperty("value", format(val["C_WCO"]))
        self.ui.STATUS.setProperty("text", format(val["Status"]))

class WorkerThread(QThread):
    Update_Status = pyqtSignal(dict)
    def run(self):
        x = 0
        Status_List = ["Not Connected", "Connected", "Run", "Hold", "Stop","Alarm","Error","Probe","Home"]
        Status_Dict = {"X_M":x,"X_WCO":x+10, \
                    "Y_M":x+20,"Y_WCO":x+20, \
                    "Z_M":x+30,"Z_WCO":x+30, \
                    "A_M":x+40,"A_WCO":x+40, \
                    "B_M":x+50,"B_WCO":x+50, \
                    "C_M":x+60,"C_WCO":x+60, \
                    "Status":'Not Connected' }
        while(1):
            for item in Status_List:
                for x in range(0,20,1):
                    Status_Dict["X_M"]  =x
                    Status_Dict["X_WCO"]=x+10
                    Status_Dict["Y_M"]  =x+20
                    Status_Dict["Y_WCO"]=x+20
                    Status_Dict["Z_M"]  =x+30
                    Status_Dict["Z_WCO"]=x+30
                    Status_Dict["A_M"]  =x+40
                    Status_Dict["A_WCO"]=x+40
                    Status_Dict["B_M"]  =x+50
                    Status_Dict["B_WCO"]=x+50
                    Status_Dict["C_M"]  =x+60
                    Status_Dict["C_WCO"]=x+60
                    print(x)
                    self.Update_Status.emit(Status_Dict)
                    time.sleep(.1)
                Status_Dict["Status"]=item
                self.Update_Status.emit(Status_Dict)

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        w = RootPendant_Main()
        w.show()
        app.exec()
    except KeyboardInterrupt:
        print('interrupted!')