# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_win.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SettingsWin(object):
    def setupUi(self, SettingsWin):
        if not SettingsWin.objectName():
            SettingsWin.setObjectName(u"SettingsWin")
        SettingsWin.resize(699, 331)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        SettingsWin.setFont(font)
        self.gridLayout = QGridLayout(SettingsWin)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 65, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(SettingsWin)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.buttonLoadBad = QPushButton(SettingsWin)
        self.buttonLoadBad.setObjectName(u"buttonLoadBad")

        self.horizontalLayout.addWidget(self.buttonLoadBad)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 66, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(SettingsWin)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.buttonLoadGood = QPushButton(SettingsWin)
        self.buttonLoadGood.setObjectName(u"buttonLoadGood")

        self.horizontalLayout_2.addWidget(self.buttonLoadGood)


        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 65, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 4, 1, 1, 1)


        self.retranslateUi(SettingsWin)

        QMetaObject.connectSlotsByName(SettingsWin)
    # setupUi

    def retranslateUi(self, SettingsWin):
        SettingsWin.setWindowTitle(QCoreApplication.translate("SettingsWin", u"Settings", None))
        self.label.setText(QCoreApplication.translate("SettingsWin", u"\u0421\u043a\u0440\u0438\u043f\u0442 \u0434\u043b\u044f \"\u043d\u0435\u0433\u0430\u0442\u0438\u0432\u043d\u043e\u0433\u043e\" \u043f\u0438\u0441\u044c\u043c\u0430", None))
        self.buttonLoadBad.setText(QCoreApplication.translate("SettingsWin", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("SettingsWin", u"\u0421\u043a\u0440\u0438\u043f\u0442 \u0434\u043b\u044f \"\u043f\u043e\u043b\u043e\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0433\u043e\" \u043f\u0438\u0441\u044c\u043c\u0430", None))
        self.buttonLoadGood.setText(QCoreApplication.translate("SettingsWin", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
    # retranslateUi

