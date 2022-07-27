from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from test_run import Ui_RootPendant_Main
import sys
import time


class RootPendant_Main(QMainWindow):


    def __init__(self):
        super().__init__()
        self.ui = Ui_RootPendant_Main()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.test_1)
        self.ui.Close.clicked.connect(self.Close)
        self.StartMainWorkerThread()

    def test_1(self):
        print("button has been pressed")
        self.ui.DRO_X_M.setProperty("value", 9120.3456)
        self.ui.DRO_X_WCO.setProperty("value", 9120.3456)

    def Close(self):
        self.close()
    
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
#        if format(val["Status"]) == "Not Connected":
#            
#            Palette= QPalette()
#            Palette.setColor(QPalette.window, QColor(50,50,50,50))
#            self.ui.STATUS.setPalette(Palette)
#            #Self.ui.setColor(QPalette::Button, QColor("#ffffff"));
#        elif format(val["Status"]) == "Connected":
#            Palette= QPalette()
#            Palette.setColor(QPalette.window, Qt.green)
#            self.ui.STATUS.setPalette(Palette)
#       case "Run":
#       case "Hold":
#       case "Stop":
#       case "Alarm":
#       case "Error":
#       case "Probe":
#       case "Home":
#       case _:
#           


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