# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_win.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWinLetter(object):
    def setupUi(self, MainWinLetter):
        if not MainWinLetter.objectName():
            MainWinLetter.setObjectName(u"MainWinLetter")
        MainWinLetter.resize(800, 600)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        MainWinLetter.setFont(font)
        self.actionOpen = QAction(MainWinLetter)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWinLetter)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_as = QAction(MainWinLetter)
        self.actionSave_as.setObjectName(u"actionSave_as")
        self.actionSettings = QAction(MainWinLetter)
        self.actionSettings.setObjectName(u"actionSettings")
        self.centralwidget = QWidget(MainWinLetter)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineStudentsNum = QLineEdit(self.centralwidget)
        self.lineStudentsNum.setObjectName(u"lineStudentsNum")
        self.lineStudentsNum.setFrame(False)
        self.lineStudentsNum.setAlignment(Qt.AlignCenter)
        self.lineStudentsNum.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineStudentsNum)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioSaveTXT = QRadioButton(self.centralwidget)
        self.radioSaveTXT.setObjectName(u"radioSaveTXT")
        self.radioSaveTXT.setChecked(True)

        self.verticalLayout.addWidget(self.radioSaveTXT)

        self.radioSaveDOCX = QRadioButton(self.centralwidget)
        self.radioSaveDOCX.setObjectName(u"radioSaveDOCX")

        self.verticalLayout.addWidget(self.radioSaveDOCX)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.buttonSaveLetters = QPushButton(self.centralwidget)
        self.buttonSaveLetters.setObjectName(u"buttonSaveLetters")

        self.verticalLayout_3.addWidget(self.buttonSaveLetters)

        self.buttonReloadLetters = QPushButton(self.centralwidget)
        self.buttonReloadLetters.setObjectName(u"buttonReloadLetters")

        self.verticalLayout_3.addWidget(self.buttonReloadLetters)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.textStudentsList = QTextEdit(self.centralwidget)
        self.textStudentsList.setObjectName(u"textStudentsList")
        self.textStudentsList.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.textStudentsList)


        self.gridLayout.addLayout(self.verticalLayout_2, 2, 0, 1, 1)

        MainWinLetter.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWinLetter)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 38))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWinLetter.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWinLetter)
        self.statusbar.setObjectName(u"statusbar")
        MainWinLetter.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSettings)

        self.retranslateUi(MainWinLetter)

        QMetaObject.connectSlotsByName(MainWinLetter)
    # setupUi

    def retranslateUi(self, MainWinLetter):
        MainWinLetter.setWindowTitle(QCoreApplication.translate("MainWinLetter", u"Auto School Letter", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWinLetter", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWinLetter", u"Save", None))
        self.actionSave_as.setText(QCoreApplication.translate("MainWinLetter", u"Save as", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWinLetter", u"Settings", None))
        self.label.setText(QCoreApplication.translate("MainWinLetter", u"\u041a\u043e\u043b-\u0432\u043e \u0443\u0447\u0435\u043d\u0438\u043a\u043e\u0432 \u0432 \u0444\u0430\u0439\u043b\u0435: ", None))
        self.radioSaveTXT.setText(QCoreApplication.translate("MainWinLetter", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c *.txt", None))
        self.radioSaveDOCX.setText(QCoreApplication.translate("MainWinLetter", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c *.docx", None))
        self.buttonSaveLetters.setText(QCoreApplication.translate("MainWinLetter", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u041f\u0438\u0441\u044c\u043c\u0430", None))
        self.buttonReloadLetters.setText(QCoreApplication.translate("MainWinLetter", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0421\u043a\u0440\u0438\u043f\u0442\u044b", None))
        self.label_2.setText(QCoreApplication.translate("MainWinLetter", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0443\u0447\u0435\u043d\u0438\u043a\u043e\u0432:", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWinLetter", u"File", None))
    # retranslateUi

