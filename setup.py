# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QApplication
from main import Ui_MainWindow
from get_config import Ui_Form
from PyQt5.QtWidgets import *  # PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
import PyQt5.QtGui as QtGui
import sys
from main import *
from method import *


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.onClicked)
        # self.ChildDialog = Child()
        self.flag = 0
        self.label_list = [
                        self.label_1_state,
                        self.label_2_state,
                        self.label_3_state,
                        self.label_4_state,
                        self.label_5_state,
                        self.label_6_state,
                        self.label_7_state,
                        self.label_8_state,
                        self.label_9_state,
                        self.label_10_state
                      ]

    def onClicked(self):
        try:
            if 'COM4' in get_serial():
                PortName = 'COM4'
            if self.flag != 0:
                self.label_list[self.flag - 1].setStyleSheet(m_grey_SheetStyle)
            if self.flag == 10:
                self.flag = 0
            cmd, res = test(PortName, self.flag)
            if res == "Pass":
                self.textEdit.append(str(cmd) + " " + str(res))
                self.label_list[self.flag].setStyleSheet(m_green_SheetStyle)
            else:
                self.textEdit.append(str(cmd) + " Fail!!!!!")
                self.label_list[self.flag].setStyleSheet(m_red_SheetStyle)
            self.flag += 1
        except:
            self.textEdit.append("找不到串口")



# class Child(QMainWindow, Ui_Form):
#     def __init__(self):
#         super(Child, self).__init__()
#         self.setupUi(self)
#         #self.pushButton.clicked.connect(self.save_json)
#
#     def OPEN(self):
#         self.show()
#
#     #def save_json(self):


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    # ch = Child()
    main.show()
    # main.push_getconfig.clicked.connect(ch.OPEN)
    sys.exit(app.exec_())
