# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Mon Mar 24 16:04:41 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(492, 427)
        self.pushButton_stream_webcam = QtGui.QPushButton(Form)
        self.pushButton_stream_webcam.setGeometry(QtCore.QRect(270, 300, 141, 71))
        self.pushButton_stream_webcam.setObjectName(_fromUtf8("pushButton_stream_webcam"))
        self.horizontalSlider_fps = QtGui.QSlider(Form)
        self.horizontalSlider_fps.setGeometry(QtCore.QRect(110, 350, 141, 29))
        self.horizontalSlider_fps.setMinimum(1)
        self.horizontalSlider_fps.setMaximum(1024)
        self.horizontalSlider_fps.setProperty("value", 50)
        self.horizontalSlider_fps.setSliderPosition(50)
        self.horizontalSlider_fps.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_fps.setObjectName(_fromUtf8("horizontalSlider_fps"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(70, 310, 31, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lcdNumber = QtGui.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(120, 300, 131, 41))
        self.lcdNumber.setProperty("value", 50.0)
        self.lcdNumber.setProperty("intValue", 50)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(50, 20, 541, 261))
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayoutWidget = QtGui.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 30, 371, 221))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lcdNumber_green = QtGui.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_green.setNumDigits(3)
        self.lcdNumber_green.setProperty("value", 100.0)
        self.lcdNumber_green.setObjectName(_fromUtf8("lcdNumber_green"))
        self.gridLayout.addWidget(self.lcdNumber_green, 1, 1, 1, 1)
        self.verticalSlider_blue = QtGui.QSlider(self.gridLayoutWidget)
        self.verticalSlider_blue.setMaximum(100)
        self.verticalSlider_blue.setProperty("value", 100)
        self.verticalSlider_blue.setSliderPosition(100)
        self.verticalSlider_blue.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_blue.setObjectName(_fromUtf8("verticalSlider_blue"))
        self.gridLayout.addWidget(self.verticalSlider_blue, 0, 2, 1, 1)
        self.verticalSlider_green = QtGui.QSlider(self.gridLayoutWidget)
        self.verticalSlider_green.setMaximum(100)
        self.verticalSlider_green.setSliderPosition(100)
        self.verticalSlider_green.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_green.setObjectName(_fromUtf8("verticalSlider_green"))
        self.gridLayout.addWidget(self.verticalSlider_green, 0, 1, 1, 1)
        self.verticalSlider_red = QtGui.QSlider(self.gridLayoutWidget)
        self.verticalSlider_red.setMaximum(100)
        self.verticalSlider_red.setSliderPosition(100)
        self.verticalSlider_red.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_red.setObjectName(_fromUtf8("verticalSlider_red"))
        self.gridLayout.addWidget(self.verticalSlider_red, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)
        self.lcdNumber_red = QtGui.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_red.setMinimumSize(QtCore.QSize(0, 25))
        self.lcdNumber_red.setNumDigits(3)
        self.lcdNumber_red.setProperty("value", 100.0)
        self.lcdNumber_red.setObjectName(_fromUtf8("lcdNumber_red"))
        self.gridLayout.addWidget(self.lcdNumber_red, 1, 0, 1, 1)
        self.lcdNumber_blue = QtGui.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_blue.setNumDigits(3)
        self.lcdNumber_blue.setProperty("value", 100.0)
        self.lcdNumber_blue.setObjectName(_fromUtf8("lcdNumber_blue"))
        self.gridLayout.addWidget(self.lcdNumber_blue, 1, 2, 1, 1)
        self.verticalSlider_brightness = QtGui.QSlider(self.gridLayoutWidget)
        self.verticalSlider_brightness.setMaximum(100)
        self.verticalSlider_brightness.setProperty("value", 100)
        self.verticalSlider_brightness.setSliderPosition(100)
        self.verticalSlider_brightness.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_brightness.setObjectName(_fromUtf8("verticalSlider_brightness"))
        self.gridLayout.addWidget(self.verticalSlider_brightness, 0, 3, 1, 1)
        self.lcdNumber_brightness = QtGui.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_brightness.setNumDigits(3)
        self.lcdNumber_brightness.setProperty("value", 100.0)
        self.lcdNumber_brightness.setProperty("intValue", 100)
        self.lcdNumber_brightness.setObjectName(_fromUtf8("lcdNumber_brightness"))
        self.gridLayout.addWidget(self.lcdNumber_brightness, 1, 3, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 2, 3, 1, 1)
        self.verticalSlider_gamma = QtGui.QSlider(self.gridLayoutWidget)
        self.verticalSlider_gamma.setMaximum(400)
        self.verticalSlider_gamma.setProperty("value", 100)
        self.verticalSlider_gamma.setSliderPosition(100)
        self.verticalSlider_gamma.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_gamma.setObjectName(_fromUtf8("verticalSlider_gamma"))
        self.gridLayout.addWidget(self.verticalSlider_gamma, 0, 4, 1, 1)
        self.lcdNumber_gamma = QtGui.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_gamma.setNumDigits(3)
        self.lcdNumber_gamma.setProperty("value", 100.0)
        self.lcdNumber_gamma.setProperty("intValue", 100)
        self.lcdNumber_gamma.setObjectName(_fromUtf8("lcdNumber_gamma"))
        self.gridLayout.addWidget(self.lcdNumber_gamma, 1, 4, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 4, 1, 1)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.horizontalSlider_fps, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdNumber.display)
        QtCore.QObject.connect(self.verticalSlider_red, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdNumber_red.display)
        QtCore.QObject.connect(self.verticalSlider_green, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdNumber_green.display)
        QtCore.QObject.connect(self.verticalSlider_blue, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdNumber_blue.display)
        QtCore.QObject.connect(self.verticalSlider_gamma, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdNumber_gamma.display)
        QtCore.QObject.connect(self.verticalSlider_brightness, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdNumber_brightness.display)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Mate Light TV", None))
        self.pushButton_stream_webcam.setText(_translate("Form", "Webcam streamen", None))
        self.label_4.setText(_translate("Form", "FPS", None))
        self.groupBox.setTitle(_translate("Form", "color correction", None))
        self.label_2.setText(_translate("Form", "Green", None))
        self.label.setText(_translate("Form", "Red", None))
        self.label_3.setText(_translate("Form", "Blue", None))
        self.label_6.setText(_translate("Form", "Brightness", None))
        self.label_5.setText(_translate("Form", "Gamma", None))

