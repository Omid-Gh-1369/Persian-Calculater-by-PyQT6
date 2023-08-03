from PyQt6 import QtCore, QtGui, QtWidgets


class Clac(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.flag = 0
        self.text_clac = ""
        Calc.setObjectName("Calc")
        Calc.resize(310, 400)
        Calc.setMinimumSize(QtCore.QSize(310, 400))
        Calc.setMaximumSize(QtCore.QSize(310, 400))
        font = QtGui.QFont()
        font.setFamily("Mj_Newspaper")
        Calc.setFont(font)
        Calc.setStyleSheet("background-color: rgb(53, 53, 53)")
        self.centralwidget = QtWidgets.QWidget(parent=Calc)
        self.centralwidget.setObjectName("centralwidget")
        self.intvalid = QtGui.QIntValidator()

        self.btn0 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn0.setGeometry(QtCore.QRect(110, 320, 40, 40))
        font = QtGui.QFont()
        font.setFamily("IPT Koodak")
        font.setPointSize(20)
        self.btn0.setFont(font)
        self.btn0.setObjectName("btn0")
        self.btn0.clicked.connect(self.send_0)

        self.btn1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(50, 280, 40, 40))
        font = QtGui.QFont()
        font.setFamily("IPT Koodak")
        font.setPointSize(20)
        self.btn1.setFont(font)
        self.btn1.setObjectName("btn1")
        self.btn1.clicked.connect(self.send_1)

        self.btn2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(110, 280, 40, 40))
        font = QtGui.QFont()
        font.setFamily("IPT Koodak")
        font.setPointSize(20)
        self.btn2.setFont(font)
        self.btn2.setObjectName("btn2")
        self.btn2.clicked.connect(self.send_2)

        self.btn3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(170, 280, 40, 40))
        font = QtGui.QFont()
        font.setFamily("IPT Koodak")
        font.setPointSize(20)
        self.btn3.setFont(font)
        self.btn3.setObjectName("btn3")
        self.btn3.clicked.connect(self.send_3)

        self.btn4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(50, 240, 40, 40))
        font = QtGui.QFont()
        font.setFamily("IPT Koodak")
        font.setPointSize(20)
        self.btn4.setFont(font)
        self.btn4.setObjectName("btn4")
        self.btn4.clicked.connect(self.send_4)

        self.btn5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn5.setGeometry(QtCore.QRect(110, 240, 40, 40))
        font = QtGui.QFont()
        font.setFamily("IPT Koodak")
        font.setPointSize(20)
        self.btn5.setFont(font)
        self.btn5.setObjectName("btn5")
        self.btn5.clicked.connect(self.send_5)

        self.btn6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn6.setGeometry(QtCore.QRect(170, 240, 40, 40))
        font = QtGui.QFont()
        font.setFamily("IPT Koodak")
        font.setPointSize(20)
        self.btn6.setFont(font)
        self.btn6.setObjectName("btn6")
        self.btn6.clicked.connect(self.send_6)

        self.btn7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn7.setGeometry(QtCore.QRect(50, 200, 40, 40))
        font = QtGui.QFont()
        font.setFamily("IPT Koodak")
        font.setPointSize(20)
        self.btn7.setFont(font)
        self.btn7.setObjectName("btn7")
        self.btn7.clicked.connect(self.send_7)

        self.btn8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn8.setGeometry(QtCore.QRect(110, 200, 40, 40))
        font = QtGui.QFont()
        font.setFamily("IPT Koodak")
        font.setPointSize(20)
        self.btn8.setFont(font)
        self.btn8.setObjectName("btn8")
        self.btn8.clicked.connect(self.send_8)

        self.btn9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn9.setGeometry(QtCore.QRect(170, 200, 40, 40))
        font = QtGui.QFont()
        font.setFamily("IPT Koodak")
        font.setPointSize(20)
        self.btn9.setFont(font)
        self.btn9.setObjectName("btn9")
        self.btn9.clicked.connect(self.send_9)

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 261, 55))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font=QtGui.QFont()
        font.setFamily("IPT Koodak")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(30, 120, 261, 41))
        self.label2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font=QtGui.QFont()
        font.setFamily("Mj_Newspaper")
        font.setPointSize(20)
        self.label2.setFont(font)
        self.label2.setStyleSheet("color:rgb(70, 70, 70)")
        self.label2.setObjectName("label2")

        self.dot_ = QtWidgets.QPushButton(parent=self.centralwidget)
        self.dot_.setGeometry(QtCore.QRect(170, 320, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.dot_.setFont(font)
        self.dot_.setObjectName("dot_")
        self.dot_.clicked.connect(self.send_dot)

        self.AC = QtWidgets.QPushButton(parent=self.centralwidget)
        self.AC.setGeometry(QtCore.QRect(50, 160, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(50)
        self.AC.setFont(font)
        self.AC.setObjectName("AC")
        self.AC.clicked.connect(self.Ac)

        self.back_space = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back_space.setGeometry(QtCore.QRect(110, 160, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(50)
        self.back_space.setFont(font)
        self.back_space.setObjectName("backspace")
        self.back_space.clicked.connect(self.back_space_)

        self.div_dec = QtWidgets.QPushButton(parent=self.centralwidget)
        self.div_dec.setGeometry(QtCore.QRect(170, 160, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(50)
        self.div_dec.setFont(font)
        self.div_dec.setObjectName("div_dec")
        self.div_dec.clicked.connect(self.div_dec_)

        self.plus = QtWidgets.QPushButton(parent=self.centralwidget)
        self.plus.setGeometry(QtCore.QRect(230, 160, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(50)
        self.plus.setFont(font)
        self.plus.setObjectName("plus")
        self.plus.clicked.connect(self.plus_)

        self.sub = QtWidgets.QPushButton(parent=self.centralwidget)
        self.sub.setGeometry(QtCore.QRect(230, 200, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(50)
        self.sub.setFont(font)
        self.sub.setObjectName("sub")
        self.sub.clicked.connect(self.sub_)

        self.mul = QtWidgets.QPushButton(parent=self.centralwidget)
        self.mul.setGeometry(QtCore.QRect(230, 240, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(50)
        self.mul.setFont(font)
        self.mul.setObjectName("mul_")
        self.mul.clicked.connect(self.mul_)

        self.power_ = QtWidgets.QPushButton(parent=self.centralwidget)
        self.power_.setGeometry(QtCore.QRect(230, 280, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(50)
        self.power_.setFont(font)
        self.power_.setObjectName("power_")
        self.power_.clicked.connect(self.powerr_)


        self.equal = QtWidgets.QPushButton(parent=self.centralwidget)
        self.equal.setGeometry(QtCore.QRect(230, 320, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(50)
        self.equal.setFont(font)
        self.equal.setObjectName("equal")
        self.equal.clicked.connect(self.equ)

        self.input = QtWidgets.QLineEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("B Karim")
        font.setPointSize(40)
        font.setBold(True)
        self.input.setFont(font)
        self.input.setValidator(self.intvalid)
        self.input.setGeometry(QtCore.QRect(20, 20, 261, 41))
        self.input.setFrame(False)
        self.input.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.input.setObjectName("input")

        Calc.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Calc)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        Calc.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Calc)
        self.statusbar.setObjectName("statusbar")
        Calc.setStatusBar(self.statusbar)

        self.retranslateUi(Calc)
        QtCore.QMetaObject.connectSlotsByName(Calc)

    def retranslateUi(self, Calc):
        sending = QtCore.QCoreApplication.translate
        Calc.setWindowTitle(sending("Calc", 'Calculater By "OMID-GH"'))
        self.btn0.setText(sending("Calc", "0"))
        self.btn1.setText(sending("Calc", "1"))
        self.btn2.setText(sending("Calc", "2"))
        self.btn3.setText(sending("Calc", "3"))
        self.btn4.setText(sending("Calc", "4"))
        self.btn5.setText(sending("Calc", "5"))
        self.btn6.setText(sending("Calc", "6"))
        self.btn7.setText(sending("Calc", "7"))
        self.btn8.setText(sending("Calc", "8"))
        self.btn9.setText(sending("Calc", "9"))
        self.dot_.setText(sending("Calc", "."))
        self.label.setText(sending("Calc", ""))
        self.label2.setText(sending("Calc", "Create By OMID-GH"))
        self.AC.setText(sending("Calc", "AC"))
        self.back_space.setText(sending("Calc", "->"))
        self.power_.setText(sending("Calc", "^"))
        self.div_dec.setText(sending("Calc", "/"))
        self.sub.setText(sending("Calc", "-"))
        self.plus.setText(sending("Calc", "+"))
        self.equal.setText(sending("Calc", "="))
        self.mul.setText(sending("Calc", "×"))
        self.input.setPlaceholderText(sending("Calc", "عدد را وارد کنید"))

    def send_0(self):
        if self.input.text == "":
            self.input.setText("0")
        else:
            text = self.input.text()
            text += "0"
            self.input.setText(text)

    def send_1(self):
        if self.input.text == "":
            self.input.setText("1")
        else:
            text = self.input.text()
            text += "1"
            self.input.setText(text)

    def send_2(self):
        if self.input.text == "":
            self.input.setText("2")
        else:
            text = self.input.text()
            text += "2"
            self.input.setText(text)

    def send_3(self):
        if self.input.text == "":
            self.input.setText("3")
        else:
            text = self.input.text()
            text += "3"
            self.input.setText(text)

    def send_4(self):
        if self.input.text == "":
            self.input.setText("4")
        else:
            text = self.input.text()
            text += "4"
            self.input.setText(text)

    def send_5(self):
        if self.input.text == "":
            self.input.setText("5")
        else:
            text = self.input.text()
            text += "5"
            self.input.setText(text)

    def send_6(self):
        if self.input.text == "":
            self.input.setText("6")
        else:
            text = self.input.text()
            text += "6"
            self.input.setText(text)

    def send_7(self):
        if self.input.text == "":
            self.input.setText("7")
        else:
            text = self.input.text()
            text += "7"
            self.input.setText(text)

    def send_8(self):
        if self.input.text == "":
            self.input.setText("8")
        else:
            text = self.input.text()
            text += "8"
            self.input.setText(text)

    def send_9(self):
        if self.input.text == "":
            self.input.setText("9")
        else:
            text = self.input.text()
            text += "9"
            self.input.setText(text)

    def send_dot(self):
        text_input = self.input.text()
        if "." in text_input:
            pass
        elif text_input == "":
            self.input.setText(".")
        else:
            text = text_input
            text += "."
            self.input.setText(text)

    def Ac(self):
        self.input.clear()

    def back_space_(self):
        text_input = self.input.text()
        if text_input == "":
            pass
        else:
            len_text = len(text_input)
            text = text_input[:len_text-1]
            self.input.setText(text)

    def plus_(self):
        self.text_calc = self.input.text()
        if self.text_calc == "":
            pass
        else:
            self.text_calc = float(self.input.text())
            self.flag = 1
            self.input.clear()

    def sub_(self):
        self.text_calc = self.input.text()
        if self.text_calc == "":
            pass
        else:
            self.text_calc = float(self.input.text())
            self.flag = 2
            self.input.clear()

    def mul_(self):
        self.text_calc = self.input.text()
        if self.text_calc == "":
            pass
        else:
            self.text_calc = float(self.input.text())
            self.flag = 3
            self.input.clear()

    def div_dec_(self):
        self.text_calc = self.input.text()
        if self.text_calc == "":
            pass
        else:
            self.text_calc = float(self.input.text())
            self.flag = 4
            self.input.clear()

    def powerr_(self):
        self.text_calc = self.input.text()
        if self.text_calc == "":
            pass
        else:
            self.text_calc = float(self.input.text())
            self.flag = 5
            self.input.clear()

    def equ(self):
        self.label.clear()
        self.text_input = self.input.text()
        if self.text_input == "":
            self.label.setText (self.text_calc)
            self.input.clear()
        if self.flag == 1:
            self.label.setText(str( float(self.text_calc) + float(self.text_input)))
            self.input.clear()
        elif self.flag == 2:
            self.label.setText(str(float(self.text_calc) - float(self.text_input)))
            self.input.clear()
        elif self.flag == 3:
            self.label.setText(str(float(self.text_calc) * float(self.text_input)))
            self.input.clear()
        elif self.flag == 4:
            self.label.setText(str(float(self.text_calc) / float(self.text_input)))
            self.input.clear()
        elif self.flag == 5:
            self.label.setText(str(float(self.text_calc) ** float(self.text_input)))
            self.input.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calc = QtWidgets.QMainWindow()
    ui = Clac()
    Calc.show()
    sys.exit(app.exec())
