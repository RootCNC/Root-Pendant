from test_run import Ui_RootPendant_Main
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc


class RootPendant_Main(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__ (*args, **kwargs)

        self.ui = Ui_RootPendant_Main()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.test_1)

    def test_1(self):
        print("button has been pressed")


if __name__ == "__main__":
    import sys
    app = qtw.QApplication(sys.argv)

    widget = RootPendant_Main()
    widget.show()

    sys.exit(app.exec_())


