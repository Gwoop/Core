import sys
import requests


from ui.Main import Ui_MainWindow

from PyQt6 import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.click1)

    def click1(self):
        url = "https://github.com/TemaTerbi/YtDownloader2.0"
        resp = requests.get(url)
        self.ui.label.setText(resp.text)

if __name__ == "__main__":


    app = QtWidgets.QApplication([])
    application = MainWindow()
    window = QtWidgets.QMainWindow()
    application.show()
    sys.exit(app.exec())