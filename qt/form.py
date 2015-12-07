# -*- coding: utf-8 -*-
 
# Form implementation generated from reading ui file 'form.ui'
#
# Created: Mon Jan 26 01:18:19 2015
#      by: PyQt4 UI code generator 4.10.4
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
 
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(325, 208)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 100, 341, 61))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 150, 301, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.kpixmapregionselectorwidget = KPixmapRegionSelectorWidget(Dialog)
        self.kpixmapregionselectorwidget.setGeometry(QtCore.QRect(-30, -20, 371, 161))
        self.kpixmapregionselectorwidget.setPixmap(QtGui.QPixmap(_fromUtf8("Desktop/IMG_0377.jpg")))
        self.kpixmapregionselectorwidget.setObjectName(_fromUtf8("kpixmapregionselectorwidget"))
 
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
 
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "This form is created with Python and QT.", None))
        self.pushButton.setText(_translate("Dialog", "OK", None))
 
from PyKDE4.kdeui import KPixmapRegionSelectorWidget