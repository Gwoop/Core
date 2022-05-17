import sys
import json
import os
import requests
from PyDMXControl.controllers import uDMXController
from PyDMXControl.profiles.Generic import Dimmer
import configparser


#from dmx import Colour, DMXInterface, DMXLight3Slot, DMXUniverse


from ui.Main import Ui_MainWindow

from PyQt6 import QtCore, QtGui, QtWidgets


config = {}




class Init:

    def dmxmain(self):

        print("dmxmain work!")

        dmx = uDMXController()
        fixture = dmx.add_fixture(Dimmer, name="test")
        fixture.dim(255, 5000) # первое значение интенсивность второе время
        dmx.web_control()
        dmx.debug_control()
        dmx.sleep_till_enter()
        dmx.close()

    def Initconf(self):
        config = configparser.ConfigParser()
        config.read("settings.ini")


    """
    PURPLE = Colour(255, 0, 255)

    with DMXInterface("FT232R") as interface:
        # Создание экземпляра
        universe = DMXUniverse()
        # источник света
        light = DMXLight3Slot(address=8)
        # добавление параметра к дмкс
        universe.add_light(light)

        # обновление интерфейса
        interface.set_frame(universe.serialise())

        # отправка параметров в сеть
        interface.send_update()

        # установка цвета
        light.set_colour(PURPLE)

        interface.set_frame(universe.serialise())
        interface.send_update()
"""




    def is_valid_channel(self,channel):
        """
        проверка на дебила на ввод канала
        """
        try:
            c = int(channel)
            return (c >= 1) and (c <= 512)
        except:
            return False

    def are_valid_values(self,values):
        """
        проверка (как я понял про dmx) RGB (0-255).
        """
        try:
            int_values = map(int, values)
            for v in int_values:
                if (v >= 0) and (v <= 255):
                    continue
                else:
                    return False
        except Exception as ex:
            # print(ex)
            return False
        return True


    """
    херня которая будет отвечать за конфиг файлы сцен для их загрузки, пока это локалка там пока ошибки это на будующее
    """

"""
    def load_rc_file(self):

        if "uDMXrc" in config:
            rcfile = config["uDMXrc"]
        else:
            if os.name == "nt":
                # для винды
                rcfile = os.path.join(os.environ["USERPROFILE"], ".uDMXrc")
            else:
                # для систем лучше винды
                rcfile = os.path.join(os.environ["HOME"], ".uDMXrc")
        try:
            cf = open(rcfile, 'r')
            for line in cf:
                tokens = line.split()


                # A DMX value or values
                elif tokens[0] in ['value', 'values']:
                    # value alias value
                    if len(tokens) >= 3:
                        if are_valid_values(tokens[2:]):
                            add_values(tokens[1], tokens[2:])
                        else:
                            print(line)
                            print("Invalid value(s)")
                    else:
                        print(line)
                        print("Invalid value statement")
                # Something we don't recognize
                else:
                    print(line)
                    print(tokens[0], "is not a recognized resource file statement")
            cf.close()
        except:
            print("Unable to open resource file", rcfile)
            
"""

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.dmxmain = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.click1)
        self.ui.pushButton_7.clicked.connect(self.click7)
        self.ui.comboBox_4.addItem("RGB")
        self.ui.comboBox_3.addItem("DMX")
        self.ui.comboBox_3.addItem("RDM")
        self.ui.comboBox_3.addItem("SPI")
        self.ui.comboBox_5.addItem("250000")
        self.ui.comboBox_6.addItem("0-4")
        self.ui.comboBox.addItem("0-16386")

        #self.ui.comboBox_3.setCurrentText("DMX")

    def click1(self):

        Init.dmxmain(self)

    def click7(self):

        text = self.ui.lineEdit_2.text()

        self.ui.label_21.setText(text)
"""
        url = "https://github.com/TemaTerbi/YtDownloader2.0"
        resp = requests.get(url)
        self.ui.label.setText(resp.text)
"""




    #def selecteditem(self):


if __name__ == "__main__":


    app = QtWidgets.QApplication([])
    application = MainWindow()
    window = QtWidgets.QMainWindow()
    application.show()
    sys.exit(app.exec())