# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bundesliga.ui'
#
# Created: Sun Mar 31 19:44:18 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import scorefeeds 

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItems(scorefeeds.league_list)
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.getscores)
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.getdesc)
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def getscores(self):
        active = str(self.comboBox.currentText())
        self.textEdit.setText(scorefeeds.scores(scorefeeds.Leagues[active]))

    def getdesc(self):
        active = str(self.comboBox.currentText())
        self.textEdit.setText(scorefeeds.description(scorefeeds.Leagues[active]))

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Scores", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "Description", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())





