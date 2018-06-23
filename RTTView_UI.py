# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RTTView.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_RTTView(object):
    def setupUi(self, RTTView):
        RTTView.setObjectName(_fromUtf8("RTTView"))
        RTTView.resize(594, 466)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RTTView.sizePolicy().hasHeightForWidth())
        RTTView.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Image/serial.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        RTTView.setWindowIcon(icon)
        self.vLayout0 = QtGui.QVBoxLayout(RTTView)
        self.vLayout0.setObjectName(_fromUtf8("vLayout0"))
        self.txtMain = QtGui.QTextEdit(RTTView)
        self.txtMain.setFrameShadow(QtGui.QFrame.Sunken)
        self.txtMain.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.txtMain.setObjectName(_fromUtf8("txtMain"))
        self.vLayout0.addWidget(self.txtMain)
        self.hLayout1 = QtGui.QHBoxLayout()
        self.hLayout1.setObjectName(_fromUtf8("hLayout1"))
        self.lblDAP = QtGui.QLabel(RTTView)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDAP.sizePolicy().hasHeightForWidth())
        self.lblDAP.setSizePolicy(sizePolicy)
        self.lblDAP.setObjectName(_fromUtf8("lblDAP"))
        self.hLayout1.addWidget(self.lblDAP)
        self.linDAP = QtGui.QLineEdit(RTTView)
        self.linDAP.setEnabled(False)
        self.linDAP.setObjectName(_fromUtf8("linDAP"))
        self.hLayout1.addWidget(self.linDAP)
        self.btnDAP = QtGui.QPushButton(RTTView)
        self.btnDAP.setEnabled(False)
        self.btnDAP.setObjectName(_fromUtf8("btnDAP"))
        self.hLayout1.addWidget(self.btnDAP)
        self.vLayout0.addLayout(self.hLayout1)
        self.hLayout2 = QtGui.QHBoxLayout()
        self.hLayout2.setObjectName(_fromUtf8("hLayout2"))
        self.lblMap = QtGui.QLabel(RTTView)
        self.lblMap.setObjectName(_fromUtf8("lblMap"))
        self.hLayout2.addWidget(self.lblMap)
        self.cmbMap = QtGui.QComboBox(RTTView)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbMap.sizePolicy().hasHeightForWidth())
        self.cmbMap.setSizePolicy(sizePolicy)
        self.cmbMap.setObjectName(_fromUtf8("cmbMap"))
        self.hLayout2.addWidget(self.cmbMap)
        self.btnMap = QtGui.QPushButton(RTTView)
        self.btnMap.setObjectName(_fromUtf8("btnMap"))
        self.hLayout2.addWidget(self.btnMap)
        self.vLayout0.addLayout(self.hLayout2)
        self.hLayout3 = QtGui.QHBoxLayout()
        self.hLayout3.setObjectName(_fromUtf8("hLayout3"))
        self.btnClear = QtGui.QPushButton(RTTView)
        self.btnClear.setObjectName(_fromUtf8("btnClear"))
        self.hLayout3.addWidget(self.btnClear)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hLayout3.addItem(spacerItem)
        self.lblOpen = QtGui.QLabel(RTTView)
        self.lblOpen.setText(_fromUtf8(""))
        self.lblOpen.setPixmap(QtGui.QPixmap(_fromUtf8("Image/inclosing.png")))
        self.lblOpen.setObjectName(_fromUtf8("lblOpen"))
        self.hLayout3.addWidget(self.lblOpen)
        self.btnOpen = QtGui.QPushButton(RTTView)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOpen.sizePolicy().hasHeightForWidth())
        self.btnOpen.setSizePolicy(sizePolicy)
        self.btnOpen.setMinimumSize(QtCore.QSize(104, 0))
        self.btnOpen.setCheckable(False)
        self.btnOpen.setObjectName(_fromUtf8("btnOpen"))
        self.hLayout3.addWidget(self.btnOpen)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.hLayout3.addItem(spacerItem1)
        self.cmbMode = QtGui.QComboBox(RTTView)
        self.cmbMode.setObjectName(_fromUtf8("cmbMode"))
        self.cmbMode.addItem(_fromUtf8(""))
        self.cmbMode.addItem(_fromUtf8(""))
        self.hLayout3.addWidget(self.cmbMode)
        self.vLayout0.addLayout(self.hLayout3)

        self.retranslateUi(RTTView)
        QtCore.QMetaObject.connectSlotsByName(RTTView)

    def retranslateUi(self, RTTView):
        RTTView.setWindowTitle(_translate("RTTView", "XIVN1987 SEGGER-RTT Viewer by DAPLink", None))
        self.lblDAP.setText(_translate("RTTView", "CMSIS-DAP 仿真器：", None))
        self.btnDAP.setText(_translate("RTTView", "...", None))
        self.lblMap.setText(_translate("RTTView", "项目.map文件路径：", None))
        self.btnMap.setText(_translate("RTTView", "...", None))
        self.btnClear.setText(_translate("RTTView", "清除", None))
        self.btnOpen.setText(_translate("RTTView", "打开连接", None))
        self.cmbMode.setItemText(0, _translate("RTTView", "文本", None))
        self.cmbMode.setItemText(1, _translate("RTTView", "波形", None))

