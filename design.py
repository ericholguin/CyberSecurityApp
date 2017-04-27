# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(3400, 742)
        MainWindow.setStyleSheet("background-color: rgb(40, 39, 49);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setStyleSheet("background-color: rgb(44, 42, 48);\n"
"\n"
"\n"
"\n"
"")
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setProperty("tabBarAutoHide", False)
        self.tabWidget.setObjectName("tabWidget")
        self.welcomeTab = QtWidgets.QWidget()
        self.welcomeTab.setObjectName("welcomeTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.welcomeTab)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.appNameLabel = QtWidgets.QLabel(self.welcomeTab)
        font = QtGui.QFont()
        font.setFamily("msbm10")
        font.setPointSize(72)
        font.setBold(False)
        font.setWeight(50)
        self.appNameLabel.setFont(font)
        self.appNameLabel.setStyleSheet("color: rgb(20, 163, 255);")
        self.appNameLabel.setObjectName("appNameLabel")
        self.verticalLayout_2.addWidget(self.appNameLabel, 0, QtCore.Qt.AlignHCenter)
        self.line_263 = QtWidgets.QFrame(self.welcomeTab)
        self.line_263.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_263.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_263.setObjectName("line_263")
        self.verticalLayout_2.addWidget(self.line_263)
        self.versionLabel = QtWidgets.QLabel(self.welcomeTab)
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.versionLabel.setFont(font)
        self.versionLabel.setStyleSheet("color: rgb(20, 163, 255);")
        self.versionLabel.setObjectName("versionLabel")
        self.verticalLayout_2.addWidget(self.versionLabel, 0, QtCore.Qt.AlignHCenter)
        self.line_264 = QtWidgets.QFrame(self.welcomeTab)
        self.line_264.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_264.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_264.setObjectName("line_264")
        self.verticalLayout_2.addWidget(self.line_264)
        self.descLabel = QtWidgets.QLabel(self.welcomeTab)
        font = QtGui.QFont()
        font.setFamily("msbm10")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.descLabel.setFont(font)
        self.descLabel.setStyleSheet("color: rgb(20, 163, 255);")
        self.descLabel.setObjectName("descLabel")
        self.verticalLayout_2.addWidget(self.descLabel, 0, QtCore.Qt.AlignHCenter)
        self.line_265 = QtWidgets.QFrame(self.welcomeTab)
        self.line_265.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_265.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_265.setObjectName("line_265")
        self.verticalLayout_2.addWidget(self.line_265)
        self.tabWidget.addTab(self.welcomeTab, "")
        self.infoGatheringTab = QtWidgets.QWidget()
        self.infoGatheringTab.setObjectName("infoGatheringTab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.infoGatheringTab)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_30 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_30.setObjectName("pushButton_30")
        self.gridLayout_4.addWidget(self.pushButton_30, 18, 2, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_4.addWidget(self.pushButton_17, 5, 2, 1, 1)
        self.pushButton_54 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_54.setObjectName("pushButton_54")
        self.gridLayout_4.addWidget(self.pushButton_54, 12, 4, 1, 1)
        self.pushButton_48 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_48.setObjectName("pushButton_48")
        self.gridLayout_4.addWidget(self.pushButton_48, 6, 4, 1, 1)
        self.pushButton_35 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_35.setObjectName("pushButton_35")
        self.gridLayout_4.addWidget(self.pushButton_35, 8, 3, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_4.addWidget(self.pushButton_13, 16, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_4.addWidget(self.pushButton_10, 13, 1, 1, 1)
        self.pushButton_58 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_58.setObjectName("pushButton_58")
        self.gridLayout_4.addWidget(self.pushButton_58, 16, 4, 1, 1)
        self.pushButton_60 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_60.setObjectName("pushButton_60")
        self.gridLayout_4.addWidget(self.pushButton_60, 18, 4, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout_4.addWidget(self.pushButton_19, 7, 2, 1, 1)
        self.pushButton_25 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_25.setObjectName("pushButton_25")
        self.gridLayout_4.addWidget(self.pushButton_25, 13, 2, 1, 1)
        self.pushButton_31 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_31.setObjectName("pushButton_31")
        self.gridLayout_4.addWidget(self.pushButton_31, 4, 3, 1, 1)
        self.pushButton_36 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_36.setObjectName("pushButton_36")
        self.gridLayout_4.addWidget(self.pushButton_36, 9, 3, 1, 1)
        self.pushButton_44 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_44.setObjectName("pushButton_44")
        self.gridLayout_4.addWidget(self.pushButton_44, 17, 3, 1, 1)
        self.pushButton_33 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_33.setObjectName("pushButton_33")
        self.gridLayout_4.addWidget(self.pushButton_33, 6, 3, 1, 1)
        self.pushButton_24 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_24.setObjectName("pushButton_24")
        self.gridLayout_4.addWidget(self.pushButton_24, 12, 2, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout_4.addWidget(self.pushButton_23, 11, 2, 1, 1)
        self.pushButton_51 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_51.setObjectName("pushButton_51")
        self.gridLayout_4.addWidget(self.pushButton_51, 9, 4, 1, 1)
        self.pushButton_45 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_45.setObjectName("pushButton_45")
        self.gridLayout_4.addWidget(self.pushButton_45, 18, 3, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_4.addWidget(self.pushButton_5, 8, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_4.addWidget(self.pushButton_4, 7, 1, 1, 1)
        self.pushButton_42 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_42.setObjectName("pushButton_42")
        self.gridLayout_4.addWidget(self.pushButton_42, 15, 3, 1, 1)
        self.pushButton_41 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_41.setObjectName("pushButton_41")
        self.gridLayout_4.addWidget(self.pushButton_41, 14, 3, 1, 1)
        self.pushButton_57 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_57.setObjectName("pushButton_57")
        self.gridLayout_4.addWidget(self.pushButton_57, 15, 4, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_4.addWidget(self.pushButton_3, 6, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_4.addWidget(self.pushButton_7, 10, 1, 1, 1)
        self.pushButton_37 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_37.setObjectName("pushButton_37")
        self.gridLayout_4.addWidget(self.pushButton_37, 10, 3, 1, 1)
        self.pushButton_34 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_34.setObjectName("pushButton_34")
        self.gridLayout_4.addWidget(self.pushButton_34, 7, 3, 1, 1)
        self.pushButton_27 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_27.setObjectName("pushButton_27")
        self.gridLayout_4.addWidget(self.pushButton_27, 15, 2, 1, 1)
        self.pushButton_40 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_40.setObjectName("pushButton_40")
        self.gridLayout_4.addWidget(self.pushButton_40, 13, 3, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout_4.addWidget(self.pushButton_22, 10, 2, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_4.addWidget(self.pushButton_8, 11, 1, 1, 1)
        self.pushButton_39 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_39.setObjectName("pushButton_39")
        self.gridLayout_4.addWidget(self.pushButton_39, 12, 3, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_4.addWidget(self.pushButton_11, 14, 1, 1, 1)
        self.pushButton_38 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_38.setObjectName("pushButton_38")
        self.gridLayout_4.addWidget(self.pushButton_38, 11, 3, 1, 1)
        self.pushButton_59 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_59.setObjectName("pushButton_59")
        self.gridLayout_4.addWidget(self.pushButton_59, 17, 4, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_4.addWidget(self.pushButton_9, 12, 1, 1, 1)
        self.pushButton_53 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_53.setObjectName("pushButton_53")
        self.gridLayout_4.addWidget(self.pushButton_53, 11, 4, 1, 1)
        self.pushButton_32 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_32.setObjectName("pushButton_32")
        self.gridLayout_4.addWidget(self.pushButton_32, 5, 3, 1, 1)
        self.pushButton_43 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_43.setObjectName("pushButton_43")
        self.gridLayout_4.addWidget(self.pushButton_43, 16, 3, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_4.addWidget(self.pushButton_18, 6, 2, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_4.addWidget(self.pushButton_14, 17, 1, 1, 1)
        self.pushButton_26 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_26.setObjectName("pushButton_26")
        self.gridLayout_4.addWidget(self.pushButton_26, 14, 2, 1, 1)
        self.pushButton_28 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_28.setObjectName("pushButton_28")
        self.gridLayout_4.addWidget(self.pushButton_28, 16, 2, 1, 1)
        self.pushButton_47 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_47.setObjectName("pushButton_47")
        self.gridLayout_4.addWidget(self.pushButton_47, 5, 4, 1, 1)
        self.pushButton_46 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_46.setObjectName("pushButton_46")
        self.gridLayout_4.addWidget(self.pushButton_46, 4, 4, 1, 1)
        self.pushButton_21 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout_4.addWidget(self.pushButton_21, 9, 2, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_4.addWidget(self.pushButton_6, 9, 1, 1, 1)
        self.pushButton_29 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_29.setObjectName("pushButton_29")
        self.gridLayout_4.addWidget(self.pushButton_29, 17, 2, 1, 1)
        self.pushButton_52 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_52.setObjectName("pushButton_52")
        self.gridLayout_4.addWidget(self.pushButton_52, 10, 4, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_4.addWidget(self.pushButton_15, 18, 1, 1, 1)
        self.pushButton_50 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_50.setObjectName("pushButton_50")
        self.gridLayout_4.addWidget(self.pushButton_50, 8, 4, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 4, 1, 1, 1)
        self.pushButton_55 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_55.setObjectName("pushButton_55")
        self.gridLayout_4.addWidget(self.pushButton_55, 13, 4, 1, 1)
        self.pushButton_49 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_49.setObjectName("pushButton_49")
        self.gridLayout_4.addWidget(self.pushButton_49, 7, 4, 1, 1)
        self.line_33 = QtWidgets.QFrame(self.infoGatheringTab)
        self.line_33.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_33.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_33.setObjectName("line_33")
        self.gridLayout_4.addWidget(self.line_33, 4, 0, 16, 1)
        self.pushButton_56 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_56.setObjectName("pushButton_56")
        self.gridLayout_4.addWidget(self.pushButton_56, 14, 4, 1, 1)
        self.InformationGatheringTitle = QtWidgets.QLabel(self.infoGatheringTab)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(32)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.InformationGatheringTitle.setFont(font)
        self.InformationGatheringTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.InformationGatheringTitle.setObjectName("InformationGatheringTitle")
        self.gridLayout_4.addWidget(self.InformationGatheringTitle, 0, 2, 2, 3)
        self.line_35 = QtWidgets.QFrame(self.infoGatheringTab)
        self.line_35.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_35.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_35.setObjectName("line_35")
        self.gridLayout_4.addWidget(self.line_35, 4, 5, 16, 1)
        self.line_4 = QtWidgets.QFrame(self.infoGatheringTab)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_4.addWidget(self.line_4, 2, 1, 1, 4)
        self.pushButton_2 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 5, 1, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout_4.addWidget(self.pushButton_20, 8, 2, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_4.addWidget(self.pushButton_16, 4, 2, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.infoGatheringTab)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_4.addWidget(self.pushButton_12, 15, 1, 1, 1)
        self.InformationGatheringTitle.raise_()
        self.line_4.raise_()
        self.line_33.raise_()
        self.line_35.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.pushButton_10.raise_()
        self.pushButton_11.raise_()
        self.pushButton_12.raise_()
        self.pushButton_13.raise_()
        self.pushButton_14.raise_()
        self.pushButton_15.raise_()
        self.pushButton_16.raise_()
        self.pushButton_17.raise_()
        self.pushButton_18.raise_()
        self.pushButton_19.raise_()
        self.pushButton_20.raise_()
        self.pushButton_21.raise_()
        self.pushButton_22.raise_()
        self.pushButton_23.raise_()
        self.pushButton_24.raise_()
        self.pushButton_25.raise_()
        self.pushButton_26.raise_()
        self.pushButton_27.raise_()
        self.pushButton_28.raise_()
        self.pushButton_29.raise_()
        self.pushButton_30.raise_()
        self.pushButton_31.raise_()
        self.pushButton_32.raise_()
        self.pushButton_33.raise_()
        self.pushButton_34.raise_()
        self.pushButton_35.raise_()
        self.pushButton_36.raise_()
        self.pushButton_37.raise_()
        self.pushButton_38.raise_()
        self.pushButton_39.raise_()
        self.pushButton_40.raise_()
        self.pushButton_41.raise_()
        self.pushButton_42.raise_()
        self.pushButton_43.raise_()
        self.pushButton_44.raise_()
        self.pushButton_45.raise_()
        self.pushButton_46.raise_()
        self.pushButton_47.raise_()
        self.pushButton_48.raise_()
        self.pushButton_49.raise_()
        self.pushButton_50.raise_()
        self.pushButton_51.raise_()
        self.pushButton_52.raise_()
        self.pushButton_53.raise_()
        self.pushButton_54.raise_()
        self.pushButton_55.raise_()
        self.pushButton_56.raise_()
        self.pushButton_57.raise_()
        self.pushButton_58.raise_()
        self.pushButton_59.raise_()
        self.pushButton_60.raise_()
        self.tabWidget.addTab(self.infoGatheringTab, "")
        self.acccheckTab = QtWidgets.QWidget()
        self.acccheckTab.setObjectName("acccheckTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.acccheckTab)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.acccheckScrollArea = QtWidgets.QScrollArea(self.acccheckTab)
        self.acccheckScrollArea.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.acccheckScrollArea.setWidgetResizable(True)
        self.acccheckScrollArea.setObjectName("acccheckScrollArea")
        self.acccheckWidgetContents = QtWidgets.QWidget()
        self.acccheckWidgetContents.setGeometry(QtCore.QRect(0, 0, 3128, 1765))
        self.acccheckWidgetContents.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.acccheckWidgetContents.setObjectName("acccheckWidgetContents")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.acccheckWidgetContents)
        self.gridLayout_6.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.line_5 = QtWidgets.QFrame(self.acccheckWidgetContents)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_6.addWidget(self.line_5, 10, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.acccheckWidgetContents)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_6.addWidget(self.line_3, 7, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.acccheckWidgetContents)
        self.line.setStyleSheet("")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_6.addWidget(self.line, 2, 0, 1, 1)
        self.acccheckTitle = QtWidgets.QLabel(self.acccheckWidgetContents)
        self.acccheckTitle.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.acccheckTitle.setFont(font)
        self.acccheckTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.acccheckTitle.setObjectName("acccheckTitle")
        self.gridLayout_6.addWidget(self.acccheckTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.acccheckH2 = QtWidgets.QLabel(self.acccheckWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.acccheckH2.setFont(font)
        self.acccheckH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.acccheckH2.setObjectName("acccheckH2")
        self.gridLayout_6.addWidget(self.acccheckH2, 6, 0, 1, 1)
        self.acccheckB1 = QtWidgets.QLabel(self.acccheckWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.acccheckB1.setFont(font)
        self.acccheckB1.setTextFormat(QtCore.Qt.AutoText)
        self.acccheckB1.setScaledContents(False)
        self.acccheckB1.setWordWrap(False)
        self.acccheckB1.setObjectName("acccheckB1")
        self.gridLayout_6.addWidget(self.acccheckB1, 5, 0, 1, 1)
        self.acccheckB4 = QtWidgets.QLabel(self.acccheckWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.acccheckB4.setFont(font)
        self.acccheckB4.setObjectName("acccheckB4")
        self.gridLayout_6.addWidget(self.acccheckB4, 12, 0, 1, 1)
        self.acccheckH3 = QtWidgets.QLabel(self.acccheckWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.acccheckH3.setFont(font)
        self.acccheckH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.acccheckH3.setObjectName("acccheckH3")
        self.gridLayout_6.addWidget(self.acccheckH3, 9, 0, 1, 1)
        self.acccheckB2 = QtWidgets.QLabel(self.acccheckWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.acccheckB2.setFont(font)
        self.acccheckB2.setObjectName("acccheckB2")
        self.gridLayout_6.addWidget(self.acccheckB2, 8, 0, 1, 1)
        self.acccheckH1 = QtWidgets.QLabel(self.acccheckWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.acccheckH1.setFont(font)
        self.acccheckH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.acccheckH1.setObjectName("acccheckH1")
        self.gridLayout_6.addWidget(self.acccheckH1, 3, 0, 1, 1)
        self.acccheckButton = QtWidgets.QPushButton(self.acccheckWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.acccheckButton.setFont(font)
        self.acccheckButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(79, 79, 79);")
        self.acccheckButton.setObjectName("acccheckButton")
        self.gridLayout_6.addWidget(self.acccheckButton, 16, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_6.addItem(spacerItem, 17, 0, 1, 1)
        self.acccheckH4 = QtWidgets.QLabel(self.acccheckWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.acccheckH4.setFont(font)
        self.acccheckH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.acccheckH4.setObjectName("acccheckH4")
        self.gridLayout_6.addWidget(self.acccheckH4, 14, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.acccheckB3 = QtWidgets.QLabel(self.acccheckWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.acccheckB3.setFont(font)
        self.acccheckB3.setObjectName("acccheckB3")
        self.gridLayout_6.addWidget(self.acccheckB3, 11, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.acccheckWidgetContents)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_6.addWidget(self.line_2, 4, 0, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.acccheckWidgetContents)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_6.addWidget(self.line_6, 13, 0, 1, 1)
        self.acccheckScrollArea.setWidget(self.acccheckWidgetContents)
        self.gridLayout_2.addWidget(self.acccheckScrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.acccheckTab, "")
        self.acevoipTab = QtWidgets.QWidget()
        self.acevoipTab.setObjectName("acevoipTab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.acevoipTab)
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.acevoipTitle = QtWidgets.QLabel(self.acevoipTab)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.acevoipTitle.setFont(font)
        self.acevoipTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.acevoipTitle.setObjectName("acevoipTitle")
        self.gridLayout_5.addWidget(self.acevoipTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.acevoipScrollArea = QtWidgets.QScrollArea(self.acevoipTab)
        self.acevoipScrollArea.setWidgetResizable(True)
        self.acevoipScrollArea.setObjectName("acevoipScrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 3128, 1417))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_7.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.acevoipButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.acevoipButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.acevoipButton.setObjectName("acevoipButton")
        self.gridLayout_7.addWidget(self.acevoipButton, 8, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_7.addItem(spacerItem1, 9, 0, 1, 1)
        self.acevoipH4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.acevoipH4.setFont(font)
        self.acevoipH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.acevoipH4.setObjectName("acevoipH4")
        self.gridLayout_7.addWidget(self.acevoipH4, 7, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.acevoipB3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.acevoipB3.setStyleSheet("color: rgb(255, 255, 255);")
        self.acevoipB3.setObjectName("acevoipB3")
        self.gridLayout_7.addWidget(self.acevoipB3, 5, 0, 1, 1)
        self.acevoipB1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.acevoipB1.setFont(font)
        self.acevoipB1.setStyleSheet("color: rgb(255, 255, 255);")
        self.acevoipB1.setObjectName("acevoipB1")
        self.gridLayout_7.addWidget(self.acevoipB1, 1, 0, 1, 1)
        self.acevoipH2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.acevoipH2.setFont(font)
        self.acevoipH2.setStyleSheet("color: rgb(56, 196, 255);\n"
"")
        self.acevoipH2.setObjectName("acevoipH2")
        self.gridLayout_7.addWidget(self.acevoipH2, 2, 0, 1, 1)
        self.acevoipH1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.acevoipH1.setFont(font)
        self.acevoipH1.setStyleSheet("color: rgb(56, 196, 255);\n"
"")
        self.acevoipH1.setObjectName("acevoipH1")
        self.gridLayout_7.addWidget(self.acevoipH1, 0, 0, 1, 1)
        self.acevoipB2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.acevoipB2.setFont(font)
        self.acevoipB2.setStyleSheet("color: rgb(255, 255, 255);")
        self.acevoipB2.setObjectName("acevoipB2")
        self.gridLayout_7.addWidget(self.acevoipB2, 3, 0, 1, 1)
        self.acevoipH3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.acevoipH3.setFont(font)
        self.acevoipH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.acevoipH3.setObjectName("acevoipH3")
        self.gridLayout_7.addWidget(self.acevoipH3, 4, 0, 1, 1)
        self.acevoipB4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.acevoipB4.setStyleSheet("color: rgb(255, 255, 255);")
        self.acevoipB4.setObjectName("acevoipB4")
        self.gridLayout_7.addWidget(self.acevoipB4, 6, 0, 1, 1)
        self.acevoipScrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_5.addWidget(self.acevoipScrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.acevoipTab, "")
        self.amapTab = QtWidgets.QWidget()
        self.amapTab.setObjectName("amapTab")
        self.gridLayout_51 = QtWidgets.QGridLayout(self.amapTab)
        self.gridLayout_51.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_51.setSpacing(6)
        self.gridLayout_51.setObjectName("gridLayout_51")
        self.amapTitle = QtWidgets.QLabel(self.amapTab)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.amapTitle.setFont(font)
        self.amapTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.amapTitle.setObjectName("amapTitle")
        self.gridLayout_51.addWidget(self.amapTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.amapScrollArea = QtWidgets.QScrollArea(self.amapTab)
        self.amapScrollArea.setWidgetResizable(True)
        self.amapScrollArea.setObjectName("amapScrollArea")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 3128, 2422))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.gridLayout_71 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_71.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_71.setSpacing(6)
        self.gridLayout_71.setObjectName("gridLayout_71")
        self.amapButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.amapButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.amapButton.setObjectName("amapButton")
        self.gridLayout_71.addWidget(self.amapButton, 8, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_71.addItem(spacerItem2, 9, 0, 1, 1)
        self.amapH4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.amapH4.setFont(font)
        self.amapH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.amapH4.setObjectName("amapH4")
        self.gridLayout_71.addWidget(self.amapH4, 7, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.amapB3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.amapB3.setFont(font)
        self.amapB3.setStyleSheet("color: rgb(255, 255, 255);")
        self.amapB3.setObjectName("amapB3")
        self.gridLayout_71.addWidget(self.amapB3, 6, 0, 1, 1)
        self.amapB1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.amapB1.setFont(font)
        self.amapB1.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.amapB1.setObjectName("amapB1")
        self.gridLayout_71.addWidget(self.amapB1, 1, 0, 1, 1)
        self.amapH2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.amapH2.setFont(font)
        self.amapH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.amapH2.setObjectName("amapH2")
        self.gridLayout_71.addWidget(self.amapH2, 2, 0, 1, 1)
        self.amapH1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.amapH1.setFont(font)
        self.amapH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.amapH1.setObjectName("amapH1")
        self.gridLayout_71.addWidget(self.amapH1, 0, 0, 1, 1)
        self.amapH3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.amapH3.setFont(font)
        self.amapH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.amapH3.setObjectName("amapH3")
        self.gridLayout_71.addWidget(self.amapH3, 4, 0, 1, 1)
        self.amapB2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.amapB2.setFont(font)
        self.amapB2.setStyleSheet("color: rgb(255, 255, 255);")
        self.amapB2.setObjectName("amapB2")
        self.gridLayout_71.addWidget(self.amapB2, 5, 0, 1, 1)
        self.amapScrollArea.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout_51.addWidget(self.amapScrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.amapTab, "")
        self.automaterTab = QtWidgets.QWidget()
        self.automaterTab.setObjectName("automaterTab")
        self.gridLayout_52 = QtWidgets.QGridLayout(self.automaterTab)
        self.gridLayout_52.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_52.setSpacing(6)
        self.gridLayout_52.setObjectName("gridLayout_52")
        self.automaterTitle = QtWidgets.QLabel(self.automaterTab)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.automaterTitle.setFont(font)
        self.automaterTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.automaterTitle.setObjectName("automaterTitle")
        self.gridLayout_52.addWidget(self.automaterTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.automaterScrollArea = QtWidgets.QScrollArea(self.automaterTab)
        self.automaterScrollArea.setWidgetResizable(True)
        self.automaterScrollArea.setObjectName("automaterScrollArea")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 3128, 1399))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.gridLayout_72 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_72.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_72.setSpacing(6)
        self.gridLayout_72.setObjectName("gridLayout_72")
        self.automaterButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_5)
        self.automaterButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.automaterButton.setObjectName("automaterButton")
        self.gridLayout_72.addWidget(self.automaterButton, 8, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_72.addItem(spacerItem3, 9, 0, 1, 1)
        self.automaterH4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.automaterH4.setFont(font)
        self.automaterH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.automaterH4.setObjectName("automaterH4")
        self.gridLayout_72.addWidget(self.automaterH4, 7, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.automaterB3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.automaterB3.setStyleSheet("color: rgb(255, 255, 255);")
        self.automaterB3.setObjectName("automaterB3")
        self.gridLayout_72.addWidget(self.automaterB3, 5, 0, 1, 1)
        self.automaterB1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.automaterB1.setFont(font)
        self.automaterB1.setStyleSheet("color: rgb(255, 255, 255);")
        self.automaterB1.setObjectName("automaterB1")
        self.gridLayout_72.addWidget(self.automaterB1, 1, 0, 1, 1)
        self.automaterH2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.automaterH2.setFont(font)
        self.automaterH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.automaterH2.setObjectName("automaterH2")
        self.gridLayout_72.addWidget(self.automaterH2, 2, 0, 1, 1)
        self.automaterH1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.automaterH1.setFont(font)
        self.automaterH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.automaterH1.setObjectName("automaterH1")
        self.gridLayout_72.addWidget(self.automaterH1, 0, 0, 1, 1)
        self.automaterB2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.automaterB2.setFont(font)
        self.automaterB2.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.automaterB2.setObjectName("automaterB2")
        self.gridLayout_72.addWidget(self.automaterB2, 3, 0, 1, 1)
        self.automaterH3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.automaterH3.setFont(font)
        self.automaterH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.automaterH3.setObjectName("automaterH3")
        self.gridLayout_72.addWidget(self.automaterH3, 4, 0, 1, 1)
        self.automaterB4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.automaterB4.setStyleSheet("color: rgb(255, 255, 255);")
        self.automaterB4.setObjectName("automaterB4")
        self.gridLayout_72.addWidget(self.automaterB4, 6, 0, 1, 1)
        self.automaterScrollArea.setWidget(self.scrollAreaWidgetContents_5)
        self.gridLayout_52.addWidget(self.automaterScrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.automaterTab, "")
        self.bingip2hostsTab = QtWidgets.QWidget()
        self.bingip2hostsTab.setObjectName("bingip2hostsTab")
        self.gridLayout_53 = QtWidgets.QGridLayout(self.bingip2hostsTab)
        self.gridLayout_53.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_53.setSpacing(6)
        self.gridLayout_53.setObjectName("gridLayout_53")
        self.bingip2hostsTitle = QtWidgets.QLabel(self.bingip2hostsTab)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.bingip2hostsTitle.setFont(font)
        self.bingip2hostsTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.bingip2hostsTitle.setObjectName("bingip2hostsTitle")
        self.gridLayout_53.addWidget(self.bingip2hostsTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.bingip2hostsArea = QtWidgets.QScrollArea(self.bingip2hostsTab)
        self.bingip2hostsArea.setWidgetResizable(True)
        self.bingip2hostsArea.setObjectName("bingip2hostsArea")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 3128, 1394))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.gridLayout_73 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_73.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_73.setSpacing(6)
        self.gridLayout_73.setObjectName("gridLayout_73")
        self.bingip2hostsButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_6)
        self.bingip2hostsButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.bingip2hostsButton.setObjectName("bingip2hostsButton")
        self.gridLayout_73.addWidget(self.bingip2hostsButton, 8, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_73.addItem(spacerItem4, 9, 0, 1, 1)
        self.bingip2hostsH4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.bingip2hostsH4.setFont(font)
        self.bingip2hostsH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.bingip2hostsH4.setObjectName("bingip2hostsH4")
        self.gridLayout_73.addWidget(self.bingip2hostsH4, 7, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.bingip2hostsB3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bingip2hostsB3.setFont(font)
        self.bingip2hostsB3.setStyleSheet("color: rgb(255, 255, 255);")
        self.bingip2hostsB3.setObjectName("bingip2hostsB3")
        self.gridLayout_73.addWidget(self.bingip2hostsB3, 5, 0, 1, 1)
        self.bingip2hostsB1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bingip2hostsB1.setFont(font)
        self.bingip2hostsB1.setStyleSheet("color: rgb(255, 255, 255);")
        self.bingip2hostsB1.setObjectName("bingip2hostsB1")
        self.gridLayout_73.addWidget(self.bingip2hostsB1, 1, 0, 1, 1)
        self.bingip2hostsH2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.bingip2hostsH2.setFont(font)
        self.bingip2hostsH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.bingip2hostsH2.setObjectName("bingip2hostsH2")
        self.gridLayout_73.addWidget(self.bingip2hostsH2, 2, 0, 1, 1)
        self.bingip2hostsH1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.bingip2hostsH1.setFont(font)
        self.bingip2hostsH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.bingip2hostsH1.setObjectName("bingip2hostsH1")
        self.gridLayout_73.addWidget(self.bingip2hostsH1, 0, 0, 1, 1)
        self.bingip2hostsB2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bingip2hostsB2.setFont(font)
        self.bingip2hostsB2.setStyleSheet("color: rgb(255, 255, 255);")
        self.bingip2hostsB2.setObjectName("bingip2hostsB2")
        self.gridLayout_73.addWidget(self.bingip2hostsB2, 3, 0, 1, 1)
        self.bingip2hostsH3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.bingip2hostsH3.setFont(font)
        self.bingip2hostsH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.bingip2hostsH3.setObjectName("bingip2hostsH3")
        self.gridLayout_73.addWidget(self.bingip2hostsH3, 4, 0, 1, 1)
        self.bingip2hostsB4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bingip2hostsB4.setFont(font)
        self.bingip2hostsB4.setStyleSheet("color: rgb(255, 255, 255);")
        self.bingip2hostsB4.setObjectName("bingip2hostsB4")
        self.gridLayout_73.addWidget(self.bingip2hostsB4, 6, 0, 1, 1)
        self.bingip2hostsArea.setWidget(self.scrollAreaWidgetContents_6)
        self.gridLayout_53.addWidget(self.bingip2hostsArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.bingip2hostsTab, "")
        self.braaTab = QtWidgets.QWidget()
        self.braaTab.setObjectName("braaTab")
        self.gridLayout_54 = QtWidgets.QGridLayout(self.braaTab)
        self.gridLayout_54.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_54.setSpacing(6)
        self.gridLayout_54.setObjectName("gridLayout_54")
        self.braaTitle = QtWidgets.QLabel(self.braaTab)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.braaTitle.setFont(font)
        self.braaTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.braaTitle.setObjectName("braaTitle")
        self.gridLayout_54.addWidget(self.braaTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.braaScrollArea = QtWidgets.QScrollArea(self.braaTab)
        self.braaScrollArea.setWidgetResizable(True)
        self.braaScrollArea.setObjectName("braaScrollArea")
        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 3128, 1617))
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.gridLayout_74 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_7)
        self.gridLayout_74.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_74.setSpacing(6)
        self.gridLayout_74.setObjectName("gridLayout_74")
        self.braaButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_7)
        self.braaButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.braaButton.setObjectName("braaButton")
        self.gridLayout_74.addWidget(self.braaButton, 7, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_74.addItem(spacerItem5, 8, 0, 1, 1)
        self.braaH4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.braaH4.setFont(font)
        self.braaH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.braaH4.setObjectName("braaH4")
        self.gridLayout_74.addWidget(self.braaH4, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.braaB3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.braaB3.setFont(font)
        self.braaB3.setStyleSheet("color: rgb(255, 255, 255);")
        self.braaB3.setObjectName("braaB3")
        self.gridLayout_74.addWidget(self.braaB3, 5, 0, 1, 1)
        self.braaB1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.braaB1.setFont(font)
        self.braaB1.setStyleSheet("color: rgb(255, 255, 255);")
        self.braaB1.setObjectName("braaB1")
        self.gridLayout_74.addWidget(self.braaB1, 1, 0, 1, 1)
        self.braaH2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.braaH2.setFont(font)
        self.braaH2.setStyleSheet("color: rgb(56, 196, 255);\n"
"")
        self.braaH2.setObjectName("braaH2")
        self.gridLayout_74.addWidget(self.braaH2, 2, 0, 1, 1)
        self.braaH1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.braaH1.setFont(font)
        self.braaH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.braaH1.setObjectName("braaH1")
        self.gridLayout_74.addWidget(self.braaH1, 0, 0, 1, 1)
        self.braaB2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.braaB2.setFont(font)
        self.braaB2.setStyleSheet("color: rgb(255, 255, 255);")
        self.braaB2.setObjectName("braaB2")
        self.gridLayout_74.addWidget(self.braaB2, 3, 0, 1, 1)
        self.braaH3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.braaH3.setFont(font)
        self.braaH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.braaH3.setObjectName("braaH3")
        self.gridLayout_74.addWidget(self.braaH3, 4, 0, 1, 1)
        self.braaScrollArea.setWidget(self.scrollAreaWidgetContents_7)
        self.gridLayout_54.addWidget(self.braaScrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.braaTab, "")
        self.CaseFileTab = QtWidgets.QWidget()
        self.CaseFileTab.setObjectName("CaseFileTab")
        self.gridLayout_55 = QtWidgets.QGridLayout(self.CaseFileTab)
        self.gridLayout_55.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_55.setSpacing(6)
        self.gridLayout_55.setObjectName("gridLayout_55")
        self.CaseFileTitle = QtWidgets.QLabel(self.CaseFileTab)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.CaseFileTitle.setFont(font)
        self.CaseFileTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.CaseFileTitle.setObjectName("CaseFileTitle")
        self.gridLayout_55.addWidget(self.CaseFileTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.CaseFileScrollArea = QtWidgets.QScrollArea(self.CaseFileTab)
        self.CaseFileScrollArea.setWidgetResizable(True)
        self.CaseFileScrollArea.setObjectName("CaseFileScrollArea")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 3128, 1130))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.gridLayout_75 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_8)
        self.gridLayout_75.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_75.setSpacing(6)
        self.gridLayout_75.setObjectName("gridLayout_75")
        self.CaseFileButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_8)
        self.CaseFileButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.CaseFileButton.setObjectName("CaseFileButton")
        self.gridLayout_75.addWidget(self.CaseFileButton, 5, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_75.addItem(spacerItem6, 6, 0, 1, 1)
        self.CaseFileH4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.CaseFileH4.setFont(font)
        self.CaseFileH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.CaseFileH4.setObjectName("CaseFileH4")
        self.gridLayout_75.addWidget(self.CaseFileH4, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.CaseFileB1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.CaseFileB1.setFont(font)
        self.CaseFileB1.setStyleSheet("color: rgb(255, 255, 255);")
        self.CaseFileB1.setObjectName("CaseFileB1")
        self.gridLayout_75.addWidget(self.CaseFileB1, 1, 0, 1, 1)
        self.CaseFileH2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.CaseFileH2.setFont(font)
        self.CaseFileH2.setStyleSheet("color: rgb(56, 196, 255);\n"
"")
        self.CaseFileH2.setObjectName("CaseFileH2")
        self.gridLayout_75.addWidget(self.CaseFileH2, 2, 0, 1, 1)
        self.CaseFileH1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.CaseFileH1.setFont(font)
        self.CaseFileH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.CaseFileH1.setObjectName("CaseFileH1")
        self.gridLayout_75.addWidget(self.CaseFileH1, 0, 0, 1, 1)
        self.CaseFileB2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.CaseFileB2.setFont(font)
        self.CaseFileB2.setStyleSheet("color: rgb(255, 255, 255);")
        self.CaseFileB2.setObjectName("CaseFileB2")
        self.gridLayout_75.addWidget(self.CaseFileB2, 3, 0, 1, 1)
        self.CaseFileScrollArea.setWidget(self.scrollAreaWidgetContents_8)
        self.gridLayout_55.addWidget(self.CaseFileScrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.CaseFileTab, "")
        self.CDPSnarfTab = QtWidgets.QWidget()
        self.CDPSnarfTab.setObjectName("CDPSnarfTab")
        self.gridLayout_56 = QtWidgets.QGridLayout(self.CDPSnarfTab)
        self.gridLayout_56.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_56.setSpacing(6)
        self.gridLayout_56.setObjectName("gridLayout_56")
        self.CDPSnarfTitle = QtWidgets.QLabel(self.CDPSnarfTab)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.CDPSnarfTitle.setFont(font)
        self.CDPSnarfTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.CDPSnarfTitle.setObjectName("CDPSnarfTitle")
        self.gridLayout_56.addWidget(self.CDPSnarfTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.CDPSnarfScrollArea = QtWidgets.QScrollArea(self.CDPSnarfTab)
        self.CDPSnarfScrollArea.setWidgetResizable(True)
        self.CDPSnarfScrollArea.setObjectName("CDPSnarfScrollArea")
        self.scrollAreaWidgetContents_81 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_81.setGeometry(QtCore.QRect(0, 0, 2903, 1433))
        self.scrollAreaWidgetContents_81.setObjectName("scrollAreaWidgetContents_81")
        self.gridLayout_76 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_81)
        self.gridLayout_76.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_76.setSpacing(6)
        self.gridLayout_76.setObjectName("gridLayout_76")
        self.CDPSnarfButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_81)
        self.CDPSnarfButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.CDPSnarfButton.setObjectName("CDPSnarfButton")
        self.gridLayout_76.addWidget(self.CDPSnarfButton, 7, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_76.addItem(spacerItem7, 8, 0, 1, 1)
        self.CDPSnarfH4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_81)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.CDPSnarfH4.setFont(font)
        self.CDPSnarfH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.CDPSnarfH4.setObjectName("CDPSnarfH4")
        self.gridLayout_76.addWidget(self.CDPSnarfH4, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.CDPSnarfB3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_81)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.CDPSnarfB3.setFont(font)
        self.CDPSnarfB3.setStyleSheet("color: rgb(255, 255, 255);")
        self.CDPSnarfB3.setObjectName("CDPSnarfB3")
        self.gridLayout_76.addWidget(self.CDPSnarfB3, 5, 0, 1, 1)
        self.CDPSnarfB1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_81)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.CDPSnarfB1.setFont(font)
        self.CDPSnarfB1.setStyleSheet("color: rgb(255, 255, 255);")
        self.CDPSnarfB1.setObjectName("CDPSnarfB1")
        self.gridLayout_76.addWidget(self.CDPSnarfB1, 1, 0, 1, 1)
        self.CDPSnarfH2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_81)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.CDPSnarfH2.setFont(font)
        self.CDPSnarfH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.CDPSnarfH2.setObjectName("CDPSnarfH2")
        self.gridLayout_76.addWidget(self.CDPSnarfH2, 2, 0, 1, 1)
        self.CDPSnarfH1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_81)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.CDPSnarfH1.setFont(font)
        self.CDPSnarfH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.CDPSnarfH1.setObjectName("CDPSnarfH1")
        self.gridLayout_76.addWidget(self.CDPSnarfH1, 0, 0, 1, 1)
        self.CDPSnarfB2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_81)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.CDPSnarfB2.setFont(font)
        self.CDPSnarfB2.setStyleSheet("color: rgb(255, 255, 255);")
        self.CDPSnarfB2.setObjectName("CDPSnarfB2")
        self.gridLayout_76.addWidget(self.CDPSnarfB2, 3, 0, 1, 1)
        self.CDPSnarfH3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_81)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.CDPSnarfH3.setFont(font)
        self.CDPSnarfH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.CDPSnarfH3.setObjectName("CDPSnarfH3")
        self.gridLayout_76.addWidget(self.CDPSnarfH3, 4, 0, 1, 1)
        self.CDPSnarfScrollArea.setWidget(self.scrollAreaWidgetContents_81)
        self.gridLayout_56.addWidget(self.CDPSnarfScrollArea, 0, 1, 1, 1)
        self.tabWidget.addTab(self.CDPSnarfTab, "")
        self.ciscoTorchTab = QtWidgets.QWidget()
        self.ciscoTorchTab.setObjectName("ciscoTorchTab")
        self.gridLayout_57 = QtWidgets.QGridLayout(self.ciscoTorchTab)
        self.gridLayout_57.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_57.setSpacing(6)
        self.gridLayout_57.setObjectName("gridLayout_57")
        self.ciscoTorchTitle = QtWidgets.QLabel(self.ciscoTorchTab)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.ciscoTorchTitle.setFont(font)
        self.ciscoTorchTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.ciscoTorchTitle.setObjectName("ciscoTorchTitle")
        self.gridLayout_57.addWidget(self.ciscoTorchTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.ciscoTorchScrollArea = QtWidgets.QScrollArea(self.ciscoTorchTab)
        self.ciscoTorchScrollArea.setWidgetResizable(True)
        self.ciscoTorchScrollArea.setObjectName("ciscoTorchScrollArea")
        self.scrollAreaWidgetContents_82 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_82.setGeometry(QtCore.QRect(0, 0, 3128, 2376))
        self.scrollAreaWidgetContents_82.setObjectName("scrollAreaWidgetContents_82")
        self.gridLayout_77 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_82)
        self.gridLayout_77.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_77.setSpacing(6)
        self.gridLayout_77.setObjectName("gridLayout_77")
        self.ciscoTorchButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_82)
        self.ciscoTorchButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.ciscoTorchButton.setObjectName("ciscoTorchButton")
        self.gridLayout_77.addWidget(self.ciscoTorchButton, 7, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_77.addItem(spacerItem8, 8, 0, 1, 1)
        self.ciscoTorchH4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_82)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.ciscoTorchH4.setFont(font)
        self.ciscoTorchH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.ciscoTorchH4.setObjectName("ciscoTorchH4")
        self.gridLayout_77.addWidget(self.ciscoTorchH4, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.ciscoTorchB3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_82)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ciscoTorchB3.setFont(font)
        self.ciscoTorchB3.setStyleSheet("color: rgb(255, 255, 255);")
        self.ciscoTorchB3.setObjectName("ciscoTorchB3")
        self.gridLayout_77.addWidget(self.ciscoTorchB3, 5, 0, 1, 1)
        self.ciscoTorchB1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_82)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ciscoTorchB1.setFont(font)
        self.ciscoTorchB1.setObjectName("ciscoTorchB1")
        self.gridLayout_77.addWidget(self.ciscoTorchB1, 1, 0, 1, 1)
        self.ciscoTorchH2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_82)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.ciscoTorchH2.setFont(font)
        self.ciscoTorchH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.ciscoTorchH2.setObjectName("ciscoTorchH2")
        self.gridLayout_77.addWidget(self.ciscoTorchH2, 2, 0, 1, 1)
        self.ciscoTorchH1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_82)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.ciscoTorchH1.setFont(font)
        self.ciscoTorchH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.ciscoTorchH1.setObjectName("ciscoTorchH1")
        self.gridLayout_77.addWidget(self.ciscoTorchH1, 0, 0, 1, 1)
        self.ciscoTorchB2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_82)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ciscoTorchB2.setFont(font)
        self.ciscoTorchB2.setStyleSheet("color: rgb(255, 255, 255);")
        self.ciscoTorchB2.setObjectName("ciscoTorchB2")
        self.gridLayout_77.addWidget(self.ciscoTorchB2, 3, 0, 1, 1)
        self.ciscoTorchH3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_82)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.ciscoTorchH3.setFont(font)
        self.ciscoTorchH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.ciscoTorchH3.setObjectName("ciscoTorchH3")
        self.gridLayout_77.addWidget(self.ciscoTorchH3, 4, 0, 1, 1)
        self.ciscoTorchScrollArea.setWidget(self.scrollAreaWidgetContents_82)
        self.gridLayout_57.addWidget(self.ciscoTorchScrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.ciscoTorchTab, "")
        self.CookieCadgerTab = QtWidgets.QWidget()
        self.CookieCadgerTab.setObjectName("CookieCadgerTab")
        self.gridLayout_58 = QtWidgets.QGridLayout(self.CookieCadgerTab)
        self.gridLayout_58.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_58.setSpacing(6)
        self.gridLayout_58.setObjectName("gridLayout_58")
        self.CookieCadgerTitle = QtWidgets.QLabel(self.CookieCadgerTab)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.CookieCadgerTitle.setFont(font)
        self.CookieCadgerTitle.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.CookieCadgerTitle.setObjectName("CookieCadgerTitle")
        self.gridLayout_58.addWidget(self.CookieCadgerTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.CookieCadgerScrollArea = QtWidgets.QScrollArea(self.CookieCadgerTab)
        self.CookieCadgerScrollArea.setWidgetResizable(True)
        self.CookieCadgerScrollArea.setObjectName("CookieCadgerScrollArea")
        self.scrollAreaWidgetContents_83 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_83.setGeometry(QtCore.QRect(0, 0, 3128, 1111))
        self.scrollAreaWidgetContents_83.setObjectName("scrollAreaWidgetContents_83")
        self.gridLayout_78 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_83)
        self.gridLayout_78.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_78.setSpacing(6)
        self.gridLayout_78.setObjectName("gridLayout_78")
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_78.addItem(spacerItem9, 8, 0, 1, 1)
        self.CookieCadgerB3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_83)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.CookieCadgerB3.setFont(font)
        self.CookieCadgerB3.setStyleSheet("color: rgb(255, 255, 255);")
        self.CookieCadgerB3.setObjectName("CookieCadgerB3")
        self.gridLayout_78.addWidget(self.CookieCadgerB3, 5, 0, 1, 1)
        self.CookieCadgerH4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_83)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.CookieCadgerH4.setFont(font)
        self.CookieCadgerH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.CookieCadgerH4.setObjectName("CookieCadgerH4")
        self.gridLayout_78.addWidget(self.CookieCadgerH4, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.CookieCadgerButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_83)
        self.CookieCadgerButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.CookieCadgerButton.setObjectName("CookieCadgerButton")
        self.gridLayout_78.addWidget(self.CookieCadgerButton, 7, 0, 1, 1)
        self.CookieCadgerB1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_83)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.CookieCadgerB1.setFont(font)
        self.CookieCadgerB1.setStyleSheet("color: rgb(255, 255, 255);")
        self.CookieCadgerB1.setObjectName("CookieCadgerB1")
        self.gridLayout_78.addWidget(self.CookieCadgerB1, 1, 0, 1, 1)
        self.CookieCadgerH2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_83)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.CookieCadgerH2.setFont(font)
        self.CookieCadgerH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.CookieCadgerH2.setObjectName("CookieCadgerH2")
        self.gridLayout_78.addWidget(self.CookieCadgerH2, 2, 0, 1, 1)
        self.CookieCadgerH1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_83)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.CookieCadgerH1.setFont(font)
        self.CookieCadgerH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.CookieCadgerH1.setObjectName("CookieCadgerH1")
        self.gridLayout_78.addWidget(self.CookieCadgerH1, 0, 0, 1, 1)
        self.CookieCadgerB2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_83)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.CookieCadgerB2.setFont(font)
        self.CookieCadgerB2.setStyleSheet("color: rgb(255, 255, 255);")
        self.CookieCadgerB2.setObjectName("CookieCadgerB2")
        self.gridLayout_78.addWidget(self.CookieCadgerB2, 3, 0, 1, 1)
        self.CookieCadgerH3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_83)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.CookieCadgerH3.setFont(font)
        self.CookieCadgerH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.CookieCadgerH3.setObjectName("CookieCadgerH3")
        self.gridLayout_78.addWidget(self.CookieCadgerH3, 4, 0, 1, 1)
        self.CookieCadgerScrollArea.setWidget(self.scrollAreaWidgetContents_83)
        self.gridLayout_58.addWidget(self.CookieCadgerScrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.CookieCadgerTab, "")
        self.copyRouterConfigTab = QtWidgets.QWidget()
        self.copyRouterConfigTab.setObjectName("copyRouterConfigTab")
        self.gridLayout_59 = QtWidgets.QGridLayout(self.copyRouterConfigTab)
        self.gridLayout_59.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_59.setSpacing(6)
        self.gridLayout_59.setObjectName("gridLayout_59")
        self.copyRouterConfigTitle = QtWidgets.QLabel(self.copyRouterConfigTab)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.copyRouterConfigTitle.setFont(font)
        self.copyRouterConfigTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.copyRouterConfigTitle.setObjectName("copyRouterConfigTitle")
        self.gridLayout_59.addWidget(self.copyRouterConfigTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.copyRouterConfigScrollArea = QtWidgets.QScrollArea(self.copyRouterConfigTab)
        self.copyRouterConfigScrollArea.setStyleSheet("color: rgb(255, 255, 255);")
        self.copyRouterConfigScrollArea.setWidgetResizable(True)
        self.copyRouterConfigScrollArea.setObjectName("copyRouterConfigScrollArea")
        self.scrollAreaWidgetContents_84 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_84.setGeometry(QtCore.QRect(0, 0, 3128, 1007))
        self.scrollAreaWidgetContents_84.setObjectName("scrollAreaWidgetContents_84")
        self.gridLayout_79 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_84)
        self.gridLayout_79.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_79.setSpacing(6)
        self.gridLayout_79.setObjectName("gridLayout_79")
        self.copyRouterConfigButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_84)
        self.copyRouterConfigButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.copyRouterConfigButton.setObjectName("copyRouterConfigButton")
        self.gridLayout_79.addWidget(self.copyRouterConfigButton, 8, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_79.addItem(spacerItem10, 9, 0, 1, 1)
        self.copyRouterConfigH4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_84)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.copyRouterConfigH4.setFont(font)
        self.copyRouterConfigH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.copyRouterConfigH4.setObjectName("copyRouterConfigH4")
        self.gridLayout_79.addWidget(self.copyRouterConfigH4, 7, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.copyRouterConfigB3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_84)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.copyRouterConfigB3.setFont(font)
        self.copyRouterConfigB3.setStyleSheet("color: rgb(255, 255, 255);")
        self.copyRouterConfigB3.setObjectName("copyRouterConfigB3")
        self.gridLayout_79.addWidget(self.copyRouterConfigB3, 5, 0, 1, 1)
        self.copyRouterConfigB1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_84)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.copyRouterConfigB1.setFont(font)
        self.copyRouterConfigB1.setObjectName("copyRouterConfigB1")
        self.gridLayout_79.addWidget(self.copyRouterConfigB1, 1, 0, 1, 1)
        self.copyRouterConfigH2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_84)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.copyRouterConfigH2.setFont(font)
        self.copyRouterConfigH2.setStyleSheet("color: rgb(56, 196, 255);\n"
"")
        self.copyRouterConfigH2.setObjectName("copyRouterConfigH2")
        self.gridLayout_79.addWidget(self.copyRouterConfigH2, 2, 0, 1, 1)
        self.copyRouterConfigH1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_84)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.copyRouterConfigH1.setFont(font)
        self.copyRouterConfigH1.setStyleSheet("color: rgb(56, 196, 255);\n"
"")
        self.copyRouterConfigH1.setObjectName("copyRouterConfigH1")
        self.gridLayout_79.addWidget(self.copyRouterConfigH1, 0, 0, 1, 1)
        self.copyRouterConfigB2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_84)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.copyRouterConfigB2.setFont(font)
        self.copyRouterConfigB2.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.copyRouterConfigB2.setObjectName("copyRouterConfigB2")
        self.gridLayout_79.addWidget(self.copyRouterConfigB2, 3, 0, 1, 1)
        self.copyRouterConfigH3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_84)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.copyRouterConfigH3.setFont(font)
        self.copyRouterConfigH3.setStyleSheet("color: rgb(56, 196, 255);\n"
"")
        self.copyRouterConfigH3.setObjectName("copyRouterConfigH3")
        self.gridLayout_79.addWidget(self.copyRouterConfigH3, 4, 0, 1, 1)
        self.copyRouterConfigB4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_84)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.copyRouterConfigB4.setFont(font)
        self.copyRouterConfigB4.setStyleSheet("color: rgb(255, 255, 255);")
        self.copyRouterConfigB4.setObjectName("copyRouterConfigB4")
        self.gridLayout_79.addWidget(self.copyRouterConfigB4, 6, 0, 1, 1)
        self.copyRouterConfigScrollArea.setWidget(self.scrollAreaWidgetContents_84)
        self.gridLayout_59.addWidget(self.copyRouterConfigScrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.copyRouterConfigTab, "")
        self.DMitryTab = QtWidgets.QWidget()
        self.DMitryTab.setObjectName("DMitryTab")
        self.gridLayout_510 = QtWidgets.QGridLayout(self.DMitryTab)
        self.gridLayout_510.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_510.setSpacing(6)
        self.gridLayout_510.setObjectName("gridLayout_510")
        self.DMitryTitle = QtWidgets.QLabel(self.DMitryTab)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.DMitryTitle.setFont(font)
        self.DMitryTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.DMitryTitle.setObjectName("DMitryTitle")
        self.gridLayout_510.addWidget(self.DMitryTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.DMitryScrollArea = QtWidgets.QScrollArea(self.DMitryTab)
        self.DMitryScrollArea.setWidgetResizable(True)
        self.DMitryScrollArea.setObjectName("DMitryScrollArea")
        self.scrollAreaWidgetContents_85 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_85.setGeometry(QtCore.QRect(0, 0, 3128, 1463))
        self.scrollAreaWidgetContents_85.setObjectName("scrollAreaWidgetContents_85")
        self.gridLayout_710 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_85)
        self.gridLayout_710.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_710.setSpacing(6)
        self.gridLayout_710.setObjectName("gridLayout_710")
        self.DMitryButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_85)
        self.DMitryButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.DMitryButton.setObjectName("DMitryButton")
        self.gridLayout_710.addWidget(self.DMitryButton, 8, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_710.addItem(spacerItem11, 9, 0, 1, 1)
        self.DMitryH4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_85)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.DMitryH4.setFont(font)
        self.DMitryH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.DMitryH4.setObjectName("DMitryH4")
        self.gridLayout_710.addWidget(self.DMitryH4, 7, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.DMitryB3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_85)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.DMitryB3.setFont(font)
        self.DMitryB3.setStyleSheet("color: rgb(255, 255, 255);")
        self.DMitryB3.setObjectName("DMitryB3")
        self.gridLayout_710.addWidget(self.DMitryB3, 5, 0, 1, 1)
        self.DMitryB1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_85)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.DMitryB1.setFont(font)
        self.DMitryB1.setStyleSheet("color: rgb(255, 255, 255);")
        self.DMitryB1.setObjectName("DMitryB1")
        self.gridLayout_710.addWidget(self.DMitryB1, 1, 0, 1, 1)
        self.DMitryH2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_85)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.DMitryH2.setFont(font)
        self.DMitryH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.DMitryH2.setObjectName("DMitryH2")
        self.gridLayout_710.addWidget(self.DMitryH2, 2, 0, 1, 1)
        self.DMitryH1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_85)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.DMitryH1.setFont(font)
        self.DMitryH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.DMitryH1.setObjectName("DMitryH1")
        self.gridLayout_710.addWidget(self.DMitryH1, 0, 0, 1, 1)
        self.DMitryB2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_85)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.DMitryB2.setFont(font)
        self.DMitryB2.setStyleSheet("color: rgb(255, 255, 255);")
        self.DMitryB2.setObjectName("DMitryB2")
        self.gridLayout_710.addWidget(self.DMitryB2, 3, 0, 1, 1)
        self.DMitryH3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_85)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.DMitryH3.setFont(font)
        self.DMitryH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.DMitryH3.setObjectName("DMitryH3")
        self.gridLayout_710.addWidget(self.DMitryH3, 4, 0, 1, 1)
        self.DMitryB4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_85)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.DMitryB4.setFont(font)
        self.DMitryB4.setStyleSheet("color: rgb(255, 255, 255);")
        self.DMitryB4.setObjectName("DMitryB4")
        self.gridLayout_710.addWidget(self.DMitryB4, 6, 0, 1, 1)
        self.DMitryScrollArea.setWidget(self.scrollAreaWidgetContents_85)
        self.gridLayout_510.addWidget(self.DMitryScrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.DMitryTab, "")
        self.dnmapTab = QtWidgets.QWidget()
        self.dnmapTab.setObjectName("dnmapTab")
        self.gridLayout_511 = QtWidgets.QGridLayout(self.dnmapTab)
        self.gridLayout_511.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_511.setSpacing(6)
        self.gridLayout_511.setObjectName("gridLayout_511")
        self.dnmapTitle = QtWidgets.QLabel(self.dnmapTab)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.dnmapTitle.setFont(font)
        self.dnmapTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.dnmapTitle.setObjectName("dnmapTitle")
        self.gridLayout_511.addWidget(self.dnmapTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.dnmapScrollArea = QtWidgets.QScrollArea(self.dnmapTab)
        self.dnmapScrollArea.setWidgetResizable(True)
        self.dnmapScrollArea.setObjectName("dnmapScrollArea")
        self.scrollAreaWidgetContents_86 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_86.setGeometry(QtCore.QRect(0, 0, 3128, 2590))
        self.scrollAreaWidgetContents_86.setObjectName("scrollAreaWidgetContents_86")
        self.gridLayout_711 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_86)
        self.gridLayout_711.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_711.setSpacing(6)
        self.gridLayout_711.setObjectName("gridLayout_711")
        self.dnmapButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_86)
        self.dnmapButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.dnmapButton.setObjectName("dnmapButton")
        self.gridLayout_711.addWidget(self.dnmapButton, 8, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_711.addItem(spacerItem12, 9, 0, 1, 1)
        self.dnmapH4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_86)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dnmapH4.setFont(font)
        self.dnmapH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.dnmapH4.setObjectName("dnmapH4")
        self.gridLayout_711.addWidget(self.dnmapH4, 7, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.dnmapB3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_86)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dnmapB3.setFont(font)
        self.dnmapB3.setStyleSheet("color: rgb(255, 255, 255);")
        self.dnmapB3.setObjectName("dnmapB3")
        self.gridLayout_711.addWidget(self.dnmapB3, 5, 0, 1, 1)
        self.dnmapB1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_86)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dnmapB1.setFont(font)
        self.dnmapB1.setStyleSheet("color: rgb(255, 255, 255);")
        self.dnmapB1.setObjectName("dnmapB1")
        self.gridLayout_711.addWidget(self.dnmapB1, 1, 0, 1, 1)
        self.dnmapH2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_86)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dnmapH2.setFont(font)
        self.dnmapH2.setStyleSheet("color: rgb(56, 196, 255);    ")
        self.dnmapH2.setObjectName("dnmapH2")
        self.gridLayout_711.addWidget(self.dnmapH2, 2, 0, 1, 1)
        self.dnmapH1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_86)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dnmapH1.setFont(font)
        self.dnmapH1.setStyleSheet("color: rgb(56, 196, 255);\n"
"")
        self.dnmapH1.setObjectName("dnmapH1")
        self.gridLayout_711.addWidget(self.dnmapH1, 0, 0, 1, 1)
        self.dnmapB2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_86)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dnmapB2.setFont(font)
        self.dnmapB2.setStyleSheet("color: rgb(255, 255, 255);")
        self.dnmapB2.setObjectName("dnmapB2")
        self.gridLayout_711.addWidget(self.dnmapB2, 3, 0, 1, 1)
        self.dnmapH3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_86)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dnmapH3.setFont(font)
        self.dnmapH3.setStyleSheet("color: rgb(56, 196, 255);\n"
"")
        self.dnmapH3.setObjectName("dnmapH3")
        self.gridLayout_711.addWidget(self.dnmapH3, 4, 0, 1, 1)
        self.dnmapB4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_86)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dnmapB4.setFont(font)
        self.dnmapB4.setStyleSheet("color: rgb(255, 255, 255);")
        self.dnmapB4.setObjectName("dnmapB4")
        self.gridLayout_711.addWidget(self.dnmapB4, 6, 0, 1, 1)
        self.dnmapScrollArea.setWidget(self.scrollAreaWidgetContents_86)
        self.gridLayout_511.addWidget(self.dnmapScrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.dnmapTab, "")
        self.dnsenumTab = QtWidgets.QWidget()
        self.dnsenumTab.setObjectName("dnsenumTab")
        self.gridLayout_512 = QtWidgets.QGridLayout(self.dnsenumTab)
        self.gridLayout_512.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_512.setSpacing(6)
        self.gridLayout_512.setObjectName("gridLayout_512")
        self.dnsenumTitle = QtWidgets.QLabel(self.dnsenumTab)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.dnsenumTitle.setFont(font)
        self.dnsenumTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.dnsenumTitle.setObjectName("dnsenumTitle")
        self.gridLayout_512.addWidget(self.dnsenumTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.dnsenumScrollArea = QtWidgets.QScrollArea(self.dnsenumTab)
        self.dnsenumScrollArea.setWidgetResizable(True)
        self.dnsenumScrollArea.setObjectName("dnsenumScrollArea")
        self.scrollAreaWidgetContents_87 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_87.setGeometry(QtCore.QRect(0, 0, 3128, 2031))
        self.scrollAreaWidgetContents_87.setObjectName("scrollAreaWidgetContents_87")
        self.gridLayout_712 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_87)
        self.gridLayout_712.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_712.setSpacing(6)
        self.gridLayout_712.setObjectName("gridLayout_712")
        self.dnsenumButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_87)
        self.dnsenumButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.dnsenumButton.setObjectName("dnsenumButton")
        self.gridLayout_712.addWidget(self.dnsenumButton, 7, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_712.addItem(spacerItem13, 8, 0, 1, 1)
        self.dnsenumH4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_87)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dnsenumH4.setFont(font)
        self.dnsenumH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.dnsenumH4.setObjectName("dnsenumH4")
        self.gridLayout_712.addWidget(self.dnsenumH4, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.dnsenumB3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_87)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dnsenumB3.setFont(font)
        self.dnsenumB3.setStyleSheet("color: rgb(255, 255, 255);")
        self.dnsenumB3.setObjectName("dnsenumB3")
        self.gridLayout_712.addWidget(self.dnsenumB3, 5, 0, 1, 1)
        self.dnsenumB1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_87)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dnsenumB1.setFont(font)
        self.dnsenumB1.setStyleSheet("color: rgb(255, 255, 255);")
        self.dnsenumB1.setObjectName("dnsenumB1")
        self.gridLayout_712.addWidget(self.dnsenumB1, 1, 0, 1, 1)
        self.dnsenumH2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_87)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dnsenumH2.setFont(font)
        self.dnsenumH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.dnsenumH2.setObjectName("dnsenumH2")
        self.gridLayout_712.addWidget(self.dnsenumH2, 2, 0, 1, 1)
        self.dnsenumH1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_87)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dnsenumH1.setFont(font)
        self.dnsenumH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.dnsenumH1.setObjectName("dnsenumH1")
        self.gridLayout_712.addWidget(self.dnsenumH1, 0, 0, 1, 1)
        self.dnsenumB2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_87)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dnsenumB2.setFont(font)
        self.dnsenumB2.setStyleSheet("color: rgb(255, 255, 255);")
        self.dnsenumB2.setObjectName("dnsenumB2")
        self.gridLayout_712.addWidget(self.dnsenumB2, 3, 0, 1, 1)
        self.dnsenumH3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_87)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dnsenumH3.setFont(font)
        self.dnsenumH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.dnsenumH3.setObjectName("dnsenumH3")
        self.gridLayout_712.addWidget(self.dnsenumH3, 4, 0, 1, 1)
        self.dnsenumScrollArea.setWidget(self.scrollAreaWidgetContents_87)
        self.gridLayout_512.addWidget(self.dnsenumScrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.dnsenumTab, "")
        self.dnsmapTab = QtWidgets.QWidget()
        self.dnsmapTab.setObjectName("dnsmapTab")
        self.gridLayout_513 = QtWidgets.QGridLayout(self.dnsmapTab)
        self.gridLayout_513.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_513.setSpacing(6)
        self.gridLayout_513.setObjectName("gridLayout_513")
        self.dnsmapTitle = QtWidgets.QLabel(self.dnsmapTab)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.dnsmapTitle.setFont(font)
        self.dnsmapTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.dnsmapTitle.setObjectName("dnsmapTitle")
        self.gridLayout_513.addWidget(self.dnsmapTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.dnsmapScrollArea = QtWidgets.QScrollArea(self.dnsmapTab)
        self.dnsmapScrollArea.setWidgetResizable(True)
        self.dnsmapScrollArea.setObjectName("dnsmapScrollArea")
        self.scrollAreaWidgetContents_88 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_88.setGeometry(QtCore.QRect(0, 0, 3128, 1500))
        self.scrollAreaWidgetContents_88.setObjectName("scrollAreaWidgetContents_88")
        self.gridLayout_713 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_88)
        self.gridLayout_713.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_713.setSpacing(6)
        self.gridLayout_713.setObjectName("gridLayout_713")
        self.dnsmapButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_88)
        self.dnsmapButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.dnsmapButton.setObjectName("dnsmapButton")
        self.gridLayout_713.addWidget(self.dnsmapButton, 8, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_713.addItem(spacerItem14, 9, 0, 1, 1)
        self.dnsmapH4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_88)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dnsmapH4.setFont(font)
        self.dnsmapH4.setStyleSheet("color: rgb(56, 196, 255);\n"
"")
        self.dnsmapH4.setObjectName("dnsmapH4")
        self.gridLayout_713.addWidget(self.dnsmapH4, 7, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.dnsmapB3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_88)
        self.dnsmapB3.setStyleSheet("color: rgb(255, 255, 255);")
        self.dnsmapB3.setObjectName("dnsmapB3")
        self.gridLayout_713.addWidget(self.dnsmapB3, 5, 0, 1, 1)
        self.dnsmapB1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_88)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dnsmapB1.setFont(font)
        self.dnsmapB1.setStyleSheet("color: rgb(255, 255, 255);")
        self.dnsmapB1.setObjectName("dnsmapB1")
        self.gridLayout_713.addWidget(self.dnsmapB1, 1, 0, 1, 1)
        self.dnsmapH2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_88)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dnsmapH2.setFont(font)
        self.dnsmapH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.dnsmapH2.setObjectName("dnsmapH2")
        self.gridLayout_713.addWidget(self.dnsmapH2, 2, 0, 1, 1)
        self.dnsmapH1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_88)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dnsmapH1.setFont(font)
        self.dnsmapH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.dnsmapH1.setObjectName("dnsmapH1")
        self.gridLayout_713.addWidget(self.dnsmapH1, 0, 0, 1, 1)
        self.dnsmapB2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_88)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dnsmapB2.setFont(font)
        self.dnsmapB2.setStyleSheet("color: rgb(255, 255, 255);")
        self.dnsmapB2.setObjectName("dnsmapB2")
        self.gridLayout_713.addWidget(self.dnsmapB2, 3, 0, 1, 1)
        self.dnsmapH3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_88)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dnsmapH3.setFont(font)
        self.dnsmapH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.dnsmapH3.setObjectName("dnsmapH3")
        self.gridLayout_713.addWidget(self.dnsmapH3, 4, 0, 1, 1)
        self.dnsmapB4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_88)
        self.dnsmapB4.setStyleSheet("color: rgb(255, 255, 255);")
        self.dnsmapB4.setObjectName("dnsmapB4")
        self.gridLayout_713.addWidget(self.dnsmapB4, 6, 0, 1, 1)
        self.dnsmapScrollArea.setWidget(self.scrollAreaWidgetContents_88)
        self.gridLayout_513.addWidget(self.dnsmapScrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.dnsmapTab, "")
        self.DNSReconTab = QtWidgets.QWidget()
        self.DNSReconTab.setObjectName("DNSReconTab")
        self.gridLayout_514 = QtWidgets.QGridLayout(self.DNSReconTab)
        self.gridLayout_514.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_514.setSpacing(6)
        self.gridLayout_514.setObjectName("gridLayout_514")
        self.DNSReconTitle = QtWidgets.QLabel(self.DNSReconTab)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.DNSReconTitle.setFont(font)
        self.DNSReconTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.DNSReconTitle.setObjectName("DNSReconTitle")
        self.gridLayout_514.addWidget(self.DNSReconTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.DNSReconScrollArea = QtWidgets.QScrollArea(self.DNSReconTab)
        self.DNSReconScrollArea.setWidgetResizable(True)
        self.DNSReconScrollArea.setObjectName("DNSReconScrollArea")
        self.scrollAreaWidgetContents_89 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_89.setGeometry(QtCore.QRect(0, 0, 3128, 2099))
        self.scrollAreaWidgetContents_89.setObjectName("scrollAreaWidgetContents_89")
        self.gridLayout_714 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_89)
        self.gridLayout_714.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_714.setSpacing(6)
        self.gridLayout_714.setObjectName("gridLayout_714")
        self.DNSReconButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_89)
        self.DNSReconButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.DNSReconButton.setObjectName("DNSReconButton")
        self.gridLayout_714.addWidget(self.DNSReconButton, 7, 0, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_714.addItem(spacerItem15, 8, 0, 1, 1)
        self.DNSReconH4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_89)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.DNSReconH4.setFont(font)
        self.DNSReconH4.setStyleSheet("color: rgb(56, 196, 255);\n"
"")
        self.DNSReconH4.setObjectName("DNSReconH4")
        self.gridLayout_714.addWidget(self.DNSReconH4, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.DNSReconB3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_89)
        self.DNSReconB3.setStyleSheet("color: rgb(255, 255, 255);")
        self.DNSReconB3.setObjectName("DNSReconB3")
        self.gridLayout_714.addWidget(self.DNSReconB3, 5, 0, 1, 1)
        self.DNSReconB1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_89)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.DNSReconB1.setFont(font)
        self.DNSReconB1.setStyleSheet("color: rgb(255, 255, 255);")
        self.DNSReconB1.setObjectName("DNSReconB1")
        self.gridLayout_714.addWidget(self.DNSReconB1, 1, 0, 1, 1)
        self.DNSReconH2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_89)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.DNSReconH2.setFont(font)
        self.DNSReconH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.DNSReconH2.setObjectName("DNSReconH2")
        self.gridLayout_714.addWidget(self.DNSReconH2, 2, 0, 1, 1)
        self.DNSReconH1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_89)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.DNSReconH1.setFont(font)
        self.DNSReconH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.DNSReconH1.setObjectName("DNSReconH1")
        self.gridLayout_714.addWidget(self.DNSReconH1, 0, 0, 1, 1)
        self.DNSReconB2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_89)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.DNSReconB2.setFont(font)
        self.DNSReconB2.setStyleSheet("color: rgb(255, 255, 255);")
        self.DNSReconB2.setObjectName("DNSReconB2")
        self.gridLayout_714.addWidget(self.DNSReconB2, 3, 0, 1, 1)
        self.DNSReconH3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_89)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.DNSReconH3.setFont(font)
        self.DNSReconH3.setStyleSheet("color: rgb(56, 196, 255);\n"
"")
        self.DNSReconH3.setObjectName("DNSReconH3")
        self.gridLayout_714.addWidget(self.DNSReconH3, 4, 0, 1, 1)
        self.DNSReconScrollArea.setWidget(self.scrollAreaWidgetContents_89)
        self.gridLayout_514.addWidget(self.DNSReconScrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.DNSReconTab, "")
        self.dnstracerTab = QtWidgets.QWidget()
        self.dnstracerTab.setObjectName("dnstracerTab")
        self.gridLayout_515 = QtWidgets.QGridLayout(self.dnstracerTab)
        self.gridLayout_515.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_515.setSpacing(6)
        self.gridLayout_515.setObjectName("gridLayout_515")
        self.dnstracerTitle = QtWidgets.QLabel(self.dnstracerTab)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.dnstracerTitle.setFont(font)
        self.dnstracerTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.dnstracerTitle.setObjectName("dnstracerTitle")
        self.gridLayout_515.addWidget(self.dnstracerTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.dnstracerScrollArea = QtWidgets.QScrollArea(self.dnstracerTab)
        self.dnstracerScrollArea.setWidgetResizable(True)
        self.dnstracerScrollArea.setObjectName("dnstracerScrollArea")
        self.scrollAreaWidgetContents_810 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_810.setGeometry(QtCore.QRect(0, 0, 3128, 973))
        self.scrollAreaWidgetContents_810.setObjectName("scrollAreaWidgetContents_810")
        self.gridLayout_715 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_810)
        self.gridLayout_715.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_715.setSpacing(6)
        self.gridLayout_715.setObjectName("gridLayout_715")
        self.dnstracerButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_810)
        self.dnstracerButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.dnstracerButton.setObjectName("dnstracerButton")
        self.gridLayout_715.addWidget(self.dnstracerButton, 7, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_715.addItem(spacerItem16, 8, 0, 1, 1)
        self.dnstracerH4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_810)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dnstracerH4.setFont(font)
        self.dnstracerH4.setStyleSheet("color: rgb(56, 196, 255);\n"
"")
        self.dnstracerH4.setObjectName("dnstracerH4")
        self.gridLayout_715.addWidget(self.dnstracerH4, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.dnstracerB3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_810)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dnstracerB3.setFont(font)
        self.dnstracerB3.setStyleSheet("color: rgb(255, 255, 255);")
        self.dnstracerB3.setObjectName("dnstracerB3")
        self.gridLayout_715.addWidget(self.dnstracerB3, 5, 0, 1, 1)
        self.dnstracerB1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_810)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dnstracerB1.setFont(font)
        self.dnstracerB1.setStyleSheet("color: rgb(255, 255, 255);")
        self.dnstracerB1.setObjectName("dnstracerB1")
        self.gridLayout_715.addWidget(self.dnstracerB1, 1, 0, 1, 1)
        self.dnstracerH2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_810)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dnstracerH2.setFont(font)
        self.dnstracerH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.dnstracerH2.setObjectName("dnstracerH2")
        self.gridLayout_715.addWidget(self.dnstracerH2, 2, 0, 1, 1)
        self.dnstracerH1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_810)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dnstracerH1.setFont(font)
        self.dnstracerH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.dnstracerH1.setObjectName("dnstracerH1")
        self.gridLayout_715.addWidget(self.dnstracerH1, 0, 0, 1, 1)
        self.dnstracerB2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_810)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dnstracerB2.setFont(font)
        self.dnstracerB2.setStyleSheet("color: rgb(255, 255, 255);")
        self.dnstracerB2.setObjectName("dnstracerB2")
        self.gridLayout_715.addWidget(self.dnstracerB2, 3, 0, 1, 1)
        self.dnstracerH3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_810)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dnstracerH3.setFont(font)
        self.dnstracerH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.dnstracerH3.setObjectName("dnstracerH3")
        self.gridLayout_715.addWidget(self.dnstracerH3, 4, 0, 1, 1)
        self.dnstracerScrollArea.setWidget(self.scrollAreaWidgetContents_810)
        self.gridLayout_515.addWidget(self.dnstracerScrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.dnstracerTab, "")
        self.dnswalkTab = QtWidgets.QWidget()
        self.dnswalkTab.setObjectName("dnswalkTab")
        self.gridLayout_516 = QtWidgets.QGridLayout(self.dnswalkTab)
        self.gridLayout_516.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_516.setSpacing(6)
        self.gridLayout_516.setObjectName("gridLayout_516")
        self.dnswalkTitle = QtWidgets.QLabel(self.dnswalkTab)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.dnswalkTitle.setFont(font)
        self.dnswalkTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.dnswalkTitle.setObjectName("dnswalkTitle")
        self.gridLayout_516.addWidget(self.dnswalkTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.dnswalkScrollArea = QtWidgets.QScrollArea(self.dnswalkTab)
        self.dnswalkScrollArea.setWidgetResizable(True)
        self.dnswalkScrollArea.setObjectName("dnswalkScrollArea")
        self.scrollAreaWidgetContents_811 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_811.setGeometry(QtCore.QRect(0, 0, 3128, 1233))
        self.scrollAreaWidgetContents_811.setObjectName("scrollAreaWidgetContents_811")
        self.gridLayout_716 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_811)
        self.gridLayout_716.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_716.setSpacing(6)
        self.gridLayout_716.setObjectName("gridLayout_716")
        self.dnswalkButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_811)
        self.dnswalkButton.setObjectName("dnswalkButton")
        self.gridLayout_716.addWidget(self.dnswalkButton, 8, 0, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_716.addItem(spacerItem17, 9, 0, 1, 1)
        self.dnswalkH4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_811)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dnswalkH4.setFont(font)
        self.dnswalkH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.dnswalkH4.setObjectName("dnswalkH4")
        self.gridLayout_716.addWidget(self.dnswalkH4, 7, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.dnswalkB3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_811)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dnswalkB3.setFont(font)
        self.dnswalkB3.setStyleSheet("color: rgb(255, 255, 255);")
        self.dnswalkB3.setObjectName("dnswalkB3")
        self.gridLayout_716.addWidget(self.dnswalkB3, 5, 0, 1, 1)
        self.dnswalkB1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_811)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dnswalkB1.setFont(font)
        self.dnswalkB1.setStyleSheet("color: rgb(255, 255, 255);")
        self.dnswalkB1.setObjectName("dnswalkB1")
        self.gridLayout_716.addWidget(self.dnswalkB1, 1, 0, 1, 1)
        self.dnswalkH2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_811)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dnswalkH2.setFont(font)
        self.dnswalkH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.dnswalkH2.setObjectName("dnswalkH2")
        self.gridLayout_716.addWidget(self.dnswalkH2, 2, 0, 1, 1)
        self.dnswalkH1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_811)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dnswalkH1.setFont(font)
        self.dnswalkH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.dnswalkH1.setObjectName("dnswalkH1")
        self.gridLayout_716.addWidget(self.dnswalkH1, 0, 0, 1, 1)
        self.dnswalkB2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_811)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dnswalkB2.setFont(font)
        self.dnswalkB2.setStyleSheet("color: rgb(255, 255, 255);")
        self.dnswalkB2.setObjectName("dnswalkB2")
        self.gridLayout_716.addWidget(self.dnswalkB2, 3, 0, 1, 1)
        self.dnswalkH3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_811)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dnswalkH3.setFont(font)
        self.dnswalkH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.dnswalkH3.setObjectName("dnswalkH3")
        self.gridLayout_716.addWidget(self.dnswalkH3, 4, 0, 1, 1)
        self.dnswalkB4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_811)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dnswalkB4.setFont(font)
        self.dnswalkB4.setStyleSheet("color: rgb(255, 255, 255);")
        self.dnswalkB4.setObjectName("dnswalkB4")
        self.gridLayout_716.addWidget(self.dnswalkB4, 6, 0, 1, 1)
        self.dnswalkScrollArea.setWidget(self.scrollAreaWidgetContents_811)
        self.gridLayout_516.addWidget(self.dnswalkScrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.dnswalkTab, "")
        self.DotDotPwnTab = QtWidgets.QWidget()
        self.DotDotPwnTab.setObjectName("DotDotPwnTab")
        self.gridLayout_517 = QtWidgets.QGridLayout(self.DotDotPwnTab)
        self.gridLayout_517.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_517.setSpacing(6)
        self.gridLayout_517.setObjectName("gridLayout_517")
        self.DotDotPwnTitle = QtWidgets.QLabel(self.DotDotPwnTab)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.DotDotPwnTitle.setFont(font)
        self.DotDotPwnTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.DotDotPwnTitle.setObjectName("DotDotPwnTitle")
        self.gridLayout_517.addWidget(self.DotDotPwnTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.DotDotPwnScrollArea = QtWidgets.QScrollArea(self.DotDotPwnTab)
        self.DotDotPwnScrollArea.setWidgetResizable(True)
        self.DotDotPwnScrollArea.setObjectName("DotDotPwnScrollArea")
        self.scrollAreaWidgetContents_812 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_812.setGeometry(QtCore.QRect(0, 0, 3128, 2928))
        self.scrollAreaWidgetContents_812.setObjectName("scrollAreaWidgetContents_812")
        self.gridLayout_717 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_812)
        self.gridLayout_717.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_717.setSpacing(6)
        self.gridLayout_717.setObjectName("gridLayout_717")
        self.DotDotPwnButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_812)
        self.DotDotPwnButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.DotDotPwnButton.setObjectName("DotDotPwnButton")
        self.gridLayout_717.addWidget(self.DotDotPwnButton, 7, 0, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_717.addItem(spacerItem18, 8, 0, 1, 1)
        self.DotDotPwnH4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_812)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.DotDotPwnH4.setFont(font)
        self.DotDotPwnH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.DotDotPwnH4.setObjectName("DotDotPwnH4")
        self.gridLayout_717.addWidget(self.DotDotPwnH4, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.DotDotPwnB3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_812)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.DotDotPwnB3.setFont(font)
        self.DotDotPwnB3.setStyleSheet("color: rgb(255, 255, 255);")
        self.DotDotPwnB3.setObjectName("DotDotPwnB3")
        self.gridLayout_717.addWidget(self.DotDotPwnB3, 5, 0, 1, 1)
        self.DotDotPwnB1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_812)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.DotDotPwnB1.setFont(font)
        self.DotDotPwnB1.setStyleSheet("color: rgb(255, 255, 255);")
        self.DotDotPwnB1.setObjectName("DotDotPwnB1")
        self.gridLayout_717.addWidget(self.DotDotPwnB1, 1, 0, 1, 1)
        self.DotDotPwnH2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_812)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.DotDotPwnH2.setFont(font)
        self.DotDotPwnH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.DotDotPwnH2.setObjectName("DotDotPwnH2")
        self.gridLayout_717.addWidget(self.DotDotPwnH2, 2, 0, 1, 1)
        self.DotDotPwnH1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_812)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.DotDotPwnH1.setFont(font)
        self.DotDotPwnH1.setStyleSheet("color: rgb(56, 196, 255);\n"
"")
        self.DotDotPwnH1.setObjectName("DotDotPwnH1")
        self.gridLayout_717.addWidget(self.DotDotPwnH1, 0, 0, 1, 1)
        self.DotDotPwnB2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_812)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.DotDotPwnB2.setFont(font)
        self.DotDotPwnB2.setStyleSheet("color: rgb(255, 255, 255);")
        self.DotDotPwnB2.setObjectName("DotDotPwnB2")
        self.gridLayout_717.addWidget(self.DotDotPwnB2, 3, 0, 1, 1)
        self.DotDotPwnH3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_812)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.DotDotPwnH3.setFont(font)
        self.DotDotPwnH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.DotDotPwnH3.setObjectName("DotDotPwnH3")
        self.gridLayout_717.addWidget(self.DotDotPwnH3, 4, 0, 1, 1)
        self.DotDotPwnScrollArea.setWidget(self.scrollAreaWidgetContents_812)
        self.gridLayout_517.addWidget(self.DotDotPwnScrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.DotDotPwnTab, "")
        self.enum4linuxTab = QtWidgets.QWidget()
        self.enum4linuxTab.setObjectName("enum4linuxTab")
        self.gridLayout_518 = QtWidgets.QGridLayout(self.enum4linuxTab)
        self.gridLayout_518.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_518.setSpacing(6)
        self.gridLayout_518.setObjectName("gridLayout_518")
        self.enum4linuxTitle = QtWidgets.QLabel(self.enum4linuxTab)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.enum4linuxTitle.setFont(font)
        self.enum4linuxTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.enum4linuxTitle.setObjectName("enum4linuxTitle")
        self.gridLayout_518.addWidget(self.enum4linuxTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.enum4linuxScrollArea = QtWidgets.QScrollArea(self.enum4linuxTab)
        self.enum4linuxScrollArea.setWidgetResizable(True)
        self.enum4linuxScrollArea.setObjectName("enum4linuxScrollArea")
        self.scrollAreaWidgetContents_813 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_813.setGeometry(QtCore.QRect(0, 0, 3128, 2560))
        self.scrollAreaWidgetContents_813.setObjectName("scrollAreaWidgetContents_813")
        self.gridLayout_718 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_813)
        self.gridLayout_718.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_718.setSpacing(6)
        self.gridLayout_718.setObjectName("gridLayout_718")
        self.enum4linuxButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_813)
        self.enum4linuxButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.enum4linuxButton.setObjectName("enum4linuxButton")
        self.gridLayout_718.addWidget(self.enum4linuxButton, 7, 0, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_718.addItem(spacerItem19, 8, 0, 1, 1)
        self.enum4linuxH4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_813)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.enum4linuxH4.setFont(font)
        self.enum4linuxH4.setStyleSheet("color: rgb(56, 196, 255);\n"
"")
        self.enum4linuxH4.setObjectName("enum4linuxH4")
        self.gridLayout_718.addWidget(self.enum4linuxH4, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.enum4linuxB3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_813)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.enum4linuxB3.setFont(font)
        self.enum4linuxB3.setStyleSheet("color: rgb(255, 255, 255);")
        self.enum4linuxB3.setObjectName("enum4linuxB3")
        self.gridLayout_718.addWidget(self.enum4linuxB3, 5, 0, 1, 1)
        self.enum4linuxB1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_813)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.enum4linuxB1.setFont(font)
        self.enum4linuxB1.setStyleSheet("color: rgb(255, 255, 255);")
        self.enum4linuxB1.setObjectName("enum4linuxB1")
        self.gridLayout_718.addWidget(self.enum4linuxB1, 1, 0, 1, 1)
        self.enum4linuxH2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_813)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.enum4linuxH2.setFont(font)
        self.enum4linuxH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.enum4linuxH2.setObjectName("enum4linuxH2")
        self.gridLayout_718.addWidget(self.enum4linuxH2, 2, 0, 1, 1)
        self.enum4linuxH1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_813)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.enum4linuxH1.setFont(font)
        self.enum4linuxH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.enum4linuxH1.setObjectName("enum4linuxH1")
        self.gridLayout_718.addWidget(self.enum4linuxH1, 0, 0, 1, 1)
        self.enum4linuxB2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_813)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.enum4linuxB2.setFont(font)
        self.enum4linuxB2.setStyleSheet("color: rgb(255, 255, 255);")
        self.enum4linuxB2.setObjectName("enum4linuxB2")
        self.gridLayout_718.addWidget(self.enum4linuxB2, 3, 0, 1, 1)
        self.enum4linuxH3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_813)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.enum4linuxH3.setFont(font)
        self.enum4linuxH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.enum4linuxH3.setObjectName("enum4linuxH3")
        self.gridLayout_718.addWidget(self.enum4linuxH3, 4, 0, 1, 1)
        self.enum4linuxScrollArea.setWidget(self.scrollAreaWidgetContents_813)
        self.gridLayout_518.addWidget(self.enum4linuxScrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.enum4linuxTab, "")
        self.enumIAXTab = QtWidgets.QWidget()
        self.enumIAXTab.setObjectName("enumIAXTab")
        self.gridLayout_519 = QtWidgets.QGridLayout(self.enumIAXTab)
        self.gridLayout_519.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_519.setSpacing(6)
        self.gridLayout_519.setObjectName("gridLayout_519")
        self.enumIAXTitle = QtWidgets.QLabel(self.enumIAXTab)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.enumIAXTitle.setFont(font)
        self.enumIAXTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.enumIAXTitle.setObjectName("enumIAXTitle")
        self.gridLayout_519.addWidget(self.enumIAXTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.enumIAXScrollArea = QtWidgets.QScrollArea(self.enumIAXTab)
        self.enumIAXScrollArea.setWidgetResizable(True)
        self.enumIAXScrollArea.setObjectName("enumIAXScrollArea")
        self.scrollAreaWidgetContents_814 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_814.setGeometry(QtCore.QRect(0, 0, 3128, 904))
        self.scrollAreaWidgetContents_814.setObjectName("scrollAreaWidgetContents_814")
        self.gridLayout_719 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_814)
        self.gridLayout_719.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_719.setSpacing(6)
        self.gridLayout_719.setObjectName("gridLayout_719")
        self.enumIAXButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_814)
        self.enumIAXButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.enumIAXButton.setObjectName("enumIAXButton")
        self.gridLayout_719.addWidget(self.enumIAXButton, 7, 0, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_719.addItem(spacerItem20, 8, 0, 1, 1)
        self.enumIAXH4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_814)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.enumIAXH4.setFont(font)
        self.enumIAXH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.enumIAXH4.setObjectName("enumIAXH4")
        self.gridLayout_719.addWidget(self.enumIAXH4, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.enumIAXB3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_814)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.enumIAXB3.setFont(font)
        self.enumIAXB3.setStyleSheet("color: rgb(255, 255, 255);")
        self.enumIAXB3.setObjectName("enumIAXB3")
        self.gridLayout_719.addWidget(self.enumIAXB3, 5, 0, 1, 1)
        self.enumIAXB1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_814)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.enumIAXB1.setFont(font)
        self.enumIAXB1.setStyleSheet("color: rgb(255, 255, 255);")
        self.enumIAXB1.setObjectName("enumIAXB1")
        self.gridLayout_719.addWidget(self.enumIAXB1, 1, 0, 1, 1)
        self.enumIAXH2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_814)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.enumIAXH2.setFont(font)
        self.enumIAXH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.enumIAXH2.setObjectName("enumIAXH2")
        self.gridLayout_719.addWidget(self.enumIAXH2, 2, 0, 1, 1)
        self.enumIAXH1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_814)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.enumIAXH1.setFont(font)
        self.enumIAXH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.enumIAXH1.setObjectName("enumIAXH1")
        self.gridLayout_719.addWidget(self.enumIAXH1, 0, 0, 1, 1)
        self.enumIAXB2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_814)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.enumIAXB2.setFont(font)
        self.enumIAXB2.setStyleSheet("color: rgb(255, 255, 255);")
        self.enumIAXB2.setObjectName("enumIAXB2")
        self.gridLayout_719.addWidget(self.enumIAXB2, 3, 0, 1, 1)
        self.enumIAXH3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_814)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.enumIAXH3.setFont(font)
        self.enumIAXH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.enumIAXH3.setObjectName("enumIAXH3")
        self.gridLayout_719.addWidget(self.enumIAXH3, 4, 0, 1, 1)
        self.enumIAXScrollArea.setWidget(self.scrollAreaWidgetContents_814)
        self.gridLayout_519.addWidget(self.enumIAXScrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.enumIAXTab, "")
        self.Faraday = QtWidgets.QWidget()
        self.Faraday.setObjectName("Faraday")
        self.gridLayout_520 = QtWidgets.QGridLayout(self.Faraday)
        self.gridLayout_520.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_520.setSpacing(6)
        self.gridLayout_520.setObjectName("gridLayout_520")
        self.FaradayTitle = QtWidgets.QLabel(self.Faraday)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.FaradayTitle.setFont(font)
        self.FaradayTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.FaradayTitle.setObjectName("FaradayTitle")
        self.gridLayout_520.addWidget(self.FaradayTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.FaradayScrollArea = QtWidgets.QScrollArea(self.Faraday)
        self.FaradayScrollArea.setWidgetResizable(True)
        self.FaradayScrollArea.setObjectName("FaradayScrollArea")
        self.scrollAreaWidgetContents_815 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_815.setGeometry(QtCore.QRect(0, 0, 3128, 3947))
        self.scrollAreaWidgetContents_815.setObjectName("scrollAreaWidgetContents_815")
        self.gridLayout_720 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_815)
        self.gridLayout_720.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_720.setSpacing(6)
        self.gridLayout_720.setObjectName("gridLayout_720")
        self.FaradayButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_815)
        self.FaradayButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.FaradayButton.setObjectName("FaradayButton")
        self.gridLayout_720.addWidget(self.FaradayButton, 8, 0, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_720.addItem(spacerItem21, 9, 0, 1, 1)
        self.FaradayH4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_815)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.FaradayH4.setFont(font)
        self.FaradayH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.FaradayH4.setObjectName("FaradayH4")
        self.gridLayout_720.addWidget(self.FaradayH4, 7, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.FaradayB3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_815)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.FaradayB3.setFont(font)
        self.FaradayB3.setStyleSheet("color: rgb(255, 255, 255);")
        self.FaradayB3.setObjectName("FaradayB3")
        self.gridLayout_720.addWidget(self.FaradayB3, 5, 0, 1, 1)
        self.FaradayB1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_815)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.FaradayB1.setFont(font)
        self.FaradayB1.setStyleSheet("color: rgb(255, 255, 255);")
        self.FaradayB1.setObjectName("FaradayB1")
        self.gridLayout_720.addWidget(self.FaradayB1, 1, 0, 1, 1)
        self.FaradayH2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_815)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.FaradayH2.setFont(font)
        self.FaradayH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.FaradayH2.setObjectName("FaradayH2")
        self.gridLayout_720.addWidget(self.FaradayH2, 2, 0, 1, 1)
        self.FaradayH1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_815)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.FaradayH1.setFont(font)
        self.FaradayH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.FaradayH1.setObjectName("FaradayH1")
        self.gridLayout_720.addWidget(self.FaradayH1, 0, 0, 1, 1)
        self.FaradayB2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_815)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.FaradayB2.setFont(font)
        self.FaradayB2.setStyleSheet("color: rgb(255, 255, 255);")
        self.FaradayB2.setObjectName("FaradayB2")
        self.gridLayout_720.addWidget(self.FaradayB2, 3, 0, 1, 1)
        self.FaradayH3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_815)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.FaradayH3.setFont(font)
        self.FaradayH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.FaradayH3.setObjectName("FaradayH3")
        self.gridLayout_720.addWidget(self.FaradayH3, 4, 0, 1, 1)
        self.FaradayB4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_815)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.FaradayB4.setFont(font)
        self.FaradayB4.setStyleSheet("color: rgb(255, 255, 255);")
        self.FaradayB4.setObjectName("FaradayB4")
        self.gridLayout_720.addWidget(self.FaradayB4, 6, 0, 1, 1)
        self.FaradayScrollArea.setWidget(self.scrollAreaWidgetContents_815)
        self.gridLayout_520.addWidget(self.FaradayScrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.Faraday, "")
        self.FierceTab = QtWidgets.QWidget()
        self.FierceTab.setObjectName("FierceTab")
        self.gridLayout_521 = QtWidgets.QGridLayout(self.FierceTab)
        self.gridLayout_521.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_521.setSpacing(6)
        self.gridLayout_521.setObjectName("gridLayout_521")
        self.FierceTitle = QtWidgets.QLabel(self.FierceTab)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.FierceTitle.setFont(font)
        self.FierceTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.FierceTitle.setObjectName("FierceTitle")
        self.gridLayout_521.addWidget(self.FierceTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.FierceScrollArea = QtWidgets.QScrollArea(self.FierceTab)
        self.FierceScrollArea.setWidgetResizable(True)
        self.FierceScrollArea.setObjectName("FierceScrollArea")
        self.scrollAreaWidgetContents_816 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_816.setGeometry(QtCore.QRect(0, 0, 3128, 2974))
        self.scrollAreaWidgetContents_816.setObjectName("scrollAreaWidgetContents_816")
        self.gridLayout_721 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_816)
        self.gridLayout_721.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_721.setSpacing(6)
        self.gridLayout_721.setObjectName("gridLayout_721")
        self.FierceButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_816)
        self.FierceButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.FierceButton.setObjectName("FierceButton")
        self.gridLayout_721.addWidget(self.FierceButton, 7, 0, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_721.addItem(spacerItem22, 8, 0, 1, 1)
        self.FierceH4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_816)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.FierceH4.setFont(font)
        self.FierceH4.setStyleSheet("color: rgb(56, 196, 255);\n"
"")
        self.FierceH4.setObjectName("FierceH4")
        self.gridLayout_721.addWidget(self.FierceH4, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.FierceB3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_816)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.FierceB3.setFont(font)
        self.FierceB3.setStyleSheet("color: rgb(255, 255, 255);")
        self.FierceB3.setObjectName("FierceB3")
        self.gridLayout_721.addWidget(self.FierceB3, 5, 0, 1, 1)
        self.FierceB1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_816)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.FierceB1.setFont(font)
        self.FierceB1.setStyleSheet("color: rgb(255, 255, 255);")
        self.FierceB1.setObjectName("FierceB1")
        self.gridLayout_721.addWidget(self.FierceB1, 1, 0, 1, 1)
        self.FierceH2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_816)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.FierceH2.setFont(font)
        self.FierceH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.FierceH2.setObjectName("FierceH2")
        self.gridLayout_721.addWidget(self.FierceH2, 2, 0, 1, 1)
        self.FierceH1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_816)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.FierceH1.setFont(font)
        self.FierceH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.FierceH1.setObjectName("FierceH1")
        self.gridLayout_721.addWidget(self.FierceH1, 0, 0, 1, 1)
        self.FierceB2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_816)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.FierceB2.setFont(font)
        self.FierceB2.setStyleSheet("color: rgb(255, 255, 255);")
        self.FierceB2.setObjectName("FierceB2")
        self.gridLayout_721.addWidget(self.FierceB2, 3, 0, 1, 1)
        self.FierceH3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_816)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.FierceH3.setFont(font)
        self.FierceH3.setStyleSheet("color: rgb(56, 196, 255);\n"
"")
        self.FierceH3.setObjectName("FierceH3")
        self.gridLayout_721.addWidget(self.FierceH3, 4, 0, 1, 1)
        self.FierceScrollArea.setWidget(self.scrollAreaWidgetContents_816)
        self.gridLayout_521.addWidget(self.FierceScrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.FierceTab, "")
        self.FireWalkTab = QtWidgets.QWidget()
        self.FireWalkTab.setObjectName("FireWalkTab")
        self.gridLayout_522 = QtWidgets.QGridLayout(self.FireWalkTab)
        self.gridLayout_522.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_522.setSpacing(6)
        self.gridLayout_522.setObjectName("gridLayout_522")
        self.FireWalkTitle = QtWidgets.QLabel(self.FireWalkTab)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.FireWalkTitle.setFont(font)
        self.FireWalkTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.FireWalkTitle.setObjectName("FireWalkTitle")
        self.gridLayout_522.addWidget(self.FireWalkTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.FireWalkScrollArea = QtWidgets.QScrollArea(self.FireWalkTab)
        self.FireWalkScrollArea.setWidgetResizable(True)
        self.FireWalkScrollArea.setObjectName("FireWalkScrollArea")
        self.scrollAreaWidgetContents_817 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_817.setGeometry(QtCore.QRect(0, 0, 3128, 1778))
        self.scrollAreaWidgetContents_817.setObjectName("scrollAreaWidgetContents_817")
        self.gridLayout_722 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_817)
        self.gridLayout_722.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_722.setSpacing(6)
        self.gridLayout_722.setObjectName("gridLayout_722")
        self.FireWalkButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_817)
        self.FireWalkButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.FireWalkButton.setObjectName("FireWalkButton")
        self.gridLayout_722.addWidget(self.FireWalkButton, 7, 0, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_722.addItem(spacerItem23, 8, 0, 1, 1)
        self.FireWalkH4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_817)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.FireWalkH4.setFont(font)
        self.FireWalkH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.FireWalkH4.setObjectName("FireWalkH4")
        self.gridLayout_722.addWidget(self.FireWalkH4, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.FireWalkB3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_817)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.FireWalkB3.setFont(font)
        self.FireWalkB3.setStyleSheet("    color: rgb(255, 255, 255);")
        self.FireWalkB3.setObjectName("FireWalkB3")
        self.gridLayout_722.addWidget(self.FireWalkB3, 5, 0, 1, 1)
        self.FireWalkB1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_817)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.FireWalkB1.setFont(font)
        self.FireWalkB1.setStyleSheet("color: rgb(255, 255, 255);")
        self.FireWalkB1.setObjectName("FireWalkB1")
        self.gridLayout_722.addWidget(self.FireWalkB1, 1, 0, 1, 1)
        self.FireWalkH2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_817)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.FireWalkH2.setFont(font)
        self.FireWalkH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.FireWalkH2.setObjectName("FireWalkH2")
        self.gridLayout_722.addWidget(self.FireWalkH2, 2, 0, 1, 1)
        self.FireWalkH1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_817)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.FireWalkH1.setFont(font)
        self.FireWalkH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.FireWalkH1.setObjectName("FireWalkH1")
        self.gridLayout_722.addWidget(self.FireWalkH1, 0, 0, 1, 1)
        self.FireWalkB2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_817)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.FireWalkB2.setFont(font)
        self.FireWalkB2.setStyleSheet("color: rgb(255, 255, 255);")
        self.FireWalkB2.setObjectName("FireWalkB2")
        self.gridLayout_722.addWidget(self.FireWalkB2, 3, 0, 1, 1)
        self.FireWalkH3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_817)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.FireWalkH3.setFont(font)
        self.FireWalkH3.setStyleSheet("color: rgb(56, 196, 255);\n"
"")
        self.FireWalkH3.setObjectName("FireWalkH3")
        self.gridLayout_722.addWidget(self.FireWalkH3, 4, 0, 1, 1)
        self.FireWalkScrollArea.setWidget(self.scrollAreaWidgetContents_817)
        self.gridLayout_522.addWidget(self.FireWalkScrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.FireWalkTab, "")
        self.fragRouteTab = QtWidgets.QWidget()
        self.fragRouteTab.setObjectName("fragRouteTab")
        self.gridLayout_523 = QtWidgets.QGridLayout(self.fragRouteTab)
        self.gridLayout_523.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_523.setSpacing(6)
        self.gridLayout_523.setObjectName("gridLayout_523")
        self.fragRouteTitle = QtWidgets.QLabel(self.fragRouteTab)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.fragRouteTitle.setFont(font)
        self.fragRouteTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.fragRouteTitle.setObjectName("fragRouteTitle")
        self.gridLayout_523.addWidget(self.fragRouteTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.fragRouteScrollArea = QtWidgets.QScrollArea(self.fragRouteTab)
        self.fragRouteScrollArea.setWidgetResizable(True)
        self.fragRouteScrollArea.setObjectName("fragRouteScrollArea")
        self.scrollAreaWidgetContents_818 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_818.setGeometry(QtCore.QRect(0, 0, 3128, 1657))
        self.scrollAreaWidgetContents_818.setObjectName("scrollAreaWidgetContents_818")
        self.gridLayout_723 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_818)
        self.gridLayout_723.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_723.setSpacing(6)
        self.gridLayout_723.setObjectName("gridLayout_723")
        self.fragRouteButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_818)
        self.fragRouteButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.fragRouteButton.setObjectName("fragRouteButton")
        self.gridLayout_723.addWidget(self.fragRouteButton, 8, 0, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_723.addItem(spacerItem24, 9, 0, 1, 1)
        self.fragRouteH4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_818)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.fragRouteH4.setFont(font)
        self.fragRouteH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.fragRouteH4.setObjectName("fragRouteH4")
        self.gridLayout_723.addWidget(self.fragRouteH4, 7, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.fragRouteB3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_818)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fragRouteB3.setFont(font)
        self.fragRouteB3.setStyleSheet("color: rgb(255, 255, 255);")
        self.fragRouteB3.setObjectName("fragRouteB3")
        self.gridLayout_723.addWidget(self.fragRouteB3, 5, 0, 1, 1)
        self.fragRouteB1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_818)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fragRouteB1.setFont(font)
        self.fragRouteB1.setStyleSheet("color: rgb(255, 255, 255);")
        self.fragRouteB1.setObjectName("fragRouteB1")
        self.gridLayout_723.addWidget(self.fragRouteB1, 1, 0, 1, 1)
        self.fragRouteH2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_818)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.fragRouteH2.setFont(font)
        self.fragRouteH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.fragRouteH2.setObjectName("fragRouteH2")
        self.gridLayout_723.addWidget(self.fragRouteH2, 2, 0, 1, 1)
        self.fragRouteH1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_818)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.fragRouteH1.setFont(font)
        self.fragRouteH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.fragRouteH1.setObjectName("fragRouteH1")
        self.gridLayout_723.addWidget(self.fragRouteH1, 0, 0, 1, 1)
        self.fragRouteB2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_818)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fragRouteB2.setFont(font)
        self.fragRouteB2.setStyleSheet("color: rgb(255, 255, 255);")
        self.fragRouteB2.setObjectName("fragRouteB2")
        self.gridLayout_723.addWidget(self.fragRouteB2, 3, 0, 1, 1)
        self.fragRouteH3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_818)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.fragRouteH3.setFont(font)
        self.fragRouteH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.fragRouteH3.setObjectName("fragRouteH3")
        self.gridLayout_723.addWidget(self.fragRouteH3, 4, 0, 1, 1)
        self.fragRouteB4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_818)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.fragRouteB4.setFont(font)
        self.fragRouteB4.setObjectName("fragRouteB4")
        self.gridLayout_723.addWidget(self.fragRouteB4, 6, 0, 1, 1)
        self.fragRouteScrollArea.setWidget(self.scrollAreaWidgetContents_818)
        self.gridLayout_523.addWidget(self.fragRouteScrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.fragRouteTab, "")
        self.fragRouterTab = QtWidgets.QWidget()
        self.fragRouterTab.setObjectName("fragRouterTab")
        self.gridLayout_524 = QtWidgets.QGridLayout(self.fragRouterTab)
        self.gridLayout_524.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_524.setSpacing(6)
        self.gridLayout_524.setObjectName("gridLayout_524")
        self.fragRouterTitle = QtWidgets.QLabel(self.fragRouterTab)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.fragRouterTitle.setFont(font)
        self.fragRouterTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.fragRouterTitle.setObjectName("fragRouterTitle")
        self.gridLayout_524.addWidget(self.fragRouterTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.fragRouterScrollArea = QtWidgets.QScrollArea(self.fragRouterTab)
        self.fragRouterScrollArea.setWidgetResizable(True)
        self.fragRouterScrollArea.setObjectName("fragRouterScrollArea")
        self.scrollAreaWidgetContents_819 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_819.setGeometry(QtCore.QRect(0, 0, 3128, 1466))
        self.scrollAreaWidgetContents_819.setObjectName("scrollAreaWidgetContents_819")
        self.gridLayout_724 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_819)
        self.gridLayout_724.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_724.setSpacing(6)
        self.gridLayout_724.setObjectName("gridLayout_724")
        self.fragRouterButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_819)
        self.fragRouterButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.fragRouterButton.setObjectName("fragRouterButton")
        self.gridLayout_724.addWidget(self.fragRouterButton, 7, 0, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_724.addItem(spacerItem25, 8, 0, 1, 1)
        self.fragRouterH4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_819)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.fragRouterH4.setFont(font)
        self.fragRouterH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.fragRouterH4.setObjectName("fragRouterH4")
        self.gridLayout_724.addWidget(self.fragRouterH4, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.fragRouterB3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_819)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.fragRouterB3.setFont(font)
        self.fragRouterB3.setStyleSheet("color: rgb(255, 255, 255);")
        self.fragRouterB3.setObjectName("fragRouterB3")
        self.gridLayout_724.addWidget(self.fragRouterB3, 5, 0, 1, 1)
        self.fragRouterB1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_819)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fragRouterB1.setFont(font)
        self.fragRouterB1.setStyleSheet("color: rgb(255, 255, 255);")
        self.fragRouterB1.setObjectName("fragRouterB1")
        self.gridLayout_724.addWidget(self.fragRouterB1, 1, 0, 1, 1)
        self.fragRouterH2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_819)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.fragRouterH2.setFont(font)
        self.fragRouterH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.fragRouterH2.setObjectName("fragRouterH2")
        self.gridLayout_724.addWidget(self.fragRouterH2, 2, 0, 1, 1)
        self.fragRouterH1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_819)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.fragRouterH1.setFont(font)
        self.fragRouterH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.fragRouterH1.setObjectName("fragRouterH1")
        self.gridLayout_724.addWidget(self.fragRouterH1, 0, 0, 1, 1)
        self.fragRouterB2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_819)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fragRouterB2.setFont(font)
        self.fragRouterB2.setStyleSheet("color: rgb(255, 255, 255);")
        self.fragRouterB2.setObjectName("fragRouterB2")
        self.gridLayout_724.addWidget(self.fragRouterB2, 3, 0, 1, 1)
        self.fragRouterH3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_819)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.fragRouterH3.setFont(font)
        self.fragRouterH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.fragRouterH3.setObjectName("fragRouterH3")
        self.gridLayout_724.addWidget(self.fragRouterH3, 4, 0, 1, 1)
        self.fragRouterScrollArea.setWidget(self.scrollAreaWidgetContents_819)
        self.gridLayout_524.addWidget(self.fragRouterScrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.fragRouterTab, "")
        self.GhostPhisherTab = QtWidgets.QWidget()
        self.GhostPhisherTab.setObjectName("GhostPhisherTab")
        self.gridLayout_525 = QtWidgets.QGridLayout(self.GhostPhisherTab)
        self.gridLayout_525.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_525.setSpacing(6)
        self.gridLayout_525.setObjectName("gridLayout_525")
        self.GhostPhisherTitle = QtWidgets.QLabel(self.GhostPhisherTab)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.GhostPhisherTitle.setFont(font)
        self.GhostPhisherTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.GhostPhisherTitle.setObjectName("GhostPhisherTitle")
        self.gridLayout_525.addWidget(self.GhostPhisherTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.GhostPhisherScrollArea = QtWidgets.QScrollArea(self.GhostPhisherTab)
        self.GhostPhisherScrollArea.setWidgetResizable(True)
        self.GhostPhisherScrollArea.setObjectName("GhostPhisherScrollArea")
        self.scrollAreaWidgetContents_820 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_820.setGeometry(QtCore.QRect(0, 0, 3128, 779))
        self.scrollAreaWidgetContents_820.setObjectName("scrollAreaWidgetContents_820")
        self.gridLayout_725 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_820)
        self.gridLayout_725.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_725.setSpacing(6)
        self.gridLayout_725.setObjectName("gridLayout_725")
        self.GhostPhisherButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_820)
        self.GhostPhisherButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.GhostPhisherButton.setObjectName("GhostPhisherButton")
        self.gridLayout_725.addWidget(self.GhostPhisherButton, 5, 0, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_725.addItem(spacerItem26, 6, 0, 1, 1)
        self.GhostPhisherH4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_820)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.GhostPhisherH4.setFont(font)
        self.GhostPhisherH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.GhostPhisherH4.setObjectName("GhostPhisherH4")
        self.gridLayout_725.addWidget(self.GhostPhisherH4, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.GhostPhisherB1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_820)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.GhostPhisherB1.setFont(font)
        self.GhostPhisherB1.setStyleSheet("color: rgb(255, 255, 255);")
        self.GhostPhisherB1.setObjectName("GhostPhisherB1")
        self.gridLayout_725.addWidget(self.GhostPhisherB1, 1, 0, 1, 1)
        self.GhostPhisherH2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_820)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.GhostPhisherH2.setFont(font)
        self.GhostPhisherH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.GhostPhisherH2.setObjectName("GhostPhisherH2")
        self.gridLayout_725.addWidget(self.GhostPhisherH2, 2, 0, 1, 1)
        self.GhostPhisherH1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_820)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.GhostPhisherH1.setFont(font)
        self.GhostPhisherH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.GhostPhisherH1.setObjectName("GhostPhisherH1")
        self.gridLayout_725.addWidget(self.GhostPhisherH1, 0, 0, 1, 1)
        self.GhostPhisherB2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_820)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.GhostPhisherB2.setFont(font)
        self.GhostPhisherB2.setStyleSheet("color: rgb(255, 255, 255);")
        self.GhostPhisherB2.setObjectName("GhostPhisherB2")
        self.gridLayout_725.addWidget(self.GhostPhisherB2, 3, 0, 1, 1)
        self.GhostPhisherScrollArea.setWidget(self.scrollAreaWidgetContents_820)
        self.gridLayout_525.addWidget(self.GhostPhisherScrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.GhostPhisherTab, "")
        self.GoLismeroTab = QtWidgets.QWidget()
        self.GoLismeroTab.setObjectName("GoLismeroTab")
        self.gridLayout_526 = QtWidgets.QGridLayout(self.GoLismeroTab)
        self.gridLayout_526.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_526.setSpacing(6)
        self.gridLayout_526.setObjectName("gridLayout_526")
        self.GoLismeroTitle = QtWidgets.QLabel(self.GoLismeroTab)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.GoLismeroTitle.setFont(font)
        self.GoLismeroTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.GoLismeroTitle.setObjectName("GoLismeroTitle")
        self.gridLayout_526.addWidget(self.GoLismeroTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.GoLismeroScrollArea = QtWidgets.QScrollArea(self.GoLismeroTab)
        self.GoLismeroScrollArea.setWidgetResizable(True)
        self.GoLismeroScrollArea.setObjectName("GoLismeroScrollArea")
        self.scrollAreaWidgetContents_821 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_821.setGeometry(QtCore.QRect(0, 0, 3128, 2376))
        self.scrollAreaWidgetContents_821.setObjectName("scrollAreaWidgetContents_821")
        self.gridLayout_726 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_821)
        self.gridLayout_726.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_726.setSpacing(6)
        self.gridLayout_726.setObjectName("gridLayout_726")
        self.GoLismeroButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_821)
        self.GoLismeroButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.GoLismeroButton.setObjectName("GoLismeroButton")
        self.gridLayout_726.addWidget(self.GoLismeroButton, 7, 0, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_726.addItem(spacerItem27, 8, 0, 1, 1)
        self.GoLismeroH4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_821)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.GoLismeroH4.setFont(font)
        self.GoLismeroH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.GoLismeroH4.setObjectName("GoLismeroH4")
        self.gridLayout_726.addWidget(self.GoLismeroH4, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.GoLismeroB3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_821)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.GoLismeroB3.setFont(font)
        self.GoLismeroB3.setStyleSheet("color: rgb(255, 255, 255);")
        self.GoLismeroB3.setObjectName("GoLismeroB3")
        self.gridLayout_726.addWidget(self.GoLismeroB3, 5, 0, 1, 1)
        self.GoLismeroB1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_821)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.GoLismeroB1.setFont(font)
        self.GoLismeroB1.setStyleSheet("color: rgb(255, 255, 255);")
        self.GoLismeroB1.setObjectName("GoLismeroB1")
        self.gridLayout_726.addWidget(self.GoLismeroB1, 1, 0, 1, 1)
        self.GoLismeroH2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_821)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.GoLismeroH2.setFont(font)
        self.GoLismeroH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.GoLismeroH2.setObjectName("GoLismeroH2")
        self.gridLayout_726.addWidget(self.GoLismeroH2, 2, 0, 1, 1)
        self.GoLismeroH1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_821)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.GoLismeroH1.setFont(font)
        self.GoLismeroH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.GoLismeroH1.setObjectName("GoLismeroH1")
        self.gridLayout_726.addWidget(self.GoLismeroH1, 0, 0, 1, 1)
        self.GoLismeroB2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_821)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.GoLismeroB2.setFont(font)
        self.GoLismeroB2.setStyleSheet("color: rgb(255, 255, 255);")
        self.GoLismeroB2.setObjectName("GoLismeroB2")
        self.gridLayout_726.addWidget(self.GoLismeroB2, 3, 0, 1, 1)
        self.GoLismeroH3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_821)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.GoLismeroH3.setFont(font)
        self.GoLismeroH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.GoLismeroH3.setObjectName("GoLismeroH3")
        self.gridLayout_726.addWidget(self.GoLismeroH3, 4, 0, 1, 1)
        self.GoLismeroScrollArea.setWidget(self.scrollAreaWidgetContents_821)
        self.gridLayout_526.addWidget(self.GoLismeroScrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.GoLismeroTab, "")
        self.goofileTab = QtWidgets.QWidget()
        self.goofileTab.setObjectName("goofileTab")
        self.gridLayout_527 = QtWidgets.QGridLayout(self.goofileTab)
        self.gridLayout_527.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_527.setSpacing(6)
        self.gridLayout_527.setObjectName("gridLayout_527")
        self.goofileTitle = QtWidgets.QLabel(self.goofileTab)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.goofileTitle.setFont(font)
        self.goofileTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.goofileTitle.setObjectName("goofileTitle")
        self.gridLayout_527.addWidget(self.goofileTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.goofileScrollArea = QtWidgets.QScrollArea(self.goofileTab)
        self.goofileScrollArea.setStyleSheet("color: rgb(255, 255, 255);")
        self.goofileScrollArea.setWidgetResizable(True)
        self.goofileScrollArea.setObjectName("goofileScrollArea")
        self.scrollAreaWidgetContents_822 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_822.setGeometry(QtCore.QRect(0, 0, 3128, 1494))
        self.scrollAreaWidgetContents_822.setObjectName("scrollAreaWidgetContents_822")
        self.gridLayout_727 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_822)
        self.gridLayout_727.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_727.setSpacing(6)
        self.gridLayout_727.setObjectName("gridLayout_727")
        self.goofileButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_822)
        self.goofileButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.goofileButton.setObjectName("goofileButton")
        self.gridLayout_727.addWidget(self.goofileButton, 7, 0, 1, 1)
        spacerItem28 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_727.addItem(spacerItem28, 8, 0, 1, 1)
        self.goofileH4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_822)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.goofileH4.setFont(font)
        self.goofileH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.goofileH4.setObjectName("goofileH4")
        self.gridLayout_727.addWidget(self.goofileH4, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.goofileB3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_822)
        self.goofileB3.setStyleSheet("color: rgb(255, 255, 255);")
        self.goofileB3.setObjectName("goofileB3")
        self.gridLayout_727.addWidget(self.goofileB3, 5, 0, 1, 1)
        self.goofileB1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_822)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.goofileB1.setFont(font)
        self.goofileB1.setStyleSheet("color: rgb(255, 255, 255);")
        self.goofileB1.setObjectName("goofileB1")
        self.gridLayout_727.addWidget(self.goofileB1, 1, 0, 1, 1)
        self.goofileH2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_822)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.goofileH2.setFont(font)
        self.goofileH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.goofileH2.setObjectName("goofileH2")
        self.gridLayout_727.addWidget(self.goofileH2, 2, 0, 1, 1)
        self.goofileH1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_822)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.goofileH1.setFont(font)
        self.goofileH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.goofileH1.setObjectName("goofileH1")
        self.gridLayout_727.addWidget(self.goofileH1, 0, 0, 1, 1)
        self.goofileB2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_822)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.goofileB2.setFont(font)
        self.goofileB2.setStyleSheet("color: rgb(255, 255, 255);")
        self.goofileB2.setObjectName("goofileB2")
        self.gridLayout_727.addWidget(self.goofileB2, 3, 0, 1, 1)
        self.goofileH3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_822)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.goofileH3.setFont(font)
        self.goofileH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.goofileH3.setObjectName("goofileH3")
        self.gridLayout_727.addWidget(self.goofileH3, 4, 0, 1, 1)
        self.goofileScrollArea.setWidget(self.scrollAreaWidgetContents_822)
        self.gridLayout_527.addWidget(self.goofileScrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.goofileTab, "")
        self.hping3Tab = QtWidgets.QWidget()
        self.hping3Tab.setObjectName("hping3Tab")
        self.gridLayout_528 = QtWidgets.QGridLayout(self.hping3Tab)
        self.gridLayout_528.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_528.setSpacing(6)
        self.gridLayout_528.setObjectName("gridLayout_528")
        self.hping3Title = QtWidgets.QLabel(self.hping3Tab)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.hping3Title.setFont(font)
        self.hping3Title.setStyleSheet("color: rgb(255, 255, 255);")
        self.hping3Title.setObjectName("hping3Title")
        self.gridLayout_528.addWidget(self.hping3Title, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.hping3ScrollArea = QtWidgets.QScrollArea(self.hping3Tab)
        self.hping3ScrollArea.setWidgetResizable(True)
        self.hping3ScrollArea.setObjectName("hping3ScrollArea")
        self.scrollAreaWidgetContents_823 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_823.setGeometry(QtCore.QRect(0, 0, 3128, 3135))
        self.scrollAreaWidgetContents_823.setObjectName("scrollAreaWidgetContents_823")
        self.gridLayout_728 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_823)
        self.gridLayout_728.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_728.setSpacing(6)
        self.gridLayout_728.setObjectName("gridLayout_728")
        self.hping3Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents_823)
        self.hping3Button.setStyleSheet("color: rgb(255, 255, 255);")
        self.hping3Button.setObjectName("hping3Button")
        self.gridLayout_728.addWidget(self.hping3Button, 7, 0, 1, 1)
        spacerItem29 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_728.addItem(spacerItem29, 8, 0, 1, 1)
        self.hping3H4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_823)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.hping3H4.setFont(font)
        self.hping3H4.setStyleSheet("color: rgb(56, 196, 255);")
        self.hping3H4.setObjectName("hping3H4")
        self.gridLayout_728.addWidget(self.hping3H4, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.hping3B3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_823)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.hping3B3.setFont(font)
        self.hping3B3.setStyleSheet("color: rgb(255, 255, 255);")
        self.hping3B3.setObjectName("hping3B3")
        self.gridLayout_728.addWidget(self.hping3B3, 5, 0, 1, 1)
        self.hping3B1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_823)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.hping3B1.setFont(font)
        self.hping3B1.setStyleSheet("color: rgb(255, 255, 255);")
        self.hping3B1.setObjectName("hping3B1")
        self.gridLayout_728.addWidget(self.hping3B1, 1, 0, 1, 1)
        self.hping3H2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_823)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.hping3H2.setFont(font)
        self.hping3H2.setStyleSheet("color: rgb(56, 196, 255);")
        self.hping3H2.setObjectName("hping3H2")
        self.gridLayout_728.addWidget(self.hping3H2, 2, 0, 1, 1)
        self.hping3H1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_823)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.hping3H1.setFont(font)
        self.hping3H1.setStyleSheet("color: rgb(56, 196, 255);")
        self.hping3H1.setObjectName("hping3H1")
        self.gridLayout_728.addWidget(self.hping3H1, 0, 0, 1, 1)
        self.hping3B2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_823)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.hping3B2.setFont(font)
        self.hping3B2.setStyleSheet("color: rgb(255, 255, 255);")
        self.hping3B2.setObjectName("hping3B2")
        self.gridLayout_728.addWidget(self.hping3B2, 3, 0, 1, 1)
        self.hping3H3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_823)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.hping3H3.setFont(font)
        self.hping3H3.setStyleSheet("color: rgb(56, 196, 255);")
        self.hping3H3.setObjectName("hping3H3")
        self.gridLayout_728.addWidget(self.hping3H3, 4, 0, 1, 1)
        self.hping3ScrollArea.setWidget(self.scrollAreaWidgetContents_823)
        self.gridLayout_528.addWidget(self.hping3ScrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.hping3Tab, "")
        self.identUserEnumTab = QtWidgets.QWidget()
        self.identUserEnumTab.setObjectName("identUserEnumTab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.identUserEnumTab)
        self.gridLayout_8.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_8.setSpacing(6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.identUserEnumScrollArea = QtWidgets.QScrollArea(self.identUserEnumTab)
        self.identUserEnumScrollArea.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.identUserEnumScrollArea.setWidgetResizable(True)
        self.identUserEnumScrollArea.setObjectName("identUserEnumScrollArea")
        self.identUserEnumScrollWidgetContents = QtWidgets.QWidget()
        self.identUserEnumScrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 3128, 1298))
        self.identUserEnumScrollWidgetContents.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.identUserEnumScrollWidgetContents.setObjectName("identUserEnumScrollWidgetContents")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.identUserEnumScrollWidgetContents)
        self.gridLayout_9.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_9.setSpacing(6)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.line_18 = QtWidgets.QFrame(self.identUserEnumScrollWidgetContents)
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.gridLayout_9.addWidget(self.line_18, 7, 0, 1, 1)
        self.line_16 = QtWidgets.QFrame(self.identUserEnumScrollWidgetContents)
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.gridLayout_9.addWidget(self.line_16, 3, 0, 1, 1)
        self.identUserEnumTitle = QtWidgets.QLabel(self.identUserEnumScrollWidgetContents)
        self.identUserEnumTitle.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.identUserEnumTitle.setFont(font)
        self.identUserEnumTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.identUserEnumTitle.setObjectName("identUserEnumTitle")
        self.gridLayout_9.addWidget(self.identUserEnumTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.identUserEnumH2 = QtWidgets.QLabel(self.identUserEnumScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.identUserEnumH2.setFont(font)
        self.identUserEnumH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.identUserEnumH2.setObjectName("identUserEnumH2")
        self.gridLayout_9.addWidget(self.identUserEnumH2, 6, 0, 1, 1)
        self.identUserEnumH3 = QtWidgets.QLabel(self.identUserEnumScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.identUserEnumH3.setFont(font)
        self.identUserEnumH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.identUserEnumH3.setObjectName("identUserEnumH3")
        self.gridLayout_9.addWidget(self.identUserEnumH3, 10, 0, 1, 1)
        self.identUserEnumH4 = QtWidgets.QLabel(self.identUserEnumScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.identUserEnumH4.setFont(font)
        self.identUserEnumH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.identUserEnumH4.setObjectName("identUserEnumH4")
        self.gridLayout_9.addWidget(self.identUserEnumH4, 14, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.identUserEnumButton = QtWidgets.QPushButton(self.identUserEnumScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.identUserEnumButton.setFont(font)
        self.identUserEnumButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(79, 79, 79);")
        self.identUserEnumButton.setObjectName("identUserEnumButton")
        self.gridLayout_9.addWidget(self.identUserEnumButton, 16, 0, 1, 1)
        self.identUserEnumB2 = QtWidgets.QLabel(self.identUserEnumScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.identUserEnumB2.setFont(font)
        self.identUserEnumB2.setObjectName("identUserEnumB2")
        self.gridLayout_9.addWidget(self.identUserEnumB2, 8, 0, 1, 1)
        self.line_21 = QtWidgets.QFrame(self.identUserEnumScrollWidgetContents)
        self.line_21.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.gridLayout_9.addWidget(self.line_21, 13, 0, 1, 1)
        self.line_20 = QtWidgets.QFrame(self.identUserEnumScrollWidgetContents)
        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.gridLayout_9.addWidget(self.line_20, 11, 0, 1, 1)
        self.identUserEnumB3 = QtWidgets.QLabel(self.identUserEnumScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.identUserEnumB3.setFont(font)
        self.identUserEnumB3.setObjectName("identUserEnumB3")
        self.gridLayout_9.addWidget(self.identUserEnumB3, 12, 0, 1, 1)
        self.identUserEnumH1 = QtWidgets.QLabel(self.identUserEnumScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.identUserEnumH1.setFont(font)
        self.identUserEnumH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.identUserEnumH1.setObjectName("identUserEnumH1")
        self.gridLayout_9.addWidget(self.identUserEnumH1, 2, 0, 1, 1)
        spacerItem30 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_9.addItem(spacerItem30, 17, 0, 1, 1)
        self.line_17 = QtWidgets.QFrame(self.identUserEnumScrollWidgetContents)
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.gridLayout_9.addWidget(self.line_17, 5, 0, 1, 1)
        self.line_22 = QtWidgets.QFrame(self.identUserEnumScrollWidgetContents)
        self.line_22.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.gridLayout_9.addWidget(self.line_22, 15, 0, 1, 1)
        self.line_15 = QtWidgets.QFrame(self.identUserEnumScrollWidgetContents)
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.gridLayout_9.addWidget(self.line_15, 1, 0, 1, 1)
        self.line_19 = QtWidgets.QFrame(self.identUserEnumScrollWidgetContents)
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.gridLayout_9.addWidget(self.line_19, 9, 0, 1, 1)
        self.identUserEnumB1 = QtWidgets.QLabel(self.identUserEnumScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.identUserEnumB1.setFont(font)
        self.identUserEnumB1.setTextFormat(QtCore.Qt.AutoText)
        self.identUserEnumB1.setScaledContents(False)
        self.identUserEnumB1.setWordWrap(False)
        self.identUserEnumB1.setObjectName("identUserEnumB1")
        self.gridLayout_9.addWidget(self.identUserEnumB1, 4, 0, 1, 1)
        self.identUserEnumScrollArea.setWidget(self.identUserEnumScrollWidgetContents)
        self.gridLayout_8.addWidget(self.identUserEnumScrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.identUserEnumTab, "")
        self.InTraceTab = QtWidgets.QWidget()
        self.InTraceTab.setObjectName("InTraceTab")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.InTraceTab)
        self.gridLayout_10.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_10.setSpacing(6)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.InTraceScrollArea = QtWidgets.QScrollArea(self.InTraceTab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.InTraceScrollArea.setFont(font)
        self.InTraceScrollArea.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.InTraceScrollArea.setWidgetResizable(True)
        self.InTraceScrollArea.setObjectName("InTraceScrollArea")
        self.InTraceScrollWidgetContents = QtWidgets.QWidget()
        self.InTraceScrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 3128, 1384))
        self.InTraceScrollWidgetContents.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.InTraceScrollWidgetContents.setObjectName("InTraceScrollWidgetContents")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.InTraceScrollWidgetContents)
        self.gridLayout_11.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_11.setSpacing(6)
        self.gridLayout_11.setObjectName("gridLayout_11")
        spacerItem31 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_11.addItem(spacerItem31, 17, 0, 1, 1)
        self.InTraceH3 = QtWidgets.QLabel(self.InTraceScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.InTraceH3.setFont(font)
        self.InTraceH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.InTraceH3.setObjectName("InTraceH3")
        self.gridLayout_11.addWidget(self.InTraceH3, 10, 0, 1, 1)
        self.InTraceH4 = QtWidgets.QLabel(self.InTraceScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.InTraceH4.setFont(font)
        self.InTraceH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.InTraceH4.setObjectName("InTraceH4")
        self.gridLayout_11.addWidget(self.InTraceH4, 14, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.InTraceB2 = QtWidgets.QLabel(self.InTraceScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.InTraceB2.setFont(font)
        self.InTraceB2.setObjectName("InTraceB2")
        self.gridLayout_11.addWidget(self.InTraceB2, 8, 0, 1, 1)
        self.InTraceTitle = QtWidgets.QLabel(self.InTraceScrollWidgetContents)
        self.InTraceTitle.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.InTraceTitle.setFont(font)
        self.InTraceTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.InTraceTitle.setObjectName("InTraceTitle")
        self.gridLayout_11.addWidget(self.InTraceTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.InTraceB3 = QtWidgets.QLabel(self.InTraceScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.InTraceB3.setFont(font)
        self.InTraceB3.setObjectName("InTraceB3")
        self.gridLayout_11.addWidget(self.InTraceB3, 12, 0, 1, 1)
        self.InTraceH1 = QtWidgets.QLabel(self.InTraceScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.InTraceH1.setFont(font)
        self.InTraceH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.InTraceH1.setObjectName("InTraceH1")
        self.gridLayout_11.addWidget(self.InTraceH1, 2, 0, 1, 1)
        self.InTraceB1 = QtWidgets.QLabel(self.InTraceScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.InTraceB1.setFont(font)
        self.InTraceB1.setTextFormat(QtCore.Qt.AutoText)
        self.InTraceB1.setScaledContents(False)
        self.InTraceB1.setWordWrap(False)
        self.InTraceB1.setObjectName("InTraceB1")
        self.gridLayout_11.addWidget(self.InTraceB1, 4, 0, 1, 1)
        self.InTraceButton = QtWidgets.QPushButton(self.InTraceScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.InTraceButton.setFont(font)
        self.InTraceButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(79, 79, 79);")
        self.InTraceButton.setObjectName("InTraceButton")
        self.gridLayout_11.addWidget(self.InTraceButton, 16, 0, 1, 1)
        self.InTraceH2 = QtWidgets.QLabel(self.InTraceScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.InTraceH2.setFont(font)
        self.InTraceH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.InTraceH2.setObjectName("InTraceH2")
        self.gridLayout_11.addWidget(self.InTraceH2, 6, 0, 1, 1)
        self.line_29 = QtWidgets.QFrame(self.InTraceScrollWidgetContents)
        self.line_29.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_29.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_29.setObjectName("line_29")
        self.gridLayout_11.addWidget(self.line_29, 13, 0, 1, 1)
        self.line_27 = QtWidgets.QFrame(self.InTraceScrollWidgetContents)
        self.line_27.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_27.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_27.setObjectName("line_27")
        self.gridLayout_11.addWidget(self.line_27, 9, 0, 1, 1)
        self.line_24 = QtWidgets.QFrame(self.InTraceScrollWidgetContents)
        self.line_24.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_24.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_24.setObjectName("line_24")
        self.gridLayout_11.addWidget(self.line_24, 3, 0, 1, 1)
        self.line_26 = QtWidgets.QFrame(self.InTraceScrollWidgetContents)
        self.line_26.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_26.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_26.setObjectName("line_26")
        self.gridLayout_11.addWidget(self.line_26, 7, 0, 1, 1)
        self.line_28 = QtWidgets.QFrame(self.InTraceScrollWidgetContents)
        self.line_28.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_28.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_28.setObjectName("line_28")
        self.gridLayout_11.addWidget(self.line_28, 11, 0, 1, 1)
        self.line_25 = QtWidgets.QFrame(self.InTraceScrollWidgetContents)
        self.line_25.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_25.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_25.setObjectName("line_25")
        self.gridLayout_11.addWidget(self.line_25, 5, 0, 1, 1)
        self.line_23 = QtWidgets.QFrame(self.InTraceScrollWidgetContents)
        self.line_23.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_23.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_23.setObjectName("line_23")
        self.gridLayout_11.addWidget(self.line_23, 1, 0, 1, 1)
        self.line_30 = QtWidgets.QFrame(self.InTraceScrollWidgetContents)
        self.line_30.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_30.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_30.setObjectName("line_30")
        self.gridLayout_11.addWidget(self.line_30, 15, 0, 1, 1)
        self.InTraceScrollArea.setWidget(self.InTraceScrollWidgetContents)
        self.gridLayout_10.addWidget(self.InTraceScrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.InTraceTab, "")
        self.iSMTPTab = QtWidgets.QWidget()
        self.iSMTPTab.setObjectName("iSMTPTab")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.iSMTPTab)
        self.gridLayout_12.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_12.setSpacing(6)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.iSMTPScrollArea = QtWidgets.QScrollArea(self.iSMTPTab)
        self.iSMTPScrollArea.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.iSMTPScrollArea.setWidgetResizable(True)
        self.iSMTPScrollArea.setObjectName("iSMTPScrollArea")
        self.iSMTPScrollWidgetContents = QtWidgets.QWidget()
        self.iSMTPScrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 3128, 2361))
        self.iSMTPScrollWidgetContents.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.iSMTPScrollWidgetContents.setObjectName("iSMTPScrollWidgetContents")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.iSMTPScrollWidgetContents)
        self.gridLayout_13.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_13.setSpacing(6)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.line_39 = QtWidgets.QFrame(self.iSMTPScrollWidgetContents)
        self.line_39.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_39.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_39.setObjectName("line_39")
        self.gridLayout_13.addWidget(self.line_39, 5, 0, 1, 1)
        self.line_40 = QtWidgets.QFrame(self.iSMTPScrollWidgetContents)
        self.line_40.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_40.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_40.setObjectName("line_40")
        self.gridLayout_13.addWidget(self.line_40, 7, 0, 1, 1)
        self.line_41 = QtWidgets.QFrame(self.iSMTPScrollWidgetContents)
        self.line_41.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_41.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_41.setObjectName("line_41")
        self.gridLayout_13.addWidget(self.line_41, 9, 0, 1, 1)
        self.iSMTPTitle = QtWidgets.QLabel(self.iSMTPScrollWidgetContents)
        self.iSMTPTitle.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.iSMTPTitle.setFont(font)
        self.iSMTPTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.iSMTPTitle.setObjectName("iSMTPTitle")
        self.gridLayout_13.addWidget(self.iSMTPTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.iSMTPH4 = QtWidgets.QLabel(self.iSMTPScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.iSMTPH4.setFont(font)
        self.iSMTPH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.iSMTPH4.setObjectName("iSMTPH4")
        self.gridLayout_13.addWidget(self.iSMTPH4, 14, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.iSMTPB2 = QtWidgets.QLabel(self.iSMTPScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.iSMTPB2.setFont(font)
        self.iSMTPB2.setObjectName("iSMTPB2")
        self.gridLayout_13.addWidget(self.iSMTPB2, 8, 0, 1, 1)
        self.iSMTPH3 = QtWidgets.QLabel(self.iSMTPScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.iSMTPH3.setFont(font)
        self.iSMTPH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.iSMTPH3.setObjectName("iSMTPH3")
        self.gridLayout_13.addWidget(self.iSMTPH3, 10, 0, 1, 1)
        self.iSMTPH1 = QtWidgets.QLabel(self.iSMTPScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.iSMTPH1.setFont(font)
        self.iSMTPH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.iSMTPH1.setObjectName("iSMTPH1")
        self.gridLayout_13.addWidget(self.iSMTPH1, 2, 0, 1, 1)
        self.iSMTPB1 = QtWidgets.QLabel(self.iSMTPScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.iSMTPB1.setFont(font)
        self.iSMTPB1.setTextFormat(QtCore.Qt.AutoText)
        self.iSMTPB1.setScaledContents(False)
        self.iSMTPB1.setWordWrap(False)
        self.iSMTPB1.setObjectName("iSMTPB1")
        self.gridLayout_13.addWidget(self.iSMTPB1, 4, 0, 1, 1)
        self.iSMTPB3 = QtWidgets.QLabel(self.iSMTPScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.iSMTPB3.setFont(font)
        self.iSMTPB3.setObjectName("iSMTPB3")
        self.gridLayout_13.addWidget(self.iSMTPB3, 12, 0, 1, 1)
        self.iSMTPButton = QtWidgets.QPushButton(self.iSMTPScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.iSMTPButton.setFont(font)
        self.iSMTPButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(79, 79, 79);")
        self.iSMTPButton.setObjectName("iSMTPButton")
        self.gridLayout_13.addWidget(self.iSMTPButton, 16, 0, 1, 1)
        self.iSMTPH2 = QtWidgets.QLabel(self.iSMTPScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.iSMTPH2.setFont(font)
        self.iSMTPH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.iSMTPH2.setObjectName("iSMTPH2")
        self.gridLayout_13.addWidget(self.iSMTPH2, 6, 0, 1, 1)
        spacerItem32 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_13.addItem(spacerItem32, 17, 0, 1, 1)
        self.line_43 = QtWidgets.QFrame(self.iSMTPScrollWidgetContents)
        self.line_43.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_43.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_43.setObjectName("line_43")
        self.gridLayout_13.addWidget(self.line_43, 11, 0, 1, 1)
        self.line_45 = QtWidgets.QFrame(self.iSMTPScrollWidgetContents)
        self.line_45.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_45.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_45.setObjectName("line_45")
        self.gridLayout_13.addWidget(self.line_45, 15, 0, 1, 1)
        self.line_44 = QtWidgets.QFrame(self.iSMTPScrollWidgetContents)
        self.line_44.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_44.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_44.setObjectName("line_44")
        self.gridLayout_13.addWidget(self.line_44, 13, 0, 1, 1)
        self.line_38 = QtWidgets.QFrame(self.iSMTPScrollWidgetContents)
        self.line_38.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_38.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_38.setObjectName("line_38")
        self.gridLayout_13.addWidget(self.line_38, 3, 0, 1, 1)
        self.line_37 = QtWidgets.QFrame(self.iSMTPScrollWidgetContents)
        self.line_37.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_37.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_37.setObjectName("line_37")
        self.gridLayout_13.addWidget(self.line_37, 1, 0, 1, 1)
        self.iSMTPScrollArea.setWidget(self.iSMTPScrollWidgetContents)
        self.gridLayout_12.addWidget(self.iSMTPScrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.iSMTPTab, "")
        self.IbdTab = QtWidgets.QWidget()
        self.IbdTab.setObjectName("IbdTab")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.IbdTab)
        self.gridLayout_14.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_14.setSpacing(6)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.IbdScrollArea = QtWidgets.QScrollArea(self.IbdTab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.IbdScrollArea.setFont(font)
        self.IbdScrollArea.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.IbdScrollArea.setWidgetResizable(True)
        self.IbdScrollArea.setObjectName("IbdScrollArea")
        self.IbdScrollWidgetContents = QtWidgets.QWidget()
        self.IbdScrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 3128, 1095))
        self.IbdScrollWidgetContents.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.IbdScrollWidgetContents.setObjectName("IbdScrollWidgetContents")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.IbdScrollWidgetContents)
        self.gridLayout_15.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_15.setSpacing(6)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.line_42 = QtWidgets.QFrame(self.IbdScrollWidgetContents)
        self.line_42.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_42.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_42.setObjectName("line_42")
        self.gridLayout_15.addWidget(self.line_42, 1, 0, 1, 1)
        self.line_46 = QtWidgets.QFrame(self.IbdScrollWidgetContents)
        self.line_46.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_46.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_46.setObjectName("line_46")
        self.gridLayout_15.addWidget(self.line_46, 5, 0, 1, 1)
        self.line_47 = QtWidgets.QFrame(self.IbdScrollWidgetContents)
        self.line_47.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_47.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_47.setObjectName("line_47")
        self.gridLayout_15.addWidget(self.line_47, 7, 0, 1, 1)
        self.line_48 = QtWidgets.QFrame(self.IbdScrollWidgetContents)
        self.line_48.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_48.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_48.setObjectName("line_48")
        self.gridLayout_15.addWidget(self.line_48, 9, 0, 1, 1)
        self.IbdTitle = QtWidgets.QLabel(self.IbdScrollWidgetContents)
        self.IbdTitle.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.IbdTitle.setFont(font)
        self.IbdTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.IbdTitle.setObjectName("IbdTitle")
        self.gridLayout_15.addWidget(self.IbdTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.IbdH4 = QtWidgets.QLabel(self.IbdScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.IbdH4.setFont(font)
        self.IbdH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.IbdH4.setObjectName("IbdH4")
        self.gridLayout_15.addWidget(self.IbdH4, 14, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.IbdB2 = QtWidgets.QLabel(self.IbdScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.IbdB2.setFont(font)
        self.IbdB2.setObjectName("IbdB2")
        self.gridLayout_15.addWidget(self.IbdB2, 8, 0, 1, 1)
        self.IbdH3 = QtWidgets.QLabel(self.IbdScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.IbdH3.setFont(font)
        self.IbdH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.IbdH3.setObjectName("IbdH3")
        self.gridLayout_15.addWidget(self.IbdH3, 10, 0, 1, 1)
        self.IbdH1 = QtWidgets.QLabel(self.IbdScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.IbdH1.setFont(font)
        self.IbdH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.IbdH1.setObjectName("IbdH1")
        self.gridLayout_15.addWidget(self.IbdH1, 2, 0, 1, 1)
        self.IbdB1 = QtWidgets.QLabel(self.IbdScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.IbdB1.setFont(font)
        self.IbdB1.setTextFormat(QtCore.Qt.AutoText)
        self.IbdB1.setScaledContents(False)
        self.IbdB1.setWordWrap(False)
        self.IbdB1.setObjectName("IbdB1")
        self.gridLayout_15.addWidget(self.IbdB1, 4, 0, 1, 1)
        self.IbdB3 = QtWidgets.QLabel(self.IbdScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.IbdB3.setFont(font)
        self.IbdB3.setObjectName("IbdB3")
        self.gridLayout_15.addWidget(self.IbdB3, 12, 0, 1, 1)
        self.IbdButton = QtWidgets.QPushButton(self.IbdScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.IbdButton.setFont(font)
        self.IbdButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(79, 79, 79);")
        self.IbdButton.setObjectName("IbdButton")
        self.gridLayout_15.addWidget(self.IbdButton, 16, 0, 1, 1)
        self.IbdH2 = QtWidgets.QLabel(self.IbdScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.IbdH2.setFont(font)
        self.IbdH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.IbdH2.setObjectName("IbdH2")
        self.gridLayout_15.addWidget(self.IbdH2, 6, 0, 1, 1)
        spacerItem33 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_15.addItem(spacerItem33, 17, 0, 1, 1)
        self.line_49 = QtWidgets.QFrame(self.IbdScrollWidgetContents)
        self.line_49.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_49.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_49.setObjectName("line_49")
        self.gridLayout_15.addWidget(self.line_49, 11, 0, 1, 1)
        self.line_50 = QtWidgets.QFrame(self.IbdScrollWidgetContents)
        self.line_50.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_50.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_50.setObjectName("line_50")
        self.gridLayout_15.addWidget(self.line_50, 13, 0, 1, 1)
        self.line_51 = QtWidgets.QFrame(self.IbdScrollWidgetContents)
        self.line_51.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_51.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_51.setObjectName("line_51")
        self.gridLayout_15.addWidget(self.line_51, 3, 0, 1, 1)
        self.line_52 = QtWidgets.QFrame(self.IbdScrollWidgetContents)
        self.line_52.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_52.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_52.setObjectName("line_52")
        self.gridLayout_15.addWidget(self.line_52, 15, 0, 1, 1)
        self.IbdScrollArea.setWidget(self.IbdScrollWidgetContents)
        self.gridLayout_14.addWidget(self.IbdScrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.IbdTab, "")
        self.MaltegoTeethTab = QtWidgets.QWidget()
        self.MaltegoTeethTab.setObjectName("MaltegoTeethTab")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.MaltegoTeethTab)
        self.gridLayout_16.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_16.setSpacing(6)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.MAltegoTeethScrollArea = QtWidgets.QScrollArea(self.MaltegoTeethTab)
        font = QtGui.QFont()
        font.setPointSize(3)
        self.MAltegoTeethScrollArea.setFont(font)
        self.MAltegoTeethScrollArea.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.MAltegoTeethScrollArea.setWidgetResizable(True)
        self.MAltegoTeethScrollArea.setObjectName("MAltegoTeethScrollArea")
        self.MaltegoTeethScrollWidgetContents = QtWidgets.QWidget()
        self.MaltegoTeethScrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 3128, 3549))
        self.MaltegoTeethScrollWidgetContents.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.MaltegoTeethScrollWidgetContents.setObjectName("MaltegoTeethScrollWidgetContents")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.MaltegoTeethScrollWidgetContents)
        self.gridLayout_17.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_17.setSpacing(6)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.line_55 = QtWidgets.QFrame(self.MaltegoTeethScrollWidgetContents)
        self.line_55.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_55.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_55.setObjectName("line_55")
        self.gridLayout_17.addWidget(self.line_55, 7, 0, 1, 1)
        self.line_60 = QtWidgets.QFrame(self.MaltegoTeethScrollWidgetContents)
        self.line_60.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_60.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_60.setObjectName("line_60")
        self.gridLayout_17.addWidget(self.line_60, 13, 0, 1, 1)
        self.line_56 = QtWidgets.QFrame(self.MaltegoTeethScrollWidgetContents)
        self.line_56.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_56.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_56.setObjectName("line_56")
        self.gridLayout_17.addWidget(self.line_56, 9, 0, 1, 1)
        spacerItem34 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_17.addItem(spacerItem34, 15, 0, 1, 1)
        self.MaltegoTeethTitle = QtWidgets.QLabel(self.MaltegoTeethScrollWidgetContents)
        self.MaltegoTeethTitle.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.MaltegoTeethTitle.setFont(font)
        self.MaltegoTeethTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.MaltegoTeethTitle.setObjectName("MaltegoTeethTitle")
        self.gridLayout_17.addWidget(self.MaltegoTeethTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.line_53 = QtWidgets.QFrame(self.MaltegoTeethScrollWidgetContents)
        self.line_53.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_53.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_53.setObjectName("line_53")
        self.gridLayout_17.addWidget(self.line_53, 1, 0, 1, 1)
        self.MaltegoTeethButton = QtWidgets.QPushButton(self.MaltegoTeethScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.MaltegoTeethButton.setFont(font)
        self.MaltegoTeethButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(79, 79, 79);")
        self.MaltegoTeethButton.setObjectName("MaltegoTeethButton")
        self.gridLayout_17.addWidget(self.MaltegoTeethButton, 14, 0, 1, 1)
        self.MaltegoTeethH4 = QtWidgets.QLabel(self.MaltegoTeethScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.MaltegoTeethH4.setFont(font)
        self.MaltegoTeethH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.MaltegoTeethH4.setObjectName("MaltegoTeethH4")
        self.gridLayout_17.addWidget(self.MaltegoTeethH4, 12, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.line_57 = QtWidgets.QFrame(self.MaltegoTeethScrollWidgetContents)
        self.line_57.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_57.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_57.setObjectName("line_57")
        self.gridLayout_17.addWidget(self.line_57, 10, 0, 1, 1)
        self.MaltegoTeethH2 = QtWidgets.QLabel(self.MaltegoTeethScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.MaltegoTeethH2.setFont(font)
        self.MaltegoTeethH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.MaltegoTeethH2.setObjectName("MaltegoTeethH2")
        self.gridLayout_17.addWidget(self.MaltegoTeethH2, 6, 0, 1, 1)
        self.MaltegoTeethB2 = QtWidgets.QLabel(self.MaltegoTeethScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.MaltegoTeethB2.setFont(font)
        self.MaltegoTeethB2.setObjectName("MaltegoTeethB2")
        self.gridLayout_17.addWidget(self.MaltegoTeethB2, 8, 0, 1, 1)
        self.line_58 = QtWidgets.QFrame(self.MaltegoTeethScrollWidgetContents)
        self.line_58.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_58.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_58.setObjectName("line_58")
        self.gridLayout_17.addWidget(self.line_58, 11, 0, 1, 1)
        self.line_54 = QtWidgets.QFrame(self.MaltegoTeethScrollWidgetContents)
        self.line_54.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_54.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_54.setObjectName("line_54")
        self.gridLayout_17.addWidget(self.line_54, 5, 0, 1, 1)
        self.line_59 = QtWidgets.QFrame(self.MaltegoTeethScrollWidgetContents)
        self.line_59.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_59.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_59.setObjectName("line_59")
        self.gridLayout_17.addWidget(self.line_59, 3, 0, 1, 1)
        self.MaltegoTeethH1 = QtWidgets.QLabel(self.MaltegoTeethScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.MaltegoTeethH1.setFont(font)
        self.MaltegoTeethH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.MaltegoTeethH1.setObjectName("MaltegoTeethH1")
        self.gridLayout_17.addWidget(self.MaltegoTeethH1, 2, 0, 1, 1)
        self.MaltegoTeethB1 = QtWidgets.QLabel(self.MaltegoTeethScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.MaltegoTeethB1.setFont(font)
        self.MaltegoTeethB1.setTextFormat(QtCore.Qt.AutoText)
        self.MaltegoTeethB1.setScaledContents(False)
        self.MaltegoTeethB1.setWordWrap(False)
        self.MaltegoTeethB1.setObjectName("MaltegoTeethB1")
        self.gridLayout_17.addWidget(self.MaltegoTeethB1, 4, 0, 1, 1)
        self.MAltegoTeethScrollArea.setWidget(self.MaltegoTeethScrollWidgetContents)
        self.gridLayout_16.addWidget(self.MAltegoTeethScrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.MaltegoTeethTab, "")
        self.masscanTab = QtWidgets.QWidget()
        self.masscanTab.setObjectName("masscanTab")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.masscanTab)
        self.gridLayout_18.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_18.setSpacing(6)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.masscanScrollArea = QtWidgets.QScrollArea(self.masscanTab)
        self.masscanScrollArea.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.masscanScrollArea.setWidgetResizable(True)
        self.masscanScrollArea.setObjectName("masscanScrollArea")
        self.masscanScrollWidgetContents = QtWidgets.QWidget()
        self.masscanScrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 3128, 1798))
        self.masscanScrollWidgetContents.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.masscanScrollWidgetContents.setObjectName("masscanScrollWidgetContents")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.masscanScrollWidgetContents)
        self.gridLayout_19.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_19.setSpacing(6)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.line_62 = QtWidgets.QFrame(self.masscanScrollWidgetContents)
        self.line_62.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_62.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_62.setObjectName("line_62")
        self.gridLayout_19.addWidget(self.line_62, 18, 0, 1, 1)
        self.masscanButton = QtWidgets.QPushButton(self.masscanScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.masscanButton.setFont(font)
        self.masscanButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(79, 79, 79);")
        self.masscanButton.setObjectName("masscanButton")
        self.gridLayout_19.addWidget(self.masscanButton, 19, 0, 1, 1)
        spacerItem35 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_19.addItem(spacerItem35, 20, 0, 1, 1)
        self.line_64 = QtWidgets.QFrame(self.masscanScrollWidgetContents)
        self.line_64.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_64.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_64.setObjectName("line_64")
        self.gridLayout_19.addWidget(self.line_64, 1, 0, 1, 1)
        self.line_65 = QtWidgets.QFrame(self.masscanScrollWidgetContents)
        self.line_65.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_65.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_65.setObjectName("line_65")
        self.gridLayout_19.addWidget(self.line_65, 11, 0, 1, 1)
        self.masscanTitle = QtWidgets.QLabel(self.masscanScrollWidgetContents)
        self.masscanTitle.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.masscanTitle.setFont(font)
        self.masscanTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.masscanTitle.setObjectName("masscanTitle")
        self.gridLayout_19.addWidget(self.masscanTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.line_61 = QtWidgets.QFrame(self.masscanScrollWidgetContents)
        self.line_61.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_61.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_61.setObjectName("line_61")
        self.gridLayout_19.addWidget(self.line_61, 7, 0, 1, 1)
        self.masscanH4 = QtWidgets.QLabel(self.masscanScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.masscanH4.setFont(font)
        self.masscanH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.masscanH4.setObjectName("masscanH4")
        self.gridLayout_19.addWidget(self.masscanH4, 17, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.line_63 = QtWidgets.QFrame(self.masscanScrollWidgetContents)
        self.line_63.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_63.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_63.setObjectName("line_63")
        self.gridLayout_19.addWidget(self.line_63, 10, 0, 1, 1)
        self.masscanH2 = QtWidgets.QLabel(self.masscanScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.masscanH2.setFont(font)
        self.masscanH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.masscanH2.setObjectName("masscanH2")
        self.gridLayout_19.addWidget(self.masscanH2, 6, 0, 1, 1)
        self.line_66 = QtWidgets.QFrame(self.masscanScrollWidgetContents)
        self.line_66.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_66.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_66.setObjectName("line_66")
        self.gridLayout_19.addWidget(self.line_66, 14, 0, 1, 1)
        self.masscanB2 = QtWidgets.QLabel(self.masscanScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.masscanB2.setFont(font)
        self.masscanB2.setObjectName("masscanB2")
        self.gridLayout_19.addWidget(self.masscanB2, 8, 0, 1, 1)
        self.masscanB3 = QtWidgets.QLabel(self.masscanScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.masscanB3.setFont(font)
        self.masscanB3.setObjectName("masscanB3")
        self.gridLayout_19.addWidget(self.masscanB3, 15, 0, 1, 1)
        self.masscanH1 = QtWidgets.QLabel(self.masscanScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.masscanH1.setFont(font)
        self.masscanH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.masscanH1.setObjectName("masscanH1")
        self.gridLayout_19.addWidget(self.masscanH1, 2, 0, 1, 1)
        self.line_68 = QtWidgets.QFrame(self.masscanScrollWidgetContents)
        self.line_68.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_68.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_68.setObjectName("line_68")
        self.gridLayout_19.addWidget(self.line_68, 3, 0, 1, 1)
        self.line_67 = QtWidgets.QFrame(self.masscanScrollWidgetContents)
        self.line_67.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_67.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_67.setObjectName("line_67")
        self.gridLayout_19.addWidget(self.line_67, 5, 0, 1, 1)
        self.masscanH3 = QtWidgets.QLabel(self.masscanScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.masscanH3.setFont(font)
        self.masscanH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.masscanH3.setObjectName("masscanH3")
        self.gridLayout_19.addWidget(self.masscanH3, 12, 0, 1, 1)
        self.masscanB1 = QtWidgets.QLabel(self.masscanScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.masscanB1.setFont(font)
        self.masscanB1.setTextFormat(QtCore.Qt.AutoText)
        self.masscanB1.setScaledContents(False)
        self.masscanB1.setWordWrap(False)
        self.masscanB1.setObjectName("masscanB1")
        self.gridLayout_19.addWidget(self.masscanB1, 4, 0, 1, 1)
        self.line_69 = QtWidgets.QFrame(self.masscanScrollWidgetContents)
        self.line_69.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_69.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_69.setObjectName("line_69")
        self.gridLayout_19.addWidget(self.line_69, 16, 0, 1, 1)
        self.masscanScrollArea.setWidget(self.masscanScrollWidgetContents)
        self.gridLayout_18.addWidget(self.masscanScrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.masscanTab, "")
        self.MetagoofilTab = QtWidgets.QWidget()
        self.MetagoofilTab.setObjectName("MetagoofilTab")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.MetagoofilTab)
        self.gridLayout_20.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_20.setSpacing(6)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.MetagoofilScrollArea = QtWidgets.QScrollArea(self.MetagoofilTab)
        self.MetagoofilScrollArea.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.MetagoofilScrollArea.setWidgetResizable(True)
        self.MetagoofilScrollArea.setObjectName("MetagoofilScrollArea")
        self.MetagoofilScrollWidgetContents = QtWidgets.QWidget()
        self.MetagoofilScrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 3128, 1586))
        self.MetagoofilScrollWidgetContents.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.MetagoofilScrollWidgetContents.setObjectName("MetagoofilScrollWidgetContents")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.MetagoofilScrollWidgetContents)
        self.gridLayout_21.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_21.setSpacing(6)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.line_70 = QtWidgets.QFrame(self.MetagoofilScrollWidgetContents)
        self.line_70.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_70.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_70.setObjectName("line_70")
        self.gridLayout_21.addWidget(self.line_70, 18, 0, 1, 1)
        self.MetagoofilButton = QtWidgets.QPushButton(self.MetagoofilScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.MetagoofilButton.setFont(font)
        self.MetagoofilButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(79, 79, 79);")
        self.MetagoofilButton.setObjectName("MetagoofilButton")
        self.gridLayout_21.addWidget(self.MetagoofilButton, 19, 0, 1, 1)
        spacerItem36 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_21.addItem(spacerItem36, 20, 0, 1, 1)
        self.line_71 = QtWidgets.QFrame(self.MetagoofilScrollWidgetContents)
        self.line_71.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_71.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_71.setObjectName("line_71")
        self.gridLayout_21.addWidget(self.line_71, 1, 0, 1, 1)
        self.line_72 = QtWidgets.QFrame(self.MetagoofilScrollWidgetContents)
        self.line_72.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_72.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_72.setObjectName("line_72")
        self.gridLayout_21.addWidget(self.line_72, 11, 0, 1, 1)
        self.MetagoofilTitle = QtWidgets.QLabel(self.MetagoofilScrollWidgetContents)
        self.MetagoofilTitle.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.MetagoofilTitle.setFont(font)
        self.MetagoofilTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.MetagoofilTitle.setObjectName("MetagoofilTitle")
        self.gridLayout_21.addWidget(self.MetagoofilTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.line_73 = QtWidgets.QFrame(self.MetagoofilScrollWidgetContents)
        self.line_73.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_73.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_73.setObjectName("line_73")
        self.gridLayout_21.addWidget(self.line_73, 7, 0, 1, 1)
        self.MetagoofilH4 = QtWidgets.QLabel(self.MetagoofilScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.MetagoofilH4.setFont(font)
        self.MetagoofilH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.MetagoofilH4.setObjectName("MetagoofilH4")
        self.gridLayout_21.addWidget(self.MetagoofilH4, 17, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.line_74 = QtWidgets.QFrame(self.MetagoofilScrollWidgetContents)
        self.line_74.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_74.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_74.setObjectName("line_74")
        self.gridLayout_21.addWidget(self.line_74, 10, 0, 1, 1)
        self.MetagoofilH2 = QtWidgets.QLabel(self.MetagoofilScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.MetagoofilH2.setFont(font)
        self.MetagoofilH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.MetagoofilH2.setObjectName("MetagoofilH2")
        self.gridLayout_21.addWidget(self.MetagoofilH2, 6, 0, 1, 1)
        self.line_75 = QtWidgets.QFrame(self.MetagoofilScrollWidgetContents)
        self.line_75.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_75.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_75.setObjectName("line_75")
        self.gridLayout_21.addWidget(self.line_75, 14, 0, 1, 1)
        self.MetagoofilB2 = QtWidgets.QLabel(self.MetagoofilScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.MetagoofilB2.setFont(font)
        self.MetagoofilB2.setObjectName("MetagoofilB2")
        self.gridLayout_21.addWidget(self.MetagoofilB2, 8, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.MetagoofilScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_21.addWidget(self.label_2, 15, 0, 1, 1)
        self.MetagoofilH1 = QtWidgets.QLabel(self.MetagoofilScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.MetagoofilH1.setFont(font)
        self.MetagoofilH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.MetagoofilH1.setObjectName("MetagoofilH1")
        self.gridLayout_21.addWidget(self.MetagoofilH1, 2, 0, 1, 1)
        self.line_76 = QtWidgets.QFrame(self.MetagoofilScrollWidgetContents)
        self.line_76.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_76.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_76.setObjectName("line_76")
        self.gridLayout_21.addWidget(self.line_76, 3, 0, 1, 1)
        self.line_77 = QtWidgets.QFrame(self.MetagoofilScrollWidgetContents)
        self.line_77.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_77.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_77.setObjectName("line_77")
        self.gridLayout_21.addWidget(self.line_77, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.MetagoofilScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(56, 196, 255);")
        self.label.setObjectName("label")
        self.gridLayout_21.addWidget(self.label, 12, 0, 1, 1)
        self.MetagoofilB1 = QtWidgets.QLabel(self.MetagoofilScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.MetagoofilB1.setFont(font)
        self.MetagoofilB1.setTextFormat(QtCore.Qt.AutoText)
        self.MetagoofilB1.setScaledContents(False)
        self.MetagoofilB1.setWordWrap(False)
        self.MetagoofilB1.setObjectName("MetagoofilB1")
        self.gridLayout_21.addWidget(self.MetagoofilB1, 4, 0, 1, 1)
        self.line_78 = QtWidgets.QFrame(self.MetagoofilScrollWidgetContents)
        self.line_78.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_78.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_78.setObjectName("line_78")
        self.gridLayout_21.addWidget(self.line_78, 16, 0, 1, 1)
        self.MetagoofilScrollArea.setWidget(self.MetagoofilScrollWidgetContents)
        self.gridLayout_20.addWidget(self.MetagoofilScrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.MetagoofilTab, "")
        self.MirandaTab = QtWidgets.QWidget()
        self.MirandaTab.setObjectName("MirandaTab")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.MirandaTab)
        self.gridLayout_22.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_22.setSpacing(6)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.MirandaScrollArea = QtWidgets.QScrollArea(self.MirandaTab)
        self.MirandaScrollArea.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.MirandaScrollArea.setWidgetResizable(True)
        self.MirandaScrollArea.setObjectName("MirandaScrollArea")
        self.MirandaScrollWidgetContents = QtWidgets.QWidget()
        self.MirandaScrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 3128, 2256))
        self.MirandaScrollWidgetContents.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.MirandaScrollWidgetContents.setObjectName("MirandaScrollWidgetContents")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.MirandaScrollWidgetContents)
        self.gridLayout_23.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_23.setSpacing(6)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.MirandaB2 = QtWidgets.QLabel(self.MirandaScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.MirandaB2.setFont(font)
        self.MirandaB2.setObjectName("MirandaB2")
        self.gridLayout_23.addWidget(self.MirandaB2, 8, 0, 1, 1)
        spacerItem37 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_23.addItem(spacerItem37, 17, 0, 1, 1)
        self.line_84 = QtWidgets.QFrame(self.MirandaScrollWidgetContents)
        self.line_84.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_84.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_84.setObjectName("line_84")
        self.gridLayout_23.addWidget(self.line_84, 13, 0, 1, 1)
        self.MirandaH3 = QtWidgets.QLabel(self.MirandaScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.MirandaH3.setFont(font)
        self.MirandaH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.MirandaH3.setObjectName("MirandaH3")
        self.gridLayout_23.addWidget(self.MirandaH3, 10, 0, 1, 1)
        self.line_80 = QtWidgets.QFrame(self.MirandaScrollWidgetContents)
        self.line_80.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_80.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_80.setObjectName("line_80")
        self.gridLayout_23.addWidget(self.line_80, 5, 0, 1, 1)
        self.line_79 = QtWidgets.QFrame(self.MirandaScrollWidgetContents)
        self.line_79.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_79.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_79.setObjectName("line_79")
        self.gridLayout_23.addWidget(self.line_79, 1, 0, 1, 1)
        self.line_81 = QtWidgets.QFrame(self.MirandaScrollWidgetContents)
        self.line_81.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_81.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_81.setObjectName("line_81")
        self.gridLayout_23.addWidget(self.line_81, 7, 0, 1, 1)
        self.MirandaH4 = QtWidgets.QLabel(self.MirandaScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.MirandaH4.setFont(font)
        self.MirandaH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.MirandaH4.setObjectName("MirandaH4")
        self.gridLayout_23.addWidget(self.MirandaH4, 14, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.MirandaH1 = QtWidgets.QLabel(self.MirandaScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.MirandaH1.setFont(font)
        self.MirandaH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.MirandaH1.setObjectName("MirandaH1")
        self.gridLayout_23.addWidget(self.MirandaH1, 2, 0, 1, 1)
        self.line_82 = QtWidgets.QFrame(self.MirandaScrollWidgetContents)
        self.line_82.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_82.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_82.setObjectName("line_82")
        self.gridLayout_23.addWidget(self.line_82, 9, 0, 1, 1)
        self.MirandaB3 = QtWidgets.QLabel(self.MirandaScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.MirandaB3.setFont(font)
        self.MirandaB3.setObjectName("MirandaB3")
        self.gridLayout_23.addWidget(self.MirandaB3, 12, 0, 1, 1)
        self.MirandaButton = QtWidgets.QPushButton(self.MirandaScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.MirandaButton.setFont(font)
        self.MirandaButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(79, 79, 79);")
        self.MirandaButton.setObjectName("MirandaButton")
        self.gridLayout_23.addWidget(self.MirandaButton, 16, 0, 1, 1)
        self.line_86 = QtWidgets.QFrame(self.MirandaScrollWidgetContents)
        self.line_86.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_86.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_86.setObjectName("line_86")
        self.gridLayout_23.addWidget(self.line_86, 15, 0, 1, 1)
        self.line_85 = QtWidgets.QFrame(self.MirandaScrollWidgetContents)
        self.line_85.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_85.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_85.setObjectName("line_85")
        self.gridLayout_23.addWidget(self.line_85, 3, 0, 1, 1)
        self.MirandaH2 = QtWidgets.QLabel(self.MirandaScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.MirandaH2.setFont(font)
        self.MirandaH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.MirandaH2.setObjectName("MirandaH2")
        self.gridLayout_23.addWidget(self.MirandaH2, 6, 0, 1, 1)
        self.line_83 = QtWidgets.QFrame(self.MirandaScrollWidgetContents)
        self.line_83.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_83.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_83.setObjectName("line_83")
        self.gridLayout_23.addWidget(self.line_83, 11, 0, 1, 1)
        self.MirandaTitle = QtWidgets.QLabel(self.MirandaScrollWidgetContents)
        self.MirandaTitle.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.MirandaTitle.setFont(font)
        self.MirandaTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.MirandaTitle.setObjectName("MirandaTitle")
        self.gridLayout_23.addWidget(self.MirandaTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.MirandaB1 = QtWidgets.QLabel(self.MirandaScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.MirandaB1.setFont(font)
        self.MirandaB1.setTextFormat(QtCore.Qt.AutoText)
        self.MirandaB1.setScaledContents(False)
        self.MirandaB1.setWordWrap(False)
        self.MirandaB1.setObjectName("MirandaB1")
        self.gridLayout_23.addWidget(self.MirandaB1, 4, 0, 1, 1)
        self.MirandaScrollArea.setWidget(self.MirandaScrollWidgetContents)
        self.gridLayout_22.addWidget(self.MirandaScrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.MirandaTab, "")
        self.nbtscanUnixwizTab = QtWidgets.QWidget()
        self.nbtscanUnixwizTab.setObjectName("nbtscanUnixwizTab")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.nbtscanUnixwizTab)
        self.gridLayout_24.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_24.setSpacing(6)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.nbtscanUnixwizScrollArea = QtWidgets.QScrollArea(self.nbtscanUnixwizTab)
        self.nbtscanUnixwizScrollArea.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.nbtscanUnixwizScrollArea.setWidgetResizable(True)
        self.nbtscanUnixwizScrollArea.setObjectName("nbtscanUnixwizScrollArea")
        self.nbtscanUnixwizScrollWidgetContents = QtWidgets.QWidget()
        self.nbtscanUnixwizScrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 3128, 1769))
        self.nbtscanUnixwizScrollWidgetContents.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.nbtscanUnixwizScrollWidgetContents.setObjectName("nbtscanUnixwizScrollWidgetContents")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.nbtscanUnixwizScrollWidgetContents)
        self.gridLayout_25.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_25.setSpacing(6)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.nbtscanUnixwizB2 = QtWidgets.QLabel(self.nbtscanUnixwizScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nbtscanUnixwizB2.setFont(font)
        self.nbtscanUnixwizB2.setObjectName("nbtscanUnixwizB2")
        self.gridLayout_25.addWidget(self.nbtscanUnixwizB2, 8, 0, 1, 1)
        spacerItem38 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_25.addItem(spacerItem38, 17, 0, 1, 1)
        self.line_87 = QtWidgets.QFrame(self.nbtscanUnixwizScrollWidgetContents)
        self.line_87.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_87.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_87.setObjectName("line_87")
        self.gridLayout_25.addWidget(self.line_87, 13, 0, 1, 1)
        self.nbtscanUnixwizH3 = QtWidgets.QLabel(self.nbtscanUnixwizScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.nbtscanUnixwizH3.setFont(font)
        self.nbtscanUnixwizH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.nbtscanUnixwizH3.setObjectName("nbtscanUnixwizH3")
        self.gridLayout_25.addWidget(self.nbtscanUnixwizH3, 10, 0, 1, 1)
        self.line_88 = QtWidgets.QFrame(self.nbtscanUnixwizScrollWidgetContents)
        self.line_88.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_88.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_88.setObjectName("line_88")
        self.gridLayout_25.addWidget(self.line_88, 5, 0, 1, 1)
        self.line_89 = QtWidgets.QFrame(self.nbtscanUnixwizScrollWidgetContents)
        self.line_89.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_89.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_89.setObjectName("line_89")
        self.gridLayout_25.addWidget(self.line_89, 1, 0, 1, 1)
        self.line_90 = QtWidgets.QFrame(self.nbtscanUnixwizScrollWidgetContents)
        self.line_90.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_90.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_90.setObjectName("line_90")
        self.gridLayout_25.addWidget(self.line_90, 7, 0, 1, 1)
        self.nbtscanUnixwizH4 = QtWidgets.QLabel(self.nbtscanUnixwizScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.nbtscanUnixwizH4.setFont(font)
        self.nbtscanUnixwizH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.nbtscanUnixwizH4.setObjectName("nbtscanUnixwizH4")
        self.gridLayout_25.addWidget(self.nbtscanUnixwizH4, 14, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.nbtscanUnixwizH1 = QtWidgets.QLabel(self.nbtscanUnixwizScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.nbtscanUnixwizH1.setFont(font)
        self.nbtscanUnixwizH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.nbtscanUnixwizH1.setObjectName("nbtscanUnixwizH1")
        self.gridLayout_25.addWidget(self.nbtscanUnixwizH1, 2, 0, 1, 1)
        self.line_91 = QtWidgets.QFrame(self.nbtscanUnixwizScrollWidgetContents)
        self.line_91.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_91.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_91.setObjectName("line_91")
        self.gridLayout_25.addWidget(self.line_91, 9, 0, 1, 1)
        self.nbtscanUnixwizB3 = QtWidgets.QLabel(self.nbtscanUnixwizScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nbtscanUnixwizB3.setFont(font)
        self.nbtscanUnixwizB3.setObjectName("nbtscanUnixwizB3")
        self.gridLayout_25.addWidget(self.nbtscanUnixwizB3, 12, 0, 1, 1)
        self.nbtscanUnixwizButton = QtWidgets.QPushButton(self.nbtscanUnixwizScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nbtscanUnixwizButton.setFont(font)
        self.nbtscanUnixwizButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(79, 79, 79);")
        self.nbtscanUnixwizButton.setObjectName("nbtscanUnixwizButton")
        self.gridLayout_25.addWidget(self.nbtscanUnixwizButton, 16, 0, 1, 1)
        self.line_92 = QtWidgets.QFrame(self.nbtscanUnixwizScrollWidgetContents)
        self.line_92.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_92.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_92.setObjectName("line_92")
        self.gridLayout_25.addWidget(self.line_92, 15, 0, 1, 1)
        self.line_93 = QtWidgets.QFrame(self.nbtscanUnixwizScrollWidgetContents)
        self.line_93.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_93.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_93.setObjectName("line_93")
        self.gridLayout_25.addWidget(self.line_93, 3, 0, 1, 1)
        self.nbtscanUnixwizH2 = QtWidgets.QLabel(self.nbtscanUnixwizScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.nbtscanUnixwizH2.setFont(font)
        self.nbtscanUnixwizH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.nbtscanUnixwizH2.setObjectName("nbtscanUnixwizH2")
        self.gridLayout_25.addWidget(self.nbtscanUnixwizH2, 6, 0, 1, 1)
        self.line_94 = QtWidgets.QFrame(self.nbtscanUnixwizScrollWidgetContents)
        self.line_94.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_94.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_94.setObjectName("line_94")
        self.gridLayout_25.addWidget(self.line_94, 11, 0, 1, 1)
        self.nbtscanUnixwizTitle = QtWidgets.QLabel(self.nbtscanUnixwizScrollWidgetContents)
        self.nbtscanUnixwizTitle.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.nbtscanUnixwizTitle.setFont(font)
        self.nbtscanUnixwizTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.nbtscanUnixwizTitle.setObjectName("nbtscanUnixwizTitle")
        self.gridLayout_25.addWidget(self.nbtscanUnixwizTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.nbtscanUnixwizB1 = QtWidgets.QLabel(self.nbtscanUnixwizScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nbtscanUnixwizB1.setFont(font)
        self.nbtscanUnixwizB1.setTextFormat(QtCore.Qt.AutoText)
        self.nbtscanUnixwizB1.setScaledContents(False)
        self.nbtscanUnixwizB1.setWordWrap(False)
        self.nbtscanUnixwizB1.setObjectName("nbtscanUnixwizB1")
        self.gridLayout_25.addWidget(self.nbtscanUnixwizB1, 4, 0, 1, 1)
        self.nbtscanUnixwizScrollArea.setWidget(self.nbtscanUnixwizScrollWidgetContents)
        self.gridLayout_24.addWidget(self.nbtscanUnixwizScrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.nbtscanUnixwizTab, "")
        self.NmapTab = QtWidgets.QWidget()
        self.NmapTab.setObjectName("NmapTab")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.NmapTab)
        self.gridLayout_27.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_27.setSpacing(6)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.NmapScrollArea = QtWidgets.QScrollArea(self.NmapTab)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.NmapScrollArea.setFont(font)
        self.NmapScrollArea.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.NmapScrollArea.setWidgetResizable(True)
        self.NmapScrollArea.setObjectName("NmapScrollArea")
        self.NmapScrollWidgetContents = QtWidgets.QWidget()
        self.NmapScrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 3128, 6326))
        self.NmapScrollWidgetContents.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.NmapScrollWidgetContents.setObjectName("NmapScrollWidgetContents")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.NmapScrollWidgetContents)
        self.gridLayout_26.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_26.setSpacing(6)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.NmapB2 = QtWidgets.QLabel(self.NmapScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.NmapB2.setFont(font)
        self.NmapB2.setObjectName("NmapB2")
        self.gridLayout_26.addWidget(self.NmapB2, 8, 0, 1, 1)
        spacerItem39 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_26.addItem(spacerItem39, 17, 0, 1, 1)
        self.line_95 = QtWidgets.QFrame(self.NmapScrollWidgetContents)
        self.line_95.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_95.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_95.setObjectName("line_95")
        self.gridLayout_26.addWidget(self.line_95, 13, 0, 1, 1)
        self.NmapH3 = QtWidgets.QLabel(self.NmapScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.NmapH3.setFont(font)
        self.NmapH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.NmapH3.setObjectName("NmapH3")
        self.gridLayout_26.addWidget(self.NmapH3, 10, 0, 1, 1)
        self.line_96 = QtWidgets.QFrame(self.NmapScrollWidgetContents)
        self.line_96.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_96.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_96.setObjectName("line_96")
        self.gridLayout_26.addWidget(self.line_96, 5, 0, 1, 1)
        self.line_97 = QtWidgets.QFrame(self.NmapScrollWidgetContents)
        self.line_97.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_97.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_97.setObjectName("line_97")
        self.gridLayout_26.addWidget(self.line_97, 1, 0, 1, 1)
        self.line_98 = QtWidgets.QFrame(self.NmapScrollWidgetContents)
        self.line_98.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_98.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_98.setObjectName("line_98")
        self.gridLayout_26.addWidget(self.line_98, 7, 0, 1, 1)
        self.NmapH4 = QtWidgets.QLabel(self.NmapScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.NmapH4.setFont(font)
        self.NmapH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.NmapH4.setObjectName("NmapH4")
        self.gridLayout_26.addWidget(self.NmapH4, 14, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.NmapH1 = QtWidgets.QLabel(self.NmapScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.NmapH1.setFont(font)
        self.NmapH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.NmapH1.setObjectName("NmapH1")
        self.gridLayout_26.addWidget(self.NmapH1, 2, 0, 1, 1)
        self.line_99 = QtWidgets.QFrame(self.NmapScrollWidgetContents)
        self.line_99.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_99.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_99.setObjectName("line_99")
        self.gridLayout_26.addWidget(self.line_99, 9, 0, 1, 1)
        self.NmapB3 = QtWidgets.QLabel(self.NmapScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.NmapB3.setFont(font)
        self.NmapB3.setObjectName("NmapB3")
        self.gridLayout_26.addWidget(self.NmapB3, 12, 0, 1, 1)
        self.NmapButton = QtWidgets.QPushButton(self.NmapScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.NmapButton.setFont(font)
        self.NmapButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(79, 79, 79);")
        self.NmapButton.setObjectName("NmapButton")
        self.gridLayout_26.addWidget(self.NmapButton, 16, 0, 1, 1)
        self.line_100 = QtWidgets.QFrame(self.NmapScrollWidgetContents)
        self.line_100.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_100.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_100.setObjectName("line_100")
        self.gridLayout_26.addWidget(self.line_100, 15, 0, 1, 1)
        self.line_101 = QtWidgets.QFrame(self.NmapScrollWidgetContents)
        self.line_101.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_101.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_101.setObjectName("line_101")
        self.gridLayout_26.addWidget(self.line_101, 3, 0, 1, 1)
        self.NmapH2 = QtWidgets.QLabel(self.NmapScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.NmapH2.setFont(font)
        self.NmapH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.NmapH2.setObjectName("NmapH2")
        self.gridLayout_26.addWidget(self.NmapH2, 6, 0, 1, 1)
        self.line_102 = QtWidgets.QFrame(self.NmapScrollWidgetContents)
        self.line_102.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_102.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_102.setObjectName("line_102")
        self.gridLayout_26.addWidget(self.line_102, 11, 0, 1, 1)
        self.NmapTitle = QtWidgets.QLabel(self.NmapScrollWidgetContents)
        self.NmapTitle.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.NmapTitle.setFont(font)
        self.NmapTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.NmapTitle.setObjectName("NmapTitle")
        self.gridLayout_26.addWidget(self.NmapTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.NmapB1 = QtWidgets.QLabel(self.NmapScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.NmapB1.setFont(font)
        self.NmapB1.setTextFormat(QtCore.Qt.AutoText)
        self.NmapB1.setScaledContents(False)
        self.NmapB1.setWordWrap(False)
        self.NmapB1.setObjectName("NmapB1")
        self.gridLayout_26.addWidget(self.NmapB1, 4, 0, 1, 1)
        self.NmapScrollArea.setWidget(self.NmapScrollWidgetContents)
        self.gridLayout_27.addWidget(self.NmapScrollArea, 0, 0, 2, 2)
        self.tabWidget.addTab(self.NmapTab, "")
        self.ntopTab = QtWidgets.QWidget()
        self.ntopTab.setObjectName("ntopTab")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.ntopTab)
        self.gridLayout_28.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_28.setSpacing(6)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.ntopScrollArea = QtWidgets.QScrollArea(self.ntopTab)
        self.ntopScrollArea.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.ntopScrollArea.setWidgetResizable(True)
        self.ntopScrollArea.setObjectName("ntopScrollArea")
        self.ntopScrollWidgetContents = QtWidgets.QWidget()
        self.ntopScrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 3128, 2862))
        self.ntopScrollWidgetContents.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.ntopScrollWidgetContents.setObjectName("ntopScrollWidgetContents")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.ntopScrollWidgetContents)
        self.gridLayout_29.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_29.setSpacing(6)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.ntopB2 = QtWidgets.QLabel(self.ntopScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ntopB2.setFont(font)
        self.ntopB2.setObjectName("ntopB2")
        self.gridLayout_29.addWidget(self.ntopB2, 8, 0, 1, 1)
        spacerItem40 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_29.addItem(spacerItem40, 17, 0, 1, 1)
        self.line_103 = QtWidgets.QFrame(self.ntopScrollWidgetContents)
        self.line_103.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_103.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_103.setObjectName("line_103")
        self.gridLayout_29.addWidget(self.line_103, 13, 0, 1, 1)
        self.ntopH3 = QtWidgets.QLabel(self.ntopScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.ntopH3.setFont(font)
        self.ntopH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.ntopH3.setObjectName("ntopH3")
        self.gridLayout_29.addWidget(self.ntopH3, 10, 0, 1, 1)
        self.line_104 = QtWidgets.QFrame(self.ntopScrollWidgetContents)
        self.line_104.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_104.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_104.setObjectName("line_104")
        self.gridLayout_29.addWidget(self.line_104, 5, 0, 1, 1)
        self.line_105 = QtWidgets.QFrame(self.ntopScrollWidgetContents)
        self.line_105.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_105.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_105.setObjectName("line_105")
        self.gridLayout_29.addWidget(self.line_105, 1, 0, 1, 1)
        self.line_106 = QtWidgets.QFrame(self.ntopScrollWidgetContents)
        self.line_106.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_106.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_106.setObjectName("line_106")
        self.gridLayout_29.addWidget(self.line_106, 7, 0, 1, 1)
        self.ntopH4 = QtWidgets.QLabel(self.ntopScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.ntopH4.setFont(font)
        self.ntopH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.ntopH4.setObjectName("ntopH4")
        self.gridLayout_29.addWidget(self.ntopH4, 14, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.ntopH1 = QtWidgets.QLabel(self.ntopScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.ntopH1.setFont(font)
        self.ntopH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.ntopH1.setObjectName("ntopH1")
        self.gridLayout_29.addWidget(self.ntopH1, 2, 0, 1, 1)
        self.line_107 = QtWidgets.QFrame(self.ntopScrollWidgetContents)
        self.line_107.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_107.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_107.setObjectName("line_107")
        self.gridLayout_29.addWidget(self.line_107, 9, 0, 1, 1)
        self.ntopB3 = QtWidgets.QLabel(self.ntopScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ntopB3.setFont(font)
        self.ntopB3.setObjectName("ntopB3")
        self.gridLayout_29.addWidget(self.ntopB3, 12, 0, 1, 1)
        self.ntopButton = QtWidgets.QPushButton(self.ntopScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ntopButton.setFont(font)
        self.ntopButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(79, 79, 79);")
        self.ntopButton.setObjectName("ntopButton")
        self.gridLayout_29.addWidget(self.ntopButton, 16, 0, 1, 1)
        self.line_108 = QtWidgets.QFrame(self.ntopScrollWidgetContents)
        self.line_108.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_108.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_108.setObjectName("line_108")
        self.gridLayout_29.addWidget(self.line_108, 15, 0, 1, 1)
        self.line_109 = QtWidgets.QFrame(self.ntopScrollWidgetContents)
        self.line_109.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_109.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_109.setObjectName("line_109")
        self.gridLayout_29.addWidget(self.line_109, 3, 0, 1, 1)
        self.ntopH2 = QtWidgets.QLabel(self.ntopScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.ntopH2.setFont(font)
        self.ntopH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.ntopH2.setObjectName("ntopH2")
        self.gridLayout_29.addWidget(self.ntopH2, 6, 0, 1, 1)
        self.line_110 = QtWidgets.QFrame(self.ntopScrollWidgetContents)
        self.line_110.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_110.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_110.setObjectName("line_110")
        self.gridLayout_29.addWidget(self.line_110, 11, 0, 1, 1)
        self.ntopTitle = QtWidgets.QLabel(self.ntopScrollWidgetContents)
        self.ntopTitle.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.ntopTitle.setFont(font)
        self.ntopTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.ntopTitle.setObjectName("ntopTitle")
        self.gridLayout_29.addWidget(self.ntopTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.ntopB1 = QtWidgets.QLabel(self.ntopScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ntopB1.setFont(font)
        self.ntopB1.setTextFormat(QtCore.Qt.AutoText)
        self.ntopB1.setScaledContents(False)
        self.ntopB1.setWordWrap(False)
        self.ntopB1.setObjectName("ntopB1")
        self.gridLayout_29.addWidget(self.ntopB1, 4, 0, 1, 1)
        self.ntopScrollArea.setWidget(self.ntopScrollWidgetContents)
        self.gridLayout_28.addWidget(self.ntopScrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.ntopTab, "")
        self.p0fTab = QtWidgets.QWidget()
        self.p0fTab.setObjectName("p0fTab")
        self.gridLayout_30 = QtWidgets.QGridLayout(self.p0fTab)
        self.gridLayout_30.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_30.setSpacing(6)
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.p0fScrollArea = QtWidgets.QScrollArea(self.p0fTab)
        self.p0fScrollArea.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.p0fScrollArea.setWidgetResizable(True)
        self.p0fScrollArea.setObjectName("p0fScrollArea")
        self.p0fScrollWidgetContents = QtWidgets.QWidget()
        self.p0fScrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 3128, 2822))
        self.p0fScrollWidgetContents.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.p0fScrollWidgetContents.setObjectName("p0fScrollWidgetContents")
        self.gridLayout_31 = QtWidgets.QGridLayout(self.p0fScrollWidgetContents)
        self.gridLayout_31.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_31.setSpacing(6)
        self.gridLayout_31.setObjectName("gridLayout_31")
        self.p0fB2 = QtWidgets.QLabel(self.p0fScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.p0fB2.setFont(font)
        self.p0fB2.setObjectName("p0fB2")
        self.gridLayout_31.addWidget(self.p0fB2, 8, 0, 1, 1)
        spacerItem41 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_31.addItem(spacerItem41, 17, 0, 1, 1)
        self.line_111 = QtWidgets.QFrame(self.p0fScrollWidgetContents)
        self.line_111.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_111.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_111.setObjectName("line_111")
        self.gridLayout_31.addWidget(self.line_111, 13, 0, 1, 1)
        self.p0fH3 = QtWidgets.QLabel(self.p0fScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.p0fH3.setFont(font)
        self.p0fH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.p0fH3.setObjectName("p0fH3")
        self.gridLayout_31.addWidget(self.p0fH3, 10, 0, 1, 1)
        self.line_112 = QtWidgets.QFrame(self.p0fScrollWidgetContents)
        self.line_112.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_112.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_112.setObjectName("line_112")
        self.gridLayout_31.addWidget(self.line_112, 5, 0, 1, 1)
        self.line_113 = QtWidgets.QFrame(self.p0fScrollWidgetContents)
        self.line_113.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_113.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_113.setObjectName("line_113")
        self.gridLayout_31.addWidget(self.line_113, 1, 0, 1, 1)
        self.line_114 = QtWidgets.QFrame(self.p0fScrollWidgetContents)
        self.line_114.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_114.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_114.setObjectName("line_114")
        self.gridLayout_31.addWidget(self.line_114, 7, 0, 1, 1)
        self.p0fH4 = QtWidgets.QLabel(self.p0fScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.p0fH4.setFont(font)
        self.p0fH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.p0fH4.setObjectName("p0fH4")
        self.gridLayout_31.addWidget(self.p0fH4, 14, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.p0fH1 = QtWidgets.QLabel(self.p0fScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.p0fH1.setFont(font)
        self.p0fH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.p0fH1.setObjectName("p0fH1")
        self.gridLayout_31.addWidget(self.p0fH1, 2, 0, 1, 1)
        self.line_115 = QtWidgets.QFrame(self.p0fScrollWidgetContents)
        self.line_115.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_115.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_115.setObjectName("line_115")
        self.gridLayout_31.addWidget(self.line_115, 9, 0, 1, 1)
        self.p0fB3 = QtWidgets.QLabel(self.p0fScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.p0fB3.setFont(font)
        self.p0fB3.setObjectName("p0fB3")
        self.gridLayout_31.addWidget(self.p0fB3, 12, 0, 1, 1)
        self.p0fButton = QtWidgets.QPushButton(self.p0fScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.p0fButton.setFont(font)
        self.p0fButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(79, 79, 79);")
        self.p0fButton.setObjectName("p0fButton")
        self.gridLayout_31.addWidget(self.p0fButton, 16, 0, 1, 1)
        self.line_116 = QtWidgets.QFrame(self.p0fScrollWidgetContents)
        self.line_116.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_116.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_116.setObjectName("line_116")
        self.gridLayout_31.addWidget(self.line_116, 15, 0, 1, 1)
        self.line_117 = QtWidgets.QFrame(self.p0fScrollWidgetContents)
        self.line_117.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_117.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_117.setObjectName("line_117")
        self.gridLayout_31.addWidget(self.line_117, 3, 0, 1, 1)
        self.p0fH2 = QtWidgets.QLabel(self.p0fScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.p0fH2.setFont(font)
        self.p0fH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.p0fH2.setObjectName("p0fH2")
        self.gridLayout_31.addWidget(self.p0fH2, 6, 0, 1, 1)
        self.line_118 = QtWidgets.QFrame(self.p0fScrollWidgetContents)
        self.line_118.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_118.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_118.setObjectName("line_118")
        self.gridLayout_31.addWidget(self.line_118, 11, 0, 1, 1)
        self.p0fTitle = QtWidgets.QLabel(self.p0fScrollWidgetContents)
        self.p0fTitle.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.p0fTitle.setFont(font)
        self.p0fTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.p0fTitle.setObjectName("p0fTitle")
        self.gridLayout_31.addWidget(self.p0fTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.p0fB1 = QtWidgets.QLabel(self.p0fScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.p0fB1.setFont(font)
        self.p0fB1.setTextFormat(QtCore.Qt.AutoText)
        self.p0fB1.setScaledContents(False)
        self.p0fB1.setWordWrap(False)
        self.p0fB1.setObjectName("p0fB1")
        self.gridLayout_31.addWidget(self.p0fB1, 4, 0, 1, 1)
        self.p0fScrollArea.setWidget(self.p0fScrollWidgetContents)
        self.gridLayout_30.addWidget(self.p0fScrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.p0fTab, "")
        self.PareseroTab = QtWidgets.QWidget()
        self.PareseroTab.setObjectName("PareseroTab")
        self.gridLayout_32 = QtWidgets.QGridLayout(self.PareseroTab)
        self.gridLayout_32.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_32.setSpacing(6)
        self.gridLayout_32.setObjectName("gridLayout_32")
        self.ParseroScrollArea = QtWidgets.QScrollArea(self.PareseroTab)
        self.ParseroScrollArea.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.ParseroScrollArea.setWidgetResizable(True)
        self.ParseroScrollArea.setObjectName("ParseroScrollArea")
        self.PareseroScrollWidgetContents = QtWidgets.QWidget()
        self.PareseroScrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 3128, 2376))
        self.PareseroScrollWidgetContents.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.PareseroScrollWidgetContents.setObjectName("PareseroScrollWidgetContents")
        self.gridLayout_33 = QtWidgets.QGridLayout(self.PareseroScrollWidgetContents)
        self.gridLayout_33.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_33.setSpacing(6)
        self.gridLayout_33.setObjectName("gridLayout_33")
        self.ParseroB2 = QtWidgets.QLabel(self.PareseroScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ParseroB2.setFont(font)
        self.ParseroB2.setObjectName("ParseroB2")
        self.gridLayout_33.addWidget(self.ParseroB2, 8, 0, 1, 1)
        spacerItem42 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_33.addItem(spacerItem42, 17, 0, 1, 1)
        self.line_119 = QtWidgets.QFrame(self.PareseroScrollWidgetContents)
        self.line_119.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_119.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_119.setObjectName("line_119")
        self.gridLayout_33.addWidget(self.line_119, 13, 0, 1, 1)
        self.ParseroH3 = QtWidgets.QLabel(self.PareseroScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.ParseroH3.setFont(font)
        self.ParseroH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.ParseroH3.setObjectName("ParseroH3")
        self.gridLayout_33.addWidget(self.ParseroH3, 10, 0, 1, 1)
        self.line_120 = QtWidgets.QFrame(self.PareseroScrollWidgetContents)
        self.line_120.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_120.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_120.setObjectName("line_120")
        self.gridLayout_33.addWidget(self.line_120, 5, 0, 1, 1)
        self.line_121 = QtWidgets.QFrame(self.PareseroScrollWidgetContents)
        self.line_121.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_121.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_121.setObjectName("line_121")
        self.gridLayout_33.addWidget(self.line_121, 1, 0, 1, 1)
        self.line_122 = QtWidgets.QFrame(self.PareseroScrollWidgetContents)
        self.line_122.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_122.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_122.setObjectName("line_122")
        self.gridLayout_33.addWidget(self.line_122, 7, 0, 1, 1)
        self.ParseroH4 = QtWidgets.QLabel(self.PareseroScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.ParseroH4.setFont(font)
        self.ParseroH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.ParseroH4.setObjectName("ParseroH4")
        self.gridLayout_33.addWidget(self.ParseroH4, 14, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.ParseroH1 = QtWidgets.QLabel(self.PareseroScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.ParseroH1.setFont(font)
        self.ParseroH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.ParseroH1.setObjectName("ParseroH1")
        self.gridLayout_33.addWidget(self.ParseroH1, 2, 0, 1, 1)
        self.line_123 = QtWidgets.QFrame(self.PareseroScrollWidgetContents)
        self.line_123.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_123.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_123.setObjectName("line_123")
        self.gridLayout_33.addWidget(self.line_123, 9, 0, 1, 1)
        self.ParseroB3 = QtWidgets.QLabel(self.PareseroScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ParseroB3.setFont(font)
        self.ParseroB3.setObjectName("ParseroB3")
        self.gridLayout_33.addWidget(self.ParseroB3, 12, 0, 1, 1)
        self.ParseroButton = QtWidgets.QPushButton(self.PareseroScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ParseroButton.setFont(font)
        self.ParseroButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(79, 79, 79);")
        self.ParseroButton.setObjectName("ParseroButton")
        self.gridLayout_33.addWidget(self.ParseroButton, 16, 0, 1, 1)
        self.line_124 = QtWidgets.QFrame(self.PareseroScrollWidgetContents)
        self.line_124.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_124.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_124.setObjectName("line_124")
        self.gridLayout_33.addWidget(self.line_124, 15, 0, 1, 1)
        self.line_125 = QtWidgets.QFrame(self.PareseroScrollWidgetContents)
        self.line_125.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_125.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_125.setObjectName("line_125")
        self.gridLayout_33.addWidget(self.line_125, 3, 0, 1, 1)
        self.ParseroH2 = QtWidgets.QLabel(self.PareseroScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.ParseroH2.setFont(font)
        self.ParseroH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.ParseroH2.setObjectName("ParseroH2")
        self.gridLayout_33.addWidget(self.ParseroH2, 6, 0, 1, 1)
        self.line_126 = QtWidgets.QFrame(self.PareseroScrollWidgetContents)
        self.line_126.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_126.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_126.setObjectName("line_126")
        self.gridLayout_33.addWidget(self.line_126, 11, 0, 1, 1)
        self.ParseroTitle = QtWidgets.QLabel(self.PareseroScrollWidgetContents)
        self.ParseroTitle.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.ParseroTitle.setFont(font)
        self.ParseroTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.ParseroTitle.setObjectName("ParseroTitle")
        self.gridLayout_33.addWidget(self.ParseroTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.ParseroB1 = QtWidgets.QLabel(self.PareseroScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ParseroB1.setFont(font)
        self.ParseroB1.setTextFormat(QtCore.Qt.AutoText)
        self.ParseroB1.setScaledContents(False)
        self.ParseroB1.setWordWrap(False)
        self.ParseroB1.setObjectName("ParseroB1")
        self.gridLayout_33.addWidget(self.ParseroB1, 4, 0, 1, 1)
        self.ParseroScrollArea.setWidget(self.PareseroScrollWidgetContents)
        self.gridLayout_32.addWidget(self.ParseroScrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.PareseroTab, "")
        self.ReconNgTab = QtWidgets.QWidget()
        self.ReconNgTab.setObjectName("ReconNgTab")
        self.gridLayout_34 = QtWidgets.QGridLayout(self.ReconNgTab)
        self.gridLayout_34.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_34.setSpacing(6)
        self.gridLayout_34.setObjectName("gridLayout_34")
        self.ReconNgScrollArea = QtWidgets.QScrollArea(self.ReconNgTab)
        self.ReconNgScrollArea.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.ReconNgScrollArea.setWidgetResizable(True)
        self.ReconNgScrollArea.setObjectName("ReconNgScrollArea")
        self.ReconNgScrollWidgetContents = QtWidgets.QWidget()
        self.ReconNgScrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 3128, 2516))
        self.ReconNgScrollWidgetContents.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.ReconNgScrollWidgetContents.setObjectName("ReconNgScrollWidgetContents")
        self.gridLayout_35 = QtWidgets.QGridLayout(self.ReconNgScrollWidgetContents)
        self.gridLayout_35.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_35.setSpacing(6)
        self.gridLayout_35.setObjectName("gridLayout_35")
        self.line_127 = QtWidgets.QFrame(self.ReconNgScrollWidgetContents)
        self.line_127.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_127.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_127.setObjectName("line_127")
        self.gridLayout_35.addWidget(self.line_127, 11, 0, 1, 1)
        spacerItem43 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_35.addItem(spacerItem43, 15, 0, 1, 1)
        self.ReconNgB2 = QtWidgets.QLabel(self.ReconNgScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ReconNgB2.setFont(font)
        self.ReconNgB2.setObjectName("ReconNgB2")
        self.gridLayout_35.addWidget(self.ReconNgB2, 8, 0, 1, 1)
        self.ReconNgH2 = QtWidgets.QLabel(self.ReconNgScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.ReconNgH2.setFont(font)
        self.ReconNgH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.ReconNgH2.setObjectName("ReconNgH2")
        self.gridLayout_35.addWidget(self.ReconNgH2, 6, 0, 1, 1)
        self.line_133 = QtWidgets.QFrame(self.ReconNgScrollWidgetContents)
        self.line_133.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_133.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_133.setObjectName("line_133")
        self.gridLayout_35.addWidget(self.line_133, 3, 0, 1, 1)
        self.line_132 = QtWidgets.QFrame(self.ReconNgScrollWidgetContents)
        self.line_132.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_132.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_132.setObjectName("line_132")
        self.gridLayout_35.addWidget(self.line_132, 13, 0, 1, 1)
        self.ReconNgTitle = QtWidgets.QLabel(self.ReconNgScrollWidgetContents)
        self.ReconNgTitle.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.ReconNgTitle.setFont(font)
        self.ReconNgTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.ReconNgTitle.setObjectName("ReconNgTitle")
        self.gridLayout_35.addWidget(self.ReconNgTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.line_131 = QtWidgets.QFrame(self.ReconNgScrollWidgetContents)
        self.line_131.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_131.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_131.setObjectName("line_131")
        self.gridLayout_35.addWidget(self.line_131, 9, 0, 1, 1)
        self.ReconNgButton = QtWidgets.QPushButton(self.ReconNgScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ReconNgButton.setFont(font)
        self.ReconNgButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(79, 79, 79);")
        self.ReconNgButton.setObjectName("ReconNgButton")
        self.gridLayout_35.addWidget(self.ReconNgButton, 14, 0, 1, 1)
        self.ReconNgH4 = QtWidgets.QLabel(self.ReconNgScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.ReconNgH4.setFont(font)
        self.ReconNgH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.ReconNgH4.setObjectName("ReconNgH4")
        self.gridLayout_35.addWidget(self.ReconNgH4, 12, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.line_130 = QtWidgets.QFrame(self.ReconNgScrollWidgetContents)
        self.line_130.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_130.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_130.setObjectName("line_130")
        self.gridLayout_35.addWidget(self.line_130, 7, 0, 1, 1)
        self.ReconNgH1 = QtWidgets.QLabel(self.ReconNgScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.ReconNgH1.setFont(font)
        self.ReconNgH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.ReconNgH1.setObjectName("ReconNgH1")
        self.gridLayout_35.addWidget(self.ReconNgH1, 2, 0, 1, 1)
        self.ReconNgB1 = QtWidgets.QLabel(self.ReconNgScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ReconNgB1.setFont(font)
        self.ReconNgB1.setTextFormat(QtCore.Qt.AutoText)
        self.ReconNgB1.setScaledContents(False)
        self.ReconNgB1.setWordWrap(False)
        self.ReconNgB1.setObjectName("ReconNgB1")
        self.gridLayout_35.addWidget(self.ReconNgB1, 4, 0, 1, 1)
        self.line_129 = QtWidgets.QFrame(self.ReconNgScrollWidgetContents)
        self.line_129.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_129.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_129.setObjectName("line_129")
        self.gridLayout_35.addWidget(self.line_129, 1, 0, 1, 1)
        self.line_134 = QtWidgets.QFrame(self.ReconNgScrollWidgetContents)
        self.line_134.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_134.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_134.setObjectName("line_134")
        self.gridLayout_35.addWidget(self.line_134, 10, 0, 1, 1)
        self.line_128 = QtWidgets.QFrame(self.ReconNgScrollWidgetContents)
        self.line_128.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_128.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_128.setObjectName("line_128")
        self.gridLayout_35.addWidget(self.line_128, 5, 0, 1, 1)
        self.ReconNgScrollArea.setWidget(self.ReconNgScrollWidgetContents)
        self.gridLayout_34.addWidget(self.ReconNgScrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.ReconNgTab, "")
        self.SETTab = QtWidgets.QWidget()
        self.SETTab.setObjectName("SETTab")
        self.gridLayout_36 = QtWidgets.QGridLayout(self.SETTab)
        self.gridLayout_36.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_36.setSpacing(6)
        self.gridLayout_36.setObjectName("gridLayout_36")
        self.SETScrollArea = QtWidgets.QScrollArea(self.SETTab)
        self.SETScrollArea.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.SETScrollArea.setWidgetResizable(True)
        self.SETScrollArea.setObjectName("SETScrollArea")
        self.SETScrollWidgetContents = QtWidgets.QWidget()
        self.SETScrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 3128, 1709))
        self.SETScrollWidgetContents.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.SETScrollWidgetContents.setObjectName("SETScrollWidgetContents")
        self.gridLayout_37 = QtWidgets.QGridLayout(self.SETScrollWidgetContents)
        self.gridLayout_37.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_37.setSpacing(6)
        self.gridLayout_37.setObjectName("gridLayout_37")
        self.SETB2 = QtWidgets.QLabel(self.SETScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SETB2.setFont(font)
        self.SETB2.setObjectName("SETB2")
        self.gridLayout_37.addWidget(self.SETB2, 8, 0, 1, 1)
        self.line_135 = QtWidgets.QFrame(self.SETScrollWidgetContents)
        self.line_135.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_135.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_135.setObjectName("line_135")
        self.gridLayout_37.addWidget(self.line_135, 11, 0, 1, 1)
        self.line_136 = QtWidgets.QFrame(self.SETScrollWidgetContents)
        self.line_136.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_136.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_136.setObjectName("line_136")
        self.gridLayout_37.addWidget(self.line_136, 3, 0, 1, 1)
        spacerItem44 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_37.addItem(spacerItem44, 15, 0, 1, 1)
        self.SETH2 = QtWidgets.QLabel(self.SETScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.SETH2.setFont(font)
        self.SETH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.SETH2.setObjectName("SETH2")
        self.gridLayout_37.addWidget(self.SETH2, 6, 0, 1, 1)
        self.SETH4 = QtWidgets.QLabel(self.SETScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.SETH4.setFont(font)
        self.SETH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.SETH4.setObjectName("SETH4")
        self.gridLayout_37.addWidget(self.SETH4, 12, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.SETTitle = QtWidgets.QLabel(self.SETScrollWidgetContents)
        self.SETTitle.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.SETTitle.setFont(font)
        self.SETTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.SETTitle.setObjectName("SETTitle")
        self.gridLayout_37.addWidget(self.SETTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.line_141 = QtWidgets.QFrame(self.SETScrollWidgetContents)
        self.line_141.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_141.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_141.setObjectName("line_141")
        self.gridLayout_37.addWidget(self.line_141, 10, 0, 1, 1)
        self.line_138 = QtWidgets.QFrame(self.SETScrollWidgetContents)
        self.line_138.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_138.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_138.setObjectName("line_138")
        self.gridLayout_37.addWidget(self.line_138, 9, 0, 1, 1)
        self.line_142 = QtWidgets.QFrame(self.SETScrollWidgetContents)
        self.line_142.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_142.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_142.setObjectName("line_142")
        self.gridLayout_37.addWidget(self.line_142, 5, 0, 1, 1)
        self.SETH1 = QtWidgets.QLabel(self.SETScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.SETH1.setFont(font)
        self.SETH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.SETH1.setObjectName("SETH1")
        self.gridLayout_37.addWidget(self.SETH1, 2, 0, 1, 1)
        self.SETButton = QtWidgets.QPushButton(self.SETScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SETButton.setFont(font)
        self.SETButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(79, 79, 79);")
        self.SETButton.setObjectName("SETButton")
        self.gridLayout_37.addWidget(self.SETButton, 14, 0, 1, 1)
        self.line_137 = QtWidgets.QFrame(self.SETScrollWidgetContents)
        self.line_137.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_137.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_137.setObjectName("line_137")
        self.gridLayout_37.addWidget(self.line_137, 13, 0, 1, 1)
        self.line_139 = QtWidgets.QFrame(self.SETScrollWidgetContents)
        self.line_139.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_139.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_139.setObjectName("line_139")
        self.gridLayout_37.addWidget(self.line_139, 7, 0, 1, 1)
        self.SETB1 = QtWidgets.QLabel(self.SETScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SETB1.setFont(font)
        self.SETB1.setTextFormat(QtCore.Qt.AutoText)
        self.SETB1.setScaledContents(False)
        self.SETB1.setWordWrap(False)
        self.SETB1.setObjectName("SETB1")
        self.gridLayout_37.addWidget(self.SETB1, 4, 0, 1, 1)
        self.line_140 = QtWidgets.QFrame(self.SETScrollWidgetContents)
        self.line_140.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_140.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_140.setObjectName("line_140")
        self.gridLayout_37.addWidget(self.line_140, 1, 0, 1, 1)
        self.SETScrollArea.setWidget(self.SETScrollWidgetContents)
        self.gridLayout_36.addWidget(self.SETScrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.SETTab, "")
        self.smtpUserEnumTab = QtWidgets.QWidget()
        self.smtpUserEnumTab.setObjectName("smtpUserEnumTab")
        self.gridLayout_38 = QtWidgets.QGridLayout(self.smtpUserEnumTab)
        self.gridLayout_38.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_38.setSpacing(6)
        self.gridLayout_38.setObjectName("gridLayout_38")
        self.smtpUserEnumScrollArea = QtWidgets.QScrollArea(self.smtpUserEnumTab)
        self.smtpUserEnumScrollArea.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.smtpUserEnumScrollArea.setWidgetResizable(True)
        self.smtpUserEnumScrollArea.setObjectName("smtpUserEnumScrollArea")
        self.smtpUserEnumScrollWidgetContents = QtWidgets.QWidget()
        self.smtpUserEnumScrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 3128, 2330))
        self.smtpUserEnumScrollWidgetContents.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.smtpUserEnumScrollWidgetContents.setObjectName("smtpUserEnumScrollWidgetContents")
        self.gridLayout_39 = QtWidgets.QGridLayout(self.smtpUserEnumScrollWidgetContents)
        self.gridLayout_39.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_39.setSpacing(6)
        self.gridLayout_39.setObjectName("gridLayout_39")
        self.line_143 = QtWidgets.QFrame(self.smtpUserEnumScrollWidgetContents)
        self.line_143.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_143.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_143.setObjectName("line_143")
        self.gridLayout_39.addWidget(self.line_143, 13, 0, 1, 1)
        spacerItem45 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_39.addItem(spacerItem45, 17, 0, 1, 1)
        self.smtpUserEnumB2 = QtWidgets.QLabel(self.smtpUserEnumScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.smtpUserEnumB2.setFont(font)
        self.smtpUserEnumB2.setObjectName("smtpUserEnumB2")
        self.gridLayout_39.addWidget(self.smtpUserEnumB2, 8, 0, 1, 1)
        self.smtpUserEnumH2 = QtWidgets.QLabel(self.smtpUserEnumScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.smtpUserEnumH2.setFont(font)
        self.smtpUserEnumH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.smtpUserEnumH2.setObjectName("smtpUserEnumH2")
        self.gridLayout_39.addWidget(self.smtpUserEnumH2, 6, 0, 1, 1)
        self.line_144 = QtWidgets.QFrame(self.smtpUserEnumScrollWidgetContents)
        self.line_144.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_144.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_144.setObjectName("line_144")
        self.gridLayout_39.addWidget(self.line_144, 3, 0, 1, 1)
        self.line_145 = QtWidgets.QFrame(self.smtpUserEnumScrollWidgetContents)
        self.line_145.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_145.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_145.setObjectName("line_145")
        self.gridLayout_39.addWidget(self.line_145, 15, 0, 1, 1)
        self.smtpUserEnumTitle = QtWidgets.QLabel(self.smtpUserEnumScrollWidgetContents)
        self.smtpUserEnumTitle.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.smtpUserEnumTitle.setFont(font)
        self.smtpUserEnumTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.smtpUserEnumTitle.setObjectName("smtpUserEnumTitle")
        self.gridLayout_39.addWidget(self.smtpUserEnumTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.line_146 = QtWidgets.QFrame(self.smtpUserEnumScrollWidgetContents)
        self.line_146.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_146.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_146.setObjectName("line_146")
        self.gridLayout_39.addWidget(self.line_146, 9, 0, 1, 1)
        self.smtpUserEnumButton = QtWidgets.QPushButton(self.smtpUserEnumScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.smtpUserEnumButton.setFont(font)
        self.smtpUserEnumButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(79, 79, 79);")
        self.smtpUserEnumButton.setObjectName("smtpUserEnumButton")
        self.gridLayout_39.addWidget(self.smtpUserEnumButton, 16, 0, 1, 1)
        self.smtpUserEnumH4 = QtWidgets.QLabel(self.smtpUserEnumScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.smtpUserEnumH4.setFont(font)
        self.smtpUserEnumH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.smtpUserEnumH4.setObjectName("smtpUserEnumH4")
        self.gridLayout_39.addWidget(self.smtpUserEnumH4, 14, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.smtpUserEnumB3 = QtWidgets.QLabel(self.smtpUserEnumScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.smtpUserEnumB3.setFont(font)
        self.smtpUserEnumB3.setObjectName("smtpUserEnumB3")
        self.gridLayout_39.addWidget(self.smtpUserEnumB3, 12, 0, 1, 1)
        self.line_147 = QtWidgets.QFrame(self.smtpUserEnumScrollWidgetContents)
        self.line_147.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_147.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_147.setObjectName("line_147")
        self.gridLayout_39.addWidget(self.line_147, 7, 0, 1, 1)
        self.smtpUserEnumH1 = QtWidgets.QLabel(self.smtpUserEnumScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.smtpUserEnumH1.setFont(font)
        self.smtpUserEnumH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.smtpUserEnumH1.setObjectName("smtpUserEnumH1")
        self.gridLayout_39.addWidget(self.smtpUserEnumH1, 2, 0, 1, 1)
        self.smtpUserEnumB1 = QtWidgets.QLabel(self.smtpUserEnumScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.smtpUserEnumB1.setFont(font)
        self.smtpUserEnumB1.setTextFormat(QtCore.Qt.AutoText)
        self.smtpUserEnumB1.setScaledContents(False)
        self.smtpUserEnumB1.setWordWrap(False)
        self.smtpUserEnumB1.setObjectName("smtpUserEnumB1")
        self.gridLayout_39.addWidget(self.smtpUserEnumB1, 4, 0, 1, 1)
        self.line_148 = QtWidgets.QFrame(self.smtpUserEnumScrollWidgetContents)
        self.line_148.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_148.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_148.setObjectName("line_148")
        self.gridLayout_39.addWidget(self.line_148, 1, 0, 1, 1)
        self.line_149 = QtWidgets.QFrame(self.smtpUserEnumScrollWidgetContents)
        self.line_149.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_149.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_149.setObjectName("line_149")
        self.gridLayout_39.addWidget(self.line_149, 11, 0, 1, 1)
        self.line_150 = QtWidgets.QFrame(self.smtpUserEnumScrollWidgetContents)
        self.line_150.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_150.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_150.setObjectName("line_150")
        self.gridLayout_39.addWidget(self.line_150, 5, 0, 1, 1)
        self.smtpUserEnumH3 = QtWidgets.QLabel(self.smtpUserEnumScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.smtpUserEnumH3.setFont(font)
        self.smtpUserEnumH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.smtpUserEnumH3.setObjectName("smtpUserEnumH3")
        self.gridLayout_39.addWidget(self.smtpUserEnumH3, 10, 0, 1, 1)
        self.smtpUserEnumScrollArea.setWidget(self.smtpUserEnumScrollWidgetContents)
        self.gridLayout_38.addWidget(self.smtpUserEnumScrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.smtpUserEnumTab, "")
        self.snmpChecktab = QtWidgets.QWidget()
        self.snmpChecktab.setObjectName("snmpChecktab")
        self.gridLayout_40 = QtWidgets.QGridLayout(self.snmpChecktab)
        self.gridLayout_40.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_40.setSpacing(6)
        self.gridLayout_40.setObjectName("gridLayout_40")
        self.snmpCheckScrollArea = QtWidgets.QScrollArea(self.snmpChecktab)
        self.snmpCheckScrollArea.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.snmpCheckScrollArea.setWidgetResizable(True)
        self.snmpCheckScrollArea.setObjectName("snmpCheckScrollArea")
        self.snmpCheckScrollWidgetContents = QtWidgets.QWidget()
        self.snmpCheckScrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 3128, 2780))
        self.snmpCheckScrollWidgetContents.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.snmpCheckScrollWidgetContents.setObjectName("snmpCheckScrollWidgetContents")
        self.gridLayout_41 = QtWidgets.QGridLayout(self.snmpCheckScrollWidgetContents)
        self.gridLayout_41.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_41.setSpacing(6)
        self.gridLayout_41.setObjectName("gridLayout_41")
        self.line_151 = QtWidgets.QFrame(self.snmpCheckScrollWidgetContents)
        self.line_151.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_151.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_151.setObjectName("line_151")
        self.gridLayout_41.addWidget(self.line_151, 13, 0, 1, 1)
        spacerItem46 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_41.addItem(spacerItem46, 17, 0, 1, 1)
        self.snmpCheckH2 = QtWidgets.QLabel(self.snmpCheckScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.snmpCheckH2.setFont(font)
        self.snmpCheckH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.snmpCheckH2.setObjectName("snmpCheckH2")
        self.gridLayout_41.addWidget(self.snmpCheckH2, 6, 0, 1, 1)
        self.line_152 = QtWidgets.QFrame(self.snmpCheckScrollWidgetContents)
        self.line_152.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_152.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_152.setObjectName("line_152")
        self.gridLayout_41.addWidget(self.line_152, 3, 0, 1, 1)
        self.line_153 = QtWidgets.QFrame(self.snmpCheckScrollWidgetContents)
        self.line_153.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_153.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_153.setObjectName("line_153")
        self.gridLayout_41.addWidget(self.line_153, 15, 0, 1, 1)
        self.snmpCheckTitle = QtWidgets.QLabel(self.snmpCheckScrollWidgetContents)
        self.snmpCheckTitle.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.snmpCheckTitle.setFont(font)
        self.snmpCheckTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.snmpCheckTitle.setObjectName("snmpCheckTitle")
        self.gridLayout_41.addWidget(self.snmpCheckTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.line_154 = QtWidgets.QFrame(self.snmpCheckScrollWidgetContents)
        self.line_154.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_154.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_154.setObjectName("line_154")
        self.gridLayout_41.addWidget(self.line_154, 9, 0, 1, 1)
        self.snmpCheckButton = QtWidgets.QPushButton(self.snmpCheckScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.snmpCheckButton.setFont(font)
        self.snmpCheckButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(79, 79, 79);")
        self.snmpCheckButton.setObjectName("snmpCheckButton")
        self.gridLayout_41.addWidget(self.snmpCheckButton, 16, 0, 1, 1)
        self.snmpCheckH4 = QtWidgets.QLabel(self.snmpCheckScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.snmpCheckH4.setFont(font)
        self.snmpCheckH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.snmpCheckH4.setObjectName("snmpCheckH4")
        self.gridLayout_41.addWidget(self.snmpCheckH4, 14, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.snmpCheckB3 = QtWidgets.QLabel(self.snmpCheckScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.snmpCheckB3.setFont(font)
        self.snmpCheckB3.setObjectName("snmpCheckB3")
        self.gridLayout_41.addWidget(self.snmpCheckB3, 12, 0, 1, 1)
        self.line_155 = QtWidgets.QFrame(self.snmpCheckScrollWidgetContents)
        self.line_155.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_155.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_155.setObjectName("line_155")
        self.gridLayout_41.addWidget(self.line_155, 7, 0, 1, 1)
        self.snmpCheckH1 = QtWidgets.QLabel(self.snmpCheckScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.snmpCheckH1.setFont(font)
        self.snmpCheckH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.snmpCheckH1.setObjectName("snmpCheckH1")
        self.gridLayout_41.addWidget(self.snmpCheckH1, 2, 0, 1, 1)
        self.snmpCheckB1 = QtWidgets.QLabel(self.snmpCheckScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.snmpCheckB1.setFont(font)
        self.snmpCheckB1.setTextFormat(QtCore.Qt.AutoText)
        self.snmpCheckB1.setScaledContents(False)
        self.snmpCheckB1.setWordWrap(False)
        self.snmpCheckB1.setObjectName("snmpCheckB1")
        self.gridLayout_41.addWidget(self.snmpCheckB1, 4, 0, 1, 1)
        self.line_156 = QtWidgets.QFrame(self.snmpCheckScrollWidgetContents)
        self.line_156.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_156.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_156.setObjectName("line_156")
        self.gridLayout_41.addWidget(self.line_156, 1, 0, 1, 1)
        self.line_157 = QtWidgets.QFrame(self.snmpCheckScrollWidgetContents)
        self.line_157.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_157.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_157.setObjectName("line_157")
        self.gridLayout_41.addWidget(self.line_157, 11, 0, 1, 1)
        self.line_158 = QtWidgets.QFrame(self.snmpCheckScrollWidgetContents)
        self.line_158.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_158.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_158.setObjectName("line_158")
        self.gridLayout_41.addWidget(self.line_158, 5, 0, 1, 1)
        self.snmpCheckH3 = QtWidgets.QLabel(self.snmpCheckScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.snmpCheckH3.setFont(font)
        self.snmpCheckH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.snmpCheckH3.setObjectName("snmpCheckH3")
        self.gridLayout_41.addWidget(self.snmpCheckH3, 10, 0, 1, 1)
        self.snmpCheckB2 = QtWidgets.QLabel(self.snmpCheckScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.snmpCheckB2.setFont(font)
        self.snmpCheckB2.setObjectName("snmpCheckB2")
        self.gridLayout_41.addWidget(self.snmpCheckB2, 8, 0, 1, 1)
        self.snmpCheckScrollArea.setWidget(self.snmpCheckScrollWidgetContents)
        self.gridLayout_40.addWidget(self.snmpCheckScrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.snmpChecktab, "")
        self.spartaTab = QtWidgets.QWidget()
        self.spartaTab.setObjectName("spartaTab")
        self.gridLayout_42 = QtWidgets.QGridLayout(self.spartaTab)
        self.gridLayout_42.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_42.setSpacing(6)
        self.gridLayout_42.setObjectName("gridLayout_42")
        self.spartaScrollArea = QtWidgets.QScrollArea(self.spartaTab)
        self.spartaScrollArea.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.spartaScrollArea.setWidgetResizable(True)
        self.spartaScrollArea.setObjectName("spartaScrollArea")
        self.spartaScrollWidgetContents = QtWidgets.QWidget()
        self.spartaScrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 3128, 1022))
        self.spartaScrollWidgetContents.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.spartaScrollWidgetContents.setObjectName("spartaScrollWidgetContents")
        self.gridLayout_43 = QtWidgets.QGridLayout(self.spartaScrollWidgetContents)
        self.gridLayout_43.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_43.setSpacing(6)
        self.gridLayout_43.setObjectName("gridLayout_43")
        self.line_159 = QtWidgets.QFrame(self.spartaScrollWidgetContents)
        self.line_159.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_159.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_159.setObjectName("line_159")
        self.gridLayout_43.addWidget(self.line_159, 11, 0, 1, 1)
        self.line_161 = QtWidgets.QFrame(self.spartaScrollWidgetContents)
        self.line_161.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_161.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_161.setObjectName("line_161")
        self.gridLayout_43.addWidget(self.line_161, 13, 0, 1, 1)
        self.spartaH2 = QtWidgets.QLabel(self.spartaScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.spartaH2.setFont(font)
        self.spartaH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.spartaH2.setObjectName("spartaH2")
        self.gridLayout_43.addWidget(self.spartaH2, 6, 0, 1, 1)
        self.spartaH4 = QtWidgets.QLabel(self.spartaScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.spartaH4.setFont(font)
        self.spartaH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.spartaH4.setObjectName("spartaH4")
        self.gridLayout_43.addWidget(self.spartaH4, 12, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.line_160 = QtWidgets.QFrame(self.spartaScrollWidgetContents)
        self.line_160.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_160.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_160.setObjectName("line_160")
        self.gridLayout_43.addWidget(self.line_160, 3, 0, 1, 1)
        self.spartaTitle = QtWidgets.QLabel(self.spartaScrollWidgetContents)
        self.spartaTitle.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.spartaTitle.setFont(font)
        self.spartaTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.spartaTitle.setObjectName("spartaTitle")
        self.gridLayout_43.addWidget(self.spartaTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.spartaButton = QtWidgets.QPushButton(self.spartaScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.spartaButton.setFont(font)
        self.spartaButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(79, 79, 79);")
        self.spartaButton.setObjectName("spartaButton")
        self.gridLayout_43.addWidget(self.spartaButton, 14, 0, 1, 1)
        spacerItem47 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_43.addItem(spacerItem47, 15, 0, 1, 1)
        self.spartaB2 = QtWidgets.QLabel(self.spartaScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.spartaB2.setFont(font)
        self.spartaB2.setObjectName("spartaB2")
        self.gridLayout_43.addWidget(self.spartaB2, 8, 0, 1, 1)
        self.line_163 = QtWidgets.QFrame(self.spartaScrollWidgetContents)
        self.line_163.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_163.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_163.setObjectName("line_163")
        self.gridLayout_43.addWidget(self.line_163, 7, 0, 1, 1)
        self.line_162 = QtWidgets.QFrame(self.spartaScrollWidgetContents)
        self.line_162.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_162.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_162.setObjectName("line_162")
        self.gridLayout_43.addWidget(self.line_162, 9, 0, 1, 1)
        self.line_166 = QtWidgets.QFrame(self.spartaScrollWidgetContents)
        self.line_166.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_166.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_166.setObjectName("line_166")
        self.gridLayout_43.addWidget(self.line_166, 5, 0, 1, 1)
        self.spartaB1 = QtWidgets.QLabel(self.spartaScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.spartaB1.setFont(font)
        self.spartaB1.setTextFormat(QtCore.Qt.AutoText)
        self.spartaB1.setScaledContents(False)
        self.spartaB1.setWordWrap(False)
        self.spartaB1.setObjectName("spartaB1")
        self.gridLayout_43.addWidget(self.spartaB1, 4, 0, 1, 1)
        self.spartaH1 = QtWidgets.QLabel(self.spartaScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.spartaH1.setFont(font)
        self.spartaH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.spartaH1.setObjectName("spartaH1")
        self.gridLayout_43.addWidget(self.spartaH1, 2, 0, 1, 1)
        self.line_165 = QtWidgets.QFrame(self.spartaScrollWidgetContents)
        self.line_165.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_165.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_165.setObjectName("line_165")
        self.gridLayout_43.addWidget(self.line_165, 10, 0, 1, 1)
        self.line_164 = QtWidgets.QFrame(self.spartaScrollWidgetContents)
        self.line_164.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_164.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_164.setObjectName("line_164")
        self.gridLayout_43.addWidget(self.line_164, 1, 0, 1, 1)
        self.spartaScrollArea.setWidget(self.spartaScrollWidgetContents)
        self.gridLayout_42.addWidget(self.spartaScrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.spartaTab, "")
        self.sscaudittab = QtWidgets.QWidget()
        self.sscaudittab.setObjectName("sscaudittab")
        self.gridLayout_44 = QtWidgets.QGridLayout(self.sscaudittab)
        self.gridLayout_44.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_44.setSpacing(6)
        self.gridLayout_44.setObjectName("gridLayout_44")
        self.sslcauditScrollArea = QtWidgets.QScrollArea(self.sscaudittab)
        self.sslcauditScrollArea.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.sslcauditScrollArea.setWidgetResizable(True)
        self.sslcauditScrollArea.setObjectName("sslcauditScrollArea")
        self.sslcauditScrollWidgetContents = QtWidgets.QWidget()
        self.sslcauditScrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 3128, 1921))
        self.sslcauditScrollWidgetContents.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.sslcauditScrollWidgetContents.setObjectName("sslcauditScrollWidgetContents")
        self.gridLayout_45 = QtWidgets.QGridLayout(self.sslcauditScrollWidgetContents)
        self.gridLayout_45.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_45.setSpacing(6)
        self.gridLayout_45.setObjectName("gridLayout_45")
        self.line_167 = QtWidgets.QFrame(self.sslcauditScrollWidgetContents)
        self.line_167.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_167.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_167.setObjectName("line_167")
        self.gridLayout_45.addWidget(self.line_167, 13, 0, 1, 1)
        self.line_168 = QtWidgets.QFrame(self.sslcauditScrollWidgetContents)
        self.line_168.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_168.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_168.setObjectName("line_168")
        self.gridLayout_45.addWidget(self.line_168, 15, 0, 1, 1)
        self.sslcauditH2 = QtWidgets.QLabel(self.sslcauditScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.sslcauditH2.setFont(font)
        self.sslcauditH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.sslcauditH2.setObjectName("sslcauditH2")
        self.gridLayout_45.addWidget(self.sslcauditH2, 6, 0, 1, 1)
        self.sslcauditH4 = QtWidgets.QLabel(self.sslcauditScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.sslcauditH4.setFont(font)
        self.sslcauditH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.sslcauditH4.setObjectName("sslcauditH4")
        self.gridLayout_45.addWidget(self.sslcauditH4, 14, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.line_169 = QtWidgets.QFrame(self.sslcauditScrollWidgetContents)
        self.line_169.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_169.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_169.setObjectName("line_169")
        self.gridLayout_45.addWidget(self.line_169, 3, 0, 1, 1)
        self.sslcauditTitle = QtWidgets.QLabel(self.sslcauditScrollWidgetContents)
        self.sslcauditTitle.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.sslcauditTitle.setFont(font)
        self.sslcauditTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.sslcauditTitle.setObjectName("sslcauditTitle")
        self.gridLayout_45.addWidget(self.sslcauditTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.sslcauditButton = QtWidgets.QPushButton(self.sslcauditScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sslcauditButton.setFont(font)
        self.sslcauditButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(79, 79, 79);")
        self.sslcauditButton.setObjectName("sslcauditButton")
        self.gridLayout_45.addWidget(self.sslcauditButton, 16, 0, 1, 1)
        spacerItem48 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_45.addItem(spacerItem48, 17, 0, 1, 1)
        self.sslcauditB2 = QtWidgets.QLabel(self.sslcauditScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sslcauditB2.setFont(font)
        self.sslcauditB2.setObjectName("sslcauditB2")
        self.gridLayout_45.addWidget(self.sslcauditB2, 8, 0, 1, 1)
        self.line_170 = QtWidgets.QFrame(self.sslcauditScrollWidgetContents)
        self.line_170.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_170.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_170.setObjectName("line_170")
        self.gridLayout_45.addWidget(self.line_170, 7, 0, 1, 1)
        self.line_171 = QtWidgets.QFrame(self.sslcauditScrollWidgetContents)
        self.line_171.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_171.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_171.setObjectName("line_171")
        self.gridLayout_45.addWidget(self.line_171, 9, 0, 1, 1)
        self.line_172 = QtWidgets.QFrame(self.sslcauditScrollWidgetContents)
        self.line_172.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_172.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_172.setObjectName("line_172")
        self.gridLayout_45.addWidget(self.line_172, 5, 0, 1, 1)
        self.sslcauditB1 = QtWidgets.QLabel(self.sslcauditScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sslcauditB1.setFont(font)
        self.sslcauditB1.setTextFormat(QtCore.Qt.AutoText)
        self.sslcauditB1.setScaledContents(False)
        self.sslcauditB1.setWordWrap(False)
        self.sslcauditB1.setObjectName("sslcauditB1")
        self.gridLayout_45.addWidget(self.sslcauditB1, 4, 0, 1, 1)
        self.sslcauditH1 = QtWidgets.QLabel(self.sslcauditScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.sslcauditH1.setFont(font)
        self.sslcauditH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.sslcauditH1.setObjectName("sslcauditH1")
        self.gridLayout_45.addWidget(self.sslcauditH1, 2, 0, 1, 1)
        self.sslcauditH3 = QtWidgets.QLabel(self.sslcauditScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.sslcauditH3.setFont(font)
        self.sslcauditH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.sslcauditH3.setObjectName("sslcauditH3")
        self.gridLayout_45.addWidget(self.sslcauditH3, 10, 0, 1, 1)
        self.line_173 = QtWidgets.QFrame(self.sslcauditScrollWidgetContents)
        self.line_173.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_173.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_173.setObjectName("line_173")
        self.gridLayout_45.addWidget(self.line_173, 11, 0, 1, 1)
        self.line_174 = QtWidgets.QFrame(self.sslcauditScrollWidgetContents)
        self.line_174.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_174.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_174.setObjectName("line_174")
        self.gridLayout_45.addWidget(self.line_174, 1, 0, 1, 1)
        self.sslcauditB3 = QtWidgets.QLabel(self.sslcauditScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sslcauditB3.setFont(font)
        self.sslcauditB3.setObjectName("sslcauditB3")
        self.gridLayout_45.addWidget(self.sslcauditB3, 12, 0, 1, 1)
        self.sslcauditScrollArea.setWidget(self.sslcauditScrollWidgetContents)
        self.gridLayout_44.addWidget(self.sslcauditScrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.sscaudittab, "")
        self.SSLsplitab = QtWidgets.QWidget()
        self.SSLsplitab.setObjectName("SSLsplitab")
        self.gridLayout_46 = QtWidgets.QGridLayout(self.SSLsplitab)
        self.gridLayout_46.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_46.setSpacing(6)
        self.gridLayout_46.setObjectName("gridLayout_46")
        self.SSLsplitScrollArea = QtWidgets.QScrollArea(self.SSLsplitab)
        self.SSLsplitScrollArea.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.SSLsplitScrollArea.setWidgetResizable(True)
        self.SSLsplitScrollArea.setObjectName("SSLsplitScrollArea")
        self.SSLsplitScrollWidgetContents = QtWidgets.QWidget()
        self.SSLsplitScrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 3128, 2435))
        self.SSLsplitScrollWidgetContents.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.SSLsplitScrollWidgetContents.setObjectName("SSLsplitScrollWidgetContents")
        self.gridLayout_47 = QtWidgets.QGridLayout(self.SSLsplitScrollWidgetContents)
        self.gridLayout_47.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_47.setSpacing(6)
        self.gridLayout_47.setObjectName("gridLayout_47")
        self.line_180 = QtWidgets.QFrame(self.SSLsplitScrollWidgetContents)
        self.line_180.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_180.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_180.setObjectName("line_180")
        self.gridLayout_47.addWidget(self.line_180, 5, 0, 1, 1)
        self.line_179 = QtWidgets.QFrame(self.SSLsplitScrollWidgetContents)
        self.line_179.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_179.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_179.setObjectName("line_179")
        self.gridLayout_47.addWidget(self.line_179, 9, 0, 1, 1)
        self.SSLsplitB3 = QtWidgets.QLabel(self.SSLsplitScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SSLsplitB3.setFont(font)
        self.SSLsplitB3.setObjectName("SSLsplitB3")
        self.gridLayout_47.addWidget(self.SSLsplitB3, 12, 0, 1, 1)
        self.line_182 = QtWidgets.QFrame(self.SSLsplitScrollWidgetContents)
        self.line_182.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_182.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_182.setObjectName("line_182")
        self.gridLayout_47.addWidget(self.line_182, 1, 0, 1, 1)
        self.line_181 = QtWidgets.QFrame(self.SSLsplitScrollWidgetContents)
        self.line_181.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_181.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_181.setObjectName("line_181")
        self.gridLayout_47.addWidget(self.line_181, 11, 0, 1, 1)
        self.line_175 = QtWidgets.QFrame(self.SSLsplitScrollWidgetContents)
        self.line_175.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_175.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_175.setObjectName("line_175")
        self.gridLayout_47.addWidget(self.line_175, 13, 0, 1, 1)
        self.SSLsplitH2 = QtWidgets.QLabel(self.SSLsplitScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.SSLsplitH2.setFont(font)
        self.SSLsplitH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.SSLsplitH2.setObjectName("SSLsplitH2")
        self.gridLayout_47.addWidget(self.SSLsplitH2, 6, 0, 1, 1)
        self.SSLsplitH1 = QtWidgets.QLabel(self.SSLsplitScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.SSLsplitH1.setFont(font)
        self.SSLsplitH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.SSLsplitH1.setObjectName("SSLsplitH1")
        self.gridLayout_47.addWidget(self.SSLsplitH1, 2, 0, 1, 1)
        self.SSLsplitH3 = QtWidgets.QLabel(self.SSLsplitScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.SSLsplitH3.setFont(font)
        self.SSLsplitH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.SSLsplitH3.setObjectName("SSLsplitH3")
        self.gridLayout_47.addWidget(self.SSLsplitH3, 10, 0, 1, 1)
        self.line_178 = QtWidgets.QFrame(self.SSLsplitScrollWidgetContents)
        self.line_178.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_178.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_178.setObjectName("line_178")
        self.gridLayout_47.addWidget(self.line_178, 7, 0, 1, 1)
        self.SSLsplitButton = QtWidgets.QPushButton(self.SSLsplitScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SSLsplitButton.setFont(font)
        self.SSLsplitButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(79, 79, 79);")
        self.SSLsplitButton.setObjectName("SSLsplitButton")
        self.gridLayout_47.addWidget(self.SSLsplitButton, 16, 0, 1, 1)
        self.SSLsplitB1 = QtWidgets.QLabel(self.SSLsplitScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SSLsplitB1.setFont(font)
        self.SSLsplitB1.setTextFormat(QtCore.Qt.AutoText)
        self.SSLsplitB1.setScaledContents(False)
        self.SSLsplitB1.setWordWrap(False)
        self.SSLsplitB1.setObjectName("SSLsplitB1")
        self.gridLayout_47.addWidget(self.SSLsplitB1, 4, 0, 1, 1)
        spacerItem49 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_47.addItem(spacerItem49, 17, 0, 1, 1)
        self.line_177 = QtWidgets.QFrame(self.SSLsplitScrollWidgetContents)
        self.line_177.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_177.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_177.setObjectName("line_177")
        self.gridLayout_47.addWidget(self.line_177, 3, 0, 1, 1)
        self.line_176 = QtWidgets.QFrame(self.SSLsplitScrollWidgetContents)
        self.line_176.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_176.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_176.setObjectName("line_176")
        self.gridLayout_47.addWidget(self.line_176, 15, 0, 1, 1)
        self.SSLsplitTitle = QtWidgets.QLabel(self.SSLsplitScrollWidgetContents)
        self.SSLsplitTitle.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.SSLsplitTitle.setFont(font)
        self.SSLsplitTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.SSLsplitTitle.setObjectName("SSLsplitTitle")
        self.gridLayout_47.addWidget(self.SSLsplitTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.SSLsplitH4 = QtWidgets.QLabel(self.SSLsplitScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.SSLsplitH4.setFont(font)
        self.SSLsplitH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.SSLsplitH4.setObjectName("SSLsplitH4")
        self.gridLayout_47.addWidget(self.SSLsplitH4, 14, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.SSLsplitB2 = QtWidgets.QLabel(self.SSLsplitScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SSLsplitB2.setFont(font)
        self.SSLsplitB2.setObjectName("SSLsplitB2")
        self.gridLayout_47.addWidget(self.SSLsplitB2, 8, 0, 1, 1)
        self.SSLsplitScrollArea.setWidget(self.SSLsplitScrollWidgetContents)
        self.gridLayout_46.addWidget(self.SSLsplitScrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.SSLsplitab, "")
        self.sslstripTab = QtWidgets.QWidget()
        self.sslstripTab.setObjectName("sslstripTab")
        self.gridLayout_48 = QtWidgets.QGridLayout(self.sslstripTab)
        self.gridLayout_48.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_48.setSpacing(6)
        self.gridLayout_48.setObjectName("gridLayout_48")
        self.sslstripScrollArea = QtWidgets.QScrollArea(self.sslstripTab)
        self.sslstripScrollArea.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.sslstripScrollArea.setWidgetResizable(True)
        self.sslstripScrollArea.setObjectName("sslstripScrollArea")
        self.sslstripScrollWidgetContents = QtWidgets.QWidget()
        self.sslstripScrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 3128, 1299))
        self.sslstripScrollWidgetContents.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.sslstripScrollWidgetContents.setObjectName("sslstripScrollWidgetContents")
        self.gridLayout_49 = QtWidgets.QGridLayout(self.sslstripScrollWidgetContents)
        self.gridLayout_49.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_49.setSpacing(6)
        self.gridLayout_49.setObjectName("gridLayout_49")
        self.line_183 = QtWidgets.QFrame(self.sslstripScrollWidgetContents)
        self.line_183.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_183.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_183.setObjectName("line_183")
        self.gridLayout_49.addWidget(self.line_183, 5, 0, 1, 1)
        self.line_184 = QtWidgets.QFrame(self.sslstripScrollWidgetContents)
        self.line_184.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_184.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_184.setObjectName("line_184")
        self.gridLayout_49.addWidget(self.line_184, 9, 0, 1, 1)
        self.sslstripB3 = QtWidgets.QLabel(self.sslstripScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sslstripB3.setFont(font)
        self.sslstripB3.setObjectName("sslstripB3")
        self.gridLayout_49.addWidget(self.sslstripB3, 12, 0, 1, 1)
        self.line_185 = QtWidgets.QFrame(self.sslstripScrollWidgetContents)
        self.line_185.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_185.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_185.setObjectName("line_185")
        self.gridLayout_49.addWidget(self.line_185, 1, 0, 1, 1)
        self.line_186 = QtWidgets.QFrame(self.sslstripScrollWidgetContents)
        self.line_186.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_186.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_186.setObjectName("line_186")
        self.gridLayout_49.addWidget(self.line_186, 11, 0, 1, 1)
        self.line_187 = QtWidgets.QFrame(self.sslstripScrollWidgetContents)
        self.line_187.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_187.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_187.setObjectName("line_187")
        self.gridLayout_49.addWidget(self.line_187, 13, 0, 1, 1)
        self.sslstripH2 = QtWidgets.QLabel(self.sslstripScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.sslstripH2.setFont(font)
        self.sslstripH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.sslstripH2.setObjectName("sslstripH2")
        self.gridLayout_49.addWidget(self.sslstripH2, 6, 0, 1, 1)
        self.sslstripH1 = QtWidgets.QLabel(self.sslstripScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.sslstripH1.setFont(font)
        self.sslstripH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.sslstripH1.setObjectName("sslstripH1")
        self.gridLayout_49.addWidget(self.sslstripH1, 2, 0, 1, 1)
        self.sslstripH3 = QtWidgets.QLabel(self.sslstripScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.sslstripH3.setFont(font)
        self.sslstripH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.sslstripH3.setObjectName("sslstripH3")
        self.gridLayout_49.addWidget(self.sslstripH3, 10, 0, 1, 1)
        self.line_188 = QtWidgets.QFrame(self.sslstripScrollWidgetContents)
        self.line_188.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_188.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_188.setObjectName("line_188")
        self.gridLayout_49.addWidget(self.line_188, 7, 0, 1, 1)
        self.sslstripButton = QtWidgets.QPushButton(self.sslstripScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sslstripButton.setFont(font)
        self.sslstripButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(79, 79, 79);")
        self.sslstripButton.setObjectName("sslstripButton")
        self.gridLayout_49.addWidget(self.sslstripButton, 16, 0, 1, 1)
        self.sslstripB1 = QtWidgets.QLabel(self.sslstripScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sslstripB1.setFont(font)
        self.sslstripB1.setTextFormat(QtCore.Qt.AutoText)
        self.sslstripB1.setScaledContents(False)
        self.sslstripB1.setWordWrap(False)
        self.sslstripB1.setObjectName("sslstripB1")
        self.gridLayout_49.addWidget(self.sslstripB1, 4, 0, 1, 1)
        spacerItem50 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_49.addItem(spacerItem50, 17, 0, 1, 1)
        self.line_189 = QtWidgets.QFrame(self.sslstripScrollWidgetContents)
        self.line_189.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_189.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_189.setObjectName("line_189")
        self.gridLayout_49.addWidget(self.line_189, 3, 0, 1, 1)
        self.line_190 = QtWidgets.QFrame(self.sslstripScrollWidgetContents)
        self.line_190.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_190.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_190.setObjectName("line_190")
        self.gridLayout_49.addWidget(self.line_190, 15, 0, 1, 1)
        self.sslstripTitle = QtWidgets.QLabel(self.sslstripScrollWidgetContents)
        self.sslstripTitle.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.sslstripTitle.setFont(font)
        self.sslstripTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.sslstripTitle.setObjectName("sslstripTitle")
        self.gridLayout_49.addWidget(self.sslstripTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.sslstripH4 = QtWidgets.QLabel(self.sslstripScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.sslstripH4.setFont(font)
        self.sslstripH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.sslstripH4.setObjectName("sslstripH4")
        self.gridLayout_49.addWidget(self.sslstripH4, 14, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.sslstripB2 = QtWidgets.QLabel(self.sslstripScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sslstripB2.setFont(font)
        self.sslstripB2.setObjectName("sslstripB2")
        self.gridLayout_49.addWidget(self.sslstripB2, 8, 0, 1, 1)
        self.sslstripScrollArea.setWidget(self.sslstripScrollWidgetContents)
        self.gridLayout_48.addWidget(self.sslstripScrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.sslstripTab, "")
        self.SSLyzeTab = QtWidgets.QWidget()
        self.SSLyzeTab.setObjectName("SSLyzeTab")
        self.gridLayout_50 = QtWidgets.QGridLayout(self.SSLyzeTab)
        self.gridLayout_50.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_50.setSpacing(6)
        self.gridLayout_50.setObjectName("gridLayout_50")
        self.SSLyzeScrollArea = QtWidgets.QScrollArea(self.SSLyzeTab)
        self.SSLyzeScrollArea.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.SSLyzeScrollArea.setWidgetResizable(True)
        self.SSLyzeScrollArea.setObjectName("SSLyzeScrollArea")
        self.SSLyzeScrollWidgetContents = QtWidgets.QWidget()
        self.SSLyzeScrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 3128, 4199))
        self.SSLyzeScrollWidgetContents.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.SSLyzeScrollWidgetContents.setObjectName("SSLyzeScrollWidgetContents")
        self.gridLayout_51 = QtWidgets.QGridLayout(self.SSLyzeScrollWidgetContents)
        self.gridLayout_51.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_51.setSpacing(6)
        self.gridLayout_51.setObjectName("gridLayout_51")
        self.line_191 = QtWidgets.QFrame(self.SSLyzeScrollWidgetContents)
        self.line_191.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_191.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_191.setObjectName("line_191")
        self.gridLayout_51.addWidget(self.line_191, 5, 0, 1, 1)
        self.line_192 = QtWidgets.QFrame(self.SSLyzeScrollWidgetContents)
        self.line_192.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_192.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_192.setObjectName("line_192")
        self.gridLayout_51.addWidget(self.line_192, 9, 0, 1, 1)
        self.SSLyzeB3 = QtWidgets.QLabel(self.SSLyzeScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SSLyzeB3.setFont(font)
        self.SSLyzeB3.setObjectName("SSLyzeB3")
        self.gridLayout_51.addWidget(self.SSLyzeB3, 12, 0, 1, 1)
        self.line_193 = QtWidgets.QFrame(self.SSLyzeScrollWidgetContents)
        self.line_193.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_193.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_193.setObjectName("line_193")
        self.gridLayout_51.addWidget(self.line_193, 1, 0, 1, 1)
        self.line_194 = QtWidgets.QFrame(self.SSLyzeScrollWidgetContents)
        self.line_194.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_194.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_194.setObjectName("line_194")
        self.gridLayout_51.addWidget(self.line_194, 11, 0, 1, 1)
        self.line_195 = QtWidgets.QFrame(self.SSLyzeScrollWidgetContents)
        self.line_195.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_195.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_195.setObjectName("line_195")
        self.gridLayout_51.addWidget(self.line_195, 13, 0, 1, 1)
        self.SSLyzeH2 = QtWidgets.QLabel(self.SSLyzeScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.SSLyzeH2.setFont(font)
        self.SSLyzeH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.SSLyzeH2.setObjectName("SSLyzeH2")
        self.gridLayout_51.addWidget(self.SSLyzeH2, 6, 0, 1, 1)
        self.SSLyzeH1 = QtWidgets.QLabel(self.SSLyzeScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.SSLyzeH1.setFont(font)
        self.SSLyzeH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.SSLyzeH1.setObjectName("SSLyzeH1")
        self.gridLayout_51.addWidget(self.SSLyzeH1, 2, 0, 1, 1)
        self.SSLyzeH3 = QtWidgets.QLabel(self.SSLyzeScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.SSLyzeH3.setFont(font)
        self.SSLyzeH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.SSLyzeH3.setObjectName("SSLyzeH3")
        self.gridLayout_51.addWidget(self.SSLyzeH3, 10, 0, 1, 1)
        self.line_196 = QtWidgets.QFrame(self.SSLyzeScrollWidgetContents)
        self.line_196.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_196.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_196.setObjectName("line_196")
        self.gridLayout_51.addWidget(self.line_196, 7, 0, 1, 1)
        self.SSLyzeButton = QtWidgets.QPushButton(self.SSLyzeScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SSLyzeButton.setFont(font)
        self.SSLyzeButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(79, 79, 79);")
        self.SSLyzeButton.setObjectName("SSLyzeButton")
        self.gridLayout_51.addWidget(self.SSLyzeButton, 16, 0, 1, 1)
        self.SSLyzeB1 = QtWidgets.QLabel(self.SSLyzeScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SSLyzeB1.setFont(font)
        self.SSLyzeB1.setTextFormat(QtCore.Qt.AutoText)
        self.SSLyzeB1.setScaledContents(False)
        self.SSLyzeB1.setWordWrap(False)
        self.SSLyzeB1.setObjectName("SSLyzeB1")
        self.gridLayout_51.addWidget(self.SSLyzeB1, 4, 0, 1, 1)
        spacerItem51 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_51.addItem(spacerItem51, 17, 0, 1, 1)
        self.line_197 = QtWidgets.QFrame(self.SSLyzeScrollWidgetContents)
        self.line_197.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_197.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_197.setObjectName("line_197")
        self.gridLayout_51.addWidget(self.line_197, 3, 0, 1, 1)
        self.line_198 = QtWidgets.QFrame(self.SSLyzeScrollWidgetContents)
        self.line_198.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_198.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_198.setObjectName("line_198")
        self.gridLayout_51.addWidget(self.line_198, 15, 0, 1, 1)
        self.SSlyzeTitle = QtWidgets.QLabel(self.SSLyzeScrollWidgetContents)
        self.SSlyzeTitle.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.SSlyzeTitle.setFont(font)
        self.SSlyzeTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.SSlyzeTitle.setObjectName("SSlyzeTitle")
        self.gridLayout_51.addWidget(self.SSlyzeTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.SSLyzeH4 = QtWidgets.QLabel(self.SSLyzeScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.SSLyzeH4.setFont(font)
        self.SSLyzeH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.SSLyzeH4.setObjectName("SSLyzeH4")
        self.gridLayout_51.addWidget(self.SSLyzeH4, 14, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.SSLyzeB2 = QtWidgets.QLabel(self.SSLyzeScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SSLyzeB2.setFont(font)
        self.SSLyzeB2.setObjectName("SSLyzeB2")
        self.gridLayout_51.addWidget(self.SSLyzeB2, 8, 0, 1, 1)
        self.SSLyzeScrollArea.setWidget(self.SSLyzeScrollWidgetContents)
        self.gridLayout_50.addWidget(self.SSLyzeScrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.SSLyzeTab, "")
        self.THCIPV6Tab = QtWidgets.QWidget()
        self.THCIPV6Tab.setObjectName("THCIPV6Tab")
        self.gridLayout_52 = QtWidgets.QGridLayout(self.THCIPV6Tab)
        self.gridLayout_52.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_52.setSpacing(6)
        self.gridLayout_52.setObjectName("gridLayout_52")
        self.THCIPV6ScrollArea = QtWidgets.QScrollArea(self.THCIPV6Tab)
        self.THCIPV6ScrollArea.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.THCIPV6ScrollArea.setWidgetResizable(True)
        self.THCIPV6ScrollArea.setObjectName("THCIPV6ScrollArea")
        self.THCIPV6ScrollWidgetContents = QtWidgets.QWidget()
        self.THCIPV6ScrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 3128, 11678))
        self.THCIPV6ScrollWidgetContents.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.THCIPV6ScrollWidgetContents.setObjectName("THCIPV6ScrollWidgetContents")
        self.gridLayout_53 = QtWidgets.QGridLayout(self.THCIPV6ScrollWidgetContents)
        self.gridLayout_53.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_53.setSpacing(6)
        self.gridLayout_53.setObjectName("gridLayout_53")
        self.line_199 = QtWidgets.QFrame(self.THCIPV6ScrollWidgetContents)
        self.line_199.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_199.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_199.setObjectName("line_199")
        self.gridLayout_53.addWidget(self.line_199, 5, 0, 1, 1)
        self.line_200 = QtWidgets.QFrame(self.THCIPV6ScrollWidgetContents)
        self.line_200.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_200.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_200.setObjectName("line_200")
        self.gridLayout_53.addWidget(self.line_200, 9, 0, 1, 1)
        self.line_201 = QtWidgets.QFrame(self.THCIPV6ScrollWidgetContents)
        self.line_201.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_201.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_201.setObjectName("line_201")
        self.gridLayout_53.addWidget(self.line_201, 1, 0, 1, 1)
        self.line_202 = QtWidgets.QFrame(self.THCIPV6ScrollWidgetContents)
        self.line_202.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_202.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_202.setObjectName("line_202")
        self.gridLayout_53.addWidget(self.line_202, 10, 0, 1, 1)
        self.line_203 = QtWidgets.QFrame(self.THCIPV6ScrollWidgetContents)
        self.line_203.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_203.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_203.setObjectName("line_203")
        self.gridLayout_53.addWidget(self.line_203, 11, 0, 1, 1)
        self.THCIPV6H2 = QtWidgets.QLabel(self.THCIPV6ScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.THCIPV6H2.setFont(font)
        self.THCIPV6H2.setStyleSheet("color: rgb(56, 196, 255);")
        self.THCIPV6H2.setObjectName("THCIPV6H2")
        self.gridLayout_53.addWidget(self.THCIPV6H2, 6, 0, 1, 1)
        self.THCIPV6H1 = QtWidgets.QLabel(self.THCIPV6ScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.THCIPV6H1.setFont(font)
        self.THCIPV6H1.setStyleSheet("color: rgb(56, 196, 255);")
        self.THCIPV6H1.setObjectName("THCIPV6H1")
        self.gridLayout_53.addWidget(self.THCIPV6H1, 2, 0, 1, 1)
        self.line_204 = QtWidgets.QFrame(self.THCIPV6ScrollWidgetContents)
        self.line_204.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_204.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_204.setObjectName("line_204")
        self.gridLayout_53.addWidget(self.line_204, 7, 0, 1, 1)
        self.THCIPV6Button = QtWidgets.QPushButton(self.THCIPV6ScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.THCIPV6Button.setFont(font)
        self.THCIPV6Button.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(79, 79, 79);")
        self.THCIPV6Button.setObjectName("THCIPV6Button")
        self.gridLayout_53.addWidget(self.THCIPV6Button, 14, 0, 1, 1)
        self.THCIPV6B1 = QtWidgets.QLabel(self.THCIPV6ScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.THCIPV6B1.setFont(font)
        self.THCIPV6B1.setTextFormat(QtCore.Qt.AutoText)
        self.THCIPV6B1.setScaledContents(False)
        self.THCIPV6B1.setWordWrap(False)
        self.THCIPV6B1.setObjectName("THCIPV6B1")
        self.gridLayout_53.addWidget(self.THCIPV6B1, 4, 0, 1, 1)
        spacerItem52 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_53.addItem(spacerItem52, 15, 0, 1, 1)
        self.line_205 = QtWidgets.QFrame(self.THCIPV6ScrollWidgetContents)
        self.line_205.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_205.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_205.setObjectName("line_205")
        self.gridLayout_53.addWidget(self.line_205, 3, 0, 1, 1)
        self.line_206 = QtWidgets.QFrame(self.THCIPV6ScrollWidgetContents)
        self.line_206.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_206.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_206.setObjectName("line_206")
        self.gridLayout_53.addWidget(self.line_206, 13, 0, 1, 1)
        self.THCIPV6Title = QtWidgets.QLabel(self.THCIPV6ScrollWidgetContents)
        self.THCIPV6Title.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.THCIPV6Title.setFont(font)
        self.THCIPV6Title.setStyleSheet("color: rgb(255, 255, 255);")
        self.THCIPV6Title.setObjectName("THCIPV6Title")
        self.gridLayout_53.addWidget(self.THCIPV6Title, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.THCIPV6H4 = QtWidgets.QLabel(self.THCIPV6ScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.THCIPV6H4.setFont(font)
        self.THCIPV6H4.setStyleSheet("color: rgb(56, 196, 255);")
        self.THCIPV6H4.setObjectName("THCIPV6H4")
        self.gridLayout_53.addWidget(self.THCIPV6H4, 12, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.THCIPV6B2 = QtWidgets.QLabel(self.THCIPV6ScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.THCIPV6B2.setFont(font)
        self.THCIPV6B2.setObjectName("THCIPV6B2")
        self.gridLayout_53.addWidget(self.THCIPV6B2, 8, 0, 1, 1)
        self.THCIPV6ScrollArea.setWidget(self.THCIPV6ScrollWidgetContents)
        self.gridLayout_52.addWidget(self.THCIPV6ScrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.THCIPV6Tab, "")
        self.theHarvesterTab = QtWidgets.QWidget()
        self.theHarvesterTab.setObjectName("theHarvesterTab")
        self.gridLayout_54 = QtWidgets.QGridLayout(self.theHarvesterTab)
        self.gridLayout_54.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_54.setSpacing(6)
        self.gridLayout_54.setObjectName("gridLayout_54")
        self.theHarvesterScrollArea = QtWidgets.QScrollArea(self.theHarvesterTab)
        self.theHarvesterScrollArea.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.theHarvesterScrollArea.setWidgetResizable(True)
        self.theHarvesterScrollArea.setObjectName("theHarvesterScrollArea")
        self.theHarvesterScrollWidgetContents = QtWidgets.QWidget()
        self.theHarvesterScrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 3128, 2438))
        self.theHarvesterScrollWidgetContents.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.theHarvesterScrollWidgetContents.setObjectName("theHarvesterScrollWidgetContents")
        self.gridLayout_55 = QtWidgets.QGridLayout(self.theHarvesterScrollWidgetContents)
        self.gridLayout_55.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_55.setSpacing(6)
        self.gridLayout_55.setObjectName("gridLayout_55")
        self.line_207 = QtWidgets.QFrame(self.theHarvesterScrollWidgetContents)
        self.line_207.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_207.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_207.setObjectName("line_207")
        self.gridLayout_55.addWidget(self.line_207, 5, 0, 1, 1)
        self.line_208 = QtWidgets.QFrame(self.theHarvesterScrollWidgetContents)
        self.line_208.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_208.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_208.setObjectName("line_208")
        self.gridLayout_55.addWidget(self.line_208, 9, 0, 1, 1)
        self.theHarvesterB3 = QtWidgets.QLabel(self.theHarvesterScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.theHarvesterB3.setFont(font)
        self.theHarvesterB3.setObjectName("theHarvesterB3")
        self.gridLayout_55.addWidget(self.theHarvesterB3, 12, 0, 1, 1)
        self.line_209 = QtWidgets.QFrame(self.theHarvesterScrollWidgetContents)
        self.line_209.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_209.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_209.setObjectName("line_209")
        self.gridLayout_55.addWidget(self.line_209, 1, 0, 1, 1)
        self.line_210 = QtWidgets.QFrame(self.theHarvesterScrollWidgetContents)
        self.line_210.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_210.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_210.setObjectName("line_210")
        self.gridLayout_55.addWidget(self.line_210, 11, 0, 1, 1)
        self.line_211 = QtWidgets.QFrame(self.theHarvesterScrollWidgetContents)
        self.line_211.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_211.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_211.setObjectName("line_211")
        self.gridLayout_55.addWidget(self.line_211, 13, 0, 1, 1)
        self.theHarvesterH2 = QtWidgets.QLabel(self.theHarvesterScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.theHarvesterH2.setFont(font)
        self.theHarvesterH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.theHarvesterH2.setObjectName("theHarvesterH2")
        self.gridLayout_55.addWidget(self.theHarvesterH2, 6, 0, 1, 1)
        self.theHarvesterH1 = QtWidgets.QLabel(self.theHarvesterScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.theHarvesterH1.setFont(font)
        self.theHarvesterH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.theHarvesterH1.setObjectName("theHarvesterH1")
        self.gridLayout_55.addWidget(self.theHarvesterH1, 2, 0, 1, 1)
        self.theHarvesterH3 = QtWidgets.QLabel(self.theHarvesterScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.theHarvesterH3.setFont(font)
        self.theHarvesterH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.theHarvesterH3.setObjectName("theHarvesterH3")
        self.gridLayout_55.addWidget(self.theHarvesterH3, 10, 0, 1, 1)
        self.line_212 = QtWidgets.QFrame(self.theHarvesterScrollWidgetContents)
        self.line_212.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_212.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_212.setObjectName("line_212")
        self.gridLayout_55.addWidget(self.line_212, 7, 0, 1, 1)
        self.theHarvesterButton = QtWidgets.QPushButton(self.theHarvesterScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.theHarvesterButton.setFont(font)
        self.theHarvesterButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(79, 79, 79);")
        self.theHarvesterButton.setObjectName("theHarvesterButton")
        self.gridLayout_55.addWidget(self.theHarvesterButton, 16, 0, 1, 1)
        self.theHarvesterB1 = QtWidgets.QLabel(self.theHarvesterScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.theHarvesterB1.setFont(font)
        self.theHarvesterB1.setTextFormat(QtCore.Qt.AutoText)
        self.theHarvesterB1.setScaledContents(False)
        self.theHarvesterB1.setWordWrap(False)
        self.theHarvesterB1.setObjectName("theHarvesterB1")
        self.gridLayout_55.addWidget(self.theHarvesterB1, 4, 0, 1, 1)
        spacerItem53 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_55.addItem(spacerItem53, 17, 0, 1, 1)
        self.line_213 = QtWidgets.QFrame(self.theHarvesterScrollWidgetContents)
        self.line_213.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_213.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_213.setObjectName("line_213")
        self.gridLayout_55.addWidget(self.line_213, 3, 0, 1, 1)
        self.line_214 = QtWidgets.QFrame(self.theHarvesterScrollWidgetContents)
        self.line_214.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_214.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_214.setObjectName("line_214")
        self.gridLayout_55.addWidget(self.line_214, 15, 0, 1, 1)
        self.theHarvesterTitle = QtWidgets.QLabel(self.theHarvesterScrollWidgetContents)
        self.theHarvesterTitle.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.theHarvesterTitle.setFont(font)
        self.theHarvesterTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.theHarvesterTitle.setObjectName("theHarvesterTitle")
        self.gridLayout_55.addWidget(self.theHarvesterTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.theHarvesterH4 = QtWidgets.QLabel(self.theHarvesterScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.theHarvesterH4.setFont(font)
        self.theHarvesterH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.theHarvesterH4.setObjectName("theHarvesterH4")
        self.gridLayout_55.addWidget(self.theHarvesterH4, 14, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.theHarvesterB2 = QtWidgets.QLabel(self.theHarvesterScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.theHarvesterB2.setFont(font)
        self.theHarvesterB2.setObjectName("theHarvesterB2")
        self.gridLayout_55.addWidget(self.theHarvesterB2, 8, 0, 1, 1)
        self.theHarvesterScrollArea.setWidget(self.theHarvesterScrollWidgetContents)
        self.gridLayout_54.addWidget(self.theHarvesterScrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.theHarvesterTab, "")
        self.TLSSLedTab = QtWidgets.QWidget()
        self.TLSSLedTab.setObjectName("TLSSLedTab")
        self.gridLayout_56 = QtWidgets.QGridLayout(self.TLSSLedTab)
        self.gridLayout_56.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_56.setSpacing(6)
        self.gridLayout_56.setObjectName("gridLayout_56")
        self.TLSSLedScrollArea = QtWidgets.QScrollArea(self.TLSSLedTab)
        self.TLSSLedScrollArea.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.TLSSLedScrollArea.setWidgetResizable(True)
        self.TLSSLedScrollArea.setObjectName("TLSSLedScrollArea")
        self.TLSSLedScrollWidgetContents = QtWidgets.QWidget()
        self.TLSSLedScrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 3128, 2008))
        self.TLSSLedScrollWidgetContents.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.TLSSLedScrollWidgetContents.setObjectName("TLSSLedScrollWidgetContents")
        self.gridLayout_57 = QtWidgets.QGridLayout(self.TLSSLedScrollWidgetContents)
        self.gridLayout_57.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_57.setSpacing(6)
        self.gridLayout_57.setObjectName("gridLayout_57")
        self.line_215 = QtWidgets.QFrame(self.TLSSLedScrollWidgetContents)
        self.line_215.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_215.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_215.setObjectName("line_215")
        self.gridLayout_57.addWidget(self.line_215, 5, 0, 1, 1)
        self.line_216 = QtWidgets.QFrame(self.TLSSLedScrollWidgetContents)
        self.line_216.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_216.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_216.setObjectName("line_216")
        self.gridLayout_57.addWidget(self.line_216, 9, 0, 1, 1)
        self.TLSSLedB3 = QtWidgets.QLabel(self.TLSSLedScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.TLSSLedB3.setFont(font)
        self.TLSSLedB3.setObjectName("TLSSLedB3")
        self.gridLayout_57.addWidget(self.TLSSLedB3, 12, 0, 1, 1)
        self.line_217 = QtWidgets.QFrame(self.TLSSLedScrollWidgetContents)
        self.line_217.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_217.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_217.setObjectName("line_217")
        self.gridLayout_57.addWidget(self.line_217, 1, 0, 1, 1)
        self.line_218 = QtWidgets.QFrame(self.TLSSLedScrollWidgetContents)
        self.line_218.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_218.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_218.setObjectName("line_218")
        self.gridLayout_57.addWidget(self.line_218, 11, 0, 1, 1)
        self.line_219 = QtWidgets.QFrame(self.TLSSLedScrollWidgetContents)
        self.line_219.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_219.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_219.setObjectName("line_219")
        self.gridLayout_57.addWidget(self.line_219, 13, 0, 1, 1)
        self.TLSSLedH2 = QtWidgets.QLabel(self.TLSSLedScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.TLSSLedH2.setFont(font)
        self.TLSSLedH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.TLSSLedH2.setObjectName("TLSSLedH2")
        self.gridLayout_57.addWidget(self.TLSSLedH2, 6, 0, 1, 1)
        self.TLSSLedH1 = QtWidgets.QLabel(self.TLSSLedScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.TLSSLedH1.setFont(font)
        self.TLSSLedH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.TLSSLedH1.setObjectName("TLSSLedH1")
        self.gridLayout_57.addWidget(self.TLSSLedH1, 2, 0, 1, 1)
        self.TLSSLedH3 = QtWidgets.QLabel(self.TLSSLedScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.TLSSLedH3.setFont(font)
        self.TLSSLedH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.TLSSLedH3.setObjectName("TLSSLedH3")
        self.gridLayout_57.addWidget(self.TLSSLedH3, 10, 0, 1, 1)
        self.line_220 = QtWidgets.QFrame(self.TLSSLedScrollWidgetContents)
        self.line_220.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_220.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_220.setObjectName("line_220")
        self.gridLayout_57.addWidget(self.line_220, 7, 0, 1, 1)
        self.TLSSLedButton = QtWidgets.QPushButton(self.TLSSLedScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.TLSSLedButton.setFont(font)
        self.TLSSLedButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(79, 79, 79);")
        self.TLSSLedButton.setObjectName("TLSSLedButton")
        self.gridLayout_57.addWidget(self.TLSSLedButton, 16, 0, 1, 1)
        self.TLSSLedB1 = QtWidgets.QLabel(self.TLSSLedScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.TLSSLedB1.setFont(font)
        self.TLSSLedB1.setTextFormat(QtCore.Qt.AutoText)
        self.TLSSLedB1.setScaledContents(False)
        self.TLSSLedB1.setWordWrap(False)
        self.TLSSLedB1.setObjectName("TLSSLedB1")
        self.gridLayout_57.addWidget(self.TLSSLedB1, 4, 0, 1, 1)
        spacerItem54 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_57.addItem(spacerItem54, 17, 0, 1, 1)
        self.line_221 = QtWidgets.QFrame(self.TLSSLedScrollWidgetContents)
        self.line_221.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_221.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_221.setObjectName("line_221")
        self.gridLayout_57.addWidget(self.line_221, 3, 0, 1, 1)
        self.line_222 = QtWidgets.QFrame(self.TLSSLedScrollWidgetContents)
        self.line_222.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_222.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_222.setObjectName("line_222")
        self.gridLayout_57.addWidget(self.line_222, 15, 0, 1, 1)
        self.TLSSLedTitle = QtWidgets.QLabel(self.TLSSLedScrollWidgetContents)
        self.TLSSLedTitle.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.TLSSLedTitle.setFont(font)
        self.TLSSLedTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.TLSSLedTitle.setObjectName("TLSSLedTitle")
        self.gridLayout_57.addWidget(self.TLSSLedTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.TLSSLedH4 = QtWidgets.QLabel(self.TLSSLedScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.TLSSLedH4.setFont(font)
        self.TLSSLedH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.TLSSLedH4.setObjectName("TLSSLedH4")
        self.gridLayout_57.addWidget(self.TLSSLedH4, 14, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.TLSSLedB2 = QtWidgets.QLabel(self.TLSSLedScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.TLSSLedB2.setFont(font)
        self.TLSSLedB2.setObjectName("TLSSLedB2")
        self.gridLayout_57.addWidget(self.TLSSLedB2, 8, 0, 1, 1)
        self.TLSSLedScrollArea.setWidget(self.TLSSLedScrollWidgetContents)
        self.gridLayout_56.addWidget(self.TLSSLedScrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.TLSSLedTab, "")
        self.twofiTab = QtWidgets.QWidget()
        self.twofiTab.setObjectName("twofiTab")
        self.gridLayout_58 = QtWidgets.QGridLayout(self.twofiTab)
        self.gridLayout_58.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_58.setSpacing(6)
        self.gridLayout_58.setObjectName("gridLayout_58")
        self.twofiScrollArea = QtWidgets.QScrollArea(self.twofiTab)
        self.twofiScrollArea.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.twofiScrollArea.setWidgetResizable(True)
        self.twofiScrollArea.setObjectName("twofiScrollArea")
        self.twofiScrollWidgetContents = QtWidgets.QWidget()
        self.twofiScrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 3128, 1186))
        self.twofiScrollWidgetContents.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.twofiScrollWidgetContents.setObjectName("twofiScrollWidgetContents")
        self.gridLayout_59 = QtWidgets.QGridLayout(self.twofiScrollWidgetContents)
        self.gridLayout_59.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_59.setSpacing(6)
        self.gridLayout_59.setObjectName("gridLayout_59")
        self.line_223 = QtWidgets.QFrame(self.twofiScrollWidgetContents)
        self.line_223.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_223.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_223.setObjectName("line_223")
        self.gridLayout_59.addWidget(self.line_223, 5, 0, 1, 1)
        self.line_227 = QtWidgets.QFrame(self.twofiScrollWidgetContents)
        self.line_227.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_227.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_227.setObjectName("line_227")
        self.gridLayout_59.addWidget(self.line_227, 11, 0, 1, 1)
        self.twofiH1 = QtWidgets.QLabel(self.twofiScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.twofiH1.setFont(font)
        self.twofiH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.twofiH1.setObjectName("twofiH1")
        self.gridLayout_59.addWidget(self.twofiH1, 2, 0, 1, 1)
        self.line_225 = QtWidgets.QFrame(self.twofiScrollWidgetContents)
        self.line_225.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_225.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_225.setObjectName("line_225")
        self.gridLayout_59.addWidget(self.line_225, 1, 0, 1, 1)
        self.twofiH4 = QtWidgets.QLabel(self.twofiScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.twofiH4.setFont(font)
        self.twofiH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.twofiH4.setObjectName("twofiH4")
        self.gridLayout_59.addWidget(self.twofiH4, 12, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.line_230 = QtWidgets.QFrame(self.twofiScrollWidgetContents)
        self.line_230.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_230.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_230.setObjectName("line_230")
        self.gridLayout_59.addWidget(self.line_230, 13, 0, 1, 1)
        self.twofiB2 = QtWidgets.QLabel(self.twofiScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.twofiB2.setFont(font)
        self.twofiB2.setObjectName("twofiB2")
        self.gridLayout_59.addWidget(self.twofiB2, 8, 0, 1, 1)
        self.line_224 = QtWidgets.QFrame(self.twofiScrollWidgetContents)
        self.line_224.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_224.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_224.setObjectName("line_224")
        self.gridLayout_59.addWidget(self.line_224, 9, 0, 1, 1)
        self.line_229 = QtWidgets.QFrame(self.twofiScrollWidgetContents)
        self.line_229.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_229.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_229.setObjectName("line_229")
        self.gridLayout_59.addWidget(self.line_229, 3, 0, 1, 1)
        spacerItem55 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_59.addItem(spacerItem55, 15, 0, 1, 1)
        self.line_228 = QtWidgets.QFrame(self.twofiScrollWidgetContents)
        self.line_228.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_228.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_228.setObjectName("line_228")
        self.gridLayout_59.addWidget(self.line_228, 7, 0, 1, 1)
        self.twofiB1 = QtWidgets.QLabel(self.twofiScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.twofiB1.setFont(font)
        self.twofiB1.setTextFormat(QtCore.Qt.AutoText)
        self.twofiB1.setScaledContents(False)
        self.twofiB1.setWordWrap(False)
        self.twofiB1.setObjectName("twofiB1")
        self.gridLayout_59.addWidget(self.twofiB1, 4, 0, 1, 1)
        self.line_226 = QtWidgets.QFrame(self.twofiScrollWidgetContents)
        self.line_226.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_226.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_226.setObjectName("line_226")
        self.gridLayout_59.addWidget(self.line_226, 10, 0, 1, 1)
        self.twofiButton = QtWidgets.QPushButton(self.twofiScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.twofiButton.setFont(font)
        self.twofiButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(79, 79, 79);")
        self.twofiButton.setObjectName("twofiButton")
        self.gridLayout_59.addWidget(self.twofiButton, 14, 0, 1, 1)
        self.twofiH2 = QtWidgets.QLabel(self.twofiScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.twofiH2.setFont(font)
        self.twofiH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.twofiH2.setObjectName("twofiH2")
        self.gridLayout_59.addWidget(self.twofiH2, 6, 0, 1, 1)
        self.twofiTitle = QtWidgets.QLabel(self.twofiScrollWidgetContents)
        self.twofiTitle.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.twofiTitle.setFont(font)
        self.twofiTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.twofiTitle.setObjectName("twofiTitle")
        self.gridLayout_59.addWidget(self.twofiTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.twofiScrollArea.setWidget(self.twofiScrollWidgetContents)
        self.gridLayout_58.addWidget(self.twofiScrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.twofiTab, "")
        self.urlCrazyTab = QtWidgets.QWidget()
        self.urlCrazyTab.setObjectName("urlCrazyTab")
        self.gridLayout_60 = QtWidgets.QGridLayout(self.urlCrazyTab)
        self.gridLayout_60.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_60.setSpacing(6)
        self.gridLayout_60.setObjectName("gridLayout_60")
        self.urlCrazyScrollArea = QtWidgets.QScrollArea(self.urlCrazyTab)
        self.urlCrazyScrollArea.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.urlCrazyScrollArea.setWidgetResizable(True)
        self.urlCrazyScrollArea.setObjectName("urlCrazyScrollArea")
        self.urlCrazyScrollWidgetContents = QtWidgets.QWidget()
        self.urlCrazyScrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 3128, 2318))
        self.urlCrazyScrollWidgetContents.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.urlCrazyScrollWidgetContents.setObjectName("urlCrazyScrollWidgetContents")
        self.gridLayout_61 = QtWidgets.QGridLayout(self.urlCrazyScrollWidgetContents)
        self.gridLayout_61.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_61.setSpacing(6)
        self.gridLayout_61.setObjectName("gridLayout_61")
        self.line_231 = QtWidgets.QFrame(self.urlCrazyScrollWidgetContents)
        self.line_231.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_231.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_231.setObjectName("line_231")
        self.gridLayout_61.addWidget(self.line_231, 5, 0, 1, 1)
        self.line_232 = QtWidgets.QFrame(self.urlCrazyScrollWidgetContents)
        self.line_232.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_232.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_232.setObjectName("line_232")
        self.gridLayout_61.addWidget(self.line_232, 9, 0, 1, 1)
        self.urlCrazyB3 = QtWidgets.QLabel(self.urlCrazyScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.urlCrazyB3.setFont(font)
        self.urlCrazyB3.setObjectName("urlCrazyB3")
        self.gridLayout_61.addWidget(self.urlCrazyB3, 12, 0, 1, 1)
        self.line_233 = QtWidgets.QFrame(self.urlCrazyScrollWidgetContents)
        self.line_233.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_233.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_233.setObjectName("line_233")
        self.gridLayout_61.addWidget(self.line_233, 1, 0, 1, 1)
        self.line_234 = QtWidgets.QFrame(self.urlCrazyScrollWidgetContents)
        self.line_234.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_234.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_234.setObjectName("line_234")
        self.gridLayout_61.addWidget(self.line_234, 11, 0, 1, 1)
        self.line_235 = QtWidgets.QFrame(self.urlCrazyScrollWidgetContents)
        self.line_235.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_235.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_235.setObjectName("line_235")
        self.gridLayout_61.addWidget(self.line_235, 13, 0, 1, 1)
        self.urlCrazyH2 = QtWidgets.QLabel(self.urlCrazyScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.urlCrazyH2.setFont(font)
        self.urlCrazyH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.urlCrazyH2.setObjectName("urlCrazyH2")
        self.gridLayout_61.addWidget(self.urlCrazyH2, 6, 0, 1, 1)
        self.urlCrazyH1 = QtWidgets.QLabel(self.urlCrazyScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.urlCrazyH1.setFont(font)
        self.urlCrazyH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.urlCrazyH1.setObjectName("urlCrazyH1")
        self.gridLayout_61.addWidget(self.urlCrazyH1, 2, 0, 1, 1)
        self.urlCrazyH3 = QtWidgets.QLabel(self.urlCrazyScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.urlCrazyH3.setFont(font)
        self.urlCrazyH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.urlCrazyH3.setObjectName("urlCrazyH3")
        self.gridLayout_61.addWidget(self.urlCrazyH3, 10, 0, 1, 1)
        self.line_236 = QtWidgets.QFrame(self.urlCrazyScrollWidgetContents)
        self.line_236.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_236.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_236.setObjectName("line_236")
        self.gridLayout_61.addWidget(self.line_236, 7, 0, 1, 1)
        self.urlCrazyButton = QtWidgets.QPushButton(self.urlCrazyScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.urlCrazyButton.setFont(font)
        self.urlCrazyButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(79, 79, 79);")
        self.urlCrazyButton.setObjectName("urlCrazyButton")
        self.gridLayout_61.addWidget(self.urlCrazyButton, 16, 0, 1, 1)
        self.urlCrazyB1 = QtWidgets.QLabel(self.urlCrazyScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.urlCrazyB1.setFont(font)
        self.urlCrazyB1.setTextFormat(QtCore.Qt.AutoText)
        self.urlCrazyB1.setScaledContents(False)
        self.urlCrazyB1.setWordWrap(False)
        self.urlCrazyB1.setObjectName("urlCrazyB1")
        self.gridLayout_61.addWidget(self.urlCrazyB1, 4, 0, 1, 1)
        spacerItem56 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_61.addItem(spacerItem56, 17, 0, 1, 1)
        self.line_237 = QtWidgets.QFrame(self.urlCrazyScrollWidgetContents)
        self.line_237.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_237.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_237.setObjectName("line_237")
        self.gridLayout_61.addWidget(self.line_237, 3, 0, 1, 1)
        self.line_238 = QtWidgets.QFrame(self.urlCrazyScrollWidgetContents)
        self.line_238.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_238.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_238.setObjectName("line_238")
        self.gridLayout_61.addWidget(self.line_238, 15, 0, 1, 1)
        self.urlCrazyTitle = QtWidgets.QLabel(self.urlCrazyScrollWidgetContents)
        self.urlCrazyTitle.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.urlCrazyTitle.setFont(font)
        self.urlCrazyTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.urlCrazyTitle.setObjectName("urlCrazyTitle")
        self.gridLayout_61.addWidget(self.urlCrazyTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.urlCrazyH4 = QtWidgets.QLabel(self.urlCrazyScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.urlCrazyH4.setFont(font)
        self.urlCrazyH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.urlCrazyH4.setObjectName("urlCrazyH4")
        self.gridLayout_61.addWidget(self.urlCrazyH4, 14, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.urlCrazyB2 = QtWidgets.QLabel(self.urlCrazyScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.urlCrazyB2.setFont(font)
        self.urlCrazyB2.setObjectName("urlCrazyB2")
        self.gridLayout_61.addWidget(self.urlCrazyB2, 8, 0, 1, 1)
        self.urlCrazyScrollArea.setWidget(self.urlCrazyScrollWidgetContents)
        self.gridLayout_60.addWidget(self.urlCrazyScrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.urlCrazyTab, "")
        self.WiresharkTab = QtWidgets.QWidget()
        self.WiresharkTab.setObjectName("WiresharkTab")
        self.gridLayout_62 = QtWidgets.QGridLayout(self.WiresharkTab)
        self.gridLayout_62.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_62.setSpacing(6)
        self.gridLayout_62.setObjectName("gridLayout_62")
        self.WiresharkScrollArea = QtWidgets.QScrollArea(self.WiresharkTab)
        self.WiresharkScrollArea.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.WiresharkScrollArea.setWidgetResizable(True)
        self.WiresharkScrollArea.setObjectName("WiresharkScrollArea")
        self.WiresharkScrollWidgetContents = QtWidgets.QWidget()
        self.WiresharkScrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 3128, 3369))
        self.WiresharkScrollWidgetContents.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.WiresharkScrollWidgetContents.setObjectName("WiresharkScrollWidgetContents")
        self.gridLayout_63 = QtWidgets.QGridLayout(self.WiresharkScrollWidgetContents)
        self.gridLayout_63.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_63.setSpacing(6)
        self.gridLayout_63.setObjectName("gridLayout_63")
        self.line_239 = QtWidgets.QFrame(self.WiresharkScrollWidgetContents)
        self.line_239.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_239.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_239.setObjectName("line_239")
        self.gridLayout_63.addWidget(self.line_239, 5, 0, 1, 1)
        self.line_240 = QtWidgets.QFrame(self.WiresharkScrollWidgetContents)
        self.line_240.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_240.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_240.setObjectName("line_240")
        self.gridLayout_63.addWidget(self.line_240, 9, 0, 1, 1)
        self.WiresharkB3 = QtWidgets.QLabel(self.WiresharkScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.WiresharkB3.setFont(font)
        self.WiresharkB3.setObjectName("WiresharkB3")
        self.gridLayout_63.addWidget(self.WiresharkB3, 12, 0, 1, 1)
        self.line_241 = QtWidgets.QFrame(self.WiresharkScrollWidgetContents)
        self.line_241.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_241.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_241.setObjectName("line_241")
        self.gridLayout_63.addWidget(self.line_241, 1, 0, 1, 1)
        self.line_242 = QtWidgets.QFrame(self.WiresharkScrollWidgetContents)
        self.line_242.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_242.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_242.setObjectName("line_242")
        self.gridLayout_63.addWidget(self.line_242, 11, 0, 1, 1)
        self.line_243 = QtWidgets.QFrame(self.WiresharkScrollWidgetContents)
        self.line_243.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_243.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_243.setObjectName("line_243")
        self.gridLayout_63.addWidget(self.line_243, 13, 0, 1, 1)
        self.WiresharkH2 = QtWidgets.QLabel(self.WiresharkScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.WiresharkH2.setFont(font)
        self.WiresharkH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.WiresharkH2.setObjectName("WiresharkH2")
        self.gridLayout_63.addWidget(self.WiresharkH2, 6, 0, 1, 1)
        self.WiresharkH1 = QtWidgets.QLabel(self.WiresharkScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.WiresharkH1.setFont(font)
        self.WiresharkH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.WiresharkH1.setObjectName("WiresharkH1")
        self.gridLayout_63.addWidget(self.WiresharkH1, 2, 0, 1, 1)
        self.WiresharkH3 = QtWidgets.QLabel(self.WiresharkScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.WiresharkH3.setFont(font)
        self.WiresharkH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.WiresharkH3.setObjectName("WiresharkH3")
        self.gridLayout_63.addWidget(self.WiresharkH3, 10, 0, 1, 1)
        self.line_244 = QtWidgets.QFrame(self.WiresharkScrollWidgetContents)
        self.line_244.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_244.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_244.setObjectName("line_244")
        self.gridLayout_63.addWidget(self.line_244, 7, 0, 1, 1)
        self.WiresharkButton = QtWidgets.QPushButton(self.WiresharkScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.WiresharkButton.setFont(font)
        self.WiresharkButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(79, 79, 79);")
        self.WiresharkButton.setObjectName("WiresharkButton")
        self.gridLayout_63.addWidget(self.WiresharkButton, 16, 0, 1, 1)
        self.WiresharkB1 = QtWidgets.QLabel(self.WiresharkScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.WiresharkB1.setFont(font)
        self.WiresharkB1.setTextFormat(QtCore.Qt.AutoText)
        self.WiresharkB1.setScaledContents(False)
        self.WiresharkB1.setWordWrap(False)
        self.WiresharkB1.setObjectName("WiresharkB1")
        self.gridLayout_63.addWidget(self.WiresharkB1, 4, 0, 1, 1)
        spacerItem57 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_63.addItem(spacerItem57, 17, 0, 1, 1)
        self.line_245 = QtWidgets.QFrame(self.WiresharkScrollWidgetContents)
        self.line_245.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_245.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_245.setObjectName("line_245")
        self.gridLayout_63.addWidget(self.line_245, 3, 0, 1, 1)
        self.line_246 = QtWidgets.QFrame(self.WiresharkScrollWidgetContents)
        self.line_246.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_246.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_246.setObjectName("line_246")
        self.gridLayout_63.addWidget(self.line_246, 15, 0, 1, 1)
        self.WiresharkTitle = QtWidgets.QLabel(self.WiresharkScrollWidgetContents)
        self.WiresharkTitle.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.WiresharkTitle.setFont(font)
        self.WiresharkTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.WiresharkTitle.setObjectName("WiresharkTitle")
        self.gridLayout_63.addWidget(self.WiresharkTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.WiresharkH4 = QtWidgets.QLabel(self.WiresharkScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.WiresharkH4.setFont(font)
        self.WiresharkH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.WiresharkH4.setObjectName("WiresharkH4")
        self.gridLayout_63.addWidget(self.WiresharkH4, 14, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.WiresharkB2 = QtWidgets.QLabel(self.WiresharkScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.WiresharkB2.setFont(font)
        self.WiresharkB2.setObjectName("WiresharkB2")
        self.gridLayout_63.addWidget(self.WiresharkB2, 8, 0, 1, 1)
        self.line_239.raise_()
        self.line_240.raise_()
        self.WiresharkB3.raise_()
        self.line_241.raise_()
        self.line_242.raise_()
        self.line_243.raise_()
        self.WiresharkH2.raise_()
        self.WiresharkH1.raise_()
        self.WiresharkH3.raise_()
        self.line_244.raise_()
        self.WiresharkButton.raise_()
        self.WiresharkB1.raise_()
        self.line_245.raise_()
        self.line_246.raise_()
        self.WiresharkH4.raise_()
        self.WiresharkB2.raise_()
        self.WiresharkTitle.raise_()
        self.WiresharkScrollArea.setWidget(self.WiresharkScrollWidgetContents)
        self.gridLayout_62.addWidget(self.WiresharkScrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.WiresharkTab, "")
        self.WOLETab = QtWidgets.QWidget()
        self.WOLETab.setObjectName("WOLETab")
        self.gridLayout_64 = QtWidgets.QGridLayout(self.WOLETab)
        self.gridLayout_64.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_64.setSpacing(6)
        self.gridLayout_64.setObjectName("gridLayout_64")
        self.WOLEScrollArea = QtWidgets.QScrollArea(self.WOLETab)
        self.WOLEScrollArea.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.WOLEScrollArea.setWidgetResizable(True)
        self.WOLEScrollArea.setObjectName("WOLEScrollArea")
        self.WOLEScrollWidgetContents = QtWidgets.QWidget()
        self.WOLEScrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 3128, 2276))
        self.WOLEScrollWidgetContents.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.WOLEScrollWidgetContents.setObjectName("WOLEScrollWidgetContents")
        self.gridLayout_65 = QtWidgets.QGridLayout(self.WOLEScrollWidgetContents)
        self.gridLayout_65.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_65.setSpacing(6)
        self.gridLayout_65.setObjectName("gridLayout_65")
        self.line_247 = QtWidgets.QFrame(self.WOLEScrollWidgetContents)
        self.line_247.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_247.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_247.setObjectName("line_247")
        self.gridLayout_65.addWidget(self.line_247, 5, 0, 1, 1)
        self.line_248 = QtWidgets.QFrame(self.WOLEScrollWidgetContents)
        self.line_248.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_248.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_248.setObjectName("line_248")
        self.gridLayout_65.addWidget(self.line_248, 9, 0, 1, 1)
        self.WOLEB3 = QtWidgets.QLabel(self.WOLEScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.WOLEB3.setFont(font)
        self.WOLEB3.setObjectName("WOLEB3")
        self.gridLayout_65.addWidget(self.WOLEB3, 12, 0, 1, 1)
        self.line_249 = QtWidgets.QFrame(self.WOLEScrollWidgetContents)
        self.line_249.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_249.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_249.setObjectName("line_249")
        self.gridLayout_65.addWidget(self.line_249, 1, 0, 1, 1)
        self.line_250 = QtWidgets.QFrame(self.WOLEScrollWidgetContents)
        self.line_250.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_250.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_250.setObjectName("line_250")
        self.gridLayout_65.addWidget(self.line_250, 11, 0, 1, 1)
        self.line_251 = QtWidgets.QFrame(self.WOLEScrollWidgetContents)
        self.line_251.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_251.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_251.setObjectName("line_251")
        self.gridLayout_65.addWidget(self.line_251, 13, 0, 1, 1)
        self.WOLEH2 = QtWidgets.QLabel(self.WOLEScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.WOLEH2.setFont(font)
        self.WOLEH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.WOLEH2.setObjectName("WOLEH2")
        self.gridLayout_65.addWidget(self.WOLEH2, 6, 0, 1, 1)
        self.WOLEH1 = QtWidgets.QLabel(self.WOLEScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.WOLEH1.setFont(font)
        self.WOLEH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.WOLEH1.setObjectName("WOLEH1")
        self.gridLayout_65.addWidget(self.WOLEH1, 2, 0, 1, 1)
        self.WOLEH3 = QtWidgets.QLabel(self.WOLEScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.WOLEH3.setFont(font)
        self.WOLEH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.WOLEH3.setObjectName("WOLEH3")
        self.gridLayout_65.addWidget(self.WOLEH3, 10, 0, 1, 1)
        self.line_252 = QtWidgets.QFrame(self.WOLEScrollWidgetContents)
        self.line_252.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_252.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_252.setObjectName("line_252")
        self.gridLayout_65.addWidget(self.line_252, 7, 0, 1, 1)
        self.WOLEButton = QtWidgets.QPushButton(self.WOLEScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.WOLEButton.setFont(font)
        self.WOLEButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(79, 79, 79);")
        self.WOLEButton.setObjectName("WOLEButton")
        self.gridLayout_65.addWidget(self.WOLEButton, 16, 0, 1, 1)
        self.WOLEB1 = QtWidgets.QLabel(self.WOLEScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.WOLEB1.setFont(font)
        self.WOLEB1.setTextFormat(QtCore.Qt.AutoText)
        self.WOLEB1.setScaledContents(False)
        self.WOLEB1.setWordWrap(False)
        self.WOLEB1.setObjectName("WOLEB1")
        self.gridLayout_65.addWidget(self.WOLEB1, 4, 0, 1, 1)
        spacerItem58 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_65.addItem(spacerItem58, 17, 0, 1, 1)
        self.line_253 = QtWidgets.QFrame(self.WOLEScrollWidgetContents)
        self.line_253.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_253.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_253.setObjectName("line_253")
        self.gridLayout_65.addWidget(self.line_253, 3, 0, 1, 1)
        self.line_254 = QtWidgets.QFrame(self.WOLEScrollWidgetContents)
        self.line_254.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_254.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_254.setObjectName("line_254")
        self.gridLayout_65.addWidget(self.line_254, 15, 0, 1, 1)
        self.WOLETitle = QtWidgets.QLabel(self.WOLEScrollWidgetContents)
        self.WOLETitle.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.WOLETitle.setFont(font)
        self.WOLETitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.WOLETitle.setObjectName("WOLETitle")
        self.gridLayout_65.addWidget(self.WOLETitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.WOLEH4 = QtWidgets.QLabel(self.WOLEScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.WOLEH4.setFont(font)
        self.WOLEH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.WOLEH4.setObjectName("WOLEH4")
        self.gridLayout_65.addWidget(self.WOLEH4, 14, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.WOLEB2 = QtWidgets.QLabel(self.WOLEScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.WOLEB2.setFont(font)
        self.WOLEB2.setObjectName("WOLEB2")
        self.gridLayout_65.addWidget(self.WOLEB2, 8, 0, 1, 1)
        self.line_247.raise_()
        self.line_248.raise_()
        self.line_249.raise_()
        self.line_250.raise_()
        self.line_251.raise_()
        self.line_252.raise_()
        self.line_253.raise_()
        self.line_254.raise_()
        self.WOLEB3.raise_()
        self.WOLEH2.raise_()
        self.WOLEH1.raise_()
        self.WOLEH3.raise_()
        self.WOLEButton.raise_()
        self.WOLEB1.raise_()
        self.WOLEH4.raise_()
        self.WOLEB2.raise_()
        self.WOLETitle.raise_()
        self.WOLEScrollArea.setWidget(self.WOLEScrollWidgetContents)
        self.gridLayout_64.addWidget(self.WOLEScrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.WOLETab, "")
        self.XplicoTab = QtWidgets.QWidget()
        self.XplicoTab.setObjectName("XplicoTab")
        self.gridLayout_66 = QtWidgets.QGridLayout(self.XplicoTab)
        self.gridLayout_66.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_66.setSpacing(6)
        self.gridLayout_66.setObjectName("gridLayout_66")
        self.XplicoScrollArea = QtWidgets.QScrollArea(self.XplicoTab)
        self.XplicoScrollArea.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.XplicoScrollArea.setWidgetResizable(True)
        self.XplicoScrollArea.setObjectName("XplicoScrollArea")
        self.XplicoScrollWidgetContents = QtWidgets.QWidget()
        self.XplicoScrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 3128, 1869))
        self.XplicoScrollWidgetContents.setStyleSheet("border-color: rgb(44, 42, 48);")
        self.XplicoScrollWidgetContents.setObjectName("XplicoScrollWidgetContents")
        self.gridLayout_67 = QtWidgets.QGridLayout(self.XplicoScrollWidgetContents)
        self.gridLayout_67.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_67.setSpacing(6)
        self.gridLayout_67.setObjectName("gridLayout_67")
        self.line_255 = QtWidgets.QFrame(self.XplicoScrollWidgetContents)
        self.line_255.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_255.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_255.setObjectName("line_255")
        self.gridLayout_67.addWidget(self.line_255, 5, 0, 1, 1)
        self.line_256 = QtWidgets.QFrame(self.XplicoScrollWidgetContents)
        self.line_256.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_256.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_256.setObjectName("line_256")
        self.gridLayout_67.addWidget(self.line_256, 9, 0, 1, 1)
        self.XplicoB3 = QtWidgets.QLabel(self.XplicoScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.XplicoB3.setFont(font)
        self.XplicoB3.setObjectName("XplicoB3")
        self.gridLayout_67.addWidget(self.XplicoB3, 12, 0, 1, 1)
        self.line_257 = QtWidgets.QFrame(self.XplicoScrollWidgetContents)
        self.line_257.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_257.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_257.setObjectName("line_257")
        self.gridLayout_67.addWidget(self.line_257, 1, 0, 1, 1)
        self.line_258 = QtWidgets.QFrame(self.XplicoScrollWidgetContents)
        self.line_258.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_258.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_258.setObjectName("line_258")
        self.gridLayout_67.addWidget(self.line_258, 11, 0, 1, 1)
        self.line_259 = QtWidgets.QFrame(self.XplicoScrollWidgetContents)
        self.line_259.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_259.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_259.setObjectName("line_259")
        self.gridLayout_67.addWidget(self.line_259, 13, 0, 1, 1)
        self.XplicoH2 = QtWidgets.QLabel(self.XplicoScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.XplicoH2.setFont(font)
        self.XplicoH2.setStyleSheet("color: rgb(56, 196, 255);")
        self.XplicoH2.setObjectName("XplicoH2")
        self.gridLayout_67.addWidget(self.XplicoH2, 6, 0, 1, 1)
        self.XplicoH1 = QtWidgets.QLabel(self.XplicoScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.XplicoH1.setFont(font)
        self.XplicoH1.setStyleSheet("color: rgb(56, 196, 255);")
        self.XplicoH1.setObjectName("XplicoH1")
        self.gridLayout_67.addWidget(self.XplicoH1, 2, 0, 1, 1)
        self.XplicoH3 = QtWidgets.QLabel(self.XplicoScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.XplicoH3.setFont(font)
        self.XplicoH3.setStyleSheet("color: rgb(56, 196, 255);")
        self.XplicoH3.setObjectName("XplicoH3")
        self.gridLayout_67.addWidget(self.XplicoH3, 10, 0, 1, 1)
        self.line_260 = QtWidgets.QFrame(self.XplicoScrollWidgetContents)
        self.line_260.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_260.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_260.setObjectName("line_260")
        self.gridLayout_67.addWidget(self.line_260, 7, 0, 1, 1)
        self.XplicoButton = QtWidgets.QPushButton(self.XplicoScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.XplicoButton.setFont(font)
        self.XplicoButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(79, 79, 79);")
        self.XplicoButton.setObjectName("XplicoButton")
        self.gridLayout_67.addWidget(self.XplicoButton, 16, 0, 1, 1)
        self.XplicoB1 = QtWidgets.QLabel(self.XplicoScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.XplicoB1.setFont(font)
        self.XplicoB1.setTextFormat(QtCore.Qt.AutoText)
        self.XplicoB1.setScaledContents(False)
        self.XplicoB1.setWordWrap(False)
        self.XplicoB1.setObjectName("XplicoB1")
        self.gridLayout_67.addWidget(self.XplicoB1, 4, 0, 1, 1)
        spacerItem59 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_67.addItem(spacerItem59, 17, 0, 1, 1)
        self.line_261 = QtWidgets.QFrame(self.XplicoScrollWidgetContents)
        self.line_261.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_261.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_261.setObjectName("line_261")
        self.gridLayout_67.addWidget(self.line_261, 3, 0, 1, 1)
        self.line_262 = QtWidgets.QFrame(self.XplicoScrollWidgetContents)
        self.line_262.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_262.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_262.setObjectName("line_262")
        self.gridLayout_67.addWidget(self.line_262, 15, 0, 1, 1)
        self.XplicoTitle = QtWidgets.QLabel(self.XplicoScrollWidgetContents)
        self.XplicoTitle.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Athelas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.XplicoTitle.setFont(font)
        self.XplicoTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.XplicoTitle.setObjectName("XplicoTitle")
        self.gridLayout_67.addWidget(self.XplicoTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.XplicoH4 = QtWidgets.QLabel(self.XplicoScrollWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.XplicoH4.setFont(font)
        self.XplicoH4.setStyleSheet("color: rgb(56, 196, 255);")
        self.XplicoH4.setObjectName("XplicoH4")
        self.gridLayout_67.addWidget(self.XplicoH4, 14, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.XplicoB2 = QtWidgets.QLabel(self.XplicoScrollWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.XplicoB2.setFont(font)
        self.XplicoB2.setObjectName("XplicoB2")
        self.gridLayout_67.addWidget(self.XplicoB2, 8, 0, 1, 1)
        self.line_255.raise_()
        self.line_256.raise_()
        self.line_257.raise_()
        self.line_258.raise_()
        self.line_259.raise_()
        self.line_260.raise_()
        self.line_261.raise_()
        self.line_262.raise_()
        self.XplicoB3.raise_()
        self.XplicoH2.raise_()
        self.XplicoH1.raise_()
        self.XplicoH3.raise_()
        self.XplicoButton.raise_()
        self.XplicoB1.raise_()
        self.XplicoH4.raise_()
        self.XplicoB2.raise_()
        self.XplicoTitle.raise_()
        self.XplicoScrollArea.setWidget(self.XplicoScrollWidgetContents)
        self.gridLayout_66.addWidget(self.XplicoScrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.XplicoTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(self.centralWidget)
        self.treeWidget.setMinimumSize(QtCore.QSize(210, 0))
        self.treeWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.treeWidget.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(44, 42, 48);\n"
"border-color: rgb(44, 42, 48);\n"
"")
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setBackground(0, QtGui.QColor(89, 89, 89, 10))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.treeWidget.headerItem().setForeground(0, brush)
        self.item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.Click1 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click2 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click3 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click4 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click5 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click6 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click7 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click8 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click9 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click10 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click11 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click12 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click13 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click14 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click15 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click16 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click17 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click18 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click19 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click20 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click21 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click22 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click23 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click24 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click25 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click26 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click27 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click28 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click29 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click30 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click31 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click32 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click33 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click34 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click35 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click36 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click37 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click38 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click39 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click40 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click41 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click42 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click43 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click44 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click45 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click46 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click47 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click48 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click49 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click50 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click51 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click52 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click53 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click54 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click55 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click56 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click57 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click58 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click59 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.Click60 = QtWidgets.QTreeWidgetItem(self.item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 3400, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuWindow = QtWidgets.QMenu(self.menuBar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionNew_Window = QtWidgets.QAction(MainWindow)
        self.actionNew_Window.setObjectName("actionNew_Window")
        self.actionClose_Window = QtWidgets.QAction(MainWindow)
        self.actionClose_Window.setObjectName("actionClose_Window")
        self.actionClose_Tab = QtWidgets.QAction(MainWindow)
        self.actionClose_Tab.setObjectName("actionClose_Tab")
        self.actionNew_Tab = QtWidgets.QAction(MainWindow)
        self.actionNew_Tab.setObjectName("actionNew_Tab")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionSelect_All = QtWidgets.QAction(MainWindow)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionEnable_Dark_Mode = QtWidgets.QAction(MainWindow)
        self.actionEnable_Dark_Mode.setObjectName("actionEnable_Dark_Mode")
        self.actionMinimize = QtWidgets.QAction(MainWindow)
        self.actionMinimize.setObjectName("actionMinimize")
        self.actionEnter_Full_Screen = QtWidgets.QAction(MainWindow)
        self.actionEnter_Full_Screen.setObjectName("actionEnter_Full_Screen")
        self.actionSelect_Next_Tab = QtWidgets.QAction(MainWindow)
        self.actionSelect_Next_Tab.setObjectName("actionSelect_Next_Tab")
        self.actionSelect_Previous_Tab = QtWidgets.QAction(MainWindow)
        self.actionSelect_Previous_Tab.setObjectName("actionSelect_Previous_Tab")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.menuFile.addAction(self.actionNew_Tab)
        self.menuFile.addAction(self.actionNew_Window)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose_Tab)
        self.menuFile.addAction(self.actionClose_Window)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addAction(self.actionSelect_All)
        self.menuView.addAction(self.actionEnable_Dark_Mode)
        self.menuWindow.addAction(self.actionMinimize)
        self.menuWindow.addAction(self.actionEnter_Full_Screen)
        self.menuWindow.addSeparator()
        self.menuWindow.addAction(self.actionSelect_Next_Tab)
        self.menuWindow.addAction(self.actionSelect_Previous_Tab)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuWindow.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "T Y R I O N"))
        self.appNameLabel.setText(_translate("MainWindow", "T Y R I O N"))
        self.versionLabel.setText(_translate("MainWindow", "V e r s i o n   1 . 0"))
        self.descLabel.setText(_translate("MainWindow", "THE GO TO ALL-IN-ONE KALI LINUX TOOL REFERENCE APP "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.welcomeTab), _translate("MainWindow", "Welcome"))
        self.pushButton_30.setText(_translate("MainWindow", "hping3"))
        self.pushButton_17.setText(_translate("MainWindow", "dnstracer"))
        self.pushButton_54.setText(_translate("MainWindow", "theHarvester"))
        self.pushButton_48.setText(_translate("MainWindow", "SPARTA"))
        self.pushButton_35.setText(_translate("MainWindow", "Maltego Teeth"))
        self.pushButton_13.setText(_translate("MainWindow", "dnmap"))
        self.pushButton_10.setText(_translate("MainWindow", "Cookie Cadger"))
        self.pushButton_58.setText(_translate("MainWindow", "Wireshark"))
        self.pushButton_60.setText(_translate("MainWindow", "Xplico"))
        self.pushButton_19.setText(_translate("MainWindow", "DotDotPwn"))
        self.pushButton_25.setText(_translate("MainWindow", "fragroute"))
        self.pushButton_31.setText(_translate("MainWindow", "ident-user-enum"))
        self.pushButton_36.setText(_translate("MainWindow", "masscan"))
        self.pushButton_44.setText(_translate("MainWindow", "Recon-ng"))
        self.pushButton_33.setText(_translate("MainWindow", "iSMTP"))
        self.pushButton_24.setText(_translate("MainWindow", "Firewalk"))
        self.pushButton_23.setText(_translate("MainWindow", "Fierce"))
        self.pushButton_51.setText(_translate("MainWindow", "sslstrip"))
        self.pushButton_45.setText(_translate("MainWindow", "SET"))
        self.pushButton_5.setText(_translate("MainWindow", "bing-ip2hosts"))
        self.pushButton_4.setText(_translate("MainWindow", "Amap"))
        self.pushButton_42.setText(_translate("MainWindow", "p0f"))
        self.pushButton_41.setText(_translate("MainWindow", "ntop"))
        self.pushButton_57.setText(_translate("MainWindow", "URLCrazy"))
        self.pushButton_3.setText(_translate("MainWindow", "Automater"))
        self.pushButton_7.setText(_translate("MainWindow", "CaseFile"))
        self.pushButton_37.setText(_translate("MainWindow", "Metagoofil"))
        self.pushButton_34.setText(_translate("MainWindow", "Ibd"))
        self.pushButton_27.setText(_translate("MainWindow", "Ghost Phisher"))
        self.pushButton_40.setText(_translate("MainWindow", "Nmap"))
        self.pushButton_22.setText(_translate("MainWindow", "Faraday"))
        self.pushButton_8.setText(_translate("MainWindow", "CDPSnarf"))
        self.pushButton_39.setText(_translate("MainWindow", "nbtscan-unixwiz"))
        self.pushButton_11.setText(_translate("MainWindow", "copy-router-config"))
        self.pushButton_38.setText(_translate("MainWindow", "Miranda"))
        self.pushButton_59.setText(_translate("MainWindow", "WOL-E"))
        self.pushButton_9.setText(_translate("MainWindow", "cisco-torch"))
        self.pushButton_53.setText(_translate("MainWindow", "THC-IPV6"))
        self.pushButton_32.setText(_translate("MainWindow", "InTrace"))
        self.pushButton_43.setText(_translate("MainWindow", "Parsero"))
        self.pushButton_18.setText(_translate("MainWindow", "dnswalk"))
        self.pushButton_14.setText(_translate("MainWindow", "dsenum"))
        self.pushButton_26.setText(_translate("MainWindow", "fragrouter"))
        self.pushButton_28.setText(_translate("MainWindow", "GoLismero"))
        self.pushButton_47.setText(_translate("MainWindow", "snmp-check"))
        self.pushButton_46.setText(_translate("MainWindow", "smtp-user-enum"))
        self.pushButton_21.setText(_translate("MainWindow", "enumIAX"))
        self.pushButton_6.setText(_translate("MainWindow", "braa"))
        self.pushButton_29.setText(_translate("MainWindow", "goofile"))
        self.pushButton_52.setText(_translate("MainWindow", "SSLyze"))
        self.pushButton_15.setText(_translate("MainWindow", "dnsmap"))
        self.pushButton_50.setText(_translate("MainWindow", "SSLsplit"))
        self.pushButton.setText(_translate("MainWindow", "acccheck"))
        self.pushButton_55.setText(_translate("MainWindow", "TLSSLed"))
        self.pushButton_49.setText(_translate("MainWindow", "sslcaudit"))
        self.pushButton_56.setText(_translate("MainWindow", "twofi"))
        self.InformationGatheringTitle.setText(_translate("MainWindow", "Information Gathering"))
        self.pushButton_2.setText(_translate("MainWindow", "ace-voip"))
        self.pushButton_20.setText(_translate("MainWindow", "enum4linux"))
        self.pushButton_16.setText(_translate("MainWindow", "DNSRecon"))
        self.pushButton_12.setText(_translate("MainWindow", "DMitry"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.infoGatheringTab), _translate("MainWindow", "Information Gathering"))
        self.acccheckTitle.setText(_translate("MainWindow", "acccheck"))
        self.acccheckH2.setText(_translate("MainWindow", "Usage:"))
        self.acccheckB1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; color:#ffffff;\">The tool is designed as a password dictionary attack tool that targets windows </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">authentication via the SMB protocol. It is really a wrapper script around the ‘smbclient’ binary, </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">and as a result is dependent on it for its execution.</span></p><p><span style=\" font-size:18pt; color:#ffffff;\"><br/>Attempts to connect to the IPC$ and ADMIN$ shares depending on which flags have been<br/>chosen, and tries a combination of usernames and passwords in the hope to identify<br/>the password to a given account via a dictionary password guessing attack.</span></p><p><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Source: </span><span style=\" font-size:18pt; color:#ffffff;\">https://labs.portcullis.co.uk/tools/acccheck/</span></p><p><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Author:</span><span style=\" font-size:18pt; color:#ffffff;\"> Faisal Dean</span><span style=\" font-size:18pt;\"><br/></span></p></body></html>"))
        self.acccheckB4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">root@kali:~#</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">acccheck.pl -T smb-ips.txt -v</span><span style=\" font-family:\'Courier New\'; font-size:18pt;\"><br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">Host:192.168.1.201, Username:Administrator, Password:BLANK</span><span style=\" font-size:18pt;\"><br/></span></p></body></html>"))
        self.acccheckH3.setText(_translate("MainWindow", "Examples:"))
        self.acccheckB2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-family:\'Courier\'; font-size:18pt; font-weight:600; color:#00b0f0;\">./acccheck </span><span style=\" font-size:18pt; color:#ffffff;\">[optional]</span><span style=\" font-size:18pt;\"><br/><br/></span><span style=\" font-family:\'Courier\'; font-size:18pt; font-weight:600; color:#00b0f0;\">-t </span><span style=\" font-size:18pt; color:#ffffff;\">[single host IP address]</span></p><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">OR</span></p><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-family:\'Courier\'; font-size:18pt; font-weight:600; color:#00b0f0;\">-T </span><span style=\" font-size:18pt; color:#ffffff;\">[file containing target ip address(es)]</span><span style=\" font-size:18pt;\"><br/><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Optional:</span></p><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-family:\'Courier\'; font-size:18pt; font-weight:600; color:#00b0f0;\">-p </span><span style=\" font-size:18pt; color:#ffffff;\">[single password]</span><span style=\" font-size:18pt;\"><br/></span><span style=\" font-family:\'Courier\'; font-size:18pt; font-weight:600; color:#00b0f0;\">-P</span><span style=\" font-size:18pt; color:#ffffff;\">[file containing passwords]</span><span style=\" font-size:18pt;\"><br/></span><span style=\" font-family:\'Courier\'; font-size:18pt; font-weight:600; color:#00b0f0;\">-u</span><span style=\" font-size:18pt; color:#ffffff;\">[single user]</span><span style=\" font-size:18pt;\"><br/></span><span style=\" font-family:\'Courier\'; font-size:18pt; font-weight:600; color:#00b0f0;\">-U </span><span style=\" font-size:18pt; color:#ffffff;\">[file containing usernames]</span><span style=\" font-size:18pt;\"><br/></span><span style=\" font-family:\'Courier\'; font-size:18pt; font-weight:600; color:#00b0f0;\">-v </span><span style=\" font-size:18pt; color:#ffffff;\">[verbose mode]</span><span style=\" font-size:18pt;\"><br/></span></p></body></html>"))
        self.acccheckH1.setText(_translate("MainWindow", "Description:"))
        self.acccheckButton.setText(_translate("MainWindow", "./accheck"))
        self.acccheckH4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#39b5ff;\">RUN ON TERMINAL :</span></p></body></html>"))
        self.acccheckB3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; color:#ffffff;\">Attempt the \'Administrator\' account with a [BLANK] password.</span><span style=\" font-size:18pt;\"><br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">acccheck -t 10.10.10.1</span><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; color:#ffffff;\">Attempt all passwords in \'password.txt\' against the \'Administrator\' account.</span><span style=\" font-size:18pt;\"><br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">acccheck -t 10.10.10.1 -P password.txt</span><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; color:#ffffff;\">Attempt all password in \'password.txt\' against all users in \'users.txt\'.</span><span style=\" font-size:18pt;\"><br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">acccehck -t 10.10.10.1 -U users.txt -P password.txt</span><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; color:#ffffff;\">Attempt a single password against a single user.</span><span style=\" font-size:18pt;\"><br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">acccheck -t 10.10.10.1 -u administrator -p password</span><span style=\" font-size:18pt;\"><br/></span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.acccheckTab), _translate("MainWindow", "acccheck"))
        self.acevoipTitle.setText(_translate("MainWindow", "ace-voip"))
        self.acevoipButton.setText(_translate("MainWindow", "./ace"))
        self.acevoipH4.setText(_translate("MainWindow", "RUN ON TERMINAL :"))
        self.acevoipB3.setText(_translate("MainWindow", "Usage requires MAC Address of IP Phone supplied with -m option\n"
"Usage: ace -t -m\n"
"\n"
"Mode to automatically discover TFTP Server IP via DHCP Option 150 (-m)\n"
"Example: ace -i eth0 -m 00:1E:F7:28:9C:8e\n"
"\n"
"Mode to specify IP Address of TFTP Server\n"
"Example: ace -i eth0 -t 192.168.10.150 -m 00:1E:F7:28:9C:8e\n"
"\n"
"Mode to specify the Voice VLAN ID\n"
"Example: ace -i eth0 -v 96 -m 00:1E:F7:28:9C:8E\n"
"\n"
"Verbose mode\n"
"Example: ace -i eth0 -v 96 -m 00:1E:F7:28:9C:8E -d\n"
"\n"
"Mode to remove vlan interface\n"
"Example: ace -r eth0.96\n"
"\n"
"Mode to auto-discover voice vlan ID in the listening mode for CDP\n"
"Example: ace -i eth0 -c 0 -m 00:1E:F7:28:9C:8E\n"
"\n"
"Mode to auto-discover voice vlan ID in the spoofing mode for CDP\n"
"Example: ace -i eth0 -c 1 -m 00:1E:F7:28:9C:8E\n"
""))
        self.acevoipB1.setText(_translate("MainWindow", "ACE (Automated Corporate Enumerator) is a simple yet powerful VoIP Corporate Directory \n"
"enumeration tool that mimics the behavior of an IP Phone in order to download the name and \n"
"extension entries that a given phone can display on its screen interface. In the same way that the \n"
"“corporate directory” feature of VoIP hardphones enables users to easily dial by name via their \n"
"VoIP handsets, ACE was developed as a research idea born from “VoIP Hopper” to automate\n"
"VoIP attacks that can be targeted against names in an enterprise Directory. The concept is that in \n"
"the future, attacks will be carried out against users based on their name, rather than targeting \n"
"VoIP traffic against random RTP audio streams or IP addresses. ACE works by using DHCP, \n"
"TFTP, and HTTP in order to download the VoIP corporate directory. It then outputs the directory \n"
"to a text file, which can be used as input to other VoIP assessment tools.\n"
"\n"
"Source: http://ucsniff.sourceforge.net/ace.html"))
        self.acevoipH2.setText(_translate("MainWindow", "Usage:"))
        self.acevoipH1.setText(_translate("MainWindow", "Description:"))
        self.acevoipB2.setText(_translate("MainWindow", "root@kali:~# ace\n"
"ACE v1.10: Automated Corporate (Data) Enumerator\n"
"Usage: ace [-i interface] [ -m mac address ] [ -t tftp server ip address | -c cdp mode | \n"
"-v voice vlan id | -r vlan interface | -d verbose mode ]\n"
"\n"
"-i (Mandatory) Interface for sniffing/sending packets\n"
"-m (Mandatory) MAC address of the victim IP phone\n"
"-t (Optional) tftp server ip address\n"
"-c (Optional) 0 CDP sniff mode, 1 CDP spoof mode\n"
"-v (Optional) Enter the voice vlan ID\n"
"-r (Optional) Removes the VLAN interface\n"
"-d (Optional) Verbose | debug mode\n"
""))
        self.acevoipH3.setText(_translate("MainWindow", "Examples:"))
        self.acevoipB4.setText(_translate("MainWindow", "root@kali:~# coming soon"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.acevoipTab), _translate("MainWindow", "ace-voip"))
        self.amapTitle.setText(_translate("MainWindow", "Amap"))
        self.amapButton.setText(_translate("MainWindow", "./amap"))
        self.amapH4.setText(_translate("MainWindow", "RUN ON TERMINAL :"))
        self.amapB3.setText(_translate("MainWindow", "root@kali:~# amap -bqv 192.168.1.15 80\n"
"Using trigger file /etc/amap/appdefs.trig ... loaded 30 triggers\n"
"Using response file /etc/amap/appdefs.resp ... loaded 346 responses\n"
"Using trigger file /etc/amap/appdefs.rpc ... loaded 450 triggers\n"
"\n"
"amap v5.4 (www.thc.org/thc-amap) started at 2014-05-13 19:07:16 - APPLICATION MAPPING mode\n"
"\n"
"Total amount of tasks to perform in plain connect mode: 23\n"
"Protocol on 192.168.1.15:80/tcp (by trigger ssl) matches http - banner: \n"
"\n"
"501 Method Not Implemented\n"
"\n"
"\n"
"<h1>Method Not Implemented</h1>\n"
"\n"
"\n"
"\n"
"to /index.html not supported.\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"<hr />\n"
"\n"
"\n"
"\n"
"\n"
"<address>Apache/2.2.22 (Debian) Server at 12\n"
"Protocol on 192.168.1.15:80/tcp (by trigger ssl) matches http-apache-2 - banner: \n"
"\n"
"501 Method Not Implemented\n"
"\n"
"</address>\n"
"<h1>Method Not Implemented</h1>\n"
"\n"
"\n"
"\n"
"to /index.html not supported.\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"<hr />\n"
"\n"
"\n"
"\n"
"\n"
"<address>Apache/2.2.22 (Debian) Server at 12\n"
"Waiting for timeout on 19 connections ...</address>amap v5.4 finished at 2014-05-13 19:07:22"))
        self.amapB1.setText(_translate("MainWindow", "Amap was the first next-generation scanning tool for pentesters. It attempts to identify \n"
"applications even if they are running on a different port than normal.\n"
"It also identifies non-ascii based applications. This is achieved by sending trigger packets, and \n"
"looking up the responses in a list of response strings.\n"
"\n"
"Source: https://www.thc.org/thc-amap/"))
        self.amapH2.setText(_translate("MainWindow", "Usage:"))
        self.amapH1.setText(_translate("MainWindow", "Description:"))
        self.amapH3.setText(_translate("MainWindow", "Examples:"))
        self.amapB2.setText(_translate("MainWindow", "root@kali:~# amap\n"
"amap v5.4 (c) 2011 by van Hauser &lt;vh@thc.org&gt; www.thc.org/thc-amap\n"
"Syntax: amap [-A|-B|-P|-W] [-1buSRHUdqv] [[-m] -o ] [-D ] [-t/-T sec] [-c cons] \n"
"[-C retries] [-p proto] [-i ] [target port [port] ...]\n"
"\n"
"Modes:\n"
"-A Map applications: send triggers and analyse responses (default)\n"
"-B Just grab banners, do not send triggers\n"
"-P No banner or application stuff - be a (full connect) port scanner\n"
"Options:\n"
"-1 Only send triggers to a port until 1st identification. Speeeeed!\n"
"-6 Use IPv6 instead of IPv4\n"
"-b Print ascii banner of responses\n"
"-i FILE Nmap machine readable outputfile to read ports from\n"
"-u Ports specified on commandline are UDP (default is TCP)\n"
"-R Do NOT identify RPC service\n"
"-H Do NOT send application triggers marked as potentially harmful\n"
"-U Do NOT dump unrecognised responses (better for scripting)\n"
"-d Dump all responses\n"
"-v Verbose mode, use twice (or more!) for debug (not recommended :-)\n"
"-q Do not report closed ports, and do not print them as unidentified\n"
"-o FILE [-m] Write output to file FILE, -m creates machine readable output\n"
"-c CONS Amount of parallel connections to make (default 32, max 256)\n"
"-C RETRIES Number of reconnects on connect timeouts (see -T) (default 3)\n"
"-T SEC Connect timeout on connection attempts in seconds (default 5)\n"
"-t SEC Response wait timeout in seconds (default 5)\n"
"-p PROTO Only send triggers for this protocol (e.g. ftp)\n"
"TARGET PORT The target address and port(s) to scan (additional to -i)\n"
"\n"
"amap is a tool to identify application protocols on target ports.\n"
"\n"
"Note: this version was NOT compiled with SSL support!\n"
"Usage hint: Options \"-bqv\" are recommended, add \"-1\" for fast/rush checks.\n"
""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.amapTab), _translate("MainWindow", "amap"))
        self.automaterTitle.setText(_translate("MainWindow", "Automater"))
        self.automaterButton.setText(_translate("MainWindow", "./automater"))
        self.automaterH4.setText(_translate("MainWindow", "RUN ON TERMINAL :"))
        self.automaterB3.setText(_translate("MainWindow", "root@kali:~# automater -s robtex 50.116.53.73\n"
"[*] Checking http://api.tekdefense.com/robtex/rob.php?q=50.116.53.73"))
        self.automaterB1.setText(_translate("MainWindow", "Automater is a URL/Domain, IP Address, and Md5 Hash OSINT tool aimed at making the \n"
"analysis process easier for intrusion Analysts. Given a target (URL, IP, or HASH) or a file full of \n"
"targets Automater will return relevant results from sources like the following: IPvoid.com, \n"
"Robtex.com, Fortiguard.com, unshorten.me, Urlvoid.com, Labs.alienvault.com, ThreatExpert, \n"
"VxVault, and VirusTotal.\n"
"\n"
"Source: http://www.tekdefense.com/automater/\n"
"\n"
""))
        self.automaterH2.setText(_translate("MainWindow", "Usage:"))
        self.automaterH1.setText(_translate("MainWindow", "Description:"))
        self.automaterB2.setText(_translate("MainWindow", "root@kali:~# automater -h\n"
"usage: Automater.py [-h] [-o OUTPUT] [-w WEB] [-c CSV] [-d DELAY] [-s SOURCE]\n"
"[--p] [--proxy PROXY] [-a USERAGENT]\n"
"target\n"
"\n"
"IP, URL, and Hash Passive Analysis tool\n"
"\n"
"positional arguments:\n"
"target List one IP Address (CIDR or dash notation accepted),\n"
"URL or Hash to query or pass the filename of a file\n"
"containing IP Address info, URL or Hash to query each\n"
"separated by a newline.\n"
"\n"
"optional arguments:\n"
"-h, --help show this help message and exit\n"
"-o OUTPUT, --output OUTPUT\n"
"This option will output the results to a file.\n"
"-w WEB, --web WEB This option will output the results to an HTML file.\n"
"-c CSV, --csv CSV This option will output the results to a CSV file.\n"
"-d DELAY, --delay DELAY\n"
"This will change the delay to the inputted seconds.\n"
"Default is 2.\n"
"-s SOURCE, --source SOURCE\n"
"This option will only run the target against a\n"
"specific source engine to pull associated domains.\n"
"Options are defined in the name attribute of the site\n"
"element in the XML configuration file\n"
"--p, --post This option tells the program to post information to\n"
"sites that allow posting. By default the program will\n"
"NOT post to sites that require a post.\n"
"--proxy PROXY This option will set a proxy to use (eg.\n"
"proxy.example.com:8080)\n"
"-a USERAGENT, --useragent USERAGENT\n"
"This option allows the user to set the user-agent seen\n"
"by web servers being utilized. By default, the user-\n"
"agent is set to Automater/version"))
        self.automaterH3.setText(_translate("MainWindow", "Examples:"))
        self.automaterB4.setText(_translate("MainWindow", "____________________ Results found for: 50.116.53.73 ____________________\n"
"[+] A records from Robtex.com: www.kali.org"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.automaterTab), _translate("MainWindow", "Automater"))
        self.bingip2hostsTitle.setText(_translate("MainWindow", "bing-ip2hosts"))
        self.bingip2hostsButton.setText(_translate("MainWindow", "./bing-ip2hosts"))
        self.bingip2hostsH4.setText(_translate("MainWindow", "RUN ON TERMINAL :"))
        self.bingip2hostsB3.setText(_translate("MainWindow", "root@kali:~# bing-ip2hosts -p microsoft.com\n"
"[ 65.55.58.201 | Scraping 1 | Found 0 | / ]\n"
"http://microsoft.com\n"
"http://research.microsoft.com\n"
"http://www.answers.microsoft.com\n"
"http://www.microsoft.com\n"
"http://www.msdn.microsoft.com\n"
"\n"
""))
        self.bingip2hostsB1.setText(_translate("MainWindow", "Bing.com is a search engine owned by Microsoft formerly known as MSN Search and Live \n"
"Search. It has a unique feature to search for websites hosted on a specific IP address. Bing-\n"
"ip2hosts uses this feature to enumerate all hostnames which Bing has indexed for a specific IP \n"
"address. This technique is considered best practice during the reconnaissance phase of a \n"
"penetration test in order to discover a larger potential attack surface. Bing-ip2hosts is written in \n"
"the Bash scripting language for Linux. This uses the mobile interface and no API key is required.\n"
"\n"
"\n"
"Source: http://www.morningstarsecurity.com/research/bing-ip2hosts\n"
"\n"
""))
        self.bingip2hostsH2.setText(_translate("MainWindow", "Usage:"))
        self.bingip2hostsH1.setText(_translate("MainWindow", "Description:"))
        self.bingip2hostsB2.setText(_translate("MainWindow", "root@kali:~# bing-ip2hosts\n"
"bing-ip2hosts (o.4) by Andrew Horton aka urbanadventurer\n"
"Homepage: http://www.morningstarsecurity.com/research/bing-ip2hosts\n"
"\n"
"Useful for web intelligence and attack surface mapping of vhosts during\n"
"penetration tests. Find hostnames that share an IP address with your target\n"
"which can be a hostname or an IP address. This makes use of Microsoft\n"
"Bing.com ability to seach by IP address, e.g. \"IP:210.48.71.196\".\n"
"\n"
"Usage: /usr/bin/bing-ip2hosts [OPTIONS] &lt;IP|hostname&gt;\n"
"\n"
"OPTIONS are:\n"
"-n Turn off the progress indicator animation\n"
"-t\n"
"\n"
"<dir>Use this directory instead of /tmp. The directory must exist.\n"
"-i Optional CSV output. Outputs the IP and hostname on each line, separated by a comma.\n"
"-p Optional http:// prefix output. Useful for right-clicking in the shell.\n"
"</dir>"))
        self.bingip2hostsH3.setText(_translate("MainWindow", "Examples:"))
        self.bingip2hostsB4.setText(_translate("MainWindow", "root@kali:~# bing-ip2hosts -p 173.194.33.80\n"
"[ 173.194.33.80 | Scraping 60-69 of 73 | Found 41 | | ]| / ]\n"
"http://asia.google.com\n"
"http://desktop.google.com\n"
"http://ejabat.google.com\n"
"http://google.netscape.com\n"
"http://partner-client.google.com\n"
"http://picasa.google.com\n"
""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.bingip2hostsTab), _translate("MainWindow", "bing-ip2hosts"))
        self.braaTitle.setText(_translate("MainWindow", "braa"))
        self.braaButton.setText(_translate("MainWindow", "./braa"))
        self.braaH4.setText(_translate("MainWindow", "RUN ON TERMINAL :"))
        self.braaB3.setText(_translate("MainWindow", "root@kali:~# braa public@192.168.1.215:.1.3.6.*\n"
"192.168.1.215:122ms:.1.3.6.1.2.1.1.1.0:Linux redhat.biz.local 2.4.20-8 #1 Thu Mar 13 17:54:28 EST 2003 i686\n"
"192.168.1.215:143ms:.1.3.6.1.2.1.1.2.0:.1.3.6.1.4.1.8072.3.2.10\n"
"192.168.1.215:122ms:.1.3.6.1.2.1.1.3.0:4051218219\n"
"192.168.1.215:122ms:.1.3.6.1.2.1.1.4.0:Root <root@localhost> (configure /etc/snmp/snmp.local.conf)\n"
"192.168.1.215:143ms:.1.3.6.1.2.1.1.5.0:redhat.biz.local\n"
"\n"
""))
        self.braaB1.setText(_translate("MainWindow", "Braa is a mass snmp scanner. The intended usage of such a tool is of course making SNMP \n"
"queries – but unlike snmpget or snmpwalk from net-snmp, it is able to query dozens or hundreds \n"
"of hosts simultaneously, and in a single process. Thus, it consumes very few system resources \n"
"and does the scanning VERY fast.\n"
"\n"
"Braa implements its OWN snmp stack, so it does NOT need any SNMP libraries like net-snmp. \n"
"The implementation is very dirty, supports only several data types, and in any case cannot be \n"
"stated ‘standard-conforming’! It was designed to be fast, and it is fast. For this reason (well, and \n"
"also because of my laziness ;), there is no ASN.1 parser in braa – you HAVE to know the \n"
"numerical values of OID’s (for instance .1.3.6.1.2.1.1.5.0 instead of system.sysName.0).\n"
"\n"
"Source: braa README \n"
"\n"
""))
        self.braaH2.setText(_translate("MainWindow", "Usage:"))
        self.braaH1.setText(_translate("MainWindow", "Description:"))
        self.braaB2.setText(_translate("MainWindow", "root@kali:~# braa -h\n"
"braa 0.81 - Mateusz \'mteg\' Golicz <mtg@elsat.net.pl>, 2003 - 2006\n"
"usage: braa [options] [query1] [query2] ...\n"
"  -h        Show this help.\n"
"  -2        Claim to be a SNMP2C agent.\n"
"  -v        Show short summary after doing all queries.\n"
"  -x        Hexdump octet-strings\n"
"  -t <s>    Wait <s> seconds for responses.\n"
"  -d <s>    Wait <s> microseconds after sending each packet.\n"
"  -p <s>    Wait <s> miliseconds between subsequent passes.\n"
"  -f <file> Load queries from file <file> (one by line).\n"
"  -a <time> Quit after <time> seconds, independent on what happens.\n"
"  -r <rc>   Retry count (default: 3).\n"
"\n"
"Query format:\n"
"  GET:   [community@]iprange[:port]:oid[/id]\n"
"  WALK:  [community@]iprange[:port]:oid.*[/id]\n"
"  SET:   [community@]iprange[:port]:oid=value[/id]\n"
"\n"
"Examples:\n"
"         public@10.253.101.1:161:.1.3.6.*\n"
"         10.253.101.1-10.253.101.255:.1.3.6.1.2.1.1.4.0=sme\n"
"         10.253.101.1:.1.3.6.1.2.1.1.1.0/description\n"
"\n"
"It is also possible to specify multiple queries at once:\n"
"         10.253.101.1-10.253.101.255:.1.3.6.1.2.1.1.4.0=sme,.1.3.6.*\n"
"         (Will set .1.3.6.1.2.1.1.4.0 to \'me\' and do a walk starting from .1.3.6)\n"
"\n"
"\n"
"Values for SET queries have to be prepended with a character specifying the value type:\n"
"  i      is INTEGER\n"
"  a      is IPADDRESS\n"
"  s      is OCTET STRING\n"
"  o      is OBJECT IDENTIFIER\n"
"If the type specifier is missing, the value type is auto-detected\n"
""))
        self.braaH3.setText(_translate("MainWindow", "Examples:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.braaTab), _translate("MainWindow", "braa"))
        self.CaseFileTitle.setText(_translate("MainWindow", "CaseFile"))
        self.CaseFileButton.setText(_translate("MainWindow", "./casefile"))
        self.CaseFileH4.setText(_translate("MainWindow", "RUN ON TERMINAL :"))
        self.CaseFileB1.setText(_translate("MainWindow", "CaseFile is the little brother to Maltego. It targets a unique market of ‘offline’ analysts whose primary \n"
"sources of information are not gained from the open-source intelligence side or can be \n"
"programmatically queried. We see these people as investigators and analysts who are working ‘on the \n"
"ground’, getting intelligence from other people in the team and building up an information map of their \n"
"investigation.\n"
"\n"
"CaseFile gives you the ability to quickly add, link and analyze data having the same graphing flexibility \n"
"and performance as Maltego without the use of transforms. CaseFile is roughly a third of the price of \n"
"Maltego. \n"
"\n"
"\n"
"CaseFile is a visual intelligence application that can be used to determine the relationships and real \n"
"world links between hundreds of different types of information.\n"
"\n"
"It gives you the ability to quickly view second, third and n-th order relationships and find links otherwise \n"
"undiscoverable with other types of intelligence tools.\n"
"\n"
"CaseFile comes bundled with many different types of entities that are commonly used in investigations \n"
"allowing you to act quickly and efficiently. CaseFile also has the ability to add custom entity types \n"
"allowing you to extend the product to your own data sets.\n"
"\n"
"\n"
"CaseFile can be used for the information gathering, analytics and intelligence phases of almost all types \n"
"of investigates, from IT Security, Law enforcement and any data driven work. It will save you time and \n"
"will allow you to work more accurately and smarter.\n"
"\n"
"CaseFile has the ability to visualise datasets stored in CSV, XLS and XLSX spreadsheet formats.\n"
"\n"
"We are not marketing people. Sorry.\n"
"\n"
"CaseFile aids you in your thinking process by visually demonstrating interconnected links between searched items.\n"
"\n"
"If access to “hidden” information determines your success, CaseFile can help you discover it.\n"
"\n"
"\n"
"Source: http://paterva.com/web6/products/casefile.php\n"
"\n"
""))
        self.CaseFileH2.setText(_translate("MainWindow", "Usage:"))
        self.CaseFileH1.setText(_translate("MainWindow", "Description:"))
        self.CaseFileB2.setText(_translate("MainWindow", "root@kali:~# casefile"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CaseFileTab), _translate("MainWindow", "CaseFile"))
        self.CDPSnarfTitle.setText(_translate("MainWindow", "CDPSnarf"))
        self.CDPSnarfButton.setText(_translate("MainWindow", "./cdpsnarf"))
        self.CDPSnarfH4.setText(_translate("MainWindow", "RUN ON TERMINAL :"))
        self.CDPSnarfB3.setText(_translate("MainWindow", "root@kali:~# cdpsnarf -i eth0 -w cdpsnarf.pcap\n"
"CDPSnarf v0.1.6 [$Rev: 797 $] initiated.\n"
"   Author: Tasos \"Zapotek\" Laskos\n"
"           <tasos.laskos@gmail.com>\n"
"              <zapotek@segfault.gr>\n"
"   Website: http://github.com/Zapotek/cdpsnarf\n"
"\n"
"Reading packets from eth0.\n"
"Waiting for a CDP packet...\n"
""))
        self.CDPSnarfB1.setText(_translate("MainWindow", "CDPSnarf is a network sniffer exclusively written to extract information from CDP packets.\n"
"\n"
"It provides all the information a “show cdp neighbors detail” command would return on a Cisco \n"
"router and even more.\n"
"\n"
"A feature list follows:\n"
"•    Time intervals between CDP advertisements\n"
"•    Source MAC address\n"
"•    CDP Version\n"
"•    TTL\n"
"•    Checksum\n"
"•    Device ID\n"
"•    Software version\n"
"•    Platform\n"
"•    Addresses\n"
"•    Port ID\n"
"•    Capabilities\n"
"•    Duplex\n"
"•    Save packets in PCAP dump file format\n"
"•    Read packets from PCAP dump files\n"
"•    Debugging information (using the “-d” flag)\n"
"•    Tested with IPv4 and IPv6\n"
"\n"
"Source: https://github.com/Zapotek/cdpsnarf\n"
"\n"
""))
        self.CDPSnarfH2.setText(_translate("MainWindow", "Usage:"))
        self.CDPSnarfH1.setText(_translate("MainWindow", "Description:"))
        self.CDPSnarfB2.setText(_translate("MainWindow", "root@kali:~# cdpsnarf -h\n"
"CDPSnarf v0.1.6 [$Rev: 797 $] initiated.\n"
"   Author: Tasos \"Zapotek\" Laskos\n"
"           <tasos.laskos@gmail.com>\n"
"              <zapotek@segfault.gr>\n"
"   Website: http://github.com/Zapotek/cdpsnarf\n"
"\n"
"cdpsnarf -i <dev> [-h] [-w savefile] [-r dumpfile] [-d]\n"
"\n"
"   -i      define the interface to sniff on\n"
"   -w      write packets to PCAP dump file\n"
"   -r      read packets from PCAP dump file\n"
"   -d      show debugging information\n"
"   -h      show help message and exit"))
        self.CDPSnarfH3.setText(_translate("MainWindow", "Examples:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CDPSnarfTab), _translate("MainWindow", "CDPSnarf"))
        self.ciscoTorchTitle.setText(_translate("MainWindow", "cisco-torch"))
        self.ciscoTorchButton.setText(_translate("MainWindow", "./cisco-torch"))
        self.ciscoTorchH4.setText(_translate("MainWindow", "RUN ON TERMINAL :"))
        self.ciscoTorchB3.setText(_translate("MainWindow", "root@kali:~# cisco-torch -A 192.168.99.202\n"
"Using config file torch.conf...\n"
"Loading include and plugin ...\n"
"\n"
"###############################################################\n"
"#   Cisco Torch Mass Scanner                   #\n"
"#   Becase we need it...                                      #\n"
"#   http://www.arhont.com/cisco-torch.pl                      #\n"
"###############################################################\n"
"\n"
"List of targets contains 1 host(s)\n"
"8853:   Checking 192.168.99.202 ...\n"
"HUH db not found, it should be in fingerprint.db\n"
"Skipping Telnet fingerprint\n"
"* Cisco by SNMP found ***\n"
"*System Description: Cisco Internetwork Operating System Software\n"
"IOS (tm) 3600 Software (C3640-IK9O3S-M), Version 12.3(22), RELEASE SOFTWARE (fc2)\n"
"Technical Support: http://www.cisco.com/techsupport\n"
"Copyright (c) 1986-2007 by cisco Systems, Inc.\n"
"Compiled Wed 24-Jan-07 1\n"
"\n"
"Cisco-IOS Webserver found\n"
" HTTP/1.1 401 Unauthorized\n"
"Date: Tue, 13 Apr 1993 00:57:07 GMT\n"
"Server: cisco-IOS\n"
"Accept-Ranges: none\n"
"WWW-Authenticate: Basic realm=\"level_15_access\"\n"
"\n"
"401 Unauthorized\n"
"\n"
"\n"
" Cisco WWW-Authenticate webserver found\n"
" HTTP/1.1 401 Unauthorized\n"
"Date: Tue, 13 Apr 1993 00:57:07 GMT\n"
"Server: cisco-IOS\n"
"Accept-Ranges: none\n"
"WWW-Authenticate: Basic realm=\"level_15_access\"\n"
"\n"
"401 Unauthorized\n"
"\n"
"\n"
"--->\n"
"- All scans done. Cisco Torch Mass Scanner  -\n"
"---> Exiting.\n"
"\n"
""))
        self.ciscoTorchB1.setText(_translate("MainWindow", "Cisco Torch mass scanning, fingerprinting, and exploitation tool was written while working on \n"
"the next edition of the “Hacking Exposed Cisco Networks”, since the tools available on the \n"
"market could not meet our needs. \n"
"\n"
"The main feature that makes Cisco-torch different from similar tools is the extensive use of \n"
"forking to launch multiple scanning processes on the background for maximum scanning \n"
"efficiency. Also, it uses several methods of application layer fingerprinting simultaneously, if \n"
"needed. We wanted something fast to discover remote Cisco hosts running Telnet, SSH, Web, \n"
"NTP and SNMP services and launch dictionary attacks against the services discovered.\n"
"\n"
"Source: http://www.hackingciscoexposed.com/?link=tools\n"
"\n"
""))
        self.ciscoTorchH2.setText(_translate("MainWindow", "Usage:"))
        self.ciscoTorchH1.setText(_translate("MainWindow", "Description:"))
        self.ciscoTorchB2.setText(_translate("MainWindow", "root@kali:~# cisco-torch\n"
"Using config file torch.conf...\n"
"Loading include and plugin ...\n"
" version\n"
"usage: cisco-torch <options> <IP,hostname,network>\n"
"\n"
"or: cisco-torch <options> -F <hostlist>\n"
"\n"
"Available options:\n"
"-O <output file>\n"
"-A      All fingerprint scan types combined\n"
"-t      Cisco Telnetd scan\n"
"-s      Cisco SSHd scan\n"
"-u      Cisco SNMP scan\n"
"-g      Cisco config or tftp file download\n"
"-n      NTP fingerprinting scan\n"
"-j      TFTP fingerprinting scan\n"
"-l <type>   loglevel\n"
"        c  critical (default)\n"
"        v  verbose\n"
"        d  debug\n"
"-w      Cisco Webserver scan\n"
"-z      Cisco IOS HTTP Authorization Vulnerability Scan\n"
"-c      Cisco Webserver with SSL support scan\n"
"-b      Password dictionary attack (use with -s, -u, -c, -w , -j or -t only)\n"
"-V      Print tool version and exit\n"
"examples:   cisco-torch -A 10.10.0.0/16\n"
"        cisco-torch -s -b -F sshtocheck.txt\n"
"        cisco-torch -w -z 10.10.0.0/16\n"
"        cisco-torch -j -b -g -F tftptocheck.txt\n"
"\n"
""))
        self.ciscoTorchH3.setText(_translate("MainWindow", "Examples:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ciscoTorchTab), _translate("MainWindow", "cisco-torch"))
        self.CookieCadgerTitle.setText(_translate("MainWindow", "Cookie Cadger"))
        self.CookieCadgerB3.setText(_translate("MainWindow", "root@kali:~# cookie-cadger"))
        self.CookieCadgerH4.setText(_translate("MainWindow", "RUN ON TERMINAL :"))
        self.CookieCadgerButton.setText(_translate("MainWindow", "./cookie-cadger"))
        self.CookieCadgerB1.setText(_translate("MainWindow", "Cookie Cadger helps identify information leakage from applications that utilize insecure HTTP \n"
"GET requests.\n"
"\n"
"Web providers have started stepping up to the plate since Firesheep was released in 2010. Today, \n"
"most major websites can provide SSL/TLS during all transactions, preventing cookie data from \n"
"leaking over wired Ethernet or insecure Wi-Fi. But the fact remains that Firesheep was more of a \n"
"toy than a tool. Cookie Cadger is the first open-source pen-testing tool ever made for intercepting \n"
"and replaying specific insecure HTTP GET requests into a browser.\n"
"\n"
"Cookie Cadgers Request Enumeration Abilities\n"
"\n"
"Cookie Cadger is a graphical utility which harnesses the power of the Wireshark suite and Java \n"
"to provide a fully cross-platform, entirely open- source utility which can monitor wired Ethernet, \n"
"insecure Wi-Fi, or load a packet capture file for offline analysis.\n"
"\n"
"Source: https://www.cookiecadger.com/\n"
"\n"
""))
        self.CookieCadgerH2.setText(_translate("MainWindow", "Usage:"))
        self.CookieCadgerH1.setText(_translate("MainWindow", "Description:"))
        self.CookieCadgerB2.setText(_translate("MainWindow", "root@kali:~# cookie-cadger --help\n"
"Cookie Cadger, version 1.06\n"
"Example usage:\n"
"java -jar CookieCadger.jar\n"
"    --tshark=/usr/sbin/tshark\n"
"    --headless=on\n"
"    --interfacenum=2    (requires --headless=on)\n"
"    --detection=on\n"
"    --demo=on\n"
"    --update=on\n"
"    --dbengine=mysql    (default is \'sqlite\' for local, file-based storage)\n"
"    --dbhost=localhost  (requires --dbengine=mysql)\n"
"    --dbuser=user       (requires --dbengine=mysql)\n"
"    --dbpass=pass       (requires --dbengine=mysql)\n"
"    --dbname=cadgerdata (requires --dbengine=mysql)\n"
"    --dbrefreshrate=15  (in seconds, requires --dbengine=mysql, requires --headless=off)\n"
""))
        self.CookieCadgerH3.setText(_translate("MainWindow", "Examples:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CookieCadgerTab), _translate("MainWindow", "Cookie Cadger"))
        self.copyRouterConfigTitle.setText(_translate("MainWindow", "copy-router-config"))
        self.copyRouterConfigButton.setText(_translate("MainWindow", "./copy-router-config"))
        self.copyRouterConfigH4.setText(_translate("MainWindow", "RUN ON TERMINAL :"))
        self.copyRouterConfigB3.setText(_translate("MainWindow", "root@kali:~# copy-router-config.pl 192.168.1.1 192.168.1.15 private\n"
""))
        self.copyRouterConfigB1.setText(_translate("MainWindow", "Copies configuration files from Cisco devices running SNMP.\n"
""))
        self.copyRouterConfigH2.setText(_translate("MainWindow", "Usage:"))
        self.copyRouterConfigH1.setText(_translate("MainWindow", "Description:"))
        self.copyRouterConfigB2.setText(_translate("MainWindow", "root@kali:~# copy-router-config.pl\n"
"\n"
"######################################################\n"
"# Copy Cisco Router config  - Using SNMP\n"
"# Hacked up by muts - muts@offensive-security.com\n"
"#######################################################\n"
"\n"
"Usage : ./copy-copy-config.pl <router-ip> <tftp-serverip> <community>\n"
"\n"
"Make sure a TFTP server is set up, preferably running from /tmp !\n"
"\n"
"\n"
"\n"
"root@kali:~# merge-router-config.pl\n"
"\n"
"######################################################\n"
"# Merge Cisco Router config  - Using SNMP\n"
"# Hacked up by muts - muts@offensive-security.com\n"
"#######################################################\n"
"\n"
"Usage : ./merge-copy-config.pl <router-ip> <tftp-serverip> <community>\n"
"\n"
"Make sure a TFTP server is set up, preferably running from /tmp !\n"
"\n"
""))
        self.copyRouterConfigH3.setText(_translate("MainWindow", "Examples:"))
        self.copyRouterConfigB4.setText(_translate("MainWindow", "root@kali:~# merge-router-config.pl 192.168.1.1 192.168.1.15 private\n"
""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.copyRouterConfigTab), _translate("MainWindow", "copy-router-config"))
        self.DMitryTitle.setText(_translate("MainWindow", "DMitry"))
        self.DMitryButton.setText(_translate("MainWindow", "./dmitry"))
        self.DMitryH4.setText(_translate("MainWindow", "RUN ON TERMINAL :"))
        self.DMitryB3.setText(_translate("MainWindow", "Run a domain whois lookup (w), an IP whois lookup (i), retrieve Netcraft info (n), search for \n"
"subdomains (s), search for email addresses (e), do a TCP port scan (p), and save the output to \n"
"example.txt (o) for the domain example.com:\n"
"\n"
""))
        self.DMitryB1.setText(_translate("MainWindow", "DMitry (Deepmagic Information Gathering Tool) is a UNIX/(GNU)Linux Command Line \n"
"Application coded in C. DMitry has the ability to gather as much information as possible about a \n"
"host. Base functionality is able to gather possible subdomains, email addresses, uptime \n"
"information, tcp port scan, whois lookups, and more.\n"
"\n"
"The following is a list of the current features:\n"
"•    An Open Source Project.\n"
"•    Perform an Internet Number whois lookup.\n"
"•    Retrieve possible uptime data, system and server data.\n"
"•    Perform a SubDomain search on a target host.\n"
"•    Perform an E-Mail address search on a target host.\n"
"•    Perform a TCP Portscan on the host target.\n"
"•    A Modular program allowing user specified modules\n"
"\n"
"Source: http://mor-pah.net/software/dmitry-deepmagic-information-gathering-tool/\n"
"\n"
""))
        self.DMitryH2.setText(_translate("MainWindow", "Usage:"))
        self.DMitryH1.setText(_translate("MainWindow", "Description:"))
        self.DMitryB2.setText(_translate("MainWindow", "root@kali:~# dmitry -h\n"
"Deepmagic Information Gathering Tool\n"
"\"There be some deep magic going on\"\n"
"\n"
"dmitry: invalid option -- \'h\'\n"
"Usage: dmitry [-winsepfb] [-t 0-9] [-o %host.txt] host\n"
"-o Save output to %host.txt or to file specified by -o file\n"
"-i Perform a whois lookup on the IP address of a host\n"
"-w Perform a whois lookup on the domain name of a host\n"
"-n Retrieve Netcraft.com information on a host\n"
"-s Perform a search for possible subdomains\n"
"-e Perform a search for possible email addresses\n"
"-p Perform a TCP port scan on a host\n"
"* -f Perform a TCP port scan on a host showing output reporting filtered ports\n"
"* -b Read in the banner received from the scanned port\n"
"* -t 0-9 Set the TTL in seconds when scanning a TCP port ( Default 2 )\n"
"*Requires the -p flagged to be passed\n"
""))
        self.DMitryH3.setText(_translate("MainWindow", "Examples:"))
        self.DMitryB4.setText(_translate("MainWindow", "root@kali:~# dmitry -winsepo example.txt example.com\n"
"Deepmagic Information Gathering Tool\n"
"\"There be some deep magic going on\"\n"
"\n"
"Writing output to \'example.txt\'\n"
"\n"
"HostIP:93.184.216.119\n"
"HostName:example.com\n"
"\n"
"Gathered Inet-whois information for 93.184.216.119\n"
"---------------------------------"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DMitryTab), _translate("MainWindow", "DMitry"))
        self.dnmapTitle.setText(_translate("MainWindow", "dnmap"))
        self.dnmapButton.setText(_translate("MainWindow", "./dnmap_client"))
        self.dnmapH4.setText(_translate("MainWindow", "RUN ON TERMINAL :"))
        self.dnmapB3.setText(_translate("MainWindow", "root@kali:~# echo \"nmap -F 192.168.1.0/24 -v -n -oA sub1\" >> dnmap.txt\n"
"root@kali:~# echo \"nmap -F 192.168.0.0/24 -v -n -oA sub0\" >> dnmap.txt\n"
"root@kali:~# dnmap_server -f dnmap.txt\n"
"+-----------------------------------------------------------------------------------------------+\n"
"| dnmap_server Version 0.6                        |\n"
"| This program is free software; you can redistribute it and/or modify         |\n"
"| it under the terms of the GNU General Public License as published by     |\n"
"| the Free Software Foundation; either version 2 of the License, or            |\n"
"| (at your option) any later version.                                              |\n"
"|                                                                                      |\n"
"| Author: Garcia Sebastian, eldraco@gmail.com                                  |\n"
"| www.mateslab.com.ar                                                              |\n"
"+-----------------------------------------------------------------------------------------------+\n"
"\n"
"=| MET:0:00:00.000544 | Amount of Online clients: 0 |=\n"
"\n"
"\n"
""))
        self.dnmapB1.setText(_translate("MainWindow", "dnmap is a framework to distribute nmap scans among several clients. It reads an already created \n"
"file with nmap commands and send those commands to each client connected to it.\n"
"\n"
"The framework use a client/server architecture. The server knows what to do and the clients do \n"
"it. All the logic and statistics are managed in the server. Nmap output is stored on both server and \n"
"client. \n"
"\n"
"Usually you would want this if you have to scan a large group of hosts and you have several \n"
"different internet connections (or friends that want to help you).\n"
"\n"
"Source: http://mateslab.weebly.com/dnmap-the-distributed-nmap.html\n"
"\n"
""))
        self.dnmapH2.setText(_translate("MainWindow", "Usage:"))
        self.dnmapH1.setText(_translate("MainWindow", "Description:"))
        self.dnmapB2.setText(_translate("MainWindow", "root@kali:~# dnmap_client -h\n"
"\n"
"+-----------------------------------------------------------------------------------------------+\n"
"| dnmap Client Version 0.6                        |\n"
"| This program is free software; you can redistribute it and/or modify        |\n"
"| it under the terms of the GNU General Public License as published by        |\n"
"| the Free Software Foundation; either version 2 of the License, or        |\n"
"| (at your option) any later version.                    |\n"
"|                                |\n"
"| Author: Garcia Sebastian, eldraco@gmail.com                |\n"
"| www.mateslab.com.ar                        |\n"
"+-----------------------------------------------------------------------------------------------+\n"
"\n"
"usage: /usr/bin/dnmap_client <options>\n"
"options:\n"
"  -s, --server-ip        IP address of dnmap server.\n"
"  -p, --server-port      Port of dnmap server. Dnmap port defaults to 46001\n"
"  -a, --alias      Your name alias so we can give credit to you for your help. Optional\n"
"  -d, --debug      Debuging.\n"
"  -m, --max-rate      Force nmaps commands to use at most this rate. Useful to slow nmap down. \n"
"Adds the --max-rate parameter.\n"
"\n"
"\n"
"\n"
"root@kali:~# dnmap_server -h\n"
"+-----------------------------------------------------------------------------------------------+\n"
"| dnmap_server Version 0.6                                                       |\n"
"| This program is free software; you can redistribute it and/or modify         |\n"
"| it under the terms of the GNU General Public License as published by     |\n"
"| the Free Software Foundation; either version 2 of the License, or            |\n"
"| (at your option) any later version.                                              |\n"
"|                                                                                      |\n"
"| Author: Garcia Sebastian, eldraco@gmail.com                                  |\n"
"| www.mateslab.com.ar                                                              |\n"
"+-----------------------------------------------------------------------------------------------+\n"
"\n"
"usage: /usr/bin/dnmap_server <options>\n"
"options:\n"
"  -f, --nmap-commands        Nmap commands file\n"
"  -p, --port        TCP port where we listen for connections.\n"
"  -L, --log-file        Log file. Defaults to /var/log/dnmap_server.conf.\n"
"  -l, --log-level       Log level. Defaults to info.\n"
"  -v, --verbose_level         Verbose level. Give a number between 1 and 5. Defaults to 1. Level 0 means be quiet.\n"
"  -t, --client-timeout         How many time should we wait before marking a client Offline. We still remember its values just in case it cames back.\n"
"  -s, --sort            Field to sort the statical value. You can choose from: Alias, #Commands, UpTime, RunCmdXMin, AvrCmdXMin, Status\n"
"  -P, --pem-file         pem file to use for TLS connection. By default we use the server.pem file provided with the server in the current directory.\n"
"\n"
"dnmap_server uses a \'<nmap-commands-file-name>.dnmaptrace\' file to know where it must continue reading the nmap commands file. If you want to start over again,\n"
"just delete the \'<nmap-commands-file-name>.dnmaptrace\' file\n"
""))
        self.dnmapH3.setText(_translate("MainWindow", "Examples:"))
        self.dnmapB4.setText(_translate("MainWindow", "root@kali:~# dnmap_client -s 192.168.1.15 -a dnmap-client1\n"
"+----------------------------------------------------------------------------------------------+\n"
"| dnmap Client Version 0.6                                                         |\n"
"| This program is free software; you can redistribute it and/or modify         |\n"
"| it under the terms of the GNU General Public License as published by     |\n"
"| the Free Software Foundation; either version 2 of the License, or            |\n"
"| (at your option) any later version.                                              |\n"
"|                                                                                      |\n"
"| Author: Garcia Sebastian, eldraco@gmail.com                                  |\n"
"| www.mateslab.com.ar                                                              |\n"
"+----------------------------------------------------------------------------------------------+\n"
"\n"
"Client Started...\n"
"Nmap output files stored in \'nmap_output\' directory...\n"
"Starting connection...\n"
"Client connected succesfully...\n"
"Waiting for more commands....\n"
"        Command Executed: nmap -F 192.168.1.0/24 -v -n -oA sub1\n"
""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dnmapTab), _translate("MainWindow", "dnmap"))
        self.dnsenumTitle.setText(_translate("MainWindow", "dnsenum"))
        self.dnsenumButton.setText(_translate("MainWindow", "./dnsenum"))
        self.dnsenumH4.setText(_translate("MainWindow", "RUN ON TERMINAL :"))
        self.dnsenumB3.setText(_translate("MainWindow", "root@kali:~# dnsenum --noreverse -o mydomain.xml example.com\n"
"dnsenum.pl VERSION:1.2.3\n"
"\n"
"-----   example.com   -----\n"
"\n"
"\n"
"Host\'s addresses:\n"
"__________________\n"
"\n"
"example.com.                             392      IN    A        93.184.216.119\n"
"\n"
"\n"
"Name Servers:\n"
"______________\n"
"\n"
"b.iana-servers.net.                      122      IN    A        199.43.133.53\n"
"a.iana-servers.net.                      122      IN    A        199.43.132.53\n"
"\n"
"\n"
"Mail (MX) Servers:\n"
"___________________"))
        self.dnsenumB1.setText(_translate("MainWindow", "Multithreaded perl script to enumerate DNS information of a domain and to discover non-\n"
"contiguous ip blocks.\n"
"\n"
"OPERATIONS:\n"
"•    Get the host’s addresse (A record).\n"
"•    Get the namservers (threaded).\n"
"•    Get the MX record (threaded).\n"
"•    Perform axfr queries on nameservers and get BIND VERSION (threaded).\n"
"•    Get extra names and subdomains via google scraping (google query = “allinurl: -www site:domain”).\n"
"•    Brute force subdomains from file, can also perform recursion on subdomain that have NS records (all threaded).\n"
"•    Calculate C class domain network ranges and perform whois queries on them (threaded).\n"
"•    Perform reverse lookups on netranges ( C class or/and whois netranges) (threaded).\n"
"•    Write to domain_ips.txt file ip-blocks.\n"
"\n"
"Source: https://github.com/fwaeytens/dnsenum\n"
"\n"
""))
        self.dnsenumH2.setText(_translate("MainWindow", "Usage:"))
        self.dnsenumH1.setText(_translate("MainWindow", "Description:"))
        self.dnsenumB2.setText(_translate("MainWindow", "root@kali:~# dnsenum -h\n"
"dnsenum.pl VERSION:1.2.3\n"
"Usage: dnsenum.pl [Options] <domain>\n"
"[Options]:\n"
"Note: the brute force -f switch is obligatory.\n"
"GENERAL OPTIONS:\n"
"  --dnsserver   <server>\n"
"            Use this DNS server for A, NS and MX queries.\n"
"  --enum        Shortcut option equivalent to --threads 5 -s 15 -w.\n"
"  -h, --help        Print this help message.\n"
"  --noreverse       Skip the reverse lookup operations.\n"
"  --private     Show and save private ips at the end of the file domain_ips.txt.\n"
"  --subfile <file>  Write all valid subdomains to this file.\n"
"  -t, --timeout <value> The tcp and udp timeout values in seconds (default: 10s).\n"
"  --threads <value> The number of threads that will perform different queries.\n"
"  -v, --verbose     Be verbose: show all the progress and all the error messages.\n"
"GOOGLE SCRAPING OPTIONS:\n"
"  -p, --pages <value>   The number of google search pages to process when scraping names,\n"
"            the default is 5 pages, the -s switch must be specified.\n"
"  -s, --scrap <value>   The maximum number of subdomains that will be scraped from Google (default 15).\n"
"BRUTE FORCE OPTIONS:\n"
"  -f, --file <file> Read subdomains from this file to perform brute force.\n"
"  -u, --update  <a|g|r|z>\n"
"            Update the file specified with the -f switch with valid subdomains.\n"
"    a (all)     Update using all results.\n"
"    g       Update using only google scraping results.\n"
"    r       Update using only reverse lookup results.\n"
"    z       Update using only zonetransfer results.\n"
"  -r, --recursion   Recursion on subdomains, brute force all discovred subdomains that have an NS record.\n"
"WHOIS NETRANGE OPTIONS:\n"
"  -d, --delay <value>   The maximum value of seconds to wait between whois queries, the value is defined randomly, default: 3s.\n"
"  -w, --whois       Perform the whois queries on c class network ranges.\n"
"             **Warning**: this can generate very large netranges and it will take lot of time to performe reverse lookups.\n"
"REVERSE LOOKUP OPTIONS:\n"
"  -e, --exclude <regexp>\n"
"            Exclude PTR records that match the regexp expression from reverse lookup results, useful on invalid hostnames.\n"
"OUTPUT OPTIONS:\n"
"  -o --output <file>    Output in XML format. Can be imported in MagicTree (www.gremwell.com)"))
        self.dnsenumH3.setText(_translate("MainWindow", "Examples:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dnsenumTab), _translate("MainWindow", "dnsenum"))
        self.dnsmapTitle.setText(_translate("MainWindow", "dnsmap"))
        self.dnsmapButton.setText(_translate("MainWindow", "./dnsmap"))
        self.dnsmapH4.setText(_translate("MainWindow", "RUN ON TERMINAL :"))
        self.dnsmapB3.setText(_translate("MainWindow", "root@kali:~# dnsmap example.com -w /usr/share/wordlists/dnsmap.txt\n"
"dnsmap 0.30 - DNS Network Mapper by pagvac (gnucitizen.org)\n"
"\n"
"[+] searching (sub)domains for example.com using /usr/share/wordlists/dnsmap.txt\n"
"[+] using maximum random delay of 10 millisecond(s) between requests\n"
"\n"
""))
        self.dnsmapB1.setText(_translate("MainWindow", "dnsmap was originally released back in 2006 and was inspired by the fictional story “The Thief \n"
"No One Saw” by Paul Craig, which can be found in the book “Stealing the Network – How to \n"
"0wn the Box”.\n"
"\n"
"dnsmap is mainly meant to be used by pentesters during the information gathering/enumeration \n"
"phase of infrastructure security assessments. During the enumeration stage, the security \n"
"consultant would typically discover the target company’s IP netblocks, domain names, phone \n"
"numbers, etc …\n"
"\n"
"Subdomain brute-forcing is another technique that should be used in the enumeration stage, as \n"
"it’s especially useful when other domain enumeration techniques such as zone transfers don’t \n"
"work (I rarely see zone transfers being publicly allowed these days by the way).\n"
"\n"
"Source: http://code.google.com/p/dnsmap/\n"
"\n"
""))
        self.dnsmapH2.setText(_translate("MainWindow", "Usage:"))
        self.dnsmapH1.setText(_translate("MainWindow", "Description:"))
        self.dnsmapB2.setText(_translate("MainWindow", "root@kali:~# dnsmap\n"
"dnsmap 0.30 - DNS Network Mapper by pagvac (gnucitizen.org)\n"
"\n"
"usage: dnsmap <target-domain> [options]\n"
"options:\n"
"-w <wordlist-file>\n"
"-r <regular-results-file>\n"
"-c <csv-results-file>\n"
"-d <delay-millisecs>\n"
"-i <ips-to-ignore> (useful if you\'re obtaining false positives)\n"
"\n"
"e.g.:\n"
"dnsmap target-domain.foo\n"
"dnsmap target-domain.foo -w yourwordlist.txt -r /tmp/domainbf_results.txt\n"
"dnsmap target-fomain.foo -r /tmp/ -d 3000\n"
"dnsmap target-fomain.foo -r ./domainbf_results.txt\n"
"\n"
"\n"
"root@kali:~# dnsmap-bulk.sh\n"
"usage: dnsmap-bulk.sh <domains-file> [results-path]\n"
"e.g.:\n"
"dnsmap-bulk.sh domains.txt\n"
"dnsmap-bulk.sh domains.txt /tmp/\n"
""))
        self.dnsmapH3.setText(_translate("MainWindow", "Examples:"))
        self.dnsmapB4.setText(_translate("MainWindow", "root@kali:~# echo \"example.com\" >> domains.txt\n"
"root@kali:~# echo \"example.org\" >> domains.txt\n"
"root@kali:~# dnsmap-bulk.sh domains.txt\n"
"dnsmap 0.30 - DNS Network Mapper by pagvac (gnucitizen.org)\n"
"\n"
"[+] searching (sub)domains for example.com using built-in wordlist\n"
"[+] using maximum random delay of 10 millisecond(s) between requests\n"
"\n"
""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dnsmapTab), _translate("MainWindow", "dnsmap"))
        self.DNSReconTitle.setText(_translate("MainWindow", "DNSRecon"))
        self.DNSReconButton.setText(_translate("MainWindow", "./dnsrecon"))
        self.DNSReconH4.setText(_translate("MainWindow", "RUN ON TERMINAL :"))
        self.DNSReconB3.setText(_translate("MainWindow", "root@kali:~# dnsrecon -d example.com -D /usr/share/wordlists/dnsmap.txt -t std --xml dnsrecon.xml\n"
"[*] Performing General Enumeration of Domain:\n"
"[*] DNSSEC is configured for example.com\n"
"[*] DNSKEYs:\n"
""))
        self.DNSReconB1.setText(_translate("MainWindow", "DNSRecon provides the ability to perform:\n"
"\n"
"•    Check all NS Records for Zone Transfers\n"
"•    Enumerate General DNS Records for a given Domain (MX, SOA, NS, A, AAAA, SPF and TXT)\n"
"•    Perform common SRV Record Enumeration. Top Level Domain (TLD) Expansion\n"
"•    Check for Wildcard Resolution\n"
"•    Brute Force subdomain and host A and AAAA records given a domain and a wordlist\n"
"•    Perform a PTR Record lookup for a given IP Range or CIDR\n"
"•    Check a DNS Server Cached records for A, AAAA and CNAME Records provided a list of host records in a text file to check\n"
"•    Enumerate Common mDNS records in the Local Network Enumerate Hosts and Subdomains using Google\n"
"\n"
"Source: DNSRecon README\n"
"\n"
"\n"
""))
        self.DNSReconH2.setText(_translate("MainWindow", "Usage:"))
        self.DNSReconH1.setText(_translate("MainWindow", "Description:"))
        self.DNSReconB2.setText(_translate("MainWindow", "root@kali:~# dnsrecon -h\n"
"Version: 0.8.7\n"
"Usage: dnsrecon.py\n"
"\n"
"Options:\n"
"-h, --help Show this help message and exit\n"
"-d, --domain Domain to Target for enumeration.\n"
"-r, --range IP Range for reverse look-up brute force in formats (first-last)\n"
"or in (range/bitmask).\n"
"-n, --name_server Domain server to use, if none is given the SOA of the\n"
"target will be used\n"
"-D, --dictionary Dictionary file of sub-domain and hostnames to use for\n"
"brute force.\n"
"-f Filter out of Brute Force Domain lookup records that resolve to\n"
"the wildcard defined IP Address when saving records.\n"
"-t, --type Specify the type of enumeration to perform:\n"
"std To Enumerate general record types, enumerates.\n"
"SOA, NS, A, AAAA, MX and SRV if AXRF on the\n"
"NS Servers fail.\n"
"\n"
"rvl To Reverse Look Up a given CIDR IP range.\n"
"\n"
"brt To Brute force Domains and Hosts using a given\n"
"dictionary.\n"
"\n"
"srv To Enumerate common SRV Records for a given\n"
"\n"
"domain.\n"
"\n"
"axfr Test all NS Servers in a domain for misconfigured\n"
"zone transfers.\n"
"\n"
"goo Perform Google search for sub-domains and hosts.\n"
"\n"
"snoop To Perform a Cache Snooping against all NS\n"
"servers for a given domain, testing all with\n"
"file containing the domains, file given with -D\n"
"option.\n"
"\n"
"tld Will remove the TLD of given domain and test against\n"
"all TLD\'s registered in IANA\n"
"\n"
"zonewalk Will perform a DNSSEC Zone Walk using NSEC Records.\n"
"\n"
"-a Perform AXFR with the standard enumeration.\n"
"-s Perform Reverse Look-up of ipv4 ranges in the SPF Record of the\n"
"targeted domain with the standard enumeration.\n"
"-g Perform Google enumeration with the standard enumeration.\n"
"-w Do deep whois record analysis and reverse look-up of IP\n"
"ranges found thru whois when doing standard query.\n"
"-z Performs a DNSSEC Zone Walk with the standard enumeration.\n"
"--threads Number of threads to use in Range Reverse Look-up, Forward\n"
"Look-up Brute force and SRV Record Enumeration\n"
"--lifetime Time to wait for a server to response to a query.\n"
"--db SQLite 3 file to save found records.\n"
"--xml XML File to save found records.\n"
"--iw Continua bruteforcing a domain even if a wildcard record resolution is discovered.\n"
"-c, --csv Comma separated value file.\n"
"-v Show attempts in the bruteforce modes.\n"
""))
        self.DNSReconH3.setText(_translate("MainWindow", "Examples:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DNSReconTab), _translate("MainWindow", "DNSRecon"))
        self.dnstracerTitle.setText(_translate("MainWindow", "dnstracer"))
        self.dnstracerButton.setText(_translate("MainWindow", "./dnstracer"))
        self.dnstracerH4.setText(_translate("MainWindow", "RUN ON TERMINAL :"))
        self.dnstracerB3.setText(_translate("MainWindow", "root@kali:~# dnstracer -r 3 -v example.com\n"
"Tracing to example.com[a] via 192.168.1.1, maximum of 3 retries\n"
"192.168.1.1 (192.168.1.1) IP HEADER\n"
"- Destination address:  192.168.1.1\n"
"DNS HEADER (send)\n"
"\n"
""))
        self.dnstracerB1.setText(_translate("MainWindow", "dnstracer determines where a given Domain Name Server (DNS) gets its information from for a \n"
"given hostname, and follows the chain of DNS servers back to the authoritative answer.\n"
"\n"
"Source: http://www.mavetju.org/unix/general.php\n"
"\n"
"\n"
""))
        self.dnstracerH2.setText(_translate("MainWindow", "Usage:"))
        self.dnstracerH1.setText(_translate("MainWindow", "Description:"))
        self.dnstracerB2.setText(_translate("MainWindow", "root@kali:~# dnstracer\n"
"DNSTRACER version 1.8.1 - (c) Edwin Groothuis - http://www.mavetju.org\n"
"Usage: dnstracer [options] [host]\n"
"    -c: disable local caching, default enabled\n"
"    -C: enable negative caching, default disabled\n"
"    -o: enable overview of received answers, default disabled\n"
"    -q <querytype>: query-type to use for the DNS requests, default A\n"
"    -r <retries>: amount of retries for DNS requests, default 3\n"
"    -s <server>: use this server for the initial request, default localhost\n"
"                 If . is specified, A.ROOT-SERVERS.NET will be used.\n"
"    -t <maximum timeout>: Limit time to wait per try\n"
"    -v: verbose\n"
"    -S <ip address>: use this source address.\n"
"    -4: don\'t query IPv6 servers\n"
"\n"
""))
        self.dnstracerH3.setText(_translate("MainWindow", "Examples:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dnstracerTab), _translate("MainWindow", "dnstracer"))
        self.dnswalkTitle.setText(_translate("MainWindow", "dnswalk"))
        self.dnswalkButton.setText(_translate("MainWindow", "./dnswalk"))
        self.dnswalkH4.setText(_translate("MainWindow", "RUN ON TERMINAL :"))
        self.dnswalkB3.setText(_translate("MainWindow", "root@kali:~# dnswalk example.com.\n"
"Checking example.com.\n"
"\n"
""))
        self.dnswalkB1.setText(_translate("MainWindow", "dnswalk is a DNS debugger. It performs zone transfers of specified domains, and checks the \n"
"database in numerous ways for internal consistency, as well as accuracy.\n"
"\n"
"Source: http://sourceforge.net/projects/dnswalk/\n"
"\n"
"\n"
""))
        self.dnswalkH2.setText(_translate("MainWindow", "Usage:"))
        self.dnswalkH1.setText(_translate("MainWindow", "Description:"))
        self.dnswalkB2.setText(_translate("MainWindow", "root@kali:~# dnswalk --help\n"
"\n"
"Usage: dnswalk [-OPTIONS [-MORE_OPTIONS]] [--] [PROGRAM_ARG1 ...]\n"
"\n"
"The following single-character options are accepted:\n"
"With arguments: -D\n"
"Boolean (without arguments): -r -f -i -a -d -m -F -l\n"
"\n"
"Options may be merged together. -- stops processing of options.\n"
"Space is not required between options and their arguments.\n"
"[Now continuing due to backward compatibility and excessive paranoia.\n"
"See ``perldoc Getopt::Std\'\' about $Getopt::Std::STANDARD_HELP_VERSION.]\n"
"Usage: dnswalk domain\n"
"domain MUST end with a \'.\'\n"
"\n"
"\n"
"-r     Recursively descend sub-domains of the specified domain.\n"
"-a     Turn on warning of duplicate A records.\n"
"-d     Print debugging and \'status\' information to stderr.  (Use only if redirecting stdout).\n"
"-m     Perform checks only if the zone has been modified since the previous run.\n"
"-F     Perform  \"fascist\"  checking.  When checking an A record, compare the PTR name for each IP address with the forward name and report mismatches.\n"
"-i     Suppress check for invalid characters in a domain name.\n"
"-l     Perform  \"lame  delegation\"  checking.   For every NS record, check to see that the listed host is  indeed returning authoritative answers for this domain.\n"
"\n"
"\n"
""))
        self.dnswalkH3.setText(_translate("MainWindow", "Examples:"))
        self.dnswalkB4.setText(_translate("MainWindow", "root@kali:~# dnswalk -r -d example.com.\n"
"Checking example.com.\n"
"\n"
""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dnswalkTab), _translate("MainWindow", "dnswalk"))
        self.DotDotPwnTitle.setText(_translate("MainWindow", "DotDotPwn"))
        self.DotDotPwnButton.setText(_translate("MainWindow", "./dotdotpwn.pl"))
        self.DotDotPwnH4.setText(_translate("MainWindow", "RUN ON TERMINAL :"))
        self.DotDotPwnB3.setText(_translate("MainWindow", "root@kali:~# dotdotpwn.pl -m http -h 192.168.1.1 -M GET\n"
"#################################################################################\n"
"#                                                                               #\n"
"#  CubilFelino                                                       Chatsubo   #\n"
"#  Security Research Lab              and            [(in)Security Dark] Labs   #\n"
"#  chr1x.sectester.net                             chatsubo-labs.blogspot.com   #\n"
"#                                                                               #\n"
"#                               pr0udly present:                                #\n"
"#                                                                               #\n"
"#  ________            __  ________            __  __________                   #\n"
"#  ______     ____ _/  |_______     ____ _/  |_______   __  _  __ ____    #\n"
"#   |    |    /  _ \\   __|    |    /  _ \\   __|     ___/ / / //       #\n"
"#   |    `   (  <_> )|  |  |    `   (  <_> )|  |  |    |          /|   |    #\n"
"#  /_______  / ____/ |__| /_______  / ____/ |__|  |____|      /_/ |___|  /  #\n"
"#          /                      /                                      /   #\n"
"#                               - DotDotPwn v3.0 -                              #\n"
"#                         The Directory Traversal Fuzzer                        #\n"
"#                         http://dotdotpwn.sectester.net                        #\n"
"#                            dotdotpwn@sectester.net                            #\n"
"#                                                                               #\n"
"#                               by chr1x & nitr0us                              #\n"
"#################################################################################\n"
"\n"
"[+] Report name: Reports/192.168.1.1_05-20-2014_08-41.txt\n"
"\n"
"[========== TARGET INFORMATION ==========]\n"
"[+] Hostname: 192.168.1.1\n"
"[+] Protocol: http\n"
"[+] Port: 80\n"
"\n"
"[=========== TRAVERSAL ENGINE ===========]\n"
"[+] Creating Traversal patterns (mix of dots and slashes)\n"
"[+] Multiplying 6 times the traversal patterns (-d switch)\n"
"[+] Creating the Special Traversal patterns\n"
"[+] Translating (back)slashes in the filenames\n"
"[+] Adapting the filenames according to the OS type detected (generic)\n"
"[+] Including Special sufixes\n"
"[+] Traversal Engine DONE ! - Total traversal tests created: 19680\n"
"\n"
"[=========== TESTING RESULTS ============]\n"
"[+] Ready to launch 3.33 traversals per second\n"
"[+] Press Enter to start the testing (You can stop it pressing Ctrl + C)\n"
"\n"
""))
        self.DotDotPwnB1.setText(_translate("MainWindow", "It’s a very flexible intelligent fuzzer to discover traversal directory vulnerabilities in software \n"
"such as HTTP/FTP/TFTP servers, Web platforms such as CMSs, ERPs, Blogs, etc. \n"
"\n"
"Also, it has a protocol-independent module to send the desired payload to the host and port \n"
"specified. On the other hand, it also could be used in a scripting way using the STDOUT module.\n"
"\n"
"It’s written in perl programming language and can be run either under *NIX or Windows \n"
"platforms. It’s the first Mexican tool included in BackTrack Linux (BT4 R2).\n"
"\n"
"Fuzzing modules supported in this version: \n"
"•    HTTP\n"
"•    HTTP URL\n"
"•    FTP\n"
"•    TFTP\n"
"•    Payload (Protocol independent)\n"
"•    STDOUT\n"
"\n"
"Source: https://github.com/wireghoul/dotdotpwn\n"
"\n"
"\n"
"\n"
""))
        self.DotDotPwnH2.setText(_translate("MainWindow", "Usage:"))
        self.DotDotPwnH1.setText(_translate("MainWindow", "Description:"))
        self.DotDotPwnB2.setText(_translate("MainWindow", "root@kali:~# dotdotpwn.pl\n"
"#################################################################################\n"
"#                                                                               #\n"
"#  CubilFelino                                                       Chatsubo   #\n"
"#  Security Research Lab              and            [(in)Security Dark] Labs   #\n"
"#  chr1x.sectester.net                             chatsubo-labs.blogspot.com   #\n"
"#                                                                               #\n"
"#                               pr0udly present:                                #\n"
"#                                                                               #\n"
"#  ________            __  ________            __  __________                   #\n"
"#  ______     ____ _/  |_______     ____ _/  |_______   __  _  __ ____    #\n"
"#   |    |    /  _ \\   __|    |    /  _ \\   __|     ___/ / / //       #\n"
"#   |    `   (  <_> )|  |  |    `   (  <_> )|  |  |    |          /|   |    #\n"
"#  /_______  / ____/ |__| /_______  / ____/ |__|  |____|      /_/ |___|  /  #\n"
"#          /                      /                                      /   #\n"
"#                               - DotDotPwn v3.0 -                              #\n"
"#                         The Directory Traversal Fuzzer                        #\n"
"#                         http://dotdotpwn.sectester.net                        #\n"
"#                            dotdotpwn@sectester.net                            #\n"
"#                                                                               #\n"
"#                               by chr1x & nitr0us                              #\n"
"#################################################################################\n"
"\n"
"Usage: ./dotdotpwn.pl -m <module> -h <host> [OPTIONS]\n"
"    Available options:\n"
"    -m  Module [http | http-url | ftp | tftp | payload | stdout]\n"
"    -h  Hostname\n"
"    -O  Operating System detection for intelligent fuzzing (nmap)\n"
"    -o  Operating System type if known (\"windows\", \"unix\" or \"generic\")\n"
"    -s  Service version detection (banner grabber)\n"
"    -d  Depth of traversals (e.g. deepness 3 equals to ../../../; default: 6)\n"
"    -f  Specific filename (e.g. /etc/motd; default: according to OS detected, defaults in TraversalEngine.pm)\n"
"    -E  Add @Extra_files in TraversalEngine.pm (e.g. web.config, httpd.conf, etc.)\n"
"    -S  Use SSL - for HTTP and Payload module (use https:// for in url for http-uri)\n"
"    -u  URL with the part to be fuzzed marked as TRAVERSAL (e.g. http://foo:8080/id.php?x=TRAVERSAL&y=31337)\n"
"    -k  Text pattern to match in the response (http-url & payload modules - e.g. \"root:\" if trying /etc/passwd)\n"
"    -p  Filename with the payload to be sent and the part to be fuzzed marked with the TRAVERSAL keyword\n"
"    -x  Port to connect (default: HTTP=80; FTP=21; TFTP=69)\n"
"    -t  Time in milliseconds between each test (default: 300 (.3 second))\n"
"    -X  Use the Bisection Algorithm to detect the exact deepness once a vulnerability has been found\n"
"    -e  File extension appended at the end of each fuzz string (e.g. \".php\", \".jpg\", \".inc\")\n"
"    -U  Username (default: \'anonymous\')\n"
"    -P  Password (default: \'dot@dot.pwn\')\n"
"    -M  HTTP Method to use when using the \'http\' module [GET | POST | HEAD | COPY | MOVE] (default: GET)\n"
"    -r  Report filename (default: \'HOST_MM-DD-YYYY_HOUR-MIN.txt\')\n"
"    -b  Break after the first vulnerability is found\n"
"    -q  Quiet mode (doesn\'t print each attempt)\n"
"    -C  Continue if no data was received from host\n"
""))
        self.DotDotPwnH3.setText(_translate("MainWindow", "Examples:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DotDotPwnTab), _translate("MainWindow", "DotDotPwn"))
        self.enum4linuxTitle.setText(_translate("MainWindow", "enum4linux"))
        self.enum4linuxButton.setText(_translate("MainWindow", "./enum4linux"))
        self.enum4linuxH4.setText(_translate("MainWindow", "RUN ON TERMINAL :"))
        self.enum4linuxB3.setText(_translate("MainWindow", "root@kali:~# enum4linux -U -o 192.168.1.200\n"
"Starting enum4linux v0.8.9 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Sun Aug 17 12:17:32 2014\n"
"\n"
" ==========================\n"
"|    Target Information    |\n"
" ==========================\n"
"Target ........... 192.168.1.200\n"
"RID Range ........ 500-550,1000-1050\n"
"Username ......... \'\'\n"
"Password ......... \'\'\n"
"Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none\n"
"\n"
"\n"
" ======================================================\n"
"|    Enumerating Workgroup/Domain on 192.168.1.200   |\n"
" ======================================================\n"
"[+] Got domain/workgroup name: KALI\n"
"\n"
""))
        self.enum4linuxB1.setText(_translate("MainWindow", "A Linux alternative to enum.exe for enumerating data from Windows and Samba hosts.\n"
"\n"
"Overview:\n"
"\n"
"Enum4linux is a tool for enumerating information from Windows and Samba systems. It \n"
"attempts to offer similar functionality to enum.exe formerly available from www.bindview.com.\n"
"\n"
"It is written in Perl and is basically a wrapper around the Samba tools smbclient, rpclient, net and \n"
"nmblookup.\n"
"\n"
"The tool usage can be found below followed by examples, previous versions of the tool can be \n"
"found at the bottom of the page.\n"
"\n"
"Key features:\n"
"•    RID cycling (When RestrictAnonymous is set to 1 on Windows 2000)\n"
"•    User listing (When RestrictAnonymous is set to 0 on Windows 2000)\n"
"•    Listing of group membership information\n"
"•    Share enumeration\n"
"•    Detecting if host is in a workgroup or a domain\n"
"•    Identifying the remote operating system\n"
"•    Password policy retrieval (using polenum)\n"
"\n"
"Source: https://labs.portcullis.co.uk/tools/enum4linux/\n"
"\n"
"\n"
""))
        self.enum4linuxH2.setText(_translate("MainWindow", "Usage:"))
        self.enum4linuxH1.setText(_translate("MainWindow", "Description:"))
        self.enum4linuxB2.setText(_translate("MainWindow", "root@kali:~# enum4linux -h\n"
"enum4linux v0.8.9 (http://labs.portcullis.co.uk/application/enum4linux/)\n"
"Copyright (C) 2011 Mark Lowe (mrl@portcullis-security.com)\n"
"\n"
"Simple wrapper around the tools in the samba package to provide similar\n"
"functionality to enum.exe (formerly from www.bindview.com).  Some additional\n"
"features such as RID cycling have also been added for convenience.\n"
"\n"
"Usage: ./enum4linux.pl [options] ip\n"
"\n"
"Options are (like \"enum\"):\n"
"    -U        get userlist\n"
"    -M        get machine list*\n"
"    -S        get sharelist\n"
"    -P        get password policy information\n"
"    -G        get group and member list\n"
"    -d        be detailed, applies to -U and -S\n"
"    -u user   specify username to use (default \"\")\n"
"    -p pass   specify password to use (default \"\")\n"
"\n"
"The following options from enum.exe aren\'t implemented: -L, -N, -D, -f\n"
"\n"
"Additional options:\n"
"    -a        Do all simple enumeration (-U -S -G -P -r -o -n -i).\n"
"              This opion is enabled if you don\'t provide any other options.\n"
"    -h        Display this help message and exit\n"
"    -r        enumerate users via RID cycling\n"
"    -R range  RID ranges to enumerate (default: 500-550,1000-1050, implies -r)\n"
"    -K n      Keep searching RIDs until n consective RIDs don\'t correspond to\n"
"              a username.  Impies RID range ends at 999999. Useful\n"
"          against DCs.\n"
"    -l        Get some (limited) info via LDAP 389/TCP (for DCs only)\n"
"    -s file   brute force guessing for share names\n"
"    -k user   User(s) that exists on remote system (default: administrator,guest,krbtgt,domain admins,root,bin,none)\n"
"              Used to get sid with \"lookupsid known_username\"\n"
"              Use commas to try several users: \"-k admin,user1,user2\"\n"
"    -o        Get OS information\n"
"    -i        Get printer information\n"
"    -w wrkg   Specify workgroup manually (usually found automatically)\n"
"    -n        Do an nmblookup (similar to nbtstat)\n"
"    -v        Verbose.  Shows full commands being run (net, rpcclient, etc.)\n"
"\n"
"RID cycling should extract a list of users from Windows (or Samba) hosts\n"
"which have RestrictAnonymous set to 1 (Windows NT and 2000), or \"Network\n"
"access: Allow anonymous SID/Name translation\" enabled (XP, 2003).\n"
"\n"
"NB: Samba servers often seem to have RIDs in the range 3000-3050.\n"
"\n"
"Dependancy info: You will need to have the samba package installed as this\n"
"script is basically just a wrapper around rpcclient, net, nmblookup and\n"
"smbclient.  Polenum from http://labs.portcullis.co.uk/application/polenum/\n"
"is required to get Password Policy info.\n"
"\n"
""))
        self.enum4linuxH3.setText(_translate("MainWindow", "Examples:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.enum4linuxTab), _translate("MainWindow", "enum4linux"))
        self.enumIAXTitle.setText(_translate("MainWindow", "enumIAX"))
        self.enumIAXButton.setText(_translate("MainWindow", "./enumIAX"))
        self.enumIAXH4.setText(_translate("MainWindow", "RUN ON TERMINAL :"))
        self.enumIAXB3.setText(_translate("MainWindow", "root@kali:~# enumiax -d /usr/share/wordlists/metasploit/unix_users.txt 192.168.1.1\n"
"\n"
""))
        self.enumIAXB1.setText(_translate("MainWindow", "enumIAX is an Inter Asterisk Exchange protocol username brute-force enumerator. enumIAX \n"
"may operate in two distinct modes; Sequential Username Guessing or Dictionary Attack.\n"
"\n"
"Source: http://enumiax.sourceforge.net/\n"
"\n"
"\n"
""))
        self.enumIAXH2.setText(_translate("MainWindow", "Usage:"))
        self.enumIAXH1.setText(_translate("MainWindow", "Description:"))
        self.enumIAXB2.setText(_translate("MainWindow", "root@kali:~# enumiax -h\n"
"enumIAX 0.4a\n"
"Dustin D. Trammell <dtrammell@tippingpoint.com>\n"
"\n"
"Usage: enumiax [options] target\n"
"  options:\n"
"    -d <dict>   Dictionary attack using <dict> file\n"
"    -i <count>  Interval for auto-save (# of operations, default 1000)\n"
"    -m #        Minimum username length (in characters)\n"
"    -M #        Maximum username length (in characters)\n"
"    -r #        Rate-limit calls (in microseconds)\n"
"    -s <file>   Read session state from state file\n"
"    -v          Increase verbosity (repeat for additional verbosity)\n"
"    -V          Print version information and exit\n"
"    -h          Print help/usage information and exit\n"
"\n"
""))
        self.enumIAXH3.setText(_translate("MainWindow", "Examples:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.enumIAXTab), _translate("MainWindow", "enumIAX"))
        self.FaradayTitle.setText(_translate("MainWindow", "Faraday"))
        self.FaradayButton.setText(_translate("MainWindow", "./python-faraday"))
        self.FaradayH4.setText(_translate("MainWindow", "RUN ON TERMINAL :"))
        self.FaradayB3.setText(_translate("MainWindow", ">>> WELCOME TO FARADAY\n"
"[+] Current Workspace: dev1\n"
"[+] API: OK\n"
"[faraday](dev1) kali#  nmap -oX /root/.faraday/data/devel1_Nmap_output-3.46164772371.xml -A 192.168.0.7 2>&1 | tee -a tmp.tu0ldZUG2JgzuHvLOjBYEzBx3Bu7O\n"
"\n"
"Starting Nmap 7.40 ( https://nmap.org ) at 2017-03-07 13:46 MST\n"
"Nmap scan report for pi-hole (192.168.0.7)\n"
"Host is up (0.0011s latency).\n"
"Not shown: 995 closed ports\n"
"PORT    STATE SERVICE    VERSION\n"
"22/tcp  open  ssh        OpenSSH 6.7p1 Raspbian 5+deb8u3 (protocol 2.0)\n"
"| ssh-hostkey:\n"
"|   1024 f7:5d:7c:e2:c5:46:32:19:08:e9:4b:79:5e:80:1c:83 (DSA)\n"
"|   2048 3c:f9:1d:ce:03:0f:2e:d2:17:05:77:af:81:54:32:fc (RSA)\n"
"|_  256 ea:20:d1:e0:e1:89:2c:65:9e:0d:d0:d0:e9:8b:9b:28 (ECDSA)\n"
"53/tcp  open  domain     dnsmasq 2.72\n"
"| dns-nsid:\n"
"|_  bind.version: dnsmasq-2.72\n"
"80/tcp  open  http       lighttpd 1.4.35\n"
"|_http-server-header: lighttpd/1.4.35\n"
"|_http-title: Welcome page\n"
"110/tcp open  tcpwrapped\n"
"143/tcp open  tcpwrapped\n"
"Device type: general purpose\n"
"Running: Linux 2.4.X|3.X\n"
"OS CPE: cpe:/o:linux:linux_kernel:2.4.37 cpe:/o:linux:linux_kernel:3.2\n"
"OS details: DD-WRT v24-sp2 (Linux 2.4.37), Linux 3.2\n"
"Network Distance: 2 hops\n"
"Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel\n"
"\n"
"TRACEROUTE (using port 80/tcp)\n"
"HOP RTT     ADDRESS\n"
"1   0.27 ms 172.16.206.2\n"
"2   0.21 ms pi-hole (192.168.0.7)\n"
"\n"
"OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .\n"
"Nmap done: 1 IP address (1 host up) scanned in 18.41 seconds\n"
"[faraday](devel1) kali#\n"
"\n"
"\n"
""))
        self.FaradayB1.setText(_translate("MainWindow", "Faraday introduces a new concept – IPE (Integrated Penetration-Test Environment) a multiuser \n"
"Penetration test IDE. Designed for distribution, indexation and analysis of the data generated \n"
"during a security audit.\n"
"\n"
"The main purpose of Faraday is to re-use the available tools in the community to take advantage \n"
"of them in a multiuser way.\n"
"\n"
"Designed for simplicity, users should notice no difference between their own terminal \n"
"application and the one included in Faraday. Developed with a specialized set of functionalities \n"
"that help users improve their own work. Do you remember yourself programming without an \n"
"IDE? Well, Faraday does the same as an IDE does for you when programming, but from the \n"
"perspective of a penetration test.\n"
"\n"
"Source: https://github.com/infobyte/faraday\n"
"\n"
"\n"
""))
        self.FaradayH2.setText(_translate("MainWindow", "Usage:"))
        self.FaradayH1.setText(_translate("MainWindow", "Description:"))
        self.FaradayB2.setText(_translate("MainWindow", "root@kali:~# python-faraday -h\n"
"usage: faraday.py [-h] [-n HOST] [-px PORT_XMLRPC] [-pr PORT_REST] [-d]\n"
"                  [--profile] [--profile-output PROFILE_OUTPUT]\n"
"                  [--profile-depth PROFILE_DEPTH] [--disable-excepthook]\n"
"                  [--dev-mode] [--ignore-deps] [--update] [--cert CERT_PATH]\n"
"                  [--gui GUI] [--cli] [-w WORKSPACE] [-r FILENAME]\n"
"\n"
"Faraday\'s launcher parser.\n"
"\n"
"optional arguments:\n"
"  -h, --help            show this help message and exit\n"
"  -d, --debug           Enables debug mode. Default = disabled\n"
"  --disable-excepthook  Disable the application exception hook that allows to\n"
"                        send error reports to developers.\n"
"  --dev-mode            Enable dev mode. This will use the user config and\n"
"                        plugin folder.\n"
"  --ignore-deps         Ignore python dependencies resolution.\n"
"  --update              Update Faraday IDE.\n"
"  --cert CERT_PATH      Path to the valid CouchDB certificate\n"
"  --gui GUI             Select interface to start faraday. Supported values\n"
"                        are gtk and \'no\' (no GUI at all). Defaults to GTK\n"
"  --cli                 Set this flag to avoid gui and use faraday as a cli.\n"
"  -w WORKSPACE, --workspace WORKSPACE\n"
"                        Workspace to be opened\n"
"  -r FILENAME, --report FILENAME\n"
"                        Report to be parsed by the cli\n"
"\n"
"connection:\n"
"  -n HOST, --hostname HOST\n"
"                        The hostname where both server APIs will listen\n"
"                        (XMLRPC and RESTful). Default = localhost\n"
"  -px PORT_XMLRPC, --port-xmlrpc PORT_XMLRPC\n"
"                        Sets the port where the api XMLRPCServer will listen.\n"
"                        Default = 9876\n"
"  -pr PORT_REST, --port-rest PORT_REST\n"
"                        Sets the port where the api RESTful server will\n"
"                        listen. Default = 9977\n"
"\n"
"profiling:\n"
"  --profile             Enables application profiling. When this option is\n"
"                        used --profile-output and --profile-depth can also be\n"
"                        used. Default = disabled\n"
"  --profile-output PROFILE_OUTPUT\n"
"                        Sets the profile output filename. If no value is\n"
"                        provided, standard output will be used\n"
"  --profile-depth PROFILE_DEPTH\n"
"                        Sets the profile number of entries (depth). Default =\n"
"                        500\n"
"\n"
"\n"
""))
        self.FaradayH3.setText(_translate("MainWindow", "Examples:"))
        self.FaradayB4.setText(_translate("MainWindow", "[faraday](devel1) kali#  dirb http://192.168.0.23/commix-testbed -w 2>&1 | tee -a tmp.qNejUxvvrPpbGPVEfwf8OZOuM1F1E\n"
"\n"
"-----------------\n"
"DIRB v2.22    \n"
"By The Dark Raver\n"
"-----------------\n"
"\n"
"START_TIME: Tue Mar  7 13:58:52 2017\n"
"URL_BASE: http://192.168.0.23/commix-testbed/\n"
"WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt\n"
"OPTION: Not Stoping on warning messages\n"
"\n"
"-----------------\n"
"\n"
"GENERATED WORDS: 4612                                                              \n"
"\n"
"---- Scanning URL: http://192.168.0.23/commix-testbed/ ----\n"
"                                                                                                                                                         ==> DIRECTORY: http://192.168.0.23/commix-testbed/css/                                                                                                                      \n"
"==> DIRECTORY: http://192.168.0.23/commix-testbed/fonts/                                                                                                                    \n"
"==> DIRECTORY: http://192.168.0.23/commix-testbed/img/                                                                                                                      \n"
"+ http://192.168.0.23/commix-testbed/index.php (CODE:200|SIZE:14346)                                                                                                        \n"
"==> DIRECTORY: http://192.168.0.23/commix-testbed/js/                                                                                                                        \n"
"==> DIRECTORY: http://192.168.0.23/commix-testbed/readme/                                                                                                                    \n"
"                                                                                                                                                                             \n"
"---- Entering directory: http://192.168.0.23/commix-testbed/css/ ----\n"
"(!) WARNING: Directory IS LISTABLE. No need to scan it.                        \n"
"    (Use mode \'-w\' if you want to scan it anyway)\n"
"                                                                                                                                                                             \n"
"---- Entering directory: http://192.168.0.23/commix-testbed/fonts/ ----\n"
"(!) WARNING: Directory IS LISTABLE. No need to scan it.                        \n"
"    (Use mode \'-w\' if you want to scan it anyway)\n"
"                                                                                                                                                                             \n"
"---- Entering directory: http://192.168.0.23/commix-testbed/img/ ----\n"
"(!) WARNING: Directory IS LISTABLE. No need to scan it.                        \n"
"    (Use mode \'-w\' if you want to scan it anyway)\n"
"                                                                                                                                                                             \n"
"---- Entering directory: http://192.168.0.23/commix-testbed/js/ ----\n"
"(!) WARNING: Directory IS LISTABLE. No need to scan it.                        \n"
"    (Use mode \'-w\' if you want to scan it anyway)\n"
"                                                                                                                                                                             \n"
"---- Entering directory: http://192.168.0.23/commix-testbed/readme/ ----\n"
"(!) WARNING: Directory IS LISTABLE. No need to scan it.                        \n"
"    (Use mode \'-w\' if you want to scan it anyway)\n"
"                                                                                                                                                                             \n"
"-----------------\n"
"END_TIME: Tue Mar  7 14:04:24 2017\n"
"DOWNLOADED: 27672 - FOUND: 1\n"
"\n"
"\n"
""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Faraday), _translate("MainWindow", "Faraday"))
        self.FierceTitle.setText(_translate("MainWindow", "Fierce"))
        self.FierceButton.setText(_translate("MainWindow", "./fierce"))
        self.FierceH4.setText(_translate("MainWindow", "RUN ON TERMINAL :"))
        self.FierceB3.setText(_translate("MainWindow", "root@kali:~# fierce -dns example.com\n"
"DNS Servers for example.com:\n"
"    b.iana-servers.net\n"
"    a.iana-servers.net\n"
"\n"
"Trying zone transfer first...\n"
"    Testing b.iana-servers.net\n"
"        Request timed out or transfer not allowed.\n"
"    Testing a.iana-servers.net\n"
"        Request timed out or transfer not allowed.\n"
"\n"
"Unsuccessful in zone transfer (it was worth a shot)\n"
"Okay, trying the good old fashioned way... brute force\n"
"\n"
"Checking for wildcard DNS...\n"
"Nope. Good.\n"
"Now performing 2280 test(s)...\n"
"\n"
"\n"
""))
        self.FierceB1.setText(_translate("MainWindow", "First what Fierce is not. Fierce is not an IP scanner, it is not a DDoS tool, it is not designed to \n"
"scan the whole Internet or perform any un-targeted attacks. It is meant specifically to locate \n"
"likely targets both inside and outside a corporate network. Only those targets are listed (unless \n"
"the -nopattern switch is used). No exploitation is performed (unless you do something \n"
"intentionally malicious with the -connect switch). Fierce is a reconnaissance tool. Fierce is a \n"
"PERL script that quickly scans domains (usually in just a few minutes, assuming no network lag) \n"
"using several tactics.\n"
"\n"
"Source: http://ha.ckers.org/fierce/\n"
"\n"
"\n"
"\n"
""))
        self.FierceH2.setText(_translate("MainWindow", "Usage:"))
        self.FierceH1.setText(_translate("MainWindow", "Description:"))
        self.FierceB2.setText(_translate("MainWindow", "root@kali:~# fierce -h\n"
"fierce.pl (C) Copywrite 2006,2007 - By RSnake at http://ha.ckers.org/fierce/\n"
"\n"
"    Usage: perl fierce.pl [-dns example.com] [OPTIONS]\n"
"\n"
"Overview:\n"
"    Fierce is a semi-lightweight scanner that helps locate non-contiguous\n"
"    IP space and hostnames against specified domains.  It\'s really meant\n"
"    as a pre-cursor to nmap, unicornscan, nessus, nikto, etc, since all\n"
"    of those require that you already know what IP space you are looking\n"
"    for.  This does not perform exploitation and does not scan the whole\n"
"    internet indiscriminately.  It is meant specifically to locate likely\n"
"    targets both inside and outside a corporate network.  Because it uses\n"
"    DNS primarily you will often find mis-configured networks that leak\n"
"    internal address space. That\'s especially useful in targeted malware.\n"
"\n"
"Options:\n"
"    -connect    Attempt to make http connections to any non RFC1918\n"
"        (public) addresses.  This will output the return headers but\n"
"        be warned, this could take a long time against a company with\n"
"        many targets, depending on network/machine lag.  I wouldn\'t\n"
"        recommend doing this unless it\'s a small company or you have a\n"
"        lot of free time on your hands (could take hours-days).\n"
"        Inside the file specified the text \"Host:\n"
"\" will be replaced\n"
"        by the host specified. Usage:\n"
"\n"
"    perl fierce.pl -dns example.com -connect headers.txt\n"
"\n"
"    -delay      The number of seconds to wait between lookups.\n"
"    -dns        The domain you would like scanned.\n"
"    -dnsfile    Use DNS servers provided by a file (one per line) for\n"
"                reverse lookups (brute force).\n"
"    -dnsserver  Use a particular DNS server for reverse lookups\n"
"        (probably should be the DNS server of the target).  Fierce\n"
"        uses your DNS server for the initial SOA query and then uses\n"
"        the target\'s DNS server for all additional queries by default.\n"
"    -file       A file you would like to output to be logged to.\n"
"    -fulloutput When combined with -connect this will output everything\n"
"        the webserver sends back, not just the HTTP headers.\n"
"    -help       This screen.\n"
"    -nopattern  Don\'t use a search pattern when looking for nearby\n"
"        hosts.  Instead dump everything.  This is really noisy but\n"
"        is useful for finding other domains that spammers might be\n"
"        using.  It will also give you lots of false positives,\n"
"        especially on large domains.\n"
"    -range      Scan an internal IP range (must be combined with\n"
"        -dnsserver).  Note, that this does not support a pattern\n"
"        and will simply output anything it finds.  Usage:\n"
"\n"
"    perl fierce.pl -range 111.222.333.0-255 -dnsserver ns1.example.co\n"
"\n"
"    -search     Search list.  When fierce attempts to traverse up and\n"
"        down ipspace it may encounter other servers within other\n"
"        domains that may belong to the same company.  If you supply a\n"
"        comma delimited list to fierce it will report anything found.\n"
"        This is especially useful if the corporate servers are named\n"
"        different from the public facing website.  Usage:\n"
"\n"
"    perl fierce.pl -dns examplecompany.com -search corpcompany,blahcompany\n"
"\n"
"        Note that using search could also greatly expand the number of\n"
"        hosts found, as it will continue to traverse once it locates\n"
"        servers that you specified in your search list.  The more the\n"
"        better.\n"
"    -suppress   Suppress all TTY output (when combined with -file).\n"
"    -tcptimeout Specify a different timeout (default 10 seconds).  You\n"
"        may want to increase this if the DNS server you are querying\n"
"        is slow or has a lot of network lag.\n"
"    -threads  Specify how many threads to use while scanning (default\n"
"      is single threaded).\n"
"    -traverse   Specify a number of IPs above and below whatever IP you\n"
"        have found to look for nearby IPs.  Default is 5 above and\n"
"        below.  Traverse will not move into other C blocks.\n"
"    -version    Output the version number.\n"
"    -wide       Scan the entire class C after finding any matching\n"
"        hostnames in that class C.  This generates a lot more traffic\n"
"        but can uncover a lot more information.\n"
"    -wordlist   Use a seperate wordlist (one word per line).  Usage:\n"
"\n"
"    perl fierce.pl -dns examplecompany.com -wordlist dictionary.txt\n"
"\n"
"\n"
""))
        self.FierceH3.setText(_translate("MainWindow", "Examples:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.FierceTab), _translate("MainWindow", "Fierce"))
        self.FireWalkTitle.setText(_translate("MainWindow", "Firewalk"))
        self.FireWalkButton.setText(_translate("MainWindow", "./firewalk"))
        self.FireWalkH4.setText(_translate("MainWindow", "RUN ON TERMINAL :"))
        self.FireWalkB3.setText(_translate("MainWindow", "root@kali:~# firewalk -S8079-8081  -i eth0 -n -pTCP 192.168.1.1 192.168.0.1\n"
"Firewalk 5.0 [gateway ACL scanner]\n"
"Firewalk state initialization completed successfully.\n"
"TCP-based scan.\n"
"Ramping phase source port: 53, destination port: 33434\n"
"Hotfoot through 192.168.1.1 using 192.168.0.1 as a metric.\n"
"Ramping Phase:\n"
" 1 (TTL  1): expired [192.168.1.1]\n"
"Binding host reached.\n"
"Scan bound at 2 hops.\n"
"Scanning Phase:\n"
"port 8079: *no response*\n"
"port 8080: A! open (port not listen) [192.168.0.1]\n"
"port 8081: *no response*\n"
"\n"
"Scan completed successfully.\n"
"\n"
"Total packets sent:                4\n"
"Total packet errors:               0\n"
"Total packets caught               2\n"
"Total packets caught of interest   2\n"
"Total ports scanned                3\n"
"Total ports open:                  1\n"
"Total ports unknown:               0\n"
"\n"
"\n"
""))
        self.FireWalkB1.setText(_translate("MainWindow", "Firewalk is an active reconnaissance network security tool that attempts to determine what layer \n"
"4 protocols a given IP forwarding device will pass. Firewalk works by sending out TCP or UDP \n"
"packets with a TTL one greater than the targeted gateway. If the gateway allows the traffic, it \n"
"will forward the packets to the next hop where they will expire and elicit an \n"
"ICMP_TIME_EXCEEDED message. If the gateway hostdoes not allow the traffic, it will likely \n"
"drop the packets on the floor and we will see no response.\n"
"\n"
"To get the correct IP TTL that will result in expired packets one beyond the gateway we need to \n"
"ramp up hop-counts. We do this in the same manner that traceroute works. Once we have the \n"
"gateway hopcount (at that point the scan is said to be `bound`) we can begin our scan.\n"
"\n"
"It is significant to note the fact that the ultimate destination host does not have to be reached. It \n"
"just needs to be somewhere downstream, on the other side of the gateway, from the scanning \n"
"host.\n"
"\n"
"Source: http://packetfactory.openwall.net/projects/firewalk/\n"
"\n"
"\n"
"\n"
""))
        self.FireWalkH2.setText(_translate("MainWindow", "Usage:"))
        self.FireWalkH1.setText(_translate("MainWindow", "Description:"))
        self.FireWalkB2.setText(_translate("MainWindow", "root@kali:~# firewalk -h\n"
"Firewalk 5.0 [gateway ACL scanner]\n"
"Usage : firewalk [options] target_gateway metric\n"
"           [-d 0 - 65535] destination port to use (ramping phase)\n"
"           [-h] program help\n"
"           [-i device] interface\n"
"           [-n] do not resolve IP addresses into hostnames\n"
"           [-p TCP | UDP] firewalk protocol\n"
"           [-r] strict RFC adherence\n"
"           [-S x - y, z] port range to scan\n"
"           [-s 0 - 65535] source port\n"
"           [-T 1 - 1000] packet read timeout in ms\n"
"           [-t 1 - 25] IP time to live\n"
"           [-v] program version\n"
"           [-x 1 - 8] expire vector\n"
"\n"
"\n"
""))
        self.FireWalkH3.setText(_translate("MainWindow", "Examples:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.FireWalkTab), _translate("MainWindow", "Firewalk"))
        self.fragRouteTitle.setText(_translate("MainWindow", "fragroute"))
        self.fragRouteButton.setText(_translate("MainWindow", "./fragroute"))
        self.fragRouteH4.setText(_translate("MainWindow", "RUN ON TERMINAL :"))
        self.fragRouteB3.setText(_translate("MainWindow", "root@kali:~# fragroute 192.168.1.123\n"
"fragroute: tcp_seg -> ip_frag -> ip_chaff -> order -> print\n"
"172.16.79.182.53735 > 192.168.1.123.80: S 617662291:617662291(0) win 29200\n"
"\n"
""))
        self.fragRouteB1.setText(_translate("MainWindow", "fragroute intercepts, modifies, and rewrites egress traffic destined for a specified host, \n"
"implementing most of the attacks described in the Secure Networks “Insertion, Evasion, and \n"
"Denial of Service: Eluding Network Intrusion Detection” paper of January 1998.\n"
"\n"
"It features a simple ruleset language to delay, duplicate, drop, fragment, overlap, print, reorder, \n"
"segment, source-route, or otherwise monkey with all outbound packets destined for a target host, \n"
"with minimal support for randomized or probabilistic behaviour.\n"
"\n"
"This tool was written in good faith to aid in the testing of network intrusion detection systems, \n"
"firewalls, and basic TCP/IP stack behaviour. Please do not abuse this software.\n"
"\n"
"Source: http://www.monkey.org/~dugsong/fragroute/\n"
"\n"
"\n"
"\n"
""))
        self.fragRouteH2.setText(_translate("MainWindow", "Usage:"))
        self.fragRouteH1.setText(_translate("MainWindow", "Description:"))
        self.fragRouteB2.setText(_translate("MainWindow", "root@kali:~# fragroute\n"
"Usage: fragroute [-f file] dst\n"
"Rules:\n"
"       delay first|last|random <ms>\n"
"       drop first|last|random <prob-%>\n"
"       dup first|last|random <prob-%>\n"
"       echo <string> ...\n"
"       ip_chaff dup|opt|<ttl>\n"
"       ip_frag <size> [old|new]\n"
"       ip_opt lsrr|ssrr <ptr> <ip-addr> ...\n"
"       ip_ttl <ttl>\n"
"       ip_tos <tos>\n"
"       order random|reverse\n"
"       print\n"
"       tcp_chaff cksum|null|paws|rexmit|seq|syn|<ttl>\n"
"       tcp_opt mss|wscale <size>\n"
"       tcp_seg <size> [old|new]\n"
"\n"
"root@kali:~# fragtest\n"
"Usage: fragtest TESTS ... <host>\n"
"\n"
"  where TESTS is any combination of the following (or \"all\"):\n"
"\n"
"  ping      prerequisite for all tests\n"
"  ip-opt    determine supported IP options (BROKEN)\n"
"  ip-tracert    determine path to target\n"
"  frag      try 8-byte IP fragments\n"
"  frag-new  try 8-byte fwd-overlapping IP fragments, favoring new data (BROKEN)\n"
"  frag-old  try 8-byte fwd-overlapping IP fragments, favoring old data\n"
"  frag-timeout  determine IP fragment reassembly timeout (BROKEN)\n"
"\n"
"\n"
""))
        self.fragRouteH3.setText(_translate("MainWindow", "Examples:"))
        self.fragRouteB4.setText(_translate("MainWindow", "root@kali:~# fragtest ip-tracert frag-new 192.168.1.123\n"
"ip-tracert: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
"\n"
"\n"
""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fragRouteTab), _translate("MainWindow", "fragroute"))
        self.fragRouterTitle.setText(_translate("MainWindow", "fragrouter"))
        self.fragRouterButton.setText(_translate("MainWindow", "./fragrouter"))
        self.fragRouterH4.setText(_translate("MainWindow", "RUN ON TERMINAL :"))
        self.fragRouterB3.setText(_translate("MainWindow", "root@kali:~# fragrouter -i eth0 -F1\n"
"fragrouter: frag-1: ordered 8-byte IP fragments\n"
"\n"
"\n"
""))
        self.fragRouterB1.setText(_translate("MainWindow", "Fragrouter is a network intrusion detection evasion toolkit. It implements most of the attacks \n"
"described in the Secure Networks “Insertion, Evasion, and Denial of Service: Eluding Network \n"
"Intrusion Detection” paper of January 1998.\n"
"\n"
"This program was written in the hopes that a more precise testing methodology might be applied \n"
"to the area of network intrusion detection, which is still a black art at best.\n"
"\n"
"Conceptually, fragrouter is just a one-way fragmenting router – IP packets get sent from the \n"
"attacker to the fragrouter, which transforms them into a fragmented data stream to forward to the \n"
"victim.\n"
"\n"
"Source: fragrouter README\n"
"\n"
"\n"
""))
        self.fragRouterH2.setText(_translate("MainWindow", "Usage:"))
        self.fragRouterH1.setText(_translate("MainWindow", "Description:"))
        self.fragRouterB2.setText(_translate("MainWindow", "root@kali:~# fragrouter\n"
"Version 1.6\n"
"Usage: fragrouter [-i interface] [-p] [-g hop] [-G hopcount] ATTACK\n"
"\n"
"where ATTACK is one of the following:\n"
"\n"
"-B1: base-1: normal IP forwarding\n"
"-F1: frag-1: ordered 8-byte IP fragments\n"
"-F2: frag-2: ordered 24-byte IP fragments\n"
"-F3: frag-3: ordered 8-byte IP fragments, one out of order\n"
"-F4: frag-4: ordered 8-byte IP fragments, one duplicate\n"
"-F5: frag-5: out of order 8-byte fragments, one duplicate\n"
"-F6: frag-6: ordered 8-byte fragments, marked last frag first\n"
"-F7: frag-7: ordered 16-byte fragments, fwd-overwriting\n"
"-T1: tcp-1: 3-whs, bad TCP checksum FIN/RST, ordered 1-byte segments\n"
"-T3: tcp-3: 3-whs, ordered 1-byte segments, one duplicate\n"
"-T4: tcp-4: 3-whs, ordered 1-byte segments, one overwriting\n"
"-T5: tcp-5: 3-whs, ordered 2-byte segments, fwd-overwriting\n"
"-T7: tcp-7: 3-whs, ordered 1-byte segments, interleaved null segments\n"
"-T8: tcp-8: 3-whs, ordered 1-byte segments, one out of order\n"
"-T9: tcp-9: 3-whs, out of order 1-byte segments\n"
"-C2: tcbc-2: 3-whs, ordered 1-byte segments, interleaved SYNs\n"
"-C3: tcbc-3: ordered 1-byte null segments, 3-whs, ordered 1-byte segments\n"
"-R1: tcbt-1: 3-whs, RST, 3-whs, ordered 1-byte segments\n"
"-I2: ins-2: 3-whs, ordered 1-byte segments, bad TCP checksums\n"
"-I3: ins-3: 3-whs, ordered 1-byte segments, no ACK set\n"
"-M1: misc-1: Windows NT 4 SP2 - http://www.dataprotect.com/ntfrag/\n"
"-M2: misc-2: Linux IP chains - http://www.dataprotect.com/ipchains/\n"
"\n"
"\n"
""))
        self.fragRouterH3.setText(_translate("MainWindow", "Examples:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fragRouterTab), _translate("MainWindow", "fragrouter"))
        self.GhostPhisherTitle.setText(_translate("MainWindow", "Ghost Phisher"))
        self.GhostPhisherButton.setText(_translate("MainWindow", "./ghost-phisher"))
        self.GhostPhisherH4.setText(_translate("MainWindow", "RUN ON TERMINAL :"))
        self.GhostPhisherB1.setText(_translate("MainWindow", "Ghost Phisher is a Wireless and Ethernet security auditing and attack software program written \n"
"using the Python Programming Language and the Python Qt GUI library, the program is able to \n"
"emulate access points and deploy.\n"
"\n"
"Ghost Phisher currently supports the following features:\n"
"•    HTTP Server\n"
"•    Inbuilt RFC 1035 DNS Server\n"
"•    Inbuilt RFC 2131 DHCP Server\n"
"•    Webpage Hosting and Credential Logger (Phishing)\n"
"•    Wifi Access point Emulator\n"
"•    Session Hijacking (Passive and Ethernet Modes)\n"
"•    ARP Cache Poisoning (MITM and DOS Attacks)\n"
"•    Penetration using Metasploit Bindings\n"
"•    Automatic credential logging using SQlite Database\n"
"•    Update Support\n"
"\n"
"Source: https://code.google.com/p/ghost-phisher/\n"
"\n"
"\n"
"\n"
""))
        self.GhostPhisherH2.setText(_translate("MainWindow", "Usage:"))
        self.GhostPhisherH1.setText(_translate("MainWindow", "Description:"))
        self.GhostPhisherB2.setText(_translate("MainWindow", "root@kali:~# ghost-phisher"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.GhostPhisherTab), _translate("MainWindow", "Ghost Phisher"))
        self.GoLismeroTitle.setText(_translate("MainWindow", "GoLismero"))
        self.GoLismeroButton.setText(_translate("MainWindow", "./golismero"))
        self.GoLismeroH4.setText(_translate("MainWindow", "RUN ON TERMINAL :"))
        self.GoLismeroB3.setText(_translate("MainWindow", "root@kali:~# golismero scan -i /root/port80.xml -o sub1-port80.html\n"
"\n"
"\n"
""))
        self.GoLismeroB1.setText(_translate("MainWindow", "GoLismero is an open source framework for security testing. It’s currently geared towards web \n"
"security, but it can easily be expanded to other kinds of scans.\n"
"\n"
"The most interesting features of the framework are:\n"
"•    Real platform independence. Tested on Windows, Linux, *BSD and OS X.\n"
"•    No native library dependencies. All of the framework has been written in pure Python.\n"
"•    Good performance when compared with other frameworks written in Python and other scripting languages.\n"
"•    Very easy to use.\n"
"•    Plugin development is extremely simple.\n"
"•    The framework also collects and unifies the results of well known tools: sqlmap, xsser, openvas, dnsrecon, theharvester\n"
"•    Integration with standards: CWE, CVE and OWASP.\n"
"•    Designed for cluster deployment in mind (not available yet).\n"
"\n"
"Source: https://github.com/golismero/golismero\n"
"\n"
"\n"
"\n"
""))
        self.GoLismeroH2.setText(_translate("MainWindow", "Usage:"))
        self.GoLismeroH1.setText(_translate("MainWindow", "Description:"))
        self.GoLismeroB2.setText(_translate("MainWindow", "root@kali:~# golismero -h\n"
"\n"
"/---------------------------------------------- \n"
"| GoLismero 2.0.0b3 - The Web Knife            |\n"
"| Contact: golismero.project<@>gmail.com       |\n"
"|                                              |\n"
"| Daniel Garcia Garcia a.k.a cr0hn (@ggdaniel) |\n"
"| Mario Vilas (@Mario_Vilas)                   |\n"
"----------------------------------------------/\n"
"\n"
"usage: golismero.py COMMAND [TARGETS...] [--options]\n"
"\n"
"  SCAN:\n"
"    Perform a vulnerability scan on the given targets. Optionally import\n"
"    results from other tools and write a report. The arguments that follow may\n"
"    be domain names, IP addresses or web pages.\n"
"\n"
"  PROFILES:\n"
"    Show a list of available config profiles. This command takes no arguments.\n"
"\n"
"  PLUGINS:\n"
"    Show a list of available plugins. This command takes no arguments.\n"
"\n"
"  INFO:\n"
"    Show detailed information on a given plugin. The arguments that follow are\n"
"    the plugin IDs. You can use glob-style wildcards.\n"
"\n"
"  REPORT:\n"
"    Write a report from an earlier scan. This command takes no arguments.\n"
"    To specify output files use the -o switch.\n"
"\n"
"  IMPORT:\n"
"    Import results from other tools and optionally write a report, but don\'t\n"
"    scan the targets. This command takes no arguments. To specify input files\n"
"    use the -i switch.\n"
"\n"
"  DUMP:\n"
"    Dump the database from an earlier scan in SQL format. This command takes no\n"
"    arguments. To specify output files use the -o switch.\n"
"\n"
"  UPDATE:\n"
"    Update GoLismero to the latest version. Requires Git to be installed and\n"
"    available in the PATH. This command takes no arguments.\n"
"\n"
"examples:\n"
"\n"
"  scan a website and show the results on screen:\n"
"    golismero.py scan http://www.example.com\n"
"\n"
"  grab Nmap results, scan all hosts found and write an HTML report:\n"
"    golismero.py scan -i nmap_output.xml -o report.html\n"
"\n"
"  grab results from OpenVAS and show them on screen, but don\'t scan anything:\n"
"    golismero.py import -i openvas_output.xml\n"
"\n"
"  show a list of all available configuration profiles:\n"
"    golismero.py profiles\n"
"\n"
"  show a list of all available plugins:\n"
"    golismero.py plugins\n"
"\n"
"  show information on all bruteforcer plugins:\n"
"    golismero.py info brute_*\n"
"\n"
"  dump the database from a previous scan:\n"
"    golismero.py dump -db example.db -o dump.sql\n"
"\n"
"\n"
""))
        self.GoLismeroH3.setText(_translate("MainWindow", "Examples:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.GoLismeroTab), _translate("MainWindow", "GoLismero"))
        self.goofileTitle.setText(_translate("MainWindow", "goofile"))
        self.goofileButton.setText(_translate("MainWindow", "./goofile"))
        self.goofileH4.setText(_translate("MainWindow", "RUN ON TERMINAL :"))
        self.goofileB3.setText(_translate("MainWindow", "root@kali:~# goofile -d kali.org -f pdf\n"
"\n"
"-------------------------------------\n"
"|Goofile v1.5                       |\n"
"|Coded by Thomas (G13) Richards     |\n"
"|www.g13net.com                     |\n"
"|code.google.com/p/goofile          |\n"
"-------------------------------------\n"
"\n"
"\n"
"Searching in kali.org for pdf\n"
"========================================\n"
"\n"
"Files found:\n"
"====================\n"
"\n"
"docs.kali.org/pdf/kali-book-fr.pdf\n"
"docs.kali.org/pdf/kali-book-es.pdf\n"
"docs.kali.org/pdf/kali-book-id.pdf\n"
"docs.kali.org/pdf/kali-book-de.pdf\n"
"docs.kali.org/pdf/kali-book-it.pdf\n"
"docs.kali.org/pdf/kali-book-ar.pdf\n"
"docs.kali.org/pdf/kali-book-ja.pdf\n"
"docs.kali.org/pdf/kali-book-nl.pdf\n"
"docs.kali.org/pdf/kali-book-ru.pdf\n"
"docs.kali.org/pdf/kali-book-en.pdf\n"
"docs.kali.org/pdf/kali-book-pt-br.pdf\n"
"docs.kali.org/pdf/kali-book-zh-hans.pdf\n"
"docs.kali.org/pdf/kali-book-sw.pdf\n"
"docs.kali.org/pdf/articles/kali-linux-live-usb-install-en.pdf\n"
"====================\n"
"\n"
"\n"
""))
        self.goofileB1.setText(_translate("MainWindow", "Use this tool to search for a specific file type in a given domain.\n"
"\n"
"\n"
""))
        self.goofileH2.setText(_translate("MainWindow", "Usage:"))
        self.goofileH1.setText(_translate("MainWindow", "Description:"))
        self.goofileB2.setText(_translate("MainWindow", "root@kali:~# goofile\n"
"\n"
"-------------------------------------\n"
"|Goofile v1.5                       |\n"
"|Coded by Thomas (G13) Richards     |\n"
"|www.g13net.com                     |\n"
"|code.google.com/p/goofile          |\n"
"-------------------------------------\n"
"\n"
"\n"
"Goofile 1.5\n"
"\n"
"usage: goofile options\n"
"\n"
"       -d: domain to search\n"
"\n"
"       -f: filetype (ex. pdf)\n"
"\n"
"example:./goofile.py -d test.com -f txt\n"
"\n"
"\n"
""))
        self.goofileH3.setText(_translate("MainWindow", "Examples:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.goofileTab), _translate("MainWindow", "goofile"))
        self.hping3Title.setText(_translate("MainWindow", "hping3"))
        self.hping3Button.setText(_translate("MainWindow", "./hping3"))
        self.hping3H4.setText(_translate("MainWindow", "RUN ON TERMINAL :"))
        self.hping3B3.setText(_translate("MainWindow", "root@kali:~# hping3 --traceroute -V -1 www.example.com\n"
"using eth0, addr: 192.168.1.15, MTU: 1500\n"
"HPING www.example.com (eth0 93.184.216.119): icmp mode set, 28 headers + 0 data bytes\n"
"hop=1 TTL 0 during transit from ip=192.168.1.1 name=UNKNOWN\n"
"hop=1 hoprtt=0.3 ms\n"
"hop=2 TTL 0 during transit from ip=192.168.0.1 name=UNKNOWN\n"
"hop=2 hoprtt=3.3 ms\n"
"\n"
"\n"
""))
        self.hping3B1.setText(_translate("MainWindow", "hping is a command-line oriented TCP/IP packet assembler/analyzer. The interface is inspired to \n"
"the ping(8) unix command, but hping isn’t only able to send ICMP echo requests. It supports \n"
"TCP, UDP, ICMP and RAW-IP protocols, has a traceroute mode, the ability to send files \n"
"between a covered channel, and many other features.\n"
"\n"
"While hping was mainly used as a security tool in the past, it can be used in many ways by \n"
"people that don’t care about security to test networks and hosts. A subset of the stuff you can do \n"
"using hping:\n"
"•    Firewall testing\n"
"•    Advanced port scanning\n"
"•    Network testing, using different protocols, TOS, fragmentation\n"
"•    Manual path MTU discovery\n"
"•    Advanced traceroute, under all the supported protocols\n"
"•    Remote OS fingerprinting\n"
"•    Remote uptime guessing\n"
"•    TCP/IP stacks auditing\n"
"•    hping can also be useful to students that are learning TCP/IP.\n"
"\n"
"Source: http://www.hping.org/\n"
"\n"
"\n"
"\n"
""))
        self.hping3H2.setText(_translate("MainWindow", "Usage:"))
        self.hping3H1.setText(_translate("MainWindow", "Description:"))
        self.hping3B2.setText(_translate("MainWindow", "root@kali:~# hping3 -h\n"
"usage: hping3 host [options]\n"
"  -h  --help      show this help\n"
"  -v  --version   show version\n"
"  -c  --count     packet count\n"
"  -i  --interval  wait (uX for X microseconds, for example -i u1000)\n"
"      --fast      alias for -i u10000 (10 packets for second)\n"
"      --faster    alias for -i u1000 (100 packets for second)\n"
"      --flood      sent packets as fast as possible. Don\'t show replies.\n"
"  -n  --numeric   numeric output\n"
"  -q  --quiet     quiet\n"
"  -I  --interface interface name (otherwise default routing interface)\n"
"  -V  --verbose   verbose mode\n"
"  -D  --debug     debugging info\n"
"  -z  --bind      bind ctrl+z to ttl           (default to dst port)\n"
"  -Z  --unbind    unbind ctrl+z\n"
"      --beep      beep for every matching packet received\n"
"Mode\n"
"  default mode     TCP\n"
"  -0  --rawip      RAW IP mode\n"
"  -1  --icmp       ICMP mode\n"
"  -2  --udp        UDP mode\n"
"  -8  --scan       SCAN mode.\n"
"                   Example: hping --scan 1-30,70-90 -S www.target.host\n"
"  -9  --listen     listen mode\n"
"IP\n"
"  -a  --spoof      spoof source address\n"
"  --rand-dest      random destionation address mode. see the man.\n"
"  --rand-source    random source address mode. see the man.\n"
"  -t  --ttl        ttl (default 64)\n"
"  -N  --id         id (default random)\n"
"  -W  --winid      use win* id byte ordering\n"
"  -r  --rel        relativize id field          (to estimate host traffic)\n"
"  -f  --frag       split packets in more frag.  (may pass weak acl)\n"
"  -x  --morefrag   set more fragments flag\n"
"  -y  --dontfrag   set don\'t fragment flag\n"
"  -g  --fragoff    set the fragment offset\n"
"  -m  --mtu        set virtual mtu, implies --frag if packet size > mtu\n"
"  -o  --tos        type of service (default 0x00), try --tos help\n"
"  -G  --rroute     includes RECORD_ROUTE option and display the route buffer\n"
"  --lsrr           loose source routing and record route\n"
"  --ssrr           strict source routing and record route\n"
"  -H  --ipproto    set the IP protocol field, only in RAW IP mode\n"
"ICMP\n"
"  -C  --icmptype   icmp type (default echo request)\n"
"  -K  --icmpcode   icmp code (default 0)\n"
"      --force-icmp send all icmp types (default send only supported types)\n"
"      --icmp-gw    set gateway address for ICMP redirect (default 0.0.0.0)\n"
"      --icmp-ts    Alias for --icmp --icmptype 13 (ICMP timestamp)\n"
"      --icmp-addr  Alias for --icmp --icmptype 17 (ICMP address subnet mask)\n"
"      --icmp-help  display help for others icmp options\n"
"UDP/TCP\n"
"  -s  --baseport   base source port             (default random)\n"
"  -p  --destport   [+][+]<port> destination port(default 0) ctrl+z inc/dec\n"
"  -k  --keep       keep still source port\n"
"  -w  --win        winsize (default 64)\n"
"  -O  --tcpoff     set fake tcp data offset     (instead of tcphdrlen / 4)\n"
"  -Q  --seqnum     shows only tcp sequence number\n"
"  -b  --badcksum   (try to) send packets with a bad IP checksum\n"
"                   many systems will fix the IP checksum sending the packet\n"
"                   so you\'ll get bad UDP/TCP checksum instead.\n"
"  -M  --setseq     set TCP sequence number\n"
"  -L  --setack     set TCP ack\n"
"  -F  --fin        set FIN flag\n"
"  -S  --syn        set SYN flag\n"
"  -R  --rst        set RST flag\n"
"  -P  --push       set PUSH flag\n"
"  -A  --ack        set ACK flag\n"
"  -U  --urg        set URG flag\n"
"  -X  --xmas       set X unused flag (0x40)\n"
"  -Y  --ymas       set Y unused flag (0x80)\n"
"  --tcpexitcode    use last tcp->th_flags as exit code\n"
"  --tcp-mss        enable the TCP MSS option with the given value\n"
"  --tcp-timestamp  enable the TCP timestamp option to guess the HZ/uptime\n"
"Common\n"
"  -d  --data       data size                    (default is 0)\n"
"  -E  --file       data from file\n"
"  -e  --sign       add \'signature\'\n"
"  -j  --dump       dump packets in hex\n"
"  -J  --print      dump printable characters\n"
"  -B  --safe       enable \'safe\' protocol\n"
"  -u  --end        tell you when --file reached EOF and prevent rewind\n"
"  -T  --traceroute traceroute mode              (implies --bind and --ttl 1)\n"
"  --tr-stop        Exit when receive the first not ICMP in traceroute mode\n"
"  --tr-keep-ttl    Keep the source TTL fixed, useful to monitor just one hop\n"
"  --tr-no-rtt       Don\'t calculate/show RTT information in traceroute mode\n"
"ARS packet description (new, unstable)\n"
"  --apd-send       Send the packet described with APD (see docs/APD.txt)\n"
"\n"
"\n"
""))
        self.hping3H3.setText(_translate("MainWindow", "Examples:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.hping3Tab), _translate("MainWindow", "hping3"))
        self.identUserEnumTitle.setText(_translate("MainWindow", "ident-user-enum"))
        self.identUserEnumH2.setText(_translate("MainWindow", "Usage:"))
        self.identUserEnumH3.setText(_translate("MainWindow", "Examples:"))
        self.identUserEnumH4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#39b5ff;\">RUN ON TERMINAL :</span></p></body></html>"))
        self.identUserEnumButton.setText(_translate("MainWindow", "ident-user-enum"))
        self.identUserEnumB2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">ident-user-enum</span></p><p><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">ident-user-enum.pl ip port</span><span style=\" font-size:18pt; color:#ffffff;\">[ port [ port ... ] ]<br/></span><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; color:#ffffff;\">Queries the ident service (113/TCP) to determine the OS-level user running<br/>the process listening on a given TCP port.  More than one port can be supplied.</span><span style=\" font-size:18pt;\"><br/></span></p></body></html>"))
        self.identUserEnumB3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; color:#ffffff;\">root@kali:~#</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">ident-user-enum 192.168.1.13 22 139 445</span><span style=\" font-family:\'Courier New\'; font-size:18pt;\"><br/></span><span style=\" font-size:18pt; color:#ffffff;\">ident-user-enum v1.0 ( http://pentestmonkey.net/tools/ident-user-enum )</span><span style=\" font-family:\'Courier New\'; font-size:18pt;\"><br/><br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">192.168.1.13:22     root<br/>192.168.1.13:139    root<br/>192.168.1.13:445    root</span></p></body></html>"))
        self.identUserEnumH1.setText(_translate("MainWindow", "Description:"))
        self.identUserEnumB1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; color:#ffffff;\">ident-user-enum is a simple PERL script to query the ident service (113/TCP) in order </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">to determine the owner of the process listening on each TCP port of a target system. </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">This can help to prioritise target service during a pentest (you might want to attack </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">services running as root first). Alternatively, the list of usernames gathered can be </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">used for password guessing attacks on other network services. </span></p><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Source: </span><a href=\"http://pentestmonkey.net/tools/user-enumeration/ident-user-enum\"><span style=\" font-size:18pt; text-decoration: underline; color:#ffffff;\">http://pentestmonkey.net/tools/user-enumeration/ident-user-enum</span></a></p><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Author:</span><span style=\" font-size:18pt; color:#ffffff;\"> pentestmonkey</span></p><p><span style=\" font-size:18pt;\"><br/></span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.identUserEnumTab), _translate("MainWindow", "ident-user-enum"))
        self.InTraceH3.setText(_translate("MainWindow", "Examples:"))
        self.InTraceH4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#39b5ff;\">RUN ON TERMINAL :</span></p></body></html>"))
        self.InTraceB2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">intrace</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">InTrace, version 1.5 (C)2007-2011 Robert Swiecki &lt;robert@swiecki.net&gt;</span><span style=\" font-family:\'Courier New\'; font-size:18pt;\"><br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">2014/05/20 09:59:29.627368 &lt;INFO&gt; </span></p><p><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">Usage: intrace &lt;-h hostname&gt; [-p &lt;port&gt;] [-d &lt;debuglevel&gt;] [-s &lt;payloadsize&gt;] [-6]</span><span style=\" font-size:18pt;\"><br/></span></p></body></html>"))
        self.InTraceTitle.setText(_translate("MainWindow", "InTrace"))
        self.InTraceB3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">root@kali:~#</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">intrace -h www.example.com -p 80 -s 4<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">InTrace 1.5 -- R: 93.184.216.119/80 (80) L: 192.168.1.130/51654<br/>Payload Size: 4 bytes, Seq: 0x0d6dbb02, Ack: 0x8605bff0<br/>Status: Packets sent #8</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/><br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">  #  [src addr]         [icmp src addr]    [pkt type]</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/> 1.  [192.168.1.1    ]  [93.184.216.119 ]  [ICMP_TIMXCEED]<br/> 2.  [192.168.0.1    ]  [93.184.216.119 ]  [ICMP_TIMXCEED]<br/> 3.  [  ---          ]  [  ---          ]  [NO REPLY]<br/> 4.  [64.59.184.185  ]  [93.184.216.119 ]  [ICMP_TIMXCEED]<br/> 5.  [66.163.70.25   ]  [93.184.216.119 ]  [ICMP_TIMXCEED]<br/> 6.  [66.163.64.150  ]  [93.184.216.119 ]  [ICMP_TIMXCEED]<br/> 7.  [66.163.75.117  ]  [93.184.216.119 ]  [ICMP_TIMXCEED]<br/> 8.  [206.223.119.59 ]  [93.184.216.119 ]  [ICMP_TIMXCEED]</span><span style=\" font-size:18pt;\"><br/></span></p></body></html>"))
        self.InTraceH1.setText(_translate("MainWindow", "Description:"))
        self.InTraceB1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; color:#ffffff;\">InTrace is a traceroute-like application that enables users to enumerate IP hops exploiting </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">existing TCP connections, both initiated from local network (local system) or from remote </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">hosts. It could be useful for network reconnaissance and firewall bypassing. </span></p><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Source: </span><a href=\"https://code.google.com/p/intrace/wiki/intrace\"><span style=\" font-size:18pt; text-decoration: underline; color:#ffffff;\">https://code.google.com/p/intrace/wiki/intrace</span></a></p><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Author: </span><span style=\" font-size:18pt; color:#ffffff;\">Robert Swiecki </span><span style=\" font-size:18pt;\"><br/></span></p></body></html>"))
        self.InTraceButton.setText(_translate("MainWindow", "intrace"))
        self.InTraceH2.setText(_translate("MainWindow", "Usage:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.InTraceTab), _translate("MainWindow", "InTrace"))
        self.iSMTPTitle.setText(_translate("MainWindow", "iSMTP"))
        self.iSMTPH4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#39b5ff;\">RUN ON TERMINAL :</span></p></body></html>"))
        self.iSMTPB2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">ismtp</span></p><p><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">./iSMTP.py </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">&lt;OPTIONS&gt;</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\"> Required:</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/><br/>    -f &lt;import file&gt;    </span><span style=\" font-size:18pt; color:#ffffff;\">Imports a list of SMTP servers for testing.<br/>(Cannot use with \'-h\'.)<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">    -h &lt;host&gt;       </span><span style=\" font-size:18pt; color:#ffffff;\">The target IP and port (IP:port).<br/>                (Cannot use with \'-f\'.)</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Spoofing:</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/><br/>    -i &lt;isa email&gt;      </span><span style=\" font-size:18pt; color:#ffffff;\">The ISA\'s email address.<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">    -s &lt;sndr email&gt;     </span><span style=\" font-size:18pt; color:#ffffff;\">The sender\'s email address.<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">    -r &lt;rcpt email&gt;     </span><span style=\" font-size:18pt; color:#ffffff;\">The recipient\'s email address.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/>       --sr &lt;email&gt;     </span><span style=\" font-size:18pt; color:#ffffff;\">Specifies both the sender\'s and recipient\'s email address.<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">    -S &lt;sndr name&gt;      </span><span style=\" font-size:18pt; color:#ffffff;\">The sender\'s first and last name.<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">    -R &lt;rcpt name&gt;      </span><span style=\" font-size:18pt; color:#ffffff;\">The recipient\'s first and last name.<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">       --SR &lt;name&gt;      </span><span style=\" font-size:18pt; color:#ffffff;\">Specifies both the sender\'s and recipient\'s first and last name.<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">    -m          </span><span style=\" font-size:18pt; color:#ffffff;\">Enables SMTP spoof testing</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">.<br/>    -a          </span><span style=\" font-size:18pt; color:#ffffff;\">Includes .txt attachment with spoofed email.<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\"> SMTP enumeration:</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/><br/>    -e &lt;file&gt;   </span><span style=\" font-size:18pt; color:#ffffff;\">Enable SMTP user enumeration testing and imports email list.<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">    -l &lt;1|2|3&gt;  </span><span style=\" font-size:18pt; color:#ffffff;\">Specifies enumeration type (1 = VRFY, 2 = RCPT TO, 3 = all).<br/>            (Default is 3.)<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">SMTP relay:<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/>    -i &lt;isa email&gt;  </span><span style=\" font-size:18pt; color:#ffffff;\">The ISA\'s email address.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/>    -x          </span><span style=\" font-size:18pt; color:#ffffff;\">Enables SMTP external relay testing.<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Misc:</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"><br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/>    -t &lt;secs&gt;  </span><span style=\" font-size:18pt; color:#ffffff;\">The timeout value. (Default is 10.)</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/>    -o </span><span style=\" font-size:18pt; color:#ffffff;\">Creates &quot;ismtp-results&quot; directory and writes output to<br/>            ismtp-results/smtp_&lt;service&gt;_&lt;ip&gt;(port).txt<br/></span><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; color:#ffffff;\">Note: Any combination of options is supported (e.g., enumeration, relay, both, all, etc.).</span><span style=\" font-size:18pt;\"><br/></span></p></body></html>"))
        self.iSMTPH3.setText(_translate("MainWindow", "Examples:"))
        self.iSMTPH1.setText(_translate("MainWindow", "Description:"))
        self.iSMTPB1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; color:#ffffff;\">Test for SMTP user enumeration (RCPT TO and VRFY), internal spoofing, and relay.</span></p><p><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Author: </span><span style=\" font-size:18pt; color:#ffffff;\">Alton Johnson</span><span style=\" font-size:18pt;\"><br/></span></p></body></html>"))
        self.iSMTPB3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">root@kali:~#</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">ismtp -f smtp-ips.txt -e /usr/share/wordlists/metasploit/unix_users.txt</span><span style=\" font-family:\'Courier New\'; font-size:18pt;\"><br/></span><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; color:#ffffff;\"> ---------------------------------------------------------------------<br/>  iSMTP v1.6 - SMTP Server Tester, Alton Johnson (alton.jx@gmail.com)<br/> ---------------------------------------------------------------------</span><span style=\" font-size:18pt;\"><br/><br/></span><span style=\" font-size:18pt; color:#ffffff;\">Testing SMTP server [user enumeration]: 192.168.1.25:25<br/> Emails provided for testing: 109<br/></span><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; color:#ffffff;\"> Performing SMTP VRFY test...<br/><br/> [-] 4Dgifts ------------- [ invalid ]<br/> [-] EZsetup ------------- [ invalid ]<br/> [+] ROOT ---------------- [ success ]<br/> [+] adm ----------------- [ success ]</span><span style=\" font-size:18pt;\"><br/></span></p></body></html>"))
        self.iSMTPButton.setText(_translate("MainWindow", "ismtp"))
        self.iSMTPH2.setText(_translate("MainWindow", "Usage:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.iSMTPTab), _translate("MainWindow", "iSMTP"))
        self.IbdTitle.setText(_translate("MainWindow", "Ibd"))
        self.IbdH4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#39b5ff;\">RUN ON TERMINAL :</span></p></body></html>"))
        self.IbdB2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#fafafa;\">lbd</span><span style=\" font-size:18pt; color:#fafafa;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#fafafa;\">/usr/bin/lbd [domain]</span><span style=\" font-size:18pt; color:#fafafa;\"> </span></p></body></html>"))
        self.IbdH3.setText(_translate("MainWindow", "Examples:"))
        self.IbdH1.setText(_translate("MainWindow", "Description:"))
        self.IbdB1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; color:#ffffff;\">Ibd (load balancing detector) detects if a given domain uses DNS and/or HTTP </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">Load-Balancing (via Server: and Date: header and diffs between server answers).</span></p><p><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Source:</span><a href=\"http://ge.mine.nu/code/lbd\"><span style=\" font-size:18pt; text-decoration: underline; color:#ffffff;\">http://ge.mine.nu/code/lbd</span></a></p><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Author: </span><span style=\" font-size:18pt; color:#ffffff;\">Stefan Behte</span><span style=\" font-size:18pt;\"><br/></span></p></body></html>"))
        self.IbdB3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">root@kali:~# </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">lbd example.com<br/><br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">lbd - load balancing detector 0.1 - Checks if a given domain uses load-balancing.<br/>Written by Stefan Behte (http://ge.mine.nu)<br/>Proof-of-concept! Might give false positives.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/><br/>Checking for DNS-Loadbalancing: NOT FOUND<br/>Checking for HTTP-Loadbalancing [Server]:<br/>ECS (sea/55ED)<br/>ECS (sea/1C15)<br/>FOUND</span><span style=\" font-size:18pt;\"><br/></span></p></body></html>"))
        self.IbdButton.setText(_translate("MainWindow", "lbd"))
        self.IbdH2.setText(_translate("MainWindow", "Usage:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.IbdTab), _translate("MainWindow", "Ibd"))
        self.MaltegoTeethTitle.setText(_translate("MainWindow", "Maltego Teeth"))
        self.MaltegoTeethButton.setText(_translate("MainWindow", "cat /opt/Teeth/README.txt"))
        self.MaltegoTeethH4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#39b5ff;\">RUN ON TERMINAL :</span></p></body></html>"))
        self.MaltegoTeethH2.setText(_translate("MainWindow", "Usage:"))
        self.MaltegoTeethB2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">root@kali:~# </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">cat /opt/Teeth/README.txt </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">NB NB: This runs on Kali Linux<br />=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt;\"><br /></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">#Make directory /opt/Teeth/<br />#Copy tgz to /opt/Teeth/<br />#Untar</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt;\"><br /><br /></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Load the config file called /opt/Teeth/etc/Maltego_config.mtz file into Maltego. <br />This is painless:<br />1) Open Maltego Tungsten (or Radium)<br />2) Click top left globe/sphere (Application button) <br />3) Import -&gt; Import configuration, choose /opt/Teeth/etc/Maltego_config.mtz<br /></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt;\"><br /></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:600; color:#ffffff;\">Notes</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\"><br />-----<br />Config file is in /opt/Teeth/etc/TeethConfig.txt<br />Everything can be set in the config file.<br /><br />Log file is /var/log/Teeth.log, tail -f it while you running transforms for<br />real time logs of what\'s happening.<br /><br />You can set DEBUG/INFO. DEBUG is useful for seeing progress - set in<br />/opt/Teeth/units/TeethLib.py line 26<br /></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt;\"><br /></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Look in cache/ directory. Here you find caches of:<br />1) Nmap results<br />2) Mirrors<br />3) SQLMAP results<br /><br />You need to remove cache files by hand if you no longer want them.<br />You can run housekeep/clear_cache.sh but it removes EVERYTHING.<br /><br />The WP brute transform uses Metasploit.Start Metasploit server so:<br />    msfconsole -r /opt/Teeth/static/Teeth-MSF.rc <br />It takes a while to start, so be patient.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">In /housekeep is killswitch.sh - it\'s the same as killall python.</span></p></body></html>"))
        self.MaltegoTeethH1.setText(_translate("MainWindow", "Description:"))
        self.MaltegoTeethB1.setText(_translate("MainWindow", "<html><head/><body><p><br/><span style=\" font-size:18pt; color:#ffffff;\">Maltego is a unique platform developed to deliver a clear threat picture to the environment </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">that an organization owns and operates. Maltego’s unique advantage is to demonstrate </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">the complexity and severity of single points of failure as well as trust relationships that </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">exist currently within the scope of your infrastructure. The unique perspective that Maltego </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">offers to both network and resource based entities is the aggregation of information posted </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">all over the internet – whether it’s the current configuration of a router poised on the edge </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">of your network or the current whereabouts of your Vice President on his international visits, </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">Maltego can locate, aggregate and visualize this information. Maltego offers the user with </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">unprecedented information. Information is leverage. Information is power. Information is </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">Maltego. </span></p><p><br/><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">What does Maltego do?</span></p><p><br/><span style=\" font-size:18pt; color:#ffffff;\">Maltego is a program that can be used to determine the relationships and real world links </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">between: </span></p><p><br/><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">People </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Groups of people (social networks) </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Companies </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Organizations </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Web sites </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Internet infrastructure such as: </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Domains </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">DNS names </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Netblocks </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">IP addresses </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Phrases </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Affiliations </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Documents and files </span></p><p><br/><span style=\" font-size:18pt; color:#ffffff;\">These entities are linked using open source intelligence. </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">Maltego is easy and quick to install – it uses Java, so it runs on Windows, Mac and Linux. </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">Maltego provides you with a graphical interface that makes seeing these relationships instant and </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">accurate – making it possible to see hidden connections. </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">Using the graphical user interface (GUI) you can see relationships easily – even if they are three </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">or four degrees of separation away. </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">Maltego is unique because it uses a powerful, flexible framework that makes customizing </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">possible. As such, Maltego can be adapted to your own, unique requirements. </span></p><p><br/><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">What can Maltego do for me?</span></p><p><br/><span style=\" font-size:18pt; color:#ffffff;\">Maltego can be used for the information gathering phase of all security related work. It will save </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">you time and will allow you to work more accurately and smarter. </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">Maltego aids you in your thinking process by visually demonstrating interconnected links </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">between searched items. </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">Maltego provide you with a much more powerful search, giving you smarter results. </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">If access to “hidden” information determines your success, Maltego can help you discover it. </span></p><p><br/><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Source:</span><a href=\"http://paterva.com/web6/products/maltego.php\"><span style=\" font-size:18pt; text-decoration: underline; color:#ffffff;\">http://paterva.com/web6/products/maltego.php</span></a></p><p><br/><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Author:</span><span style=\" font-size:18pt; color:#ffffff;\"> Paterva </span><br/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MaltegoTeethTab), _translate("MainWindow", "Maltego Teeth"))
        self.masscanButton.setText(_translate("MainWindow", "masscan"))
        self.masscanTitle.setText(_translate("MainWindow", "massscan"))
        self.masscanH4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#39b5ff;\">RUN ON TERMINAL :</span></p></body></html>"))
        self.masscanH2.setText(_translate("MainWindow", "Usage:"))
        self.masscanB2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">masscan</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#ffffff;\">usage:</span><span style=\" font-size:18pt;\"><br /></span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">masscan -p80,8000-8100 10.0.0.0/8 --rate=10000</span><span style=\" font-size:18pt;\"><br /></span><span style=\" font-size:18pt; color:#ffffff;\">scan some web ports on 10.x.x.x at 10kpps</span><span style=\" font-size:18pt;\"><br /></span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">masscan --nmap</span><span style=\" font-size:18pt;\"><br /></span><span style=\" font-size:18pt; color:#ffffff;\">list those options that are compatible with nmap</span><span style=\" font-size:18pt;\"><br /></span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">masscan -p80 10.0.0.0/8 --banners -oB &lt;filename&gt;</span><span style=\" font-size:18pt;\"><br /></span><span style=\" font-size:18pt; color:#ffffff;\">save results of scan in binary format to &lt;filename&gt;</span><span style=\" font-size:18pt;\"><br /></span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">masscan --open --banners --readscan &lt;filename&gt; -oX &lt;savefile&gt;</span><span style=\" font-size:18pt;\"><br /></span><span style=\" font-size:18pt; color:#ffffff;\">read binary scan results in &lt;filename&gt; and save them as xml in &lt;savefile&gt;</span><span style=\" font-size:18pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p></body></html>"))
        self.masscanB3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">root@kali:~# </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">masscan -p22,80,445 192.168.1.0/24</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600;\"><br/><br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">Starting masscan 1.0.3 (http://bit.ly/14GZzcT) at 2014-05-13 21:35:12 GMT</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600;\"><br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"> -- forced options: -sS -Pn -n --randomize-hosts -v --send-eth<br/>Initiating SYN Stealth Scan<br/>Scanning 256 hosts [3 ports/host]<br/>Discovered open port 22/tcp on 192.168.1.217<br/>Discovered open port 445/tcp on 192.168.1.220<br/>Discovered open port 80/tcp on 192.168.1.230</span><span style=\" font-size:18pt;\"><br/></span></p></body></html>"))
        self.masscanH1.setText(_translate("MainWindow", "Description:"))
        self.masscanH3.setText(_translate("MainWindow", "Examples:"))
        self.masscanB1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; color:#fcfcfc;\">This is the fastest Internet port scanner. It can scan the entire Internet in under 6 minutes, </span></p><p><span style=\" font-size:18pt; color:#fcfcfc;\">transmitting 10 million packets per second. </span></p><p><span style=\" font-size:18pt; color:#fcfcfc;\">It produces results similar to nmap, the most famous port scanner. Internally, it operates more </span></p><p><span style=\" font-size:18pt; color:#fcfcfc;\">like scanrand, unicornscan, and ZMap, using asynchronous transmission. The major difference is </span></p><p><span style=\" font-size:18pt; color:#fcfcfc;\">that it’s faster than these other scanners. In addition, it’s more flexible, allowing arbitrary address </span></p><p><span style=\" font-size:18pt; color:#fcfcfc;\">ranges and port ranges. </span></p><p><span style=\" font-size:18pt; color:#fcfcfc;\">NOTE: masscan uses a custom TCP/IP stack. Anything other than simple port scans will cause </span></p><p><span style=\" font-size:18pt; color:#fcfcfc;\">conflict with the local TCP/IP stack. This means you need to either use the -S option to use a </span></p><p><span style=\" font-size:18pt; color:#fcfcfc;\">separate IP address, or configure your operating system to firewall the ports that masscan uses. </span></p><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#fcfcfc;\">Source:</span><a href=\"https://github.com/robertdavidgraham/masscan\"><span style=\" font-size:18pt; text-decoration: underline; color:#fcfcfc;\">https://github.com/robertdavidgraham/masscan</span></a></p><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#fcfcfc;\">Author:</span><span style=\" font-size:18pt; color:#fcfcfc;\"> Robert Graham </span><span style=\" font-size:18pt;\"><br/></span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.masscanTab), _translate("MainWindow", "masscan"))
        self.MetagoofilButton.setText(_translate("MainWindow", "metagoofil"))
        self.MetagoofilTitle.setText(_translate("MainWindow", "Metagoofil"))
        self.MetagoofilH4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#39b5ff;\">RUN ON TERMINAL :</span></p></body></html>"))
        self.MetagoofilH2.setText(_translate("MainWindow", "Usage:"))
        self.MetagoofilB2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">metagoofil</span><span style=\" font-size:18pt;\">   </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#ffffff;\">Usage:</span><span style=\" font-size:18pt;\">  </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">metagoofil options</span><span style=\" font-size:18pt;\"><br /><br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">-d:</span><span style=\" font-size:18pt; color:#00b0f0;\"> </span><span style=\" font-size:18pt; color:#ffffff;\">domain to search</span><span style=\" font-size:18pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">-t:</span><span style=\" font-size:18pt; color:#00b0f0;\"> </span><span style=\" font-size:18pt; color:#ffffff;\">filetype to download (pdf,doc,xls,ppt,odp,ods,docx,xlsx,pptx)<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">-l:</span><span style=\" font-size:18pt; color:#00b0f0;\"> </span><span style=\" font-size:18pt; color:#ffffff;\">limit of results to search (default 200)<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">-h:</span><span style=\" font-size:18pt; color:#ffffff;\"> work with documents in directory (use &quot;yes&quot; for local analysis)</span><span style=\" font-size:18pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">-n:</span><span style=\" font-size:18pt; color:#00b0f0;\"> </span><span style=\" font-size:18pt; color:#ffffff;\">limit of files to download<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">-o:</span><span style=\" font-size:18pt; color:#00b0f0;\"> </span><span style=\" font-size:18pt; color:#ffffff;\">working directory (location to save downloaded files)<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">-f: </span><span style=\" font-size:18pt; color:#ffffff;\">output file</span><span style=\" font-size:18pt;\"> </span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">metagoofil.py -d apple.com -t doc,pdf -l 200 -n 50 -o applefiles -f results.html<br/>  metagoofil.py -h yes -o applefiles -f results.html (local dir analysis)</span></p><p><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">root@kali:~# </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">metagoofil -d kali.org -t pdf -l 100 -n 25 -o kalipdf -f kalipdf.html</span></p><p><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">[\'pdf\']<br/><br/>[-] Starting online search...<br/><br/>[-] Searching for pdf files, with a limit of 100<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">Searching 100 results...<br/>Results: 21 files found<br/>Starting to download 25 of them:</span><span style=\" font-size:18pt;\"><br/></span></p></body></html>"))
        self.MetagoofilH1.setText(_translate("MainWindow", "Description:"))
        self.label.setText(_translate("MainWindow", "Examples:"))
        self.MetagoofilB1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; color:#ffffff;\">Metagoofil is an information gathering tool designed for extracting metadata of public </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">documents (pdf,doc,xls,ppt,docx,pptx,xlsx) belonging to a target company. </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">Metagoofil will perform a search in Google to identify and download the documents to local disk </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">and then will extract the metadata with different libraries like Hachoir, PdfMiner? and others. </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">With the results it will generate a report with usernames, software versions and servers or </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">machine names that will help Penetration testers in the information gathering phase. </span></p><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; color:#ffffff;\">Source: </span><a href=\"http://www.edge-security.com/metagoofil.php\"><span style=\" font-size:18pt; text-decoration: underline; color:#ffffff;\">http://www.edge-security.com/metagoofil.php</span></a></p><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; color:#ffffff;\">Author: Christian Martorella </span><span style=\" font-size:18pt;\"><br/></span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MetagoofilTab), _translate("MainWindow", "Metagoofil"))
        self.MirandaB2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">miranda -h<br /><br /></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Command line usage:</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">/usr/bin/miranda [OPTIONS]<br /><br />    -s &lt;struct file&gt;    </span><span style=\" font-size:18pt; color:#ffffff;\">Load previous host data from struct file</span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">    -l &lt;log file&gt;       </span><span style=\" font-size:18pt; color:#ffffff;\">Log user-supplied commands to log file</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />    -i &lt;interface&gt;      </span><span style=\" font-size:18pt; color:#ffffff;\">Specify the name of the interface to use (Linux only, requires root)</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />    -u          </span><span style=\" font-size:18pt; color:#ffffff;\">Disable show-uniq-hosts-only option</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />    -d          </span><span style=\" font-size:18pt; color:#ffffff;\">Enable debug mode</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />    -v          </span><span style=\" font-size:18pt; color:#ffffff;\">Enable verbose mode</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />    -h          </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Show help</span><span style=\" font-size:18pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p></body></html>"))
        self.MirandaH3.setText(_translate("MainWindow", "Examples:"))
        self.MirandaH4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#39b5ff;\">RUN ON TERMINAL :</span></p></body></html>"))
        self.MirandaH1.setText(_translate("MainWindow", "Description:"))
        self.MirandaB3.setText(_translate("MainWindow", "<html><head/><body><p><br/><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">root@kali:~# </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">miranda -i eth0 -v<br/><br/>Binding to interface eth0 ...<br/><br/>Verbose mode enabled!<br/>upnp&gt; msearch<br/><br/>Entering discovery mode for \'upnp:rootdevice\', Ctl+C to stop...<br/><br/>****************************************************************<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">SSDP notification message from 192.168.1.230:80<br/>XML file is located at http://192.168.1.230:80/description.xml<br/>Device is running FreeRTOS/6.0.5, UPnP/1.0, IpBridge/0.1</span><br/></p></body></html>"))
        self.MirandaButton.setText(_translate("MainWindow", "miranda"))
        self.MirandaH2.setText(_translate("MainWindow", "Usage:"))
        self.MirandaTitle.setText(_translate("MainWindow", "Miranda"))
        self.MirandaB1.setText(_translate("MainWindow", "<html><head/><body><p><br/><span style=\" font-size:18pt; color:#ffffff;\">Miranda is a Python-based Universal Plug-N-Play client application designed to discover, query </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">and interact with UPNP devices, particularly Internet Gateway Devices (aka, routers). It can be </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">used to audit UPNP-enabled devices on a network for possible vulnerabilities. Some of its </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">features include: </span></p><p><br/><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-size:18pt; color:#ffffff;\">Interactive shell with tab completion and command history </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-size:18pt; color:#ffffff;\">Passive and active discovery of UPNP devices </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-size:18pt; color:#ffffff;\">Customizable MSEARCH queries (query for specific devices/services) </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-size:18pt; color:#ffffff;\">Full control over application settings such as IP addresses, ports and headers </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-size:18pt; color:#ffffff;\">Simple enumeration of UPNP devices, services, actions and variables </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-size:18pt; color:#ffffff;\">Correlation of input/output state variables with service actions </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-size:18pt; color:#ffffff;\">Ability to send actions to UPNP services/devices </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-size:18pt; color:#ffffff;\">Ability to save data to file for later analysis and collaboration </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-size:18pt; color:#ffffff;\">Command logging </span></p><p><br/><span style=\" font-size:18pt; color:#ffffff;\">Miranda was built on and for a Linux system and has been tested on a Linux 2.6 kernel with </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">Python 2.5. However, since it is written in Python, most functionality should be available for any </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">Python-supported platform. Miranda has been tested against IGDs from various vendors, </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">including Linksys, D-Link, Belkin and ActionTec. All Python modules came installed by default </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">on a Linux Mint 5 (Ubuntu 8.04) test system. </span></p><p><br/><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Source:</span><a href=\"https://code.google.com/p/mirandaupnptool/\"><span style=\" font-size:18pt; text-decoration: underline; color:#ffffff;\">https://code.google.com/p/mirandaupnptool/</span></a></p><p><br/><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Author: </span><span style=\" font-size:18pt; color:#ffffff;\">Craig Heffner </span></p><p><br/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MirandaTab), _translate("MainWindow", "Miranda"))
        self.nbtscanUnixwizB2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">nbtscan-unixwiz</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">nbtscan 1.0.35 - 2008-04-08 - http://www.unixwiz.net/tools/</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /><br />usage: nbtscan-unixwiz [options] target [targets...]<br /><br /> </span><span style=\" font-size:18pt; color:#ffffff;\">  Targets are lists of IP addresses, DNS names, or address<br />   ranges. Ranges can be in /nbits notation (&quot;192.168.12.0/24&quot;)<br />   or with a range in the last octet (&quot;192.168.12.64-97&quot;)</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /><br />   -V        </span><span style=\" font-size:18pt; color:#ffffff;\">show Version information<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">   -f        </span><span style=\" font-size:18pt; color:#ffffff;\">show Full NBT resource record responses (recommended)</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />   -H        </span><span style=\" font-size:18pt; color:#ffffff;\">generate HTTP headers</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />   -v       </span><span style=\" font-size:18pt; font-weight:600; color:#00b0f0;\"> </span><span style=\" font-size:18pt; color:#ffffff;\">turn on more Verbose debugging</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />   -n        </span><span style=\" font-size:18pt; color:#ffffff;\">No looking up inverse names of IP addresses responding</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />   -p &lt;n&gt;    </span><span style=\" font-size:18pt; color:#ffffff;\">bind to UDP Port &lt;n&gt; (default=0)</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />   -m        </span><span style=\" font-size:18pt; color:#ffffff;\">include MAC address in response (implied by \'-f\')</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />   -T &lt;n&gt;    </span><span style=\" font-size:18pt; color:#ffffff;\">Timeout the no-responses in &lt;n&gt; seconds (default=2 secs)</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />   -w &lt;n&gt;    </span><span style=\" font-size:18pt; color:#ffffff;\">Wait &lt;n&gt; msecs after each write (default=10 ms)</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />   -t &lt;n&gt;    </span><span style=\" font-size:18pt; color:#ffffff;\">Try each address &lt;n&gt; tries (default=1)</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />   -P        </span><span style=\" font-size:18pt; color:#ffffff;\">generate results in perl hashref format</span><span style=\" font-size:18pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p></body></html>"))
        self.nbtscanUnixwizH3.setText(_translate("MainWindow", "Examples:"))
        self.nbtscanUnixwizH4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#39b5ff;\">RUN ON TERMINAL :</span></p></body></html>"))
        self.nbtscanUnixwizH1.setText(_translate("MainWindow", "Description:"))
        self.nbtscanUnixwizB3.setText(_translate("MainWindow", "<html><head/><body><p><br/><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">root@kali:~# </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">nbtscan-unixwiz -n 192.168.0.100-110<br/>192.168.0.105   WORKGROUP\\RETROPIE              SHARING<br/>*timeout </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">(normal end of scan)</span></p><p><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">root@kali:~# </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">nbtscan-unixwiz -f 192.168.0.38<br/>192.168.0.38    WORKGROUP\\DOOKOSSEL             SHARING<br/>  DOOKOSSEL      &lt;00&gt; UNIQUE </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">Workstation Service</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br/>  DOOKOSSEL      &lt;03&gt; UNIQUE </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">Messenger Service&lt;3&gt;</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br/>  DOOKOSSEL      &lt;20&gt; UNIQUE </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">File Server Service</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br/>  ..__MSBROWSE__.&lt;01&gt; GROUP  </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">Master Browser</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br/>  WORKGROUP      &lt;00&gt; GROUP  </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">Domain Name</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br/>  WORKGROUP      &lt;1d&gt; UNIQUE </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">Master Browser</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br/>  WORKGROUP      &lt;1e&gt; GROUP  </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">Browser Service Elections</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br/>  00:00:00:00:00:00   ETHER</span><br/></p></body></html>"))
        self.nbtscanUnixwizButton.setText(_translate("MainWindow", "nbtscan-unixwiz"))
        self.nbtscanUnixwizH2.setText(_translate("MainWindow", "Usage:"))
        self.nbtscanUnixwizTitle.setText(_translate("MainWindow", "nbtscan-unixwiz"))
        self.nbtscanUnixwizB1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; color:#ffffff;\">This is a command-line tool that scans for open NETBIOS nameservers on a local or remote </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">TCP/IP network, and this is a first step in finding of open shares. It is based on the functionality </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">of the standard Windows tool nbtstat, but it operates on a range of addresses instead of just one. </span></p><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Source:</span><a href=\"http://unixwiz.net/tools/nbtscan.html\"><span style=\" font-size:18pt; text-decoration: underline; color:#ffffff;\">http://unixwiz.net/tools/nbtscan.html</span></a></p><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Author: </span><span style=\" font-size:18pt; color:#ffffff;\">Steve Friedl </span><span style=\" font-size:18pt;\"><br/></span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.nbtscanUnixwizTab), _translate("MainWindow", "nbtscan-unix"))
        self.NmapB2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">nping -h<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Nping 0.6.40 ( http://nmap.org/nping )</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Usage:</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">nping [Probe mode] [Options] {target specification}<br /><br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">TARGET SPECIFICATION:</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">  Targets may be specified as hostnames, IP addresses, networks, etc.<br />  Ex: scanme.nmap.org, microsoft.com/24, 192.168.0.1; 10.0.*.1-24</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">PROBE MODES:</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --tcp-connect                    :</span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\"> Unprivileged TCP connect probe mode.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --tcp                            : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">TCP probe mode.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --udp                            : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">UDP probe mode.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --icmp                           : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">ICMP probe mode.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --arp                            : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">ARP/RARP probe mode.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --tr, --traceroute               : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Traceroute mode (can only be used with</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />                                     </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">TCP/UDP/ICMP modes).</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">TCP CONNECT MODE:</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />   -p, --dest-port &lt;port spec&gt;     : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set destination port(s).</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />   -g, --source-port &lt;portnumber&gt;  : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Try to use a custom source</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">port.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">TCP PROBE MODE:</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />   -g, --source-port &lt;portnumber&gt;  : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set source port.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />   -p, --dest-port &lt;port spec&gt;     : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set destination port(s).</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />   --seq &lt;seqnumber&gt;               : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set sequence number.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />   --flags &lt;flag list&gt;             : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set TCP flags</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">(ACK,PSH,RST,SYN,FIN...)</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />   --ack &lt;acknumber&gt;               : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set ACK number.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />   --win &lt;size&gt;                    : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set window size.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />   --badsum                        : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Use a random invalid</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">checksum.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">UDP PROBE MODE:</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />   -g, --source-port &lt;portnumber&gt;  : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set source port.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />   -p, --dest-port &lt;port spec&gt;     : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set destination port(s).</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />   --badsum                        : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Use a random invalid checksum.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">ICMP PROBE MODE:</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --icmp-type &lt;type&gt;               : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">ICMP type.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --icmp-code &lt;code&gt;               : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">ICMP code.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --icmp-id &lt;id&gt;                   : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set identifier.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --icmp-seq &lt;n&gt;                   : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set sequence number.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --icmp-redirect-addr &lt;addr&gt;      : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set redirect address.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --icmp-param-pointer &lt;pnt&gt;       : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set parameter problem</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">pointer.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --icmp-advert-lifetime &lt;time&gt;    : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set router advertisement</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#fff7f7;\">lifetime.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --icmp-advert-entry &lt;IP,pref&gt;    : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Add router advertisement entry.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --icmp-orig-time  &lt;timestamp&gt;    : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set originate timestamp.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --icmp-recv-time  &lt;timestamp&gt;    : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set receive timestamp.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --icmp-trans-time &lt;timestamp&gt;    : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set transmit timestamp.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">ARP/RARP PROBE MODE:</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --arp-type &lt;type&gt;                : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Type: ARP, ARP-reply, RARP,</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">RARP-reply.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --arp-sender-mac &lt;mac&gt;           : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set sender MAC address.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --arp-sender-ip  &lt;addr&gt;          : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set sender IP address.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --arp-target-mac &lt;mac&gt;           : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set target MAC address.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --arp-target-ip  &lt;addr&gt;          : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set target IP address.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">IPv4 OPTIONS:</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  -S, --source-ip                  : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set source IP address.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --dest-ip &lt;addr&gt;                 : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set destination IP address</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">(used as an</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"><br />                                     </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">alternative to {target</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">specification} ).</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --tos &lt;tos&gt;                      : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set type of service field</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">(8bits).</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --id  &lt;id&gt;                       : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set identification field</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">(16 bits).</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --df                             : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set Don\'t Fragment flag.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --mf                             : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set More Fragments flag.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --ttl &lt;hops&gt;                     : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set time to live [0-255].</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --badsum-ip                      : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Use a random invalid</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">checksum.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --ip-options &lt;S|R [route]|L [route]|T|U ...&gt; : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set IP options</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --ip-options &lt;hex string&gt;                    : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set IP options</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --mtu &lt;size&gt;                     : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set MTU. Packets get</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">fragmented if MTU is<br />                                     small enough.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">IPv6 OPTIONS:</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  -6, --IPv6                       : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Use IP version 6.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --dest-ip                        : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set destination IP address</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">(used as an</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />                                     </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">alternative to {target</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">specification}).</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --hop-limit                      : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">S</span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">et hop limit (same as IPv4</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">TTL).</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --traffic-class &lt;class&gt; :        : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set traffic class.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --flow &lt;label&gt;                   : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set flow label.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">ETHERNET OPTIONS:</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --dest-mac &lt;mac&gt;                 : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set destination mac</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">address. (Disables<br />                                     ARP resolution)</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --source-mac &lt;mac&gt;               : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set source MAC address.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --ether-type &lt;type&gt;              : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set EtherType value.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">PAYLOAD OPTIONS:</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --data &lt;hex string&gt;              : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Include a custom payload.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --data-string &lt;text&gt;             : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Include a custom ASCII</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">text.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --data-length &lt;len&gt;              : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Include len random bytes as</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">payload.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">ECHO CLIENT/SERVER:</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --echo-client &lt;passphrase&gt;       : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Run Nping in client mode.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --echo-server &lt;passphrase&gt;       : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Run Nping in server mode.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --echo-port &lt;port&gt;               : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Use custom &lt;port&gt; to listen</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">or connect.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --no-crypto                      : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Disable encryption and</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">authentication.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --once                           : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Stop the server after one</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">connection.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --safe-payloads                  : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Erase application data in</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">echoed packets.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">TIMING AND PERFORMANCE:</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">  Options which take &lt;time&gt; are in seconds, or append \'ms\' (milliseconds),</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">  \'s\' (seconds), \'m\' (minutes), or \'h\' (hours) to the value (e.g. 30m, 0.25h).</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --delay &lt;time&gt;                   : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Adjust delay between probes.<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">  --rate  &lt;rate&gt;                   : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Send num packets per second.<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">MISC:<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">  -h, --help                       : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Display help information</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">.<br />  -V, --version                    : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Display current version</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">number.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  -c, --count &lt;n&gt;                  : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Stop after &lt;n&gt; rounds.<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">  -e, --interface &lt;name&gt;           : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Use supplied network interface.<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">  -H, --hide-sent                  : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Do not display sent packets.<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">  -N, --no-capture                 : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Do not try to capture replies.<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">  --privileged                     : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Assume user is fully privileged.<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">  --unprivileged                   : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Assume user lacks raw socket privileges.<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">  --send-eth                       : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Send packets at the raw Ethernet layer.<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">  --send-ip                        : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Send packets using raw IP sockets.<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">  --bpf-filter &lt;filter spec&gt;       : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Specify custom BPF filter</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">.<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">OUTPUT:</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  -v                               : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Increment verbosity level by one.<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">  -v[level]                        : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set verbosity level. E.g: -v4<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">  -d                               : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Increment debugging level by one.<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">  -d[level]                        : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set debugging level. E.g: -d3<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">  -q                               : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Decrease verbosity level by one.<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">  -q[N]                            : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Decrease verbosity level N times<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">  --quiet                          : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set verbosity and debug level to minimum.<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">  --debug                          : </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Set verbosity and debug to the max level.<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /><br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">SEE THE MAN PAGE FOR MANY MORE OPTIONS, DESCRIPTIONS, AND EXAMPLES</span><span style=\" font-size:18pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"> </span><span style=\" font-size:18pt;\"> </span></p></body></html>"))
        self.NmapH3.setText(_translate("MainWindow", "Examples:"))
        self.NmapH4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#39b5ff;\">RUN ON TERMINAL :</span></p></body></html>"))
        self.NmapH1.setText(_translate("MainWindow", "Description:"))
        self.NmapB3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">root@kali:~# </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">nmap -v -A -sV 192.168.1.1<br/><br/></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">Starting Nmap 6.45 ( http://nmap.org ) at 2014-05-13 18:40 MDT</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br/></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">NSE: Loaded 118 scripts for scanning.<br/>NSE: Script Pre-scanning</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">.<br/></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">Initiating ARP Ping Scan at 18:40</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br/>Scanning 192.168.1.1 [1 port]<br/>Completed ARP Ping Scan at 18:40, 0.06s elapsed (1 total hosts)<br/>Initiating Parallel DNS resolution of 1 host. at 18:40<br/>Completed Parallel DNS resolution of 1 host. at 18:40, 0.00s elapsed<br/></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">Initiating SYN Stealth Scan at 18:40</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br/>Scanning router.localdomain (192.168.1.1) [1000 ports]<br/>Discovered open port 53/tcp on 192.168.1.1<br/>Discovered open port 22/tcp on 192.168.1.1<br/>Discovered open port 80/tcp on 192.168.1.1<br/>Discovered open port 3001/tcp on 192.168.1.1</span></p><p><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"/></p></body></html>"))
        self.NmapButton.setText(_translate("MainWindow", "nmap"))
        self.NmapH2.setText(_translate("MainWindow", "Usage:"))
        self.NmapTitle.setText(_translate("MainWindow", "Nmap"))
        self.NmapB1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\"><br/>Nmap (“Network Mapper”) is a free and open source (license) utility for network discovery and </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">security auditing. Many systems and network administrators also find it useful for tasks such as </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">network inventory, managing service upgrade schedules, and monitoring host or service </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">uptime. Nmap uses raw IP packets in novel ways to determine what hosts are available on the </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">network, what services (application name and version) those hosts are offering, what operating </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">systems (and OS versions) they are running, what type of packet filters/firewalls are in use, and </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">dozens of other characteristics. It was designed to rapidly scan large networks, but works fine </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">against single hosts. Nmap runs on all major computer operating systems, and official binary </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">packages are available for Linux, Windows, and Mac OS X. In addition to the classic command </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">line Nmap executable, the Nmap suite includes an advanced GUI and results viewer (Zenmap), a </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">flexible data transfer, redirection, and debugging tool (Ncat), a utility for comparing scan results </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">(Ndiff), and a packet generation and response analysis tool (Nping). </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">Nmap was named “Security Product of the Year” by Linux Journal, Info World, </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">LinuxQuestions.Org, and Codetalker Digest. It was even featured in twelve movies, including </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">The Matrix Reloaded, Die Hard 4, Girl With the Dragon Tattoo, and The Bourne Ultimatum. </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">Nmap is … </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Flexible:</span><span style=\" font-size:18pt; color:#ffffff;\"> Supports dozens of advanced techniques for mapping out networks filled with IP filters, firewalls, </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">routers, and other obstacles. This includes many port scanning mechanisms (both TCP &amp; UDP),</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">OS detection, version detection, ping sweeps, and more. See the documentation page. </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Powerful:</span><span style=\" font-size:18pt; color:#ffffff;\"> Nmap has been used to scan huge networks of literally hundreds of thousands of machines. </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Portable:</span><span style=\" font-size:18pt; color:#ffffff;\"> Most operating systems are supported, including Linux, Microsoft Windows, FreeBSD, OpenBSD, </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">Solaris, IRIX, Mac OS X, HP-UX, NetBSD, Sun OS, Amiga, and more. </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Easy: </span><span style=\" font-size:18pt; color:#ffffff;\">While Nmap offers a rich set of advanced features for power users, you can start out as simply as</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">“nmap -v -A targethost”. Both traditional command line and graphical (GUI) versions are available to suit your </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">preference. Binaries are available for those who do not wish to compile Nmap from source. </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Free: </span><span style=\" font-size:18pt; color:#ffffff;\">The primary goals of the Nmap Project is to help make the Internet a little more secure and to provide </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">administrators/auditors/hackers with an advanced tool for exploring their networks. Nmap is available</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">for free download, and also comes </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">with full source code that you may modify and redistribute under the terms of the license. </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Well Documented:</span><span style=\" font-size:18pt; color:#ffffff;\"> Significant effort has been put into comprehensive and up-to-date man pages, </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">whitepapers, tutorials, and even a </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">whole book! Find them in multiple languages here. </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Supported: </span><span style=\" font-size:18pt; color:#ffffff;\">While Nmap comes with no warranty, it is well supported by a vibrant community of </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">developers and users. Most of this</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">interaction occurs on the Nmap mailing lists. Most bug reports and questions should be sent to the</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">nmap-dev list, </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">but only after you read</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">the guidelines. We recommend that all users subscribe to the low-traffic nmap-hackers announcement list. </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">You can also find Nmap on Facebook and Twitter. For real-time chat, join the #nmap channel on Freenode or </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">EFNet. </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Acclaimed:</span><span style=\" font-size:18pt; color:#ffffff;\"> Nmap has won numerous awards, including “Information Security Product of the Year” </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">by Linux Journal, Info World and </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">Codetalker Digest. It has been featured in hundreds of magazine articles, several movies, dozens of books, </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">and one comic book series. </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">Visit the press page for further details. </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Popular:</span><span style=\" font-size:18pt; color:#ffffff;\"> Thousands of people download Nmap every day, and it is included with many operating systems </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">(Redhat Linux, Debian Linux, Gentoo, FreeBSD, OpenBSD, etc). It is among the top ten (out of 30,000) </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">programs at the Freshmeat.Net repository. </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">This is important because it lends Nmap its vibrant development and user support communities. </span></p><p><span style=\" font-size:18pt; color:#ffffff;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Source:</span><a href=\"http://nmap.org/\"><span style=\" font-size:18pt; text-decoration: underline; color:#ffffff;\">http://nmap.org/</span></a></p><p><span style=\" font-size:18pt; color:#ffffff;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Author:</span><span style=\" font-size:18pt; color:#ffffff;\"> Fyodor </span></p><p><span style=\" font-size:18pt; color:#ffffff;\"><br/></span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.NmapTab), _translate("MainWindow", "Nmap"))
        self.ntopB2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">ntop -h</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"> </span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">ntop [OPTION]<br /><br /></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">Basic options:</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-h             | --help] </span><span style=\" font-family:\'Courier New\'; color:#00b0f0;\">              </span><span style=\" font-family:\'Times New Roman\'; color:#00b0f0;\">                      </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Display this help and exit</span><span style=\" font-family:\'Courier New\'; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">    [-u &lt;user&gt;      | --user &lt;user&gt;]                      </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Userid/name to run ntop under (see man page)</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-t &lt;number&gt;    | --trace-level &lt;number&gt;]             </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Trace level [0-6]</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-P &lt;path&gt;      | --db-file-path &lt;path&gt;]              </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Path for ntop internal database files</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-Q &lt;path&gt;      | --spool-file-path &lt;path&gt;]          </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\"> Path for ntop spool files</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-w &lt;port&gt;      | --http-server &lt;port&gt;]              </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\"> Web server (http:) port (or address:port) to listen on</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br /><br /></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">Advanced options:</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-4             | --ipv4]                             </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Use IPv4 connections</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-6             | --ipv6]                             </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Use IPv6 connections</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-a &lt;file&gt;      | --access-log-file &lt;file&gt;]           </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">File for ntop web server access log</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-b             | --disable-decoders]                 </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Disable protocol decoders</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-c             | --sticky-hosts]                     </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Idle hosts are not purged from memory</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-d             | --daemon]                           </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Run ntop in daemon mode</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-e &lt;number&gt;    | --max-table-rows &lt;number&gt;]          </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Maximum number of table rows to report</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-f &lt;file&gt;      | --traffic-dump-file &lt;file&gt;]         </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Traffic dump file (see tcpdump)</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-g             | --track-local-hosts]                </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Track only local hosts</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-i &lt;name&gt;      | --interface &lt;name&gt;]                 </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Interface name or names to monitor</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-j             | --create-other-packets]             </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Create file ntop-other-pkts.XXX.pcap file</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-l &lt;path&gt;      | --pcap-log &lt;path&gt;]                  </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Dump packets captured to a file (debug only!)</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-m &lt;addresses&gt; | --local-subnets &lt;addresses&gt;]        </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Local subnetwork(s) (see man page)</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-n &lt;mode&gt;      | --numeric-ip-addresses &lt;mode&gt;]      </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Numeric IP addresses DNS resolution mode:<br />                                                          0 - No DNS resolution at all<br />                                                          1 - DNS resolution for local hosts only<br />                                                          2 - DNS resolution for remote hosts only<br /></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">    [-p &lt;list&gt;      | --protocols &lt;list&gt;]                 </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">List of IP protocols to monitor (see man page)</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-q             | --create-suspicious-packets]        </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Create file ntop-suspicious-pkts.XXX.pcap file</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-r &lt;number&gt;    | --refresh-time &lt;number&gt;]            </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Refresh time in seconds, default is 120</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-s             | --no-promiscuous]                   </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Disable promiscuous mode</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-x &lt;max num hash entries&gt; ]                          </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Max num. hash entries ntop can handle (default 8192)</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-z             | --disable-sessions]                 </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Disable TCP session tracking</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-A]                                                  </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Ask admin user password and exit</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [               | --set-admin-password=&lt;pass&gt;]        </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Set password for the admin user to &lt;pass&gt;</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [               | --w3c]                              </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Add extra headers to make better html</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-B &lt;filter&gt;]   | --filter-expression                 </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Packet filter expression, like tcpdump (for all interfaces)</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />                                                          </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">You can also set per-interface filter:</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />                                                          </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">eth0=tcp,eth1=udp ....</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-C &lt;rate&gt;]     | --sampling-rate                     </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Packet capture sampling rate [default: 1 (no sampling)]</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-D &lt;name&gt;      | --domain &lt;name&gt;]                    </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Internet domain name</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-F &lt;spec&gt;      | --flow-spec &lt;specs&gt;]               </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\"> Flow specs (see man page)</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-K             | --enable-debug]                     </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Enable debug mode</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-L]                                                  </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Do logging via syslog</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [               | --use-syslog=&lt;facility&gt;]            </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Do logging via syslog, facility (\'=\' is REQUIRED)</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-M             | --no-interface-merge]               </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Don\'t merge network interfaces (see man page)</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-O &lt;path&gt;      | --pcap-file-path &lt;path&gt;]            </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Path for log files in pcap format</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-U &lt;URL&gt;       | --mapper &lt;URL&gt;]                     </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">URL (mapper.pl) for displaying host location</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-V             | --version]                          </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Output version information and exit</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [-X &lt;max num TCP sessions&gt; ]                          </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Max num. TCP sessions ntop can handle (default 32768)</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [--disable-instantsessionpurge]                       </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Disable instant FIN</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">session purge</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [--disable-mutexextrainfo]                            </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Disable extra mutex info</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [--disable-stopcap]                                   </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Capture packets even if there\'s no memory left</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [--disable-ndpi]                                      </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Disable nDPI for protocol discovery</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [--disable-python]                                    </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Disable Python interpreter</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [--instance &lt;name&gt;]                                  </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\"> Set log name for this ntop instance</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [--p3p-cp]                                            </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Set return value for p3p compact policy, header</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [--p3p-uri]                                          </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\"> Set return value for p3p policyref header</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [--skip-version-check]                                </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Skip ntop version check</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    [--known-subnets &lt;networks&gt;]                          </span><span style=\" font-family:\'Courier New\'; color:#ffffff;\">List of known subnets (separated by ,)<br />                                                          If the argument starts with @ it is assumed it is a file path<br />                                                          E.g. 192.168.0.0/14=home,172.16.0.0/16=private</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br /><br /></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">NOTE<br />    * You can configure further ntop options via the web<br />      interface [Menu Admin -&gt; Config].<br />    * The command line options are not permanent, i.e. they<br />      are not persistent across ntop initializations.</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"> </span> </p></body></html>"))
        self.ntopH3.setText(_translate("MainWindow", "Examples:"))
        self.ntopH4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#39b5ff;\">RUN ON TERMINAL :</span></p></body></html>"))
        self.ntopH1.setText(_translate("MainWindow", "Description:"))
        self.ntopB3.setText(_translate("MainWindow", "<html><head/><body><p><br/><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">root@kali:~# </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">ntop -B &quot;src host 192.168.1.1&quot;</span><br/></p></body></html>"))
        self.ntopButton.setText(_translate("MainWindow", "ntop"))
        self.ntopH2.setText(_translate("MainWindow", "Usage:"))
        self.ntopTitle.setText(_translate("MainWindow", "ntop"))
        self.ntopB1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; color:#ffffff;\">ntop is a tool that shows the network usage, similar to what the popular top Unix command does. </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">ntop is based on pcapture (ftp://ftp.ee.lbl.gov/pcapture.tar.Z) and it has been written in a portable </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">way in order to virtually run on every Unix platform. </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">ntop can be used in both interactive or web mode. In the first case, ntop displays the network </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">status on the user’s terminal whereas in web mode a web browser (e.g. netscape) can attach to </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">ntop (that acts as a web server) and get a dump of the network status. In the latter case, ntop can </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">be seen as a simple RMON-like agent with an embedded web interface. </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">ntop uses libpcap, a system-independent interface for user-level packet capture. </span></p><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Source:</span><span style=\" font-size:18pt; color:#ffffff;\"> ntop README </span></p><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Author: </span><span style=\" font-size:18pt; color:#ffffff;\">Luca Deri </span><span style=\" font-size:18pt;\"><br/></span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ntopTab), _translate("MainWindow", "ntop"))
        self.p0fB2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">p0f [ ...options... ] [ \'filter rule\' ]<br /><br /></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Network interface options:</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /><br />  -i iface  </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">- listen on the specified network interface</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  -r file   </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">- read offline pcap data from a given file</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  -p        </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">- put the listening interface in promiscuous mode</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  -L        </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">- list all available interfaces</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /><br /></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Operating mode and output settings:</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /><br />  -f file   </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">- read fingerprint database from \'file\' (p0f.fp)</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  -o file   </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">- write information to the specified log file</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  -s name   </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">- answer to API queries at a named unix socket</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  -u user   </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">- switch to the specified unprivileged account and</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">chroot</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  -d        </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">- fork into background (requires -o or -s)</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /><br /></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Performance-related options:</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /><br />  -S limit  </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">- limit number of parallel API connections (20)</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  -t c,h    </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">- set connection / host cache age limits (30s,120m)</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  -m c,h    </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">- cap the number of active connections / hosts (1000,10000)</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /><br /></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Optional filter expressions (man tcpdump) can be specified in the command<br />line to prevent p0f from looking at incidental network traffic.<br /><br />Problems? You can reach the author at &lt;lcamtuf@coredump.cx&gt;.</span><span style=\" font-size:18pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"> </span><span style=\" font-size:18pt;\"> </span></p></body></html>"))
        self.p0fH3.setText(_translate("MainWindow", "Examples:"))
        self.p0fH4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#39b5ff;\">RUN ON TERMINAL :</span></p></body></html>"))
        self.p0fH1.setText(_translate("MainWindow", "Description:"))
        self.p0fB3.setText(_translate("MainWindow", "<html><head/><body><p><br/><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">root@kali:~# </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">p0f -i eth0 -p -o /tmp/p0f.log<br/>--- p0f 3.07b by Michal Zalewski &lt;lcamtuf@coredump.cx&gt; ---<br/><br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">[+] Closed 1 file descriptor.<br/>[+] Loaded 320 signatures from \'p0f.fp\'.<br/>[+] Intercepting traffic on interface \'eth0\'.<br/>[+] Default packet filtering configured [+VLAN].<br/>[+] Log file \'/tmp/p0f.log\' opened for writing.<br/>[+] Entered main event loop.<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/>.-[ 192.168.1.15/35834 -&gt; 173.246.39.185/873 (syn) ]-<br/>|<br/>| client   = 192.168.1.15/35834<br/>| os       = Linux 2.2.x-3.x<br/>| dist     = 0<br/>| params   = generic<br/>| raw_sig  = 4:64+0:0:1460:mss*20,10:mss,sok,ts,nop,ws:df,id+:0</span></p><p><br/></p></body></html>"))
        self.p0fButton.setText(_translate("MainWindow", "p0f"))
        self.p0fH2.setText(_translate("MainWindow", "Usage:"))
        self.p0fTitle.setText(_translate("MainWindow", "p0f"))
        self.p0fB1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\"><br/></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">P0f is a tool that utilizes an array of sophisticated, purely passive traffic fingerprinting</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">mechanisms to identify the players behind any incidental TCP/IP communications (often as little</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">as a single normal SYN) without interfering in any way. Version 3 is a complete rewrite of the</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">original codebase, incorporating a significant number of improvements to network-level</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">fingerprinting, and introducing the ability to reason about application-level payloads (e.g.,</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">HTTP).</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Some of p0f’s capabilities include:</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Highly scalable and extremely fast identification of the operating system and software on both endpoints of a vanilla TCP</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">connection – especially in settings where NMap probes are blocked, too slow, unreliable, or would simply set off alarms.</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Measurement of system uptime and network hookup, distance (including topology behind NAT or packet filters), </span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">user language preferences, and so on.</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Automated detection of connection sharing / NAT, load balancing, and application-level proxying setups.</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Detection of clients and servers that forge declarative statements such as X-Mailer or User-Agent.</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">The tool can be operated in the foreground or as a daemon, and offers a simple real-time API for</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">third-party components that wish to obtain additional information about the actors they are</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">talking to.</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Common uses for p0f include reconnaissance during penetration tests; routine network</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">monitoring; detection of unauthorized network interconnects in corporate environments;</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">providing signals for abuse-prevention tools; and miscellanous forensics.</span></p><p><span style=\" font-size:18pt; color:#ffffff;\"><br/></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:600; color:#ffffff;\">Source:</span><a href=\"http://lcamtuf.coredump.cx/p0f3/\"><span style=\" font-family:\'Times New Roman\'; font-size:18pt; text-decoration: underline; color:#ffffff;\">http://lcamtuf.coredump.cx/p0f3/</span></a></p><p><span style=\" font-size:18pt; color:#ffffff;\"><br/></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:600; color:#ffffff;\">Author:</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\"> Michal Zalewski</span></p><p><span style=\" font-size:18pt; color:#ffffff;\"><br/></span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.p0fTab), _translate("MainWindow", "p0f"))
        self.ParseroB2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">parsero -h</span><span style=\" font-size:18pt; font-weight:600;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#00b0f0;\"> </span><span style=\" font-size:18pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">____<br />| _ \\ __ _ _ __ ___  ___ _ __ ___<br />| |_)/ _` | \'__/ __|/ _ \\ \'__/ _ \\<br />| __/ (_| | | \\__ \\   __/| |  (_) |<br />|_| \\__, _|_| |___/ \\___ |_| \\___/</span><span style=\" font-size:18pt; font-weight:600;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#00b0f0;\"> </span><span style=\" font-size:18pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#00b0f0;\"> </span><span style=\" font-size:18pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">usage: </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">parsero [-h] [-u URL] [-o] [-sb]</span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\"><br /></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:600; color:#ffffff;\">optional arguments:</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\"><br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">-h, </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">--help show this help message and exit</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">-u </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">URL Type the URL which will be analyz</span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">ed</span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">-o </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Show only the &quot;HTTP 200&quot; status code</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">-sb </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Search in Bing indexed Disallows</span><span style=\" font-size:18pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">  </span></p></body></html>"))
        self.ParseroH3.setText(_translate("MainWindow", "Examples:"))
        self.ParseroH4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#39b5ff;\">RUN ON TERMINAL :</span></p></body></html>"))
        self.ParseroH1.setText(_translate("MainWindow", "Description:"))
        self.ParseroB3.setText(_translate("MainWindow", "<html><head/><body><p><br/><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">root@kali:~# parsero -u www.bing.com -sb<br/><br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">Starting Parsero v0.75 (https://github.com/behindthefirewalls/Parsero) at 06/09/14 12:48:25</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">Parsero scan report for www.bing.com</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/>http://www.bing.com/travel/secure </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">301 Moved Permanently</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/>http://www.bing.com/travel/flight/flightSearchAction </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">301 Moved Permanently</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/>http://www.bing.com/travel/css </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">301 Moved Permanently</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/>http://www.bing.com/results </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">404 Not Found<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">http://www.bing.com/spbasic </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">404 Not Found</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/>http://www.bing.com/entities/search </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">302 Found</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/>http://www.bing.com/translator/? </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">200 OK</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/>http://www.bing.com/Proxy.ashx </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">404 Not Found<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">http://www.bing.com/images/search? </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">200 OK</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/>http://www.bing.com/travel/hotel/hotelSearch </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">301 Moved Permanently<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">http://www.bing.com/static/ </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">404 Not Found<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">http://www.bing.com/offers/proxy/dealsserver/api/log </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">405 Method Not Allowed<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">http://www.bing.com/shenghuo </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">301 Moved Permanently<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">http://www.bing.com/widget/render </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">200 OK</span></p><p><br/></p></body></html>"))
        self.ParseroButton.setText(_translate("MainWindow", "parsero"))
        self.ParseroH2.setText(_translate("MainWindow", "Usage:"))
        self.ParseroTitle.setText(_translate("MainWindow", "Parsero"))
        self.ParseroB1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\"><br/></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Parsero is a free script written in Python which reads the Robots.txt file of a web server and</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">looks at the Disallow entries. The Disallow entries tell the search engines what directories or</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">files hosted on a web server mustn’t be indexed. For example, “Disallow: /portal/login” means</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">that the content on www.example.com/portal/login it’s not allowed to be indexed by crawlers</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">like Google, Bing, Yahoo… This is the way the administrator have to not share sensitive or</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">private information with the search engines.</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">But sometimes these paths typed in the Disallows entries are directly accessible by the users</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">without using a search engine, just visiting the URL and the Path, and sometimes they are not</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">available to be visited by anybody… Because it is really common that the administrators write a</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">lot of Disallows and some of them are available and some of them are not, you can use Parsero in</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">order to check the HTTP status code of each Disallow entry in order to check automatically if</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">these directories are available or not.</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Also, the fact the administrator write a robots.txt, it doesn’t mean that the files or directories</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">typed in the Dissallow entries will not be indexed by Bing, Google, Yahoo… For this reason,</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Parsero is capable of searching in Bing to locate content indexed without the web administrator</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">authorization. Parsero will check the HTTP status code in the same way for each Bing result.</span></p><p><span style=\" color:#ffffff;\"><br/></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:600; color:#ffffff;\">Source:</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\"/><a href=\"https://github.com/behindthefirewalls/Parsero\"><span style=\" font-family:\'Times New Roman\'; font-size:18pt; text-decoration: underline; color:#ffffff;\">https://github.com/behindthefirewalls/Parsero</span></a></p><p><span style=\" color:#ffffff;\"><br/></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:600; color:#ffffff;\">Author:</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\"> Javier Nieto</span></p><p><br/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PareseroTab), _translate("MainWindow", "Parsero"))
        self.ReconNgB2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#ffffff;\">root@kali:~# </span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#00b0f0;\">recon-ng <br />                                                                </span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#ffffff;\">                        <br />    _/_/_/    _/_/_/_/    _/_/_/    _/_/_/    _/      _/            _/      _/    _/_/_/<br />   _/    _/  _/        _/        _/      _/  _/_/    _/            _/_/    _/  _/       <br />  _/_/_/    _/_/_/    _/        _/      _/  _/  _/  _/  _/_/_/_/  _/  _/  _/  _/  _/_/_/<br /> _/    _/  _/        _/        _/      _/  _/    _/_/            _/    _/_/  _/      _/ <br />_/    _/  _/_/_/_/    _/_/_/    _/_/_/    _/      _/            _/      _/    _/_/_/    <br />                                                                                        <br />     +---------------------------------------------------------------------------+      <br />     |  _                     ___    _                        __                 |      <br />     | |_)| _  _|_  |_|.|| _   |  _ |_ _  _ _  _ _|_o _  _   (_  _  _    _o_|_   |      <br />     | |_)|(_|(_|\\  | ||||_\\  _|_| || (_)| |||(_| | |(_)| |  __)(/_(_|_|| | | \\/ |      <br />     |                                                                        /  |      <br />     |              Consulting | Research | Development | Training               |      <br />     |                     http://www.blackhillsinfosec.com                      |      <br />     +---------------------------------------------------------------------------+ </span><span style=\" font-size:14pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#00b0f0;\"><br /><br />                      </span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#ffffff;\">[recon-ng v3.5.1, Tim Tomes (@LaNMaSteR53)]                       </span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#00b0f0;\"><br /><br />[65] Recon modules<br />[6]  Discovery modules<br />[4]  Reporting modules<br />[3]  Import modules<br />[2]  Exploitation modules<br /><br />[recon-ng][default] &gt; </span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#ffffff;\">use recon/hosts/enum/http/web/xssed</span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#00b0f0;\"><br />[recon-ng][default][xssed] &gt; </span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#ffffff;\">set DOMAIN cisco.com</span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#00b0f0;\"><br />DOMAIN =&gt; </span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#ffffff;\">cisco.com</span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#00b0f0;\"><br />[recon-ng][default][xssed] &gt; </span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#ffffff;\">run</span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#00b0f0;\"><br />[*] URL:</span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#ffffff;\"> http://xssed.com/search?key=cisco.com</span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#ffffff;\">--------------------------------------------------</span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#00b0f0;\"><br />[*] Mirror: </span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#ffffff;\">http://xssed.com/mirror/76478/</span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#00b0f0;\"><br />[*] Domain: </span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#ffffff;\">www.cisco.com</span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#00b0f0;\"><br />[*] URL: </span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#ffffff;\">http://www.cisco.com/survey/exit.html?http://xssed.com/</span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#00b0f0;\"><br />[*] Date submitted: </span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#ffffff;\">16/02/2012</span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#00b0f0;\"><br />[*] Date published:</span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#ffffff;\"> 16/02/2012</span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#00b0f0;\"><br />[*] Category: </span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#ffffff;\">Redirect</span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#00b0f0;\"><br />[*] Status: </span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#ffffff;\">UNFIXED</span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#ffffff;\">--------------------------------------------------</span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#00b0f0;\"><br />[*] Mirror: </span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#ffffff;\">http://xssed.com/mirror/76294/</span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#00b0f0;\"><br />[*] Domain: </span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#ffffff;\">developer.cisco.com</span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#00b0f0;\"><br />[*] URL: </span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#ffffff;\">http://developer.cisco.com/web/webdialer/wikidocs?p_p_id=1_WAR_wikinavigationportlet_INSTANCE_v</span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#800080;\"><br />    </span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#ffffff;\">eD7&amp;p&lt;br&gt;_p_lifecycle=0&amp;p_p_state=normal&amp;p_p_mode=view&amp;p_p_col_id=column-1&amp;p_p_col_count=1&amp;p_r_p<br />    _185834411_no&lt;br&gt;deId=803209&amp;p_r_p_185834411_title=%22%3E%3Ch1%3ECross-<br />    Site%20Scripting%20@matiaslonigro%3C/h1%3E%3Cs&lt;br&gt;cript%3Ealert%28/xss/%29%3C/script%3E</span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#00b0f0;\"><br />[*] Date submitted: </span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#ffffff;\">10/02/2012</span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#00b0f0;\"><br />[*] Date published: </span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#ffffff;\">13/02/2012</span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#00b0f0;\"><br />[*] Category: </span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#ffffff;\">XSS</span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#00b0f0;\"><br />[*] Status: </span><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#ffffff;\">UNFIXED</span><span style=\" font-size:14pt; color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:600; color:#00b0f0;\"> </span><span style=\" font-size:14pt;\"> </span></p></body></html>"))
        self.ReconNgH2.setText(_translate("MainWindow", "Usage:"))
        self.ReconNgTitle.setText(_translate("MainWindow", "Recon-ng"))
        self.ReconNgButton.setText(_translate("MainWindow", "recon-ng"))
        self.ReconNgH4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#39b5ff;\">RUN ON TERMINAL :</span></p></body></html>"))
        self.ReconNgH1.setText(_translate("MainWindow", "Description:"))
        self.ReconNgB1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\"><br/>Recon-ng is a full-featured Web Reconnaissance framework written in Python. Complete with </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">independent modules, database interaction, built in convenience functions, interactive help, </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">and command completion, Recon-ng provides a powerful environment in which open source </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">web-based reconnaissance can be conducted quickly and thoroughly. </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">Recon-ng has a look and feel similar to the Metasploit Framework, reducing the learning curve </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">for leveraging the framework. However, it is quite different. Recon-ng is not intended to </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">compete with existing frameworks, as it is designed exclusively for web-based open source </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">reconnaissance. If you want to exploit, use the Metasploit Framework. If you want to Social </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">Engineer, us the Social Engineer Toolkit. If you want to conduct reconnaissance, use Recon-ng! </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">See the Usage Guide for more information. </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">Recon-ng is a completely modular framework and makes it easy for even the newest of Python </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">developers to contribute. Each module is a subclass of the “module” class. The “module” class </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">is a customized “cmd” interpreter equipped with built-in functionality that provides simple </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">interfaces to common tasks such as standardizing output, interacting with the database, making </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">web requests, and managing API keys. Therefore, all the hard work has been done. Building </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">modules is simple and takes little more than a few minutes. See the Development Guide for </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">more information. </span></p><p><span style=\" font-size:18pt; color:#ffffff;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Source:</span><a href=\"https://bitbucket.org/LaNMaSteR53/recon-ng\"><span style=\" font-size:18pt; text-decoration: underline; color:#ffffff;\">https://bitbucket.org/LaNMaSteR53/recon-ng</span></a></p><p><span style=\" font-size:18pt; color:#ffffff;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Author: </span><span style=\" font-size:18pt; color:#ffffff;\">Tim Tomes </span></p><p><span style=\" font-size:18pt; color:#ffffff;\"><br/></span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ReconNgTab), _translate("MainWindow", "Recon-ng"))
        self.SETB2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">root@kali:~# </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">setoolkit<br /><br />            </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">:::===  :::===== :::====<br />            :::     :::      :::====<br />             =====  ======     ===<br />                === ===        ===<br />            ======  ========   ===<br /><br /><br />[---]        The Social-Engineer Toolkit (SET)         [---]<br />[---]        Created by: David Kennedy (ReL1K)         [---]<br />[---]                Version: 5.4.8                    [---]<br />[---]              Codename: \'Walkers\'                 [---]<br />[---]        Follow us on Twitter: @TrustedSec         [---]<br />[---]        Follow me on Twitter: @HackingDave        [---]<br />[---]       Homepage: https://www.trustedsec.com       [---]</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br /><br />        </span><span style=\" font-family:\'Times New Roman\'; font-weight:600; color:#ffffff;\">Welcome to the Social-Engineer Toolkit (SET).<br />             The one stop shop for all of your SE needs.<br /><br />         Join us on irc.freenode.net in channel #setoolkit<br /><br />       The Social-Engineer Toolkit is a product of TrustedSec.<br /><br />                 Visit: https://www.trustedsec.com</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br /><br /> Select from the menu:<br /><br />   1) Social-Engineering Attacks<br />   2) Fast-Track Penetration Testing<br />   3) Third Party Modules<br />   4) Update the Metasploit Framework<br />   5) Update the Social-Engineer Toolkit<br />   6) Update SET configuration<br />   7) Help, Credits, and About<br /><br />  99) Exit the Social-Engineer Toolkit<br /><br />set&gt;</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"> </span> </p></body></html>"))
        self.SETH2.setText(_translate("MainWindow", "Usage:"))
        self.SETH4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#39b5ff;\">RUN ON TERMINAL :</span></p></body></html>"))
        self.SETTitle.setText(_translate("MainWindow", "SET"))
        self.SETH1.setText(_translate("MainWindow", "Description:"))
        self.SETButton.setText(_translate("MainWindow", "set"))
        self.SETB1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\"><br/></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">The Social-Engineer Toolkit is an open-source penetration testing framework designed for</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Social-Engineering. SET has a number of custom attack vectors that allow you to make a</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">believable attack in a fraction of the time.</span></p><p><span style=\" font-size:18pt; color:#ffffff;\"><br/></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:600; color:#ffffff;\">Source:</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\"/><a href=\"https://github.com/trustedsec/social-engineer-toolkit/\"><span style=\" font-family:\'Times New Roman\'; font-size:18pt; text-decoration: underline; color:#ffffff;\">https://github.com/trustedsec/social-engineer-toolkit/</span></a></p><p><span style=\" font-size:18pt; color:#ffffff;\"><br/></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:600; color:#ffffff;\">Author:</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\"> David Kennedy, TrustedSec, LLC</span></p><p><span style=\" font-size:18pt; color:#ffffff;\"><br/></span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SETTab), _translate("MainWindow", "SET"))
        self.smtpUserEnumB2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">smtp-user-enum -h<br /></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">smtp-user-enum v1.2 ( http://pentestmonkey.net/tools/smtp-user-enum )</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /><br /></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:600; color:#ffffff;\">Usage:</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">smtp-user-enum.pl [options] </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">( -u username | -U file-of-usernames ) ( -t host | -T file-of-targets )<br /><br /></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:600; color:#ffffff;\">options are:</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />    -m n     </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Maximum number of processes (default: 5)</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />    -M </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">mode  Method to use for username guessing EXPN, VRFY or</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">RCPT (default: VRFY)</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />    -u </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">user  Check if user exists on remote system</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />    -f </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">addr  MAIL FROM email address.  Used only in &quot;RCPT TO&quot; mode (default: user@example.com)</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />    -D </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">dom   Domain to append to supplied user list to make email addresses (Default: none)</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />                 </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Use this option when you want to guess valid email addresses instead of just usernames<br />                         e.g. &quot;-D example.com&quot; would guess foo@example.com, bar@example.com, etc.  Instead of<br />                          simply the usernames foo and bar.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />    -U file  </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">File of usernames to check via smtp service</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />    -t host  </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Server host running smtp service</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />    -T file  </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">File of hostnames running the smtp service</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />    -p port  </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">TCP port on which smtp service runs (default: 25)</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />    -d       </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Debugging output</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />    -t n     </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Wait a maximum of n seconds for reply (default: 5)</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />    -v       </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Verbose</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />    -h       </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">This help message</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /><br /></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Also see smtp-user-enum-user-docs.pdf from the smtp-user-enum tar ball.</span><span style=\" font-size:18pt;\"> </span></p></body></html>"))
        self.smtpUserEnumH2.setText(_translate("MainWindow", "Usage:"))
        self.smtpUserEnumTitle.setText(_translate("MainWindow", "smtp-user-enum"))
        self.smtpUserEnumButton.setText(_translate("MainWindow", "smtp-user-enum"))
        self.smtpUserEnumH4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#39b5ff;\">RUN ON TERMINAL :</span></p></body></html>"))
        self.smtpUserEnumB3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">$</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"> smtp-user-enum.pl -M VRFY -U users.txt -t 10.0.0.1<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">$</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"> smtp-user-enum.pl -M EXPN -u admin1 -t 10.0.0.1<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">$</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"> smtp-user-enum.pl -M RCPT -U users.txt -T mail-server-ips.txt<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">$</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"> smtp-user-enum.pl -M EXPN -D example.com -U users.txt -t 10.0.0.1</span></p><p><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">root@kali:~# </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">smtp-user-enum -M VRFY -u root -t 192.168.1.25<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">Starting smtp-user-enum v1.2 ( http://pentestmonkey.net/tools/smtp-user-enum )</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/><br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">----------------------------------------------------------<br/>|                   Scan Information                       |<br/> ----------------------------------------------------------</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/><br/>Mode ..................... VRFY<br/>Worker Processes ......... 5<br/>Target count ............. 1<br/>Username count ........... 1<br/>Target TCP port .......... 25<br/>Query timeout ............ 5 secs<br/>Target domain ............<br/><br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">######## Scan started at Tue May 13 16:06:28 2014 #########</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/>192.168.1.25: root exists<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">######## Scan completed at Tue May 13 16:06:29 2014 #########</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/>1 results.<br/><br/>1 queries in 1 seconds (1.0 queries / sec)</span></p><p><br/></p></body></html>"))
        self.smtpUserEnumH1.setText(_translate("MainWindow", "Description:"))
        self.smtpUserEnumB1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\"><br/></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">smtp-user-enum is a tool for enumerating OS-level user accounts on Solaris via the SMTP</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">service (sendmail). Enumeration is performed by inspecting the responses to VRFY, EXPN and</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">RCPT TO commands. It could be adapted to work against other vulnerable SMTP daemons, but</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">this hasn’t been done as of v1.0.</span></p><p><span style=\" font-size:18pt; color:#ffffff;\"><br/></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:600; color:#ffffff;\">Source:</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\"> http://pentestmonkey.net/tools/user-enumeration/smtp-user-enum</span></p><p><span style=\" font-size:18pt; color:#ffffff;\"><br/></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:600; color:#ffffff;\">Author: </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">pentestmonkey</span></p><p><span style=\" font-size:18pt; color:#ffffff;\"><br/></span></p></body></html>"))
        self.smtpUserEnumH3.setText(_translate("MainWindow", "Examples:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.smtpUserEnumTab), _translate("MainWindow", "smtp-user-enum"))
        self.snmpCheckH2.setText(_translate("MainWindow", "Usage:"))
        self.snmpCheckTitle.setText(_translate("MainWindow", "snmp-check"))
        self.snmpCheckButton.setText(_translate("MainWindow", "snmp-check"))
        self.snmpCheckH4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#39b5ff;\">RUN ON TERMINAL :</span></p></body></html>"))
        self.snmpCheckB3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">root@kali:~# </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">snmp-check -t 192.168.1.2 -c public<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">snmpcheck v1.8 - SNMP enumerator<br/>Copyright (c) 2005-2011 by Matteo Cantoni (www.nothink.org)</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/><br/> [*] Try to connect to 192.168.1.2<br/> [*] Connected to 192.168.1.2<br/> [*] Starting enumeration at 2014-05-13 16:16:22<br/><br/> [*] System information</span><span style=\" font-size:18pt;\"/></p><p><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"/><span style=\" font-size:18pt;\"/></p></body></html>"))
        self.snmpCheckH1.setText(_translate("MainWindow", "Description:"))
        self.snmpCheckB1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\"><br/></span><span style=\" font-size:18pt; color:#ffffff;\">Like to snmpwalk, snmp-check allows you to enumerate the SNMP devices and places the </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">output in a very human readable friendly format. It could be useful for penetration testing or </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">systems monitoring. Distributed under GPL license and based on “Athena-2k” script by jshaw. </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">Features </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">snmp-check supports the following enumerations: </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">contact </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">description </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">detect write access (separate action by enumeration) </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">devices </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">domain </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">hardware and storage informations </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">hostname </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">IIS statistics </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">IP forwarding </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">listening UDP ports </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">location </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">motd </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">mountpoints </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">network interfaces </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">network services </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">processes </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">routing information </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">software components </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">system uptime </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">TCP connections </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">total memory </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">uptime </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; font-weight:600; color:#ffffff;\">·</span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">user accounts </span></p><p><span style=\" color:#ffffff;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Source:</span><span style=\" font-size:18pt; color:#ffffff;\"> http://www.nothink.org/codes/snmpcheck/index.php </span></p><p><span style=\" color:#ffffff;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Author:</span><span style=\" font-size:18pt; color:#ffffff;\"> Matteo Cantoni </span></p><p><br/></p></body></html>"))
        self.snmpCheckH3.setText(_translate("MainWindow", "Examples:"))
        self.snmpCheckB2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">snmp-check -h<br /></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">snmpcheck v1.8 - SNMP enumerator<br />Copyright (c) 2005-2011 by Matteo Cantoni (www.nothink.org)</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /><br /> </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Usage: </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">snmpcheck -t &lt;IP address&gt;<br /><br />    -t : </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">target host;</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /><br />    -p : </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">SNMP port; default port is 161;</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />    -c : </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">SNMP community; default is public;<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">    -v : </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">SNMP version (1,2); default is 1;</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />    -r : </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">request retries; default is 0;</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /><br />    -w : </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">detect write access (separate action by enumeration);</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /><br />    -d : </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">disable \'TCP connections\' enumeration!</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />    -T : </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">force timeout in seconds; default is 20. Max is 60;</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />    -D : </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">enable debug;</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />    -h : </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">show help menu;</span><span style=\" font-size:18pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"> </span><span style=\" font-size:18pt;\"> </span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.snmpChecktab), _translate("MainWindow", "snmp-check"))
        self.spartaH2.setText(_translate("MainWindow", "Usage:"))
        self.spartaH4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#39b5ff;\">RUN ON TERMINAL :</span></p></body></html>"))
        self.spartaTitle.setText(_translate("MainWindow", "SPARTA"))
        self.spartaButton.setText(_translate("MainWindow", "sparta"))
        self.spartaB2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">$ sparta</span><span style=\" font-size:18pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"> </span><span style=\" font-size:18pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">[+] Creating temporary files..</span><span style=\" font-size:18pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">[+] Wordlist was created/opened: /tmp/sparta-lQq6jS-tool-output/sparta-usernames.txt</span><span style=\" font-size:18pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">[+] Wordlist was created/opened: /tmp/sparta-lQq6jS-tool-output/sparta-passwords.txt</span><span style=\" font-size:18pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">[+] Loading settings file..</span><span style=\" font-size:18pt;\"> </span></p></body></html>"))
        self.spartaB1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\"><br/></span><span style=\" font-size:18pt; color:#ffffff;\">SPARTA is a python GUI application that simplifies network infrastructure penetration testing </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">by aiding the penetration tester in the scanning and enumeration phase. It allows the tester to </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">save time by having point-and-click access to their toolkit and by displaying all tool output in a </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">convenient way. If less time is spent setting up commands and tools, more time can be spent </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">focusing on analysing results. </span></p><p><span style=\" color:#ffffff;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Source:</span><a href=\"http://sparta.secforce.com/\"><span style=\" font-size:18pt; text-decoration: underline; color:#ffffff;\">http://sparta.secforce.com/</span></a></p><p><span style=\" color:#ffffff;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Author:</span><span style=\" font-size:18pt; color:#ffffff;\"> SECFORCE (Antonio Quina and Leonidas Stavliotis) </span></p><p><br/></p></body></html>"))
        self.spartaH1.setText(_translate("MainWindow", "Description:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.spartaTab), _translate("MainWindow", "SPARTA"))
        self.sslcauditH2.setText(_translate("MainWindow", "Usage:"))
        self.sslcauditH4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#39b5ff;\">RUN ON TERMINAL :</span></p></body></html>"))
        self.sslcauditTitle.setText(_translate("MainWindow", "sslcaudit"))
        self.sslcauditButton.setText(_translate("MainWindow", "sslcaudit"))
        self.sslcauditB2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">sslcaudit -h</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:600; color:#ffffff;\">Usage:</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">sslcaudit [OPTIONS]<br /><br />Options:<br />  --version             </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">show program\'s version number and exit</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  -h, --help            </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">show this help message and exit</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  -l LISTEN_ON          </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Specify IP address and TCP PORT to</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">listen on, in format of HOST:PORT. Default is</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">0.0.0.0:8443</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  -m MODULES            </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Launch specific modules. For     now the only functional<br />                                module is \'sslcert\'. There is also \'dummy\' module used<br />                                for internal testing or as a template code for new<br />                                modules. Default is sslcert</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  -v VERBOSE            </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Increase verbosity level. Default is 0. Try 1.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  -d DEBUG_LEVEL      </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">  Set debug level. Default is 0, which disables debugging output. Try 1 to enable it.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  -c NCLIENTS           </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Number of clients to handle before quitting. By default sslcaudit will quit as soon as it gets one<br />                                client fully processed.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  -N TEST_NAME         </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\"> Set the name of the test. If specified will appear in the leftmost column in the output.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  -T SELF_TEST          </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Launch self-test. 0 - plain TCP client,</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">1 - CN verifying client, 2 - curl.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --user-cn=USER_CN     </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Set user-specified CN.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --server=SERVER       </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Where to fetch the server certificate from, in HOST:PORT format.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --user-cert=USER_CERT_FILE<br />                        </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Set path to file containing the user-supplied certificate.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --user-key=USER_KEY_FILE<br />                        </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Set path to file containing the user-supplied key.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --user-ca-cert=USER_CA_CERT_FILE<br />                        </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Set path to file containing certificate</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">for user-supplied CA.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --user-ca-key=USER_CA_KEY_FILE<br />                        </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Set path to file containing key for user-supplied CA.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --no-default-cn       </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Do not use default CN</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --no-self-signed      </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Don\'t try self-signed certificates</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />  --no-user-cert-signed<br />                        </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Do not sign server certificates with</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">user-supplied one</span><span style=\" font-size:18pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"> </span><span style=\" font-size:18pt;\"> </span></p></body></html>"))
        self.sslcauditB1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\"><br/></span><span style=\" font-size:18pt; color:#ffffff;\">The goal of sslcaudit project is to develop a utility to automate testing SSL/TLS clients for </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">resistance against MITM attacks. It might be useful for testing a thick client, a mobile </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">application, an appliance, pretty much anything communicating over SSL/TLS over TCP. </span></p><p><span style=\" color:#ffffff;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Source:</span><a href=\"http://www.gremwell.com/sites/default/files/sslcaudit/doc/sslcaudit-user-guide-1.0.pdf\"><span style=\" font-size:18pt; text-decoration: underline; color:#ffffff;\">http://www.gremwell.com/sites/default/files/sslcaudit/doc/sslcaudit-user-guide-1.0.pdf</span></a></p><p><span style=\" color:#ffffff;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Author:</span><span style=\" font-size:18pt; color:#ffffff;\"> Gremwell </span><span style=\" color:#ffffff;\"><br/></span></p></body></html>"))
        self.sslcauditH1.setText(_translate("MainWindow", "Description:"))
        self.sslcauditH3.setText(_translate("MainWindow", "Examples:"))
        self.sslcauditB3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">root@kali:~# </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">sslcaudit -l 0.0.0.0:443 -v 1<br/># filebag location: sslcaudit.1<br/>127.0.0.1:38978  selfsigned(www.example.com)</span></p><p><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">tlsv1 alert unknown ca</span></p><p><span style=\" font-size:18pt;\"><br/></span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sscaudittab), _translate("MainWindow", "sslcaudit"))
        self.SSLsplitB3.setText(_translate("MainWindow", "<html><head/><body><p><br/><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">sslsplit -k ca.key -c ca.pem -P  https 127.0.0.1 8443  https ::1 8443</span></p><p><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">root@kali:~# </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">sslsplit -D -l connections.log -j /tmp/sslsplit/ -S /tmp/ -k ca.key -c ca.crt ssl 0.0.0.0 8443 tcp 0.0.0.0 8080<br/>Generated RSA key for leaf certs.<br/>SSLsplit 0.4.6 (built 2013-06-06)<br/></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">Copyright (c) 2009-2013, Daniel Roethlisberger &lt;daniel@roe.ch&gt;<br/>http://www.roe.ch/SSLsplit</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br/>Features: -DDISABLE_SSLV2_SESSION_CACHE -DHAVE_NETFILTER<br/>NAT engines: netfilter* tproxy<br/>netfilter:  IP_TRANSPARENT SOL_IPV6 !IPV6_ORIGINAL_DST<br/>compiled against OpenSSL 1.0.1e 11 Feb 2013 (1000105f)<br/>rtlinked against OpenSSL 1.0.1e 11 Feb 2013 (1000105f)<br/></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">TLS Server Name Indication (SNI) supported<br/>OpenSSL is thread-safe with THREADI</span><br/></p></body></html>"))
        self.SSLsplitH2.setText(_translate("MainWindow", "Usage:"))
        self.SSLsplitH1.setText(_translate("MainWindow", "Description:"))
        self.SSLsplitH3.setText(_translate("MainWindow", "Examples:"))
        self.SSLsplitButton.setText(_translate("MainWindow", "sslsplit"))
        self.SSLsplitB1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\"><br/></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">SSLsplit is a tool for man-in-the-middle attacks against SSL/TLS encrypted network</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">connections. Connections are transparently intercepted through a network address translation</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">engine and redirected to SSLsplit. SSLsplit terminates SSL/TLS and initiates a new SSL/TLS</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">connection to the original destination address, while logging all data transmitted. SSLsplit is</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">intended to be useful for network forensics and penetration testing.</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">SSLsplit supports plain TCP, plain SSL, HTTP and HTTPS connections over both IPv4 and</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">IPv6. For SSL and HTTPS connections, SSLsplit generates and signs forged X509v3 certificates</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">on-the-fly, based on the original server certificate subject DN and subjectAltName extension.</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">SSLsplit fully supports Server Name Indication (SNI) and is able to work with RSA, DSA and</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">ECDSA keys and DHE and ECDHE cipher suites. SSLsplit can also use existing certificates of</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">which the private key is available, instead of generating forged ones. SSLsplit supports NULL</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">prefix CN certificates and can deny OCSP requests in a generic way. SSLsplit removes HPKP</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">response headers in order to prevent public key pinning.</span></p><p><span style=\" font-size:18pt; color:#ffffff;\"><br/></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:600; color:#ffffff;\">Source:</span><a href=\"http://www.roe.ch/SSLsplit\"><span style=\" font-family:\'Times New Roman\'; font-size:18pt; text-decoration: underline; color:#ffffff;\">http://www.roe.ch/SSLsplit</span></a></p><p><span style=\" font-size:18pt; color:#ffffff;\"><br/></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:600; color:#ffffff;\">Author:</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\"> Daniel Roethlisberger</span></p><p><br/></p></body></html>"))
        self.SSLsplitTitle.setText(_translate("MainWindow", "SSLsplit"))
        self.SSLsplitH4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#39b5ff;\">RUN ON TERMINAL :</span></p></body></html>"))
        self.SSLsplitB2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">sslsplit -h</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Times New Roman\'; font-weight:600; color:#ffffff;\">Usage:</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">sslsplit [options...] [proxyspecs...]<br />  -c pemfile  </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">use CA cert (and key) from pemfile to sign forged certs</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -k pemfile  </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">use CA key (and cert) from pemfile to sign forged certs</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -C pemfile  </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">use CA chain from pemfile (intermediate and root CA certs)</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -K pemfile  </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">use key from pemfile for leaf certs (default: generate)</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -t certdir  </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">use cert+chain+key PEM files from certdir to target all sites</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />              </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">matching the common names (non-matching: generate if CA)</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -O          </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">deny all OCSP requests on all proxyspecs</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -P          </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">passthrough SSL connections if they cannot be split because of</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />              </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">client cert auth or no matching cert and no CA (default: drop)</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -g pemfile  </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">use DH group params from pemfile (default: keyfiles or auto)</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -G curve    </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">use ECDH named curve (default: secp160r2 for non-RSA leafkey)</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -Z          </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">disable SSL/TLS compression on all connections<br />  -s ciphers  use the given OpenSSL cipher suite spec (default:</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">ALL:-aNULL)</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -e engine   </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">specify default NAT engine to use (default: netfilter)</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -E          </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">list available NAT engines and exit</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -u user     </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">drop privileges to user (default if run as root: nobody)</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -j jaildir  </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">chroot() to jaildir (default if run as root: /var/empty)</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -p pidfile  </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">write pid to pidfile (default: no pid file)</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -l logfile  </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">connect log: log one line summary per connection to logfile</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -L logfile  </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">content log: full data to file or named pipe (excludes -S)</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -S logdir   </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">content log: full data to separate files in dir (excludes -L)</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -d          </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">daemon mode: run in background, log error messages to syslog</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -D          </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">debug mode: run in foreground, log debug messages on stderr</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -V          </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">print version information and exit</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -h          </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">print usage information and exit<br />  proxyspec = type listenaddr+port [natengine|targetaddr+port|&quot;sni&quot;+port]</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  e.g.        http 0.0.0.0 8080 www.roe.ch 80  # http/4; static hostname dst<br />              https ::1 8443 2001:db8::1 443   # https/6; static address dst<br />              https 127.0.0.1 9443 sni 443     # https/4; SNI DNS lookups<br />              tcp 127.0.0.1 10025              # tcp/4; default NAT engine<br />              ssl 2001:db8::2 9999 pf          # ssl/6; NAT engine \'pf\'</span> </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SSLsplitab), _translate("MainWindow", "SSLsplit"))
        self.sslstripB3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">root@kali:~# </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">sslstrip -w sslstrip.log -l 8080<br/><br/>sslstrip 0.9 by Moxie Marlinspike running...</span></p><p><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"/></p></body></html>"))
        self.sslstripH2.setText(_translate("MainWindow", "Usage:"))
        self.sslstripH1.setText(_translate("MainWindow", "Description:"))
        self.sslstripH3.setText(_translate("MainWindow", "Examples:"))
        self.sslstripButton.setText(_translate("MainWindow", "sslstrip"))
        self.sslstripB1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\"><br/>sslstrip is a tool that transparently hijacks HTTP traffic on a network, watch for HTTPS links and </span></p><p><span style=\" color:#ffffff;\">redirects, and then map those links into look-alike HTTP links or homograph-similar HTTPS links. </span></p><p><span style=\" color:#ffffff;\">It also supports modes for supplying a favicon which looks like a lock icon, selective logging, and </span></p><p><span style=\" color:#ffffff;\">session denial. </span></p><p><span style=\" color:#ffffff;\"><br/></span><span style=\" font-weight:600; color:#ffffff;\">Source: </span><span style=\" color:#ffffff;\">http://www.thoughtcrime.org/software/sslstrip/ </span></p><p><span style=\" color:#ffffff;\"><br/></span><span style=\" font-weight:600; color:#ffffff;\">Author: </span><span style=\" color:#ffffff;\">Moxie Marlinspike </span></p><p><span style=\" color:#ffffff;\"><br/></span></p></body></html>"))
        self.sslstripTitle.setText(_translate("MainWindow", "sslstrip"))
        self.sslstripH4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#39b5ff;\">RUN ON TERMINAL :</span></p></body></html>"))
        self.sslstripB2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">sslstrip -h<br /><br /></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">sslstrip 0.9 by Moxie Marlinspike</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Usage:</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">sslstrip &lt;options&gt;<br /><br /></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Options:</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />-w &lt;filename&gt;, --write=&lt;filename&gt; Specify file to log to (optional).<br />-p , --post                       </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Log only SSL POSTs. (default)</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />-s , --ssl                        </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Log all SSL traffic to and from server.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />-a , --all                        </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Log all SSL and HTTP traffic</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">to and from server.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />-l &lt;port&gt;, --listen=&lt;port&gt;        </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Port to listen on (default</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">10000).</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />-f , --favicon                    </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Substitute a lock favicon on</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">secure requests.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />-k , --killsessions               </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Kill sessions in progress.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />-h                                </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Print this help message.</span><span style=\" font-size:18pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"> </span><span style=\" font-size:18pt;\"> </span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sslstripTab), _translate("MainWindow", "sslstrip"))
        self.SSLyzeB3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">root@kali:~# </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">sslyze --regular www.example.com<br/><br/></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\"> REGISTERING AVAILABLE PLUGINS<br/> -----------------------------</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br/><br/>  PluginCompression<br/>  PluginCertInfo<br/>  PluginSessionResumption<br/>  PluginSessionRenegotiation<br/>  PluginOpenSSLCipherSuites<br/><br/><br/><br/></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\"> CHECKING HOST(S) AVAILABILITY<br/> -----------------------------</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br/><br/>   www.example.com:443                 =&gt; 93.184.216.119:443<br/><br/><br/><br/></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\"> SCAN RESULTS FOR WWW.EXAMPLE.COM:443 - 93.184.216.119:443<br/> ---------------------------------------------------------</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br/><br/>  * Compression :<br/>        Compression Support:      Disabled<br/><br/>  * Certificate :<br/>      Validation w/ Mozilla\'s CA Store:  Certificate is Trusted</span></p><p><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"/></p></body></html>"))
        self.SSLyzeH2.setText(_translate("MainWindow", "Usage:"))
        self.SSLyzeH1.setText(_translate("MainWindow", "Description:"))
        self.SSLyzeH3.setText(_translate("MainWindow", "Examples:"))
        self.SSLyzeButton.setText(_translate("MainWindow", "sslyze"))
        self.SSLyzeB1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\"><br/></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">SSLyze is a Python tool that can analyze the SSL configuration of a server by connecting to it. It</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">is designed to be fast and comprehensive, and should help organizations and testers identify mis</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">configurations affecting their SSL servers.</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Key features include:</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Multi-processed and multi-threaded scanning (it’s fast)</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">SSL 2.0/3.0 and TLS 1.0/1.1/1.2 compatibility</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Performance testing: session resumption and TLS tickets support</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Security testing: weak cipher suites, insecure renegotiation, CRIME, Heartbleed and more</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Server certificate validation and revocation checking through OCSP stapling</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Support for StartTLS handshakes on SMTP, XMPP, LDAP, POP, IMAP, RDP and FTP</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Support for client certificates when scanning servers that perform mutual authentication</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">XML output to further process the scan results</span></p><p><span style=\" color:#ffffff;\"><br/></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:600; color:#ffffff;\">Source:</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\"> https://github.com/iSECPartners/sslyze</span></p><p><span style=\" color:#ffffff;\"><br/></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:600; color:#ffffff;\">Author:</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\"> iSECPartners</span></p><p><span style=\" color:#ffffff;\"><br/></span></p></body></html>"))
        self.SSlyzeTitle.setText(_translate("MainWindow", "SSLyze"))
        self.SSLyzeH4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#39b5ff;\">RUN ON TERMINAL :</span></p></body></html>"))
        self.SSLyzeB2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">sslyze -h<br /><br /><br /><br /> REGISTERING AVAILABLE PLUGINS<br /> -----------------------------<br /><br />  PluginSessionResumption<br />  PluginOpenSSLCipherSuites<br />  PluginCompression<br />  PluginCertInfo<br />  PluginSessionRenegotiation<br /><br /><br /><br /></span><span style=\" font-family:\'Times New Roman\'; font-weight:600; color:#ffffff;\">Usage:</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">sslyze [options] target1.com target2.com:443 etc...<br /><br /></span><span style=\" font-family:\'Times New Roman\'; font-weight:600; color:#ffffff;\">Options:</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  --version             </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">show program\'s version number and exit</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -h, --help            </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">show this help message and exit</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  --xml_out=XML_FILE    </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Writes the scan results as an XML document to the file</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />                        </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">XML_FILE.</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  --targets_in=TARGETS_IN<br />                        </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Reads the list of targets to scan from the file</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />                        </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">TARGETS_IN. It should contain one host:port per line.</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  --timeout=TIMEOUT     </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Sets the timeout value in seconds used for every</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />                        </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">socket connection made to the target server(s).</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />                        </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Default is 5s.</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  --https_tunnel=HTTPS_TUNNEL<br />                        </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Sets an HTTP CONNECT proxy to tunnel SSL traffic to</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />                       </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\"> the target server(s). HTTP_TUNNEL should be</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />                        </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">\'host:port\'. Requires Python 2.7</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  --starttls=STARTTLS   </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Identifies the target server(s) as a SMTP or an XMPP</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />                      </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">  server(s) and scans the server(s) using STARTTLS.</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />                        </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">STARTTLS should be \'smtp\' or \'xmpp\'.</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  --xmpp_to=XMPP_TO     </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Optional setting for STARTTLS XMPP.  XMPP_TO should be</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />                        </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">the hostname to be put in the \'to\'</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">attribute of the<br />                        XMPP stream. Default is the server\'s</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">hostname.</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  --regular             </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Regular HTTPS scan; shortcut for</span><span style=\" font-family:\'Times New Roman\'; color:#00b0f0;\"> --sslv2</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"> --sslv3<br />                        --tlsv1 --reneg --resum --certinfo --http_get<br />                        --hide_rejected_ciphers --compression --tlsv1_1<br />                        --tlsv1_2<br /><br /></span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">  Client certificate support:</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    --cert=CERT         </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Client certificate filename.</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    --certform=CERTFORM<br />                        </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Client certificate format. DER or PEM (default).</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    --key=KEY           </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Client private key filename.</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    --keyform=KEYFORM   </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Client private key format. DER or PEM (default).</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    --pass=KEYPASS      </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Client private key passphrase.</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br /><br />  </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">PluginSessionResumption:</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Analyzes the target server\'s SSL session resumption capabilities.</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br /><br />    --resum             </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Tests the server for session ressumption support,<br />                        using session IDs and TLS session tickets (RFC 5077).</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    --resum_rate        </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Performs 100 session resumptions with the target<br />                        server, in order to estimate the session resumption<br />                        rate.<br /><br />  PluginOpenSSLCipherSuites:</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Scans the target server for supported OpenSSL cipher suites.</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br /><br />    --sslv2             </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Lists the SSL 2.0 OpenSSL cipher suites supported by</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />                        </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">the server.</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    --sslv3             </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Lists the SSL 3.0 OpenSSL cipher suites supported by</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />                        </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">the server.</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    --tlsv1             </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Lists the TLS 1.0 OpenSSL cipher suites supported by</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">                        the server.</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    --tlsv1_1           </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Lists the TLS 1.1 OpenSSL cipher suites supported by</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />                        </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">the server.</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    --tlsv1_2           </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Lists the TLS 1.2 OpenSSL cipher suites supported by</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">                        the server.</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    --http_get          </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Option - For each cipher suite, sends an HTTP GET</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />                       </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\"> request after completing the SSL handshake and returns</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />                        </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">the HTTP status code.</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    --hide_rejected_ciphers<br />                        </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Option - Hides the (usually long) list of cipher</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />                        </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">suites that were rejected by the server.</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br /><br />  </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">PluginCompression:</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    --compression      </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\"> Tests the server for Zlib compression support.</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br /><br /></span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">  PluginCertInfo:</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    --certinfo=CERTINFO<br />                        </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Verifies the target server\'s certificate validity</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />                        </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">against Mozilla\'s trusted root store, and prints<br />                        relevant fields of the certificate. CERTINFO should be<br />                        \'basic\' or \'full\'.<br /><br />  PluginSessionRenegotiation:</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />    --reneg             </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Tests the target server\'s support for client-initiated</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />                     </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">   renegotiations and secure renegotiations.</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"> </span> </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SSLyzeTab), _translate("MainWindow", "SSLyze"))
        self.THCIPV6H2.setText(_translate("MainWindow", "Usage:"))
        self.THCIPV6H1.setText(_translate("MainWindow", "Description:"))
        self.THCIPV6Button.setText(_translate("MainWindow", "thcipv6"))
        self.THCIPV6B1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\"><br/>A complete tool set to attack the inherent protocol weaknesses of IPV6 and ICMP6, and </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">includes an easy to use packet factory library. </span></p><p><span style=\" font-size:18pt; color:#ffffff;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Source:</span><span style=\" font-size:18pt; color:#ffffff;\"> https://www.thc.org/thc-ipv6/ </span></p><p><span style=\" font-size:18pt; color:#ffffff;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Author:</span><span style=\" font-size:18pt; color:#ffffff;\"> The Hacker’s Choice </span></p><p><br/></p></body></html>"))
        self.THCIPV6Title.setText(_translate("MainWindow", "THC-IPV6"))
        self.THCIPV6H4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#39b5ff;\">RUN ON TERMINAL :</span></p></body></html>"))
        self.THCIPV6B2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:small; color:#080808;\">6to4test.sh – Tests if the IPv4 target has a dynamic 6to4 tunnel active</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# 6to4test.sh</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />Syntax: /usr/bin/6to4test.sh interface ipv4address<br />This little script tests if the IPv4 target has a dynamic 6to4 tunnel active<br />Requires address6 and thcping6 from thc-ipv6</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">address6 – Converts a mac or ipv4 address to an ipv6 address</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# address6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />address6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax:<br />    address6 mac-address [ipv6-prefix]<br />    address6 ipv4-address [ipv6-prefix]<br />    address6 ipv6-address<br /><br />Converts a mac or ipv4 address to an ipv6 address (link local if no prefix is<br />given as 2nd option) or, when given an ipv6 address, prints the mac or ipv4<br />address. Prints all possible variations. Returns -1 on errors or the number of<br />variations found</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">alive6 – Shows alive addresses in the segment</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# alive6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />alive6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: alive6 [-I srcip6] [-i file] [-o file] [-DM] [-p] [-F] [-e opt] [-s port,..] [-a port,..] [-u port,..] [-W TIME] [-dlrvS] interface [unicast-or-multicast-address [remote-router]]<br /><br />Shows alive addresses in the segment. If you specify a remote router, the<br />packets are sent with a routing header prefixed by fragmentation<br />Options:<br />  -i file    check systems from input file<br />  -o file    write results to output file<br />  -M         enumerate hardware addresses (MAC) from input addresses (slow!)<br />  -D         enumerate DHCP address space from input addresses<br />  -p         send a ping packet for alive check (default)<br />  -e dst,hop send an errornous packets: destination (default), hop-by-hop<br />  -s port,port,..  TCP-SYN packet to ports for alive check<br />  -a port,port,..  TCP-ACK packet to ports for alive check<br />  -u port,port,..  UDP packet to ports for alive check<br />  -d         DNS resolve alive ipv6 addresses<br />  -n number  how often to send each packet (default: local 1, remote 2)<br />  -W time    time in ms to wait after sending a packet (default: 1)<br />  -S         slow mode, get best router for each remote target or when proxy-NA<br />  -I srcip6  use the specified IPv6 address as source<br />  -l         use link-local address instead of global address<br />  -v         verbose (twice: detailed information, thrice: dumping all packets)<br />Target address on command line or in input file can include ranges in the form<br />of 2001:db8::1-fff or 2001:db8::1-2:0-ffff:0:0-ffff, etc.<br />Returns -1 on errors, 0 if a system was found alive or 1 if nothing was found.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">covert_send6 – Sends the content of FILE covertly to the target</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# covert_send6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />covert_send6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: covert_send6 [-m mtu] [-k key] [-s resend] interface target file [port]<br /><br />Options:<br />  -m mtu     specifies the maximum MTU (default: interface MTU, min: 1000)<br />  -k key     encrypt the content with Blowfish-160<br />  -s resend  send each packet RESEND number of times, default: 1<br /><br />Sends the content of FILE covertly to the target, And its POC - dont except<br />too much sophistication - its just put into the destination header.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">covert_send6d – Writes covertly received content to FILE</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# covert_send6d</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />covert_send6d v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: covert_send6d [-k key] interface file<br /><br />Options:<br />  -k key     decrypt the content with Blowfish-160<br /><br />Writes covertly received content to FILE.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">denial6 – Performs various denial of service attacks on a target</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# denial6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />denial6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: denial6 interface destination test-case-number<br /><br />Performs various denial of service attacks on a target<br />If a system is vulnerable, it can crash or be under heavy load, so be careful!<br />If not test-case-number is supplied, the list of shown.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">detect-new-ip6 – This tools detects new ipv6 addresses joining the local network</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# detect-new-ip6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />detect-new-ip6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: detect-new-ip6 interface [script]<br /><br />This tools detects new ipv6 addresses joining the local network.<br />If script is supplied, it is executed with the detected IPv6 address as first<br />and the interface as second command line option.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">detect_sniffer6 – Tests if systems on the local LAN are sniffing</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# detect_sniffer6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />detect_sniffer6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: detect_sniffer6 interface [target6]<br /><br />Tests if systems on the local LAN are sniffing.<br />Works against Windows, Linux, OS/X and *BSD<br />If no target is given, the link-local-all-nodes address is used, which<br />however rarely works.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">dnsdict6 – Enumerates a domain for DNS entries</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# dnsdict6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />dnsdict6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: dnsdict6 [-d46] [-s|-m|-l|-x] [-t THREADS] [-D] domain [dictionary-file]<br /><br />Enumerates a domain for DNS entries, it uses a dictionary file if supplied<br />or a built-in list otherwise. This tool is based on dnsmap by gnucitizen.org.<br /><br />Options:<br /> -4      also dump IPv4 addresses<br /> -t NO   specify the number of threads to use (default: 8, max: 32).<br /> -D      dump the selected built-in wordlist, no scanning.<br /> -d      display IPv6 information on NS and MX DNS domain information.<br /> -S      perform SRV service name guessing<br /> -[smlx] choose the dictionary size by -s(mall=50), -m(edium=796) (DEFAULT)<br />           -l(arge=1416), or -x(treme=3211)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">dnsrevenum6 – Performs a fast reverse DNS enumeration and is able to cope with slow servers</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# dnsrevenum6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />dnsrevenum6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: dnsrevenum6 dns-server ipv6address<br /><br />Performs a fast reverse DNS enumeration and is able to cope with slow servers.<br />Examples:<br />  dnsrevenum6 dns.test.com 2001:db8:42a8::/48<br />  dnsrevenum6 dns.test.com 8.a.2.4.8.b.d.0.1.0.0.2.ip6.arpa</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">dnssecwalk – Perform DNSSEC NSEC walking</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# dnssecwalk</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />dnssecwalk v1.2 (c) 2013 by Marc Heuse &lt;mh@mh-sec.de&gt; http://www.mh-sec.de<br /><br />Syntax: dnssecwalk [-e46] dns-server domain<br /><br />Options:<br /> -e  ensure that the domain is present in found addresses, quit otherwise<br /> -4  resolve found entries to IPv4 addresses<br /> -6  resolve found entries to IPv6 addresses<br /><br />Perform DNSSEC NSEC walking.<br /><br />Example: dnssecwalk dns.test.com test.com</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">dos_mld.sh – If specified, the multicast address of the target will be dropped first</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# dos_mld.sh</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />Syntax: /usr/bin/dos_mld.sh [-2] interface [target-link-local-address multicast-address]<br />If specified, the multicast address of the target will be dropped first.<br />All multicast traffic will cease after a while.<br />Specify -2 to use MLDv2.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">dos-new-ip6 – This tools prevents new ipv6 interfaces to come up</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# dos-new-ip6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />dos-new-ip6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: dos-new-ip6 interface<br /><br />This tools prevents new ipv6 interfaces to come up, by sending answers to<br />duplicate ip6 checks (DAD). This results in a DOS for new ipv6 devices.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">dump_router6 – Dumps all local routers and their information</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# dump_router6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />dump_router6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: dump_router6 interface<br /><br />Dumps all local routers and their information</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">exploit6 – Performs exploits of various CVE known IPv6 vulnerabilities on the destination</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# exploit6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />exploit6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: exploit6 interface destination [test-case-number]<br /><br />Performs exploits of various CVE known IPv6 vulnerabilities on the destination<br />Note that for exploitable overflows only \'AAA...\' strings are used.<br />If a system is vulnerable, it will crash, so be careful!</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">extract_hosts6.sh – prints the host parts of IPv6 addresses in FILE</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# extract_hosts6.sh</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />/usr/bin/extract_hosts6.sh FILE<br />prints the host parts of IPv6 addresses in FILE</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">extract_networks6.sh – prints the networks found in FILE</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# extract_networks6.sh</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />/usr/bin/extract_networks6.sh FILE<br />prints the networks found in FILE</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">fake_advertise6 – Advertise ipv6 address on the network</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# fake_advertise6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />fake_advertise6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: fake_advertise6 [-DHF] [-Ors] [-n count] [-w seconds] interface ip-address-advertised [target-address [mac-address-advertised [source-ip-address]]]<br /><br />Advertise ipv6 address on the network (with own mac if not specified),<br />sending it to the all-nodes multicast address if no target address is set.<br />Source ip addresss is the address advertised if not set.<br /><br />Sending options:<br />  -n count    send how many packets (default: forever)<br />  -w seconds  wait time between the packets sent (default: 5)<br />Flag options:<br />  -O  do NOT set the override flag (default: on)<br />  -r  DO set the router flag (default: off)<br />  -s  DO set the solicitate flag (default: off)<br />ND Security evasion options (can be combined):<br />  -H  add a hop-by-hop header<br />  -F  add a one shot fragment header (can be specified multiple times)<br />  -D  add a large destination header which fragments the packet.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">fake_dhcps6 – Fake DHCPv6 server</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# fake_dhcps6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />fake_dhcps6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: fake_dhcps6 interface network-address/prefix-length dns-server [dhcp-server-ip-address [mac-address]]<br /><br />Fake DHCPv6 server. Use to configure an address and set a DNS server</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">fake_dns6d – Fake DNS server that serves the same ipv6 address to any lookup request</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# fake_dns6d</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />fake_dns6d v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: fake_dns6d interface ipv6-address [fake-ipv6-address [fake-mac]]<br />Fake DNS server that serves the same ipv6 address to any lookup request<br />You can use this together with parasite6 if clients have a fixed DNS server<br />Note: very simple server. Does not honor multiple queries in a packet, norNS, MX, etc. lookups.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">fake_dnsupdate6 – Fake DNS updater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# fake_dnsupdate6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />fake_dnsupdate6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: fake_dnsupdate6 dns-server full-qualified-host-dns-name ipv6address<br /><br />Example: fake_dnsupdate6 dns.test.com myhost.sub.test.com ::1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">fake_mipv6 – Will redirect all packets for home-address to care-of-address</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# fake_mipv6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />fake_mipv6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: fake_mipv6 interface home-address home-agent-address care-of-address<br /><br />If the mobile IPv6 home-agent is mis-configured to accept MIPV6 updates without<br />IPSEC, this will redirect all packets for home-address to care-of-address</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">fake_mld26</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# fake_mld26</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />fake_mld26 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: fake_mld26 [-l] interface add|delete|query [multicast-address [target-address [ttl [own-ip [own-mac-address [destination-mac-address]]]]]]<br /><br />This uses the MLDv2 protocol. Only a subset of what the protocol is able to<br />do is possible to implement via a command line. Code it if you need something.<br />Ad(d)vertise or delete yourself - or anyone you want - in a multicast group of your choice<br />Query ask on the network who is listening to multicast addresses<br />Use -l to loop and send (in 5s intervals) until Control-C is pressed.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">fake_mld6 – Ad(d)vertise or delete yourself – or anyone you want</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# fake_mld6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />fake_mld6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: fake_mld6 [-l] interface add|delete|query [multicast-address [target-address [ttl [own-ip [own-mac-address [destination-mac-address]]]]]]<br /><br />Ad(d)vertise or delete yourself - or anyone you want - in a multicast group of your choice<br />Query ask on the network who is listening to multicast addresses<br />Use -l to loop and send (in 5s intervals) until Control-C is pressed.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">fake_mldrouter6 – Announce, delete or soliciated MLD router</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# fake_mldrouter6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />fake_mldrouter6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: fake_mldrouter6 [-l] interface advertise|solicitate|terminate [own-ip [own-mac-address]]<br /><br />Announce, delete or soliciated MLD router - yourself or others.<br />Use -l to loop and send (in 5s intervals) until Control-C is pressed.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">fake_pim6</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# fake_pim6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />fake_pim6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax:<br />  fake_pim6 [-t ttl] [-s src6] [-d dst6] interface hello [dr_priority]<br />  fake_pim6 [-t ttl] [-s src6] [-d dst6] interface join|prune neighbor6 multicast6 target6<br /><br />The hello command takes optionally the DR priority (default: 0).<br />The join and prune commands need the multicast group to modify, the target<br />address that joins or leavs and the neighbor PIM router<br />Use -s to spoof the source ip6, -d to send to another address than ff02::d,<br />and -t to set a different TTL (default: 1)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">fake_router26 – Announce yourself as a router and try to become the default router</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# fake_router26</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />fake_router26 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: fake_router26 [-E type] [-A network/prefix] [-R network/prefix] [-D dns-server] [-s sourceip] [-S sourcemac] [-ardl seconds] [-Tt ms] [-n no] [-i interval] interface<br /><br />Options:<br /> -A network/prefix  add autoconfiguration network (up to 16 times)<br /> -a seconds         valid lifetime of prefix -A (defaults to 99999)<br /> -R network/prefix  add a route entry (up to 16 times)<br /> -r seconds         route entry lifetime of -R (defaults to 4096)<br /> -D dns-server      specify a DNS server (up to 16 times)<br /> -L searchlist      specify the DNS domain search list, seperate entries with ,<br /> -d seconds         dns entry lifetime of -D (defaults to 4096<br /> -M mtu             the MTU to send, defaults to the interface setting<br /> -s sourceip        the source ip of the router, defaults to your link local<br /> -S sourcemac       the source mac of the router, defaults to your interface<br /> -l seconds         router lifetime (defaults to 2048)<br /> -T ms              reachable timer (defaults to 0)<br /> -t ms              retrans timer (defaults to 0)<br /> -p priority        priority &quot;low&quot;, &quot;medium&quot;, &quot;high&quot; (default), &quot;reserved&quot;<br /> -F flags           Set one or more of the following flags: managed, other,<br />                   homeagent, proxy, reserved; seperate by comma<br /> -E type            Router Advertisement Guard Evasion option. Types:<br />     H             simple hop-by-hop header<br />     1             simple one-shot fragmentation header (can add multiple)<br />     D             insert a large destination header so that it fragments<br />     O             overlapping fragments for keep-first targets (Win, BSD, Mac)<br />     o             overlapping fragments for keep-last targets (Linux, Solaris)<br />                    Examples: -E H111, -E D<br /> -m mac-address    if only one machine should receive the RAs (not with -E DoO)<br /> -i interval       time between RA packets (default: 5)<br /> -n number         number of RAs to send (default: unlimited)<br /><br />Announce yourself as a router and try to become the default router.<br />If a non-existing link-local or mac address is supplied, this results in a DOS.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">fake_router6 – Announce yourself as a router and try to become the default router.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# fake_router6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />fake_router6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: fake_router6 [-HFD] interface network-address/prefix-length [dns-server [router-ip-link-local [mtu [mac-address]]]]<br /><br />Announce yourself as a router and try to become the default router.<br />If a non-existing link-local or mac address is supplied, this results in a DOS.<br />Option -H adds hop-by-hop, -F fragmentation header and -D dst header.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">fake_solicitate6 – Solicate ipv6 address on the network</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# fake_solicitate6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />fake_solicitate6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: fake_solicitate6 [-DHF] interface ip-address-solicitated [target-address [mac-address-solicitated [source-ip-address]]]<br /><br />Solicate ipv6 address on the network, sending it to the all-nodes multicast address</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">firewall6 – Performs various ACL bypass attempts to check implementations</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# firewall6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />firewall6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: firewall6 [-u] interface destination port [test-case-no]<br /><br />Performs various ACL bypass attempts to check implementations.<br />Defaults to TCP ports, option -u switches to UDP.<br />For all test cases to work, ICMPv6 ping to thhe destination must be allowed.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">flood_advertise6 – Flood the local network with neighbor advertisements</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# flood_advertise6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />flood_advertise6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: flood_advertise6 interface<br /><br />Flood the local network with neighbor advertisements.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">flood_dhcpc6 – DHCP client flooder</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# flood_dhcpc6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />flood_dhcpc6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: flood_dhcpc6 [-n|-N] [-1] [-d] interface [domain-name]<br /><br />DHCP client flooder. Use to deplete the IP address pool a DHCP6 server is<br />offering. Note: if the pool is very large, this is rather senseless. :-)<br /><br />By default the link-local IP MAC address is random, however this won\'t work<br />in some circumstances. -n will use the real MAC, -N the real MAC and<br />link-local address. -1 will only solicate an address but not request it.<br />If -N is not used, you should run parasite6 in parallel.<br />Use -d to force DNS updates, you can specify a domain name on the commandline.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">flood_mld26 – Flood the local network with MLDv2 reports</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# flood_mld26</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />flood_mld26 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: flood_mld26 interface<br /><br />Flood the local network with MLDv2 reports.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">flood_mld6 – Flood the local network with MLD reports</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# flood_mld6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />flood_mld6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: flood_mld6 interface<br /><br />Flood the local network with MLD reports.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">flood_mldrouter6 – Flood the local network with MLD router advertisements</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# flood_mldrouter6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />flood_mldrouter6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: flood_mldrouter6 interface<br /><br />Flood the local network with MLD router advertisements.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">flood_router26 – Flood the local network with router advertisements</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# flood_router26</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />flood_router26 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: flood_router26 [-HFD] [-s] [-RPA] interface<br /><br />Flood the local network with router advertisements.<br />Each packet contains 17 prefix and route enries<br />-F/-D/-H add fragment/destination/hopbyhop header to bypass RA guard security.<br />-R does only send routing entries, no prefix information.<br />-P does only send prefix information, no routing entries.<br />-A is like -P but implements an attack by George Kargiotakis to disable privacy extensions<br />The option -s uses small lifetimes, resulting in a more devasting impact</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">flood_router6 – Flood the local network with router advertisements</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# flood_router6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />flood_router6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: flood_router6 [-HFD] interface<br /><br />Flood the local network with router advertisements.<br />-F/-D/-H add fragment/destination/hopbyhop header to bypass RA guard security.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">flood_solicitate6 – Flood the network with neighbor solicitations</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# flood_solicitate6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />flood_solicitate6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: flood_solicitate6 interface [target]<br /><br />Flood the network with neighbor solicitations.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">fragmentation6 – Performs fragment firewall and implementation checks</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# fragmentation6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />fragmentation6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: fragmentation6 [-fp] [-n number] interface destination [test-case-no]<br /><br />-f activates flooding mode, no pauses between sends; -p disables first and<br />final pings, -n number specifies how often each test is performed<br /><br />Performs fragment firewall and implementation checks, incl. denial-of-service.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">fuzz_ip6 – Fuzzes an icmp6 packet</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# fuzz_ip6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />fuzz_ip6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: fuzz_ip6 [-x] [-t number | -T number] [-p number] [-IFSDHRJ] [-X|-1|-2|-3|-4|-5|-6|-7|-8|-9|-0 port] interface unicast-or-multicast-address [address-in-data-pkt]<br /><br />Fuzzes an icmp6 packet<br />Options:<br /> -X         do not add any ICMP/TCP header (tranport laye)<br /> -1         fuzz ICMP6 echo request (default)<br /> -2         fuzz ICMP6 neighbor solicitation<br /> -3         fuzz ICMP6 neighbor advertisement<br /> -4         fuzz ICMP6 router advertisement<br /> -5         fuzz multicast listener report packet<br /> -6         fuzz multicast listener done packet<br /> -7         fuzz multicast listener query packet<br /> -8         fuzz multicast listener v2 report packet<br /> -9         fuzz multicast listener v2 query packet<br /> -0         fuzz node query packet<br /> -s port    fuzz TCP-SYN packet against port<br /> -x         tries all 256 values for flag and byte types<br /> -t number  continue from test no. number<br /> -T number  only performs test no. number<br /> -p number  perform an alive check every number of tests (default: none)<br /> -a         do not perform initial and final alive test<br /> -n number  how many times to send each packet (default: 1)<br /> -I         fuzz the IP header too<br /> -F         add one-shot fragmentation, and fuzz it too (for 1)<br /> -S         add source-routing, and fuzz it too (for 1)<br /> -D         add destination header, and fuzz it too (for 1)<br /> -H         add hop-by-hop header, and fuzz it too (for 1 and 5-9)<br /> -R         add router alert header, and fuzz it too (for 5-9 and all)<br /> -J         add jumbo packet header, and fuzz it too (for 1)<br />You can only define one of -0 ... -9 and -s, defaults to -1.<br />Returns -1 on error, 0 on tests done and targt alive or 1 on target crash.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">implementation6 – Performs some ipv6 implementation checks</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# implementation6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />implementation6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: implementation6 [-p] [-s sourceip6] interface destination [test-case-number]<br /><br />Options:<br />  -s sourceip6  use the specified source IPv6 address<br />  -p            do not perform an alive check at the beginning and end<br />Performs some ipv6 implementation checks, can be used to test some<br />firewall features too. Takes approx. 2 minutes to complete.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">implementation6d – Identifies test packets by the implementation6 tool</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# implementation6d</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />implementation6d v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: implementation6d interface<br /><br />Identifies test packets by the implementation6 tool, useful to check what<br />packets passed a firewall</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">inject_alive6 – This tool answers to keep-alive requests on PPPoE and 6in4 tunnels</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# inject_alive6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />inject_alive6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: inject_alive6 [-ap] interface<br /><br />This tool answers to keep-alive requests on PPPoE and 6in4 tunnels; for PPPoE<br />it also sends keep-alive requests.<br />Note that the appropriate environment variable THC_IPV6_{PPPOE|6IN4} must be set<br />Option -a will actively send alive requests every 15 seconds.<br />Option -p will not send replies to alive requests.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">inverse_lookup6 – Performs an inverse address query</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# inverse_lookup6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />inverse_lookup6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: inverse_lookup6 interface mac-address<br /><br />Performs an inverse address query, to get the IPv6 addresses that are assigned<br />to a MAC address. Note that only few systems support this yet.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">kill_router6 – Announce that a target a router going down to delete it from the routing tables</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# kill_router6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />kill_router6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: kill_router6 [-HFD] interface router-address [srcmac [dstmac]]<br /><br />Announce that a target a router going down to delete it from the routing tables.<br />If you supply a \'*\' as router-address, this tool will sniff the network for any<br />RA packet and immediately send the kill packet.<br />Option -H adds hop-by-hop, -F fragmentation header and -D dst header.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">ndpexhaust26 – Flood the target /64 network with ICMPv6 TooBig error messages</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# ndpexhaust26</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />ndpexhaust26 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: ndpexhaust26 [-acpPTUrR] [-s sourceip6] interface target-network<br /><br />Options:<br /> -a      add a hop-by-hop header with router alert<br /> -c      do not calculate the checksum to save time<br /> -p      send ICMPv6 Echo Requests<br /> -P      send ICMPv6 Echo Reply<br /> -T      send ICMPv6 Time-to-live-exeeded<br /> -U      send ICMPv6 Unreachable (no route)<br /> -r      randomize the source from your /64 prefix<br /> -R      randomize the source fully<br /> -s sourceip6  use this as source ipv6 address<br /><br />Flood the target /64 network with ICMPv6 TooBig error messages.<br />This tool version is manyfold more effective than ndpexhaust6.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">ndpexhaust6 – Flood the target /64 network with ICMPv6 TooBig error messages</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# ndpexhaust26</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />ndpexhaust26 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: ndpexhaust26 [-acpPTUrR] [-s sourceip6] interface target-network<br /><br />Options:<br /> -a      add a hop-by-hop header with router alert<br /> -c      do not calculate the checksum to save time<br /> -p      send ICMPv6 Echo Requests<br /> -P      send ICMPv6 Echo Reply<br /> -T      send ICMPv6 Time-to-live-exeeded<br /> -U      send ICMPv6 Unreachable (no route)<br /> -r      randomize the source from your /64 prefix<br /> -R      randomize the source fully<br /> -s sourceip6  use this as source ipv6 address<br /><br />Flood the target /64 network with ICMPv6 TooBig error messages.<br />This tool version is manyfold more effective than ndpexhaust6.<br />root@kali:~# ndpexhaust6<br />ndpexhaust6 by mario fleischmann &lt;mario.fleischmann@1und1.de&gt;<br /><br />Syntax: ndpexhaust6 interface destination-network [sourceip]<br /><br />Randomly pings IPs in target network</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">node_query6 – Sends an ICMPv6 node query request to the target</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# node_query6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />node_query6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: node_query6 interface target<br /><br />Sends an ICMPv6 node query request to the target and dumps the replies.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">parasite6 – This is an “ARP spoofer” for IPv6</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# parasite6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />parasite6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: parasite6 [-lRFHD] interface [fake-mac]<br /><br />This is an &quot;ARP spoofer&quot; for IPv6, redirecting all local traffic to your own<br />system (or nirvana if fake-mac does not exist) by answering falsely to<br />Neighbor Solitication requests<br />Option -l loops and resends the packets per target every 5 seconds.<br />Option -R will also try to inject the destination of the solicitation<br />NS security bypass: -F fragment, -H hop-by-hop and -D large destination header</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">passive_discovery6 – Passively sniffs the network and dump all client’s IPv6 addresses</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# passive_discovery6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />passive_discovery6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: passive_discovery6 [-Ds] [-m maxhop] [-R prefix] interface [script]<br /><br />Options:<br /> -D          do also dump destination addresses (does not work with -m)<br /> -s          do only print the addresses, no other output<br /> -m maxhop   the maximum number of hops a target which is dumped may be away.<br />             0 means local only, the maximum amount to make sense is usually 5<br /> -R prefix   exchange the defined prefix with the link local prefix<br /><br />Passively sniffs the network and dump all client\'s IPv6 addresses detected.<br />Note that in a switched environment you get better results when additionally<br />starting parasite6, however this will impact the network.<br />If a script name is specified after the interface, it is called with the<br />detected ipv6 address as first and the interface as second option.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">randicmp6 – Sends all ICMPv6 type and code combinations to destination</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# randicmp6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />Syntax: randicmp6 [-s sourceip] interface destination [type [code]]<br /><br />Sends all ICMPv6 type and code combinations to destination.<br />Option -s  sets the source ipv6 address.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">redir6 – Implant a route into victim-ip, which redirects all traffic to target-ip</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# redir6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />redir6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: redir6 interface victim-ip target-ip original-router new-router [new-router-mac] [hop-limit]<br /><br />Implant a route into victim-ip, which redirects all traffic to target-ip to<br />new-ip. You must know the router which would handle the route.<br />If the new-router-mac does not exist, this results in a DOS.<br />If the TTL of the target is not 64, then specify this is the last option.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">redirsniff6 – Implant a route into victim-ip, which redirects all traffic to destination-ip</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# redirsniff6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />redirsniff6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: redirsniff6 interface victim-ip destination-ip original-router [new-router [new-router-mac]]<br /><br />Implant a route into victim-ip, which redirects all traffic to destination-ip to<br />new-router. This is done on all traffic that flows by that matches<br />victim-&gt;target. You must know the router which would handle the route.<br />If the new-router/-mac does not exist, this results in a DOS.<br />You can supply a wildcard (\'*\') for victim-ip and/or destination-ip.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">rsmurf6 – Smurfs the local network of the victim</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# rsmurf6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />rsmurf6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: rsmurf6 interface victim-ip<br /><br />Smurfs the local network of the victim. Note: this depends on an<br />implementation error, currently only verified on Linux.<br />Evil: &quot;ff02::1&quot; as victim will DOS your local LAN completely</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">sendpees6 – Send SEND neighbor solicitation messages</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# sendpees6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />sendpees6 by willdamn &lt;willdamn@gmail.com&gt;<br /><br />usage: sendpees6 &lt;inf&gt; &lt;key_length&gt; &lt;prefix&gt; &lt;victim&gt;<br /><br />Send SEND neighbor solicitation messages and make target to verify a lota CGA and RSA signatures</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">sendpeesmp6 – Send SEND neighbor solicitation messages</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# sendpeesmp6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />original sendpees by willdamn &lt;willdamn@gmail.com&gt;<br />modified sendpeesMP by Marcin Pohl &lt;marcinpohl@gmail.com&gt;<br />Code based on thc-ipv6<br /><br />usage: sendpeesmp6 &lt;inferface&gt; &lt;key_length&gt; &lt;prefix&gt; &lt;victim&gt;<br /><br />Send SEND neighbor solicitation messages and make target to verify a lota CGA and RSA signatures<br />Example: sendpeesmp6 eth0 2048 fe80:: fe80::1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">smurf6 – Smurf the target with icmp echo replies</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# smurf6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />smurf6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: smurf6 interface victim-ip [multicast-network-address]<br /><br />Smurf the target with icmp echo replies. Target of echo request is the<br />local all-nodes multicast address if not specified</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">thcping6 – Craft your special icmpv6 echo request packet</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# thcping6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />thcping6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: thcping6 [-af] [-H o:s:v] [-D o:s:v] [-F dst] [-t ttl] [-c class] [-l label] [-d size] [-S port|-U port] interface src6 dst6 [srcmac [dstmac [data]]]<br /><br />Craft your special icmpv6 echo request packet.<br />You can put an &quot;x&quot; into src6, srcmac and dstmac for an automatic value.<br />Options:<br />  -a              add a hop-by-hop header with router alert option.<br />  -q              add a hop-by-hop header with quickstart option.<br />  -E              send as ethertype IPv4<br />  -H o:s:v        add a hop-by-hop header with special content<br />  -D o:s:v        add a destination header with special content<br />  -D &quot;xxx&quot;        add a large destination header which fragments the packet<br />  -f              add a one-shot fragementation header<br />  -F ipv6address  use source routing to this final destination<br />  -t ttl          specify TTL (default: 64)<br />  -c class        specify a class (0-4095)<br />  -l label        specify a label (0-1048575)<br />  -d data_size    define the size of the ping data buffer<br />  -S port         use a TCP SYN packet on the defined port instead of ping<br />  -U port         use a UDP packet on the defined port instead of ping<br />o:s:v syntax: option-no:size:value, value is in hex, e.g. 1:2:feab<br />Returns -1 on error or no reply, 0 on normal reply or 1 on error reply.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">thcsyn6 – Flood the target port with TCP-SYN packets</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# thcsyn6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />thcsyn6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: thcsyn6 [-AcDrRS] [-p port] [-s sourceip6] interface target port<br /><br />Options:<br /> -A      send TCP-ACK packets<br /> -S      send TCP-SYN-ACK packets<br /> -r      randomize the source from your /64 prefix<br /> -R      randomize the source fully<br /> -s sourceip6  use this as source ipv6 address<br /> -D      randomize the destination (treat as /64)<br /> -p port       use fixed source port<br /><br />Flood the target port with TCP-SYN packets. If you supply &quot;x&quot; as port, it<br />is randomized.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">toobig6 – Implants the specified mtu on the target</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# toobig6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />toobig6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: toobig6 [-u] interface target-ip existing-ip mtu [hop-limit]<br /><br />Implants the specified mtu on the target.<br />If the TTL of the target is not 64, then specify this as the last option.<br />Option -u will send the TooBig without the spoofed ping6 from existing-ip.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1.4%;\"><span style=\" font-family:\'Noto Sans,sans-serif\'; font-size:large; color:#080808;\">trace6 – A basic but very fast traceroute6 program</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f1f1f1;\"><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808; background-color:#f1f1f1;\">root@kali:~# trace6</span><span style=\" font-family:\'Monaco,Lucida Console,monospace\'; font-size:13px; color:#080808;\"><br />trace6 v2.3 (c) 2013 by van Hauser / THC &lt;vh@thc.org&gt; www.thc.org<br /><br />Syntax: trace6 [-abdt] [-s src6] interface targetaddress [port]<br /><br />Options:<br />  -a       insert a hop-by-hop header with router alert option.<br />  -D       insert a destination extension header<br />  -E       insert a destination extension header with an invalid option<br />  -F       insert a one-shot fragmentation header<br />  -b       instead of an ICMP6 Ping, use TooBig (you will not see the target)<br />  -B       instead of an ICMP6 Ping, use PingReply (you will not see the target)<br />  -d       resolves the IPv6 addresses to DNS.<br />  -t       enables tunnel detection<br />  -s src6  specifies the source IPv6 address<br />Maximum hop reach: 31<br /><br />A basic but very fast traceroute6 program.<br />If no port is specified, ICMP6 Ping requests are used, otherwise TCP SYN<br />packets to the specified port. Options D, E and F can be use multiple times.</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.THCIPV6Tab), _translate("MainWindow", "THC-IPV6"))
        self.theHarvesterB3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">root@kali:~# </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">theharvester -d kali.org -l 500 -b google</span></p><p><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"/></p><p><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">[-] Searching in Google:</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br/>        Searching 0 results...<br/>        Searching 100 results...<br/>        Searching 200 results...<br/>        Searching 300 results...<br/>        Searching 400 results...<br/>        Searching 500 results...</span></p><p><span style=\" font-family:\'Times New Roman\';\"/></p><p><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br/></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">root@kali:~# </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">theharvester -d microsoft.com -l 500 -b google<br/></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">root@kali:~# </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">theharvester -d microsoft.com -b pgp<br/></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">root@kali:~# </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">theharvester -d microsoft -l 200 -b linkedin</span></p></body></html>"))
        self.theHarvesterH2.setText(_translate("MainWindow", "Usage:"))
        self.theHarvesterH1.setText(_translate("MainWindow", "Description:"))
        self.theHarvesterH3.setText(_translate("MainWindow", "Examples:"))
        self.theHarvesterButton.setText(_translate("MainWindow", "theharvester"))
        self.theHarvesterB1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\"><br/></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">The objective of this program is to gather emails, subdomains, hosts, employee names, open</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">ports and banners from different public sources like search engines, PGP key servers and</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">SHODAN computer database.</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">This tool is intended to help Penetration testers in the early stages of the penetration test in order</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">to understand the customer footprint on the Internet. It is also useful for anyone that wants to</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">know what an attacker can see about their organization.</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">This is a complete rewrite of the tool with new features like:</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Time delays between request</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">All sources search</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Virtual host verifier</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Active enumeration (DNS enumeration, Reverse lookups, TLD expansion)</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Integration with SHODAN computer database, to get the open ports and banners</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Save to XML and HTML</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Basic graph with stats</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">New sources</span></p><p><span style=\" color:#ffffff;\"><br/></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:600; color:#ffffff;\">Source:</span><a href=\"https://code.google.com/p/theharvester/\"><span style=\" font-family:\'Times New Roman\'; font-size:18pt; text-decoration: underline; color:#ffffff;\">https://code.google.com/p/theharvester/</span></a></p><p><span style=\" color:#ffffff;\"><br/></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:600; color:#ffffff;\">Author:</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\"> Christian Martorella</span></p><p><br/></p></body></html>"))
        self.theHarvesterTitle.setText(_translate("MainWindow", "theHarvester"))
        self.theHarvesterH4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#39b5ff;\">RUN ON TERMINAL :</span></p></body></html>"))
        self.theHarvesterB2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">theharvester<br /><br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">*******************************************************************<br />*                                                                 *<br />* | |_| |__   ___    /\\  /\\__ _ _ ____   _____  ___| |_ ___ _ __  *<br />* | __| \'_ \\ / _ \\  / /_/ / _` | \'__\\ \\ / / _ \\/ __| __/ _ \\ \'__| *<br />* | |_| | | |  __/ / __  / (_| | |   \\ V /  __/\\__ \\ ||  __/ |    *<br />*  \\__|_| |_|\\___| \\/ /_/ \\__,_|_|    \\_/ \\___||___/\\__\\___|_|    *<br />*                                                                 *<br />* TheHarvester Ver. 2.2a                                          *<br />* Coded by Christian Martorella                                   *<br />* Edge-Security Research                                          *<br />* cmartorella@edge-security.com                                   *<br />*******************************************************************</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /><br /><br /></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:600; color:#ffffff;\">Usage:</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">theharvester options<br /><br />       -d: </span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Domain to search or company name</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />       -b: </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Data source (google,bing,bingapi,pgp,linkedin,google-profiles,people123,jigsaw,all)</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />       -s: </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Start in result number X (default 0)</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />       -v: </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Verify host name via dns resolution and search for virtual hosts</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />       -f: </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Save the results into an HTML and XML file<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">       -n: </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Perform a DNS reverse query on all ranges discovered</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />       -c: </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Perform a DNS brute force for the domain name</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />       -t: </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Perform a DNS TLD expansion discovery<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">       -e: </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Use this DNS server</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />       -l: </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Limit the number of results to work with(bing goes from 50 to 50 results,<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">       -h: </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">use SHODAN database to query discovered hosts</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />            </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">google 100 to 100, and pgp doesn\'t use this option)</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /><br /></span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.theHarvesterTab), _translate("MainWindow", "theHarvester"))
        self.TLSSLedB3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">root@kali:~# </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">tlssled 192.168.1.1 443<br/>------------------------------------------------------<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> TLSSLed - (1.3) based on sslscan and openssl<br/>                 by Raul Siles (www.taddong.com)</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/>------------------------------------------------------<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">openssl version: OpenSSL 1.0.1e 11 Feb 2013<br/>    sslscan version 1.8.2</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/>------------------------------------------------------<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">Date: 20140513-165131</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/>------------------------------------------------------<br/><br/>[*] Analyzing SSL/TLS on 192.168.1.1:443 ...<br/>    [.] Output directory: TLSSLed_1.3_192.168.1.1_443_20140513-165131 ...<br/><br/>[*] Checking if the target service speaks SSL/TLS...<br/>    [.] The target service 192.168.1.1:443 seems to speak SSL/TLS...<br/><br/>    [.] Using SSL/TLS protocol version:<br/>        (empty means I\'m using the default openssl protocol version(s))<br/><br/>[*] Running sslscan on 192.168.1.1:443 ...<br/><br/>    [-] Testing for SSLv2 ...<br/><br/>    [-] Testing for the NULL cipher ...</span></p><p><br/></p></body></html>"))
        self.TLSSLedH2.setText(_translate("MainWindow", "Usage:"))
        self.TLSSLedH1.setText(_translate("MainWindow", "Description:"))
        self.TLSSLedH3.setText(_translate("MainWindow", "Examples:"))
        self.TLSSLedButton.setText(_translate("MainWindow", "tlssled"))
        self.TLSSLedB1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\"><br/>TLSSLed is a Linux shell script whose purpose is to evaluate the security of a target SSL/TLS </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">(HTTPS) web server implementation. It is based on sslscan, a thorough SSL/TLS scanner that is </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">based on the openssl library, and on the “openssl s_client” command line tool. The current </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">tests include checking if the target supports the SSLv2 protocol, the NULL cipher, weak ciphers </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">based on their key length (40 or 56 bits), the availability of strong ciphers (like AES), if the digital </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">certificate is MD5 signed, and the current SSL/TLS renegotiation capabilities. </span></p><p><span style=\" font-size:18pt; color:#ffffff;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Source: </span><a href=\"http://www.taddong.com/en/lab.html\"><span style=\" font-size:18pt; text-decoration: underline; color:#ffffff;\">http://www.taddong.com/en/lab.html</span></a></p><p><span style=\" font-size:18pt; color:#ffffff;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Author:</span><span style=\" font-size:18pt; color:#ffffff;\"> Raul Siles, Taddong SL </span></p><p><br/></p></body></html>"))
        self.TLSSLedTitle.setText(_translate("MainWindow", "TLSSLed"))
        self.TLSSLedH4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#39b5ff;\">RUN ON TERMINAL :</span></p></body></html>"))
        self.TLSSLedB2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">tlssled<br />------------------------------------------------------<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> TLSSLed - (1.3) based on sslscan and openssl<br />                 by Raul Siles (www.taddong.com)</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />------------------------------------------------------<br />    </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">openssl version: OpenSSL 1.0.1e 11 Feb 2013<br />    sslscan version 1.8.2<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">------------------------------------------------------<br />    </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">Date: 20140520-110731</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />------------------------------------------------------<br /><br />[!] Usage: /usr/bin/tlssled &lt;hostname or IP_address&gt; &lt;port&gt;</span><span style=\" font-size:18pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"> </span><span style=\" font-size:18pt;\"> </span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TLSSLedTab), _translate("MainWindow", "TLSSLed"))
        self.twofiH1.setText(_translate("MainWindow", "Description:"))
        self.twofiH4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#39b5ff;\">RUN ON TERMINAL :</span></p></body></html>"))
        self.twofiB2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">root@kali:~# </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">twofi -h<br /></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">twofi 1.0 Robin Wood (robin@digininja.org) (www.digininja.org)<br />twofi - Twitter Words Of Interest</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br /><br /></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">Usage: </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">twofi [OPTIONS]<br />--help, -h: </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">show help</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />--count, -c: </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">include the count with the words</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />--min_word_length, -m: </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">minimum word length</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />--term_file, -T file: </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">a file containing a list of terms</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />--terms, -t: </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">comma separated usernames</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">quote words containing spaces, no space after commas</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />--user_file, -U file: </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">a file containing a list of users</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />--users, -u: </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">comma separated search terms<br />quote words containing spaces, no space after commas</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />--verbose, -v: </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">verbose</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"> </span> </p></body></html>"))
        self.twofiB1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\"><br/></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">When attempting to crack passwords custom word lists are very useful additions to standard</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">dictionaries. An interesting idea originally released on the “7 Habits of Highly Effective</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Hackers” blog was to use Twitter to help generate those lists based on searches for keywords</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">related to the list that is being cracked. This idea has been expanded into twofi which will take</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">multiple search terms and return a word list sorted by most common first.</span></p><p><span style=\" font-size:18pt; color:#ffffff;\"><br/></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:600; color:#ffffff;\">Source: </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">http://www.digininja.org/projects/twofi.php</span></p><p><span style=\" font-size:18pt; color:#ffffff;\"><br/></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:600; color:#ffffff;\">Author:</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\"> Robin Wood</span></p><p><span style=\" color:#ffffff;\"><br/></span></p></body></html>"))
        self.twofiButton.setText(_translate("MainWindow", "twofi"))
        self.twofiH2.setText(_translate("MainWindow", "Usage:"))
        self.twofiTitle.setText(_translate("MainWindow", "twofi"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.twofiTab), _translate("MainWindow", "twofi"))
        self.urlCrazyB3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">root@kali:~# </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">urlcrazy -k dvorak -r example.com<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">URLCrazy Domain Report</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/>Domain    : example.com<br/>Keyboard  : dvorak<br/>At        : 2014-05-13 17:04:01 -0600<br/><br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"># Please wait. 95 hostnames to process</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/><br/>Typo Type              Typo            CC-A  Extn<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">---------------------------------------------------</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/>Character Omission     eample.com      ?     com<br/>Character Omission     examle.com      ?     com<br/>Character Omission     exampe.com      ?     com<br/>Character Omission     exampl.com      ?     com<br/>Character Omission     example.cm      ?     cm<br/>Character Omission     exaple.com      ?     com</span></p><p><br/></p></body></html>"))
        self.urlCrazyH2.setText(_translate("MainWindow", "Usage:"))
        self.urlCrazyH1.setText(_translate("MainWindow", "Description:"))
        self.urlCrazyH3.setText(_translate("MainWindow", "Examples:"))
        self.urlCrazyButton.setText(_translate("MainWindow", "urlcrazy"))
        self.urlCrazyB1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\"><br/></span><span style=\" font-size:18pt; color:#ffffff;\">Generate and test domain typos and variations to detect and perform typo squatting, URL </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">hijacking, phishing, and corporate espionage. </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">Features: </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-size:18pt; color:#ffffff;\">Generates 15 types of domain variants </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-size:18pt; color:#ffffff;\">Knows over 8000 common misspellings </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-size:18pt; color:#ffffff;\">Supports cosmic ray induced bit flipping </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-size:18pt; color:#ffffff;\">Multiple keyboard layouts (qwerty, azerty, qwertz, dvorak) </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-size:18pt; color:#ffffff;\">Checks if a domain variant is valid </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-size:18pt; color:#ffffff;\">Test if domain variants are in use </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-size:18pt; color:#ffffff;\">Estimate popularity of a domain variant </span></p><p><span style=\" color:#ffffff;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Source: </span><span style=\" font-size:18pt; color:#ffffff;\">http://www.morningstarsecurity.com/research/urlcrazy </span></p><p><span style=\" color:#ffffff;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Author:</span><span style=\" font-size:18pt; color:#ffffff;\"> Andrew Horton </span></p><p><br/></p></body></html>"))
        self.urlCrazyTitle.setText(_translate("MainWindow", "UrlCrazy"))
        self.urlCrazyH4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#39b5ff;\">RUN ON TERMINAL :</span></p></body></html>"))
        self.urlCrazyB2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">urlcrazy -h<br /></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">URLCrazy version 0.5<br />by Andrew Horton (urbanadventurer)<br />http://www.morningstarsecurity.com/research/urlcrazy<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Generate and test domain typos and variations to detect and perform typo squatting, URL hijacking,<br />phishing, and corporate espionage.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\"><br />Supports the following domain variations:<br />Character omission, character repeat, adjacent character swap, adjacent character replacement, double<br />character replacement, adjacent character insertion, missing dot, strip dashes, singular or pluralise,<br />common misspellings, vowel swaps, homophones, bit flipping (cosmic rays), homoglyphs, wrong top level<br />domain, and wrong second level domain.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /><br /></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:600; color:#ffffff;\">Usage:</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">/usr/bin/urlcrazy [options] domain<br /><br /></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Options</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /> -k, --keyboard=LAYOUT  </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Options are: qwerty, azerty, qwertz, dvorak (default: qwerty)</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /> -p, --popularity   </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Check domain popularity with Google</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /> -r, --no-resolve   </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Do not resolve DNS</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /> -i, --show-invalid </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Show invalid domain names</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /> -f, --format=TYPE  </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Human readable or CSV (default: human readable)</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /> -o, --output=FILE  </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Output file</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /> -h, --help     </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">This help</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /> -v, --version      </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Print version information. This version is 0.5</span><span style=\" font-size:18pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"> </span><span style=\" font-size:18pt;\"> </span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.urlCrazyTab), _translate("MainWindow", "UrlCrazy"))
        self.WiresharkB3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">root@kali:~# </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">wireshark</span></p><p/></body></html>"))
        self.WiresharkH2.setText(_translate("MainWindow", "Usage:"))
        self.WiresharkH1.setText(_translate("MainWindow", "Description:"))
        self.WiresharkH3.setText(_translate("MainWindow", "Examples:"))
        self.WiresharkButton.setText(_translate("MainWindow", "wireshark"))
        self.WiresharkB1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\"><br/></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Wireshark is the world’s foremost network protocol analyzer. It lets you see what’s happening</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">on your network at a microscopic level. It is the de facto (and often de jure) standard across</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">many industries and educational institutions. Wireshark development thrives thanks to the</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">contributions of networking experts across the globe. It is the continuation of a project that</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">started in 1998. </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Wireshark has a rich feature set which includes the following:</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Deep inspection of hundreds of protocols, with more being added all the time</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Live capture and offline analysis</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Standard three-pane packet browser</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Multi-platform: Runs on Windows, Linux, OS X, Solaris, FreeBSD, NetBSD, and many others</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Captured network data can be browsed via a GUI, or via the TTY-mode TShark utility</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">The most powerful display filters in the industry</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Rich VoIP analysis</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Capture files compressed with gzip can be decompressed on the fly</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Live data can be read from Ethernet, IEEE 802.11, PPP/HDLC, ATM, Bluetooth, USB, Token Ring, Frame Relay, FDDI, </span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">and others (depending on your platform)</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Coloring rules can be applied to the packet list for quick, intuitive analysis</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Output can be exported to XML, PostScript®, CSV, or plain text</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Decryption support for many protocols, including IPsec, ISAKMP, Kerberos, SNMPv3, SSL/TLS, WEP, and WPA/WPA2</span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Read/write many different capture file formats: tcpdump (libpcap), Pcap NG, Catapult DCT2000, Cisco Secure IDS iplog, </span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Microsoft Network Monitor, Network * General Sniffer® (compressed and uncompressed), Sniffer® Pro, and NetXray®, </span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Network Instruments Observer, NetScreen snoop, Novell LANalyzer, RADCOM WAN/LAN Analyzer, Shomiti/Finisar </span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Surveyor, Tektronix K12xx, Visual Networks Visual UpTime, WildPackets EtherPeek/TokenPeek/AiroPeek, and many others</span></p><p><span style=\" font-size:18pt; color:#ffffff;\"><br/></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:600; color:#ffffff;\">Source:</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\"> http://www.wireshark.org/about.html</span></p><p><span style=\" font-size:18pt; color:#ffffff;\"><br/></span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:600; color:#ffffff;\">Author:</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\"> Gerald Combs and contributors</span></p><p><br/></p></body></html>"))
        self.WiresharkTitle.setText(_translate("MainWindow", "Wireshark"))
        self.WiresharkH4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#39b5ff;\">RUN ON TERMINAL :</span></p></body></html>"))
        self.WiresharkB2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">wireshark -h<br /></span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">Wireshark 1.10.2 (SVN Rev 51934 from /trunk-1.10)<br />Interactively dump and analyze network traffic.<br />See http://www.wireshark.org for more information.<br /><br />Copyright 1998-2013 Gerald Combs &lt;gerald@wireshark.org&gt; and contributors.<br />This is free software; see the source for copying conditions. There is NO<br />warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br /><br /></span><span style=\" font-family:\'Times New Roman\'; font-weight:600; color:#ffffff;\">Usage:</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">wireshark [options] ... [ &lt;infile&gt; ]<br /><br /></span><span style=\" font-family:\'Times New Roman\'; font-weight:600; color:#ffffff;\">Capture interface:</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -i &lt;interface&gt;           </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">name or idx of interface (def: first non-loopback)</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -f &lt;capture filter&gt;      </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">packet filter in libpcap filter syntax</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -s &lt;snaplen&gt;             </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">packet snapshot length (def: 65535)</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -p                       </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">don\'t capture in promiscuous mode</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -k                       </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">start capturing immediately (def: do nothing)<br /></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">  -S                       </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">update packet display when new packets are captured<br /></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">  -l                       </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">turn on automatic scrolling while -S is in use<br /></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">  -I                       </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">capture in monitor mode, if available</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -B &lt;buffer size&gt;         </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">size of kernel buffer (def: 2MB)<br /></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">  -y &lt;link type&gt;           </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">link layer type (def: first appropriate)</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -D                       </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">print list of interfaces and exit</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -L                       </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">print list of link-layer types of iface and exit</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br /><br /></span><span style=\" font-family:\'Times New Roman\'; font-weight:600; color:#ffffff;\">Capture stop conditions:</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -c &lt;packet count&gt;        </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">stop after n packets (def: infinite)</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -a &lt;autostop cond.&gt; ...  </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">duration:NUM - stop after NUM seconds</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />                           </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">filesize:NUM - stop this file after NUM KB</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />                              </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">files:NUM - stop after NUM files</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Times New Roman\'; font-weight:600; color:#ffffff;\">Capture output:</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -b &lt;ringbuffer opt.&gt; ... </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">duration:NUM - switch to next file after NUM secs<br /></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">                           </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">filesize:NUM - switch to next file after NUM KB<br /></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">                              </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">files:NUM - ringbuffer: replace after NUM files<br /></span><span style=\" font-family:\'Times New Roman\'; font-weight:600; color:#ffffff;\">Input file:<br /></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">  -r &lt;infile&gt;              </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">set the filename to read from (no pipes or stdin!)<br /></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Times New Roman\'; font-weight:600; color:#ffffff;\">Processing:</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -R &lt;read filter&gt;         </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">packet filter in Wireshark display filter syntax<br /></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">  -n                       </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">disable all name resolutions (def: all enabled)<br /></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">  -N &lt;name resolve flags&gt;  </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">enable specific name resolution(s): &quot;mntC&quot;<br /></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Times New Roman\'; font-weight:600; color:#ffffff;\">User interface:</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -C &lt;config profile&gt;      </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">start with specified configuration profile<br /></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">  -Y &lt;display filter&gt;      </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">start with the given display filter</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -g &lt;packet number&gt;       </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">go to specified packet number after </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">&quot;-r&quot;<br />  -J &lt;jump filter&gt;         </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">jump to the first packet matching the (display)<br /></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">                           </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">filter</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -j                       </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">search backwards for a matching packet after &quot;-J&quot;<br /></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">  -m &lt;font&gt;                </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">set the font name used for most text<br /></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">  -t a|ad|d|dd|e|r|u|ud    </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">output format of time stamps (def: r: rel. to first)<br /></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">  -u s|hms                 </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">output format of seconds (def: s: seconds)<br /></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">  -X &lt;key&gt;:&lt;value&gt;         </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">eXtension options, see man page for details<br /></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">  -z &lt;statistics&gt;          </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">show various statistics, see man page for details<br /></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Times New Roman\'; font-weight:600; color:#ffffff;\">Output:</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -w &lt;outfile|-&gt;           </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">set the output filename (or \'-\' for stdout)<br /></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br /></span><span style=\" font-family:\'Times New Roman\'; font-weight:600; color:#ffffff;\">Miscellaneous:</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -h                       </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">display this help and exit<br /></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">  -v                       </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">display version info and exit<br /></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">  -P &lt;key&gt;:&lt;path&gt;          </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">persconf:path - personal configuration files<br />                               persdata:path - personal data fi</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#ffffff;\">les</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -o &lt;name&gt;:&lt;value&gt; ...    </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">override preference or recent setting</span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"><br />  -K &lt;keytab&gt;              </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">keytab file to use for kerberos decryption<br /></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\">  --display=DISPLAY   </span><span style=\" font-family:\'Times New Roman\'; color:#ffffff;\">     X display to use</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-weight:600; color:#00b0f0;\"> </span> </p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.WiresharkTab), _translate("MainWindow", "Wireshark"))
        self.WOLEB3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">root@kali:~# </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">wol-e -f<br/><br/>    [*] WOL-E 1.0 [*]<br/>    [*] Wake on LAN Explorer - Scan for Apple devices.<br/><br/>    [*] arping 192.168.1.0/24 on eth0<br/>    [*] Apple device detected: de:ad:be:ef:46:32 192.168.1.12. saving to AppleTargets.txt</span><span style=\" font-size:18pt;\"/></p><p><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"/><span style=\" font-size:18pt;\"/></p></body></html>"))
        self.WOLEH2.setText(_translate("MainWindow", "Usage:"))
        self.WOLEH1.setText(_translate("MainWindow", "Description:"))
        self.WOLEH3.setText(_translate("MainWindow", "Examples:"))
        self.WOLEButton.setText(_translate("MainWindow", "wol-e"))
        self.WOLEB1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\"><br/></span><span style=\" font-size:18pt; color:#ffffff;\">WOL-E is a suite of tools for the Wake on LAN feature of network attached computers, this is </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">now enabled by default on many Apple computers. These tools include: </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-size:18pt; color:#ffffff;\">Bruteforcing the MAC address to wake up clients </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-size:18pt; color:#ffffff;\">Sniffing WOL attempts on the network and saving them to disk </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-size:18pt; color:#ffffff;\">Sniffing WOL passwords on the network and saving them to disk </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-size:18pt; color:#ffffff;\">Waking up single clients (post sniffing attack) </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-size:18pt; color:#ffffff;\">Scanning for Apple devices on the network for WOL enabling </span></p><p><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#ffffff;\">·</span><span style=\" font-size:18pt; color:#ffffff;\">Sending bulk WOL requests to all detected Apple clients </span></p><p><span style=\" color:#ffffff;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Source:</span><span style=\" font-size:18pt; color:#ffffff;\"> https://code.google.com/p/wol-e/ </span></p><p><span style=\" color:#ffffff;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Author:</span><span style=\" font-size:18pt; color:#ffffff;\"> Nathaniel Carew </span></p><p><span style=\" color:#ffffff;\"><br/></span></p></body></html>"))
        self.WOLETitle.setText(_translate("MainWindow", "WOL-E"))
        self.WOLEH4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#39b5ff;\">RUN ON TERMINAL :</span></p></body></html>"))
        self.WOLEB2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">wol-e -h<br /><br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">[*] WOL-E 1.0<br />[*] Wake on LAN Explorer - A collection a WOL tools.<br />[*] by Nathaniel Carew</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /><br />    -m<br />       </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\"> Waking up single computers.<br />        If a password is required use the -k 00:12:34:56:78:90 at the end of the above command.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />        wol-e -m 00:12:34:56:78:90 -b 192.168.1.255 -p &lt;port&gt; -k &lt;pass&gt;<br />        Defaults:<br />        Port: 9<br />        Broadcast: 255.255.255.255<br />        Pass: empty<br /><br />    -s<br />        </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">Sniffing the network for WOL requests and passwords.<br />        All captured WOL requests will be displayed on screen and written to /usr/share/wol-e/WOLClients.txt.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />        wol-e -s -i eth0<br /><br />    -a<br />        </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:600; color:#ffffff;\">Bruteforce powering on WOL clients.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />        wol-e -a -p &lt;port&gt;<br />        </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:600; color:#ffffff;\">Place the address ranges into the bfmac.lst that you wish to bruteforce.<br />        They should be in the following format:</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />        00:12:34:56<br />        Default port: 9<br /><br />    -f<br />       </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:600; color:#ffffff;\"> Detecting Apple devices on the network for WOL enabling.<br />        This will output to the screen and write to /usr/share/wol-e/AppleTargets.txt for detected Apple MAC\'s.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />        wol-e -f<br /><br />    -fa<br />        </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:600; color:#ffffff;\">Attempt to wake all detected Apple targets in /usr/share/wol-e/AppleTargets.txt.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />        </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:600; color:#ffffff;\">This will send a single WOL packet to each client in the list and tell you how many clients were attempted.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />        wol-e -fa</span><span style=\" font-size:18pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"> </span><span style=\" font-size:18pt;\"> </span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.WOLETab), _translate("MainWindow", "WOL-E"))
        self.XplicoB3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\">root@kali:~# </span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">xplico -m rltm -i eth0<br/>xplico v1.0.1<br/></span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">Internet Traffic Decoder (NFAT).<br/>See http://www.xplico.org for more information.<br/><br/>Copyright 2007-2012 Gianluca Costa &amp; Andrea de Franceschi and contributors.<br/>This is free software; see the source for copying conditions. There is NO<br/>warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.<br/><br/>This product includes GeoLite data created by MaxMind, available from http://www.maxmind.com/.<br/>Configuration file (/opt/xplico/cfg/xplico_cli.cfg) found!<br/>GeoLiteCity.dat found!</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br/>pcapf: running: 0/0, subflow:0/0, tot pkt:1<br/>pol: running: 0/0, subflow:0/0, tot pkt:0<br/>eth: running: 0/0, subflow:0/0, tot pkt:1<br/>pppoe: running: 0/0, subflow:0/0, tot pkt:0<br/>ppp: running: 0/0, subflow:0/0, tot pkt:0<br/>ip: running: 0/0, subflow:0/0, tot pkt:0</span><span style=\" font-size:18pt;\"/></p><p><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"/><span style=\" font-size:18pt;\"/></p></body></html>"))
        self.XplicoH2.setText(_translate("MainWindow", "Usage:"))
        self.XplicoH1.setText(_translate("MainWindow", "Description:"))
        self.XplicoH3.setText(_translate("MainWindow", "Examples:"))
        self.XplicoButton.setText(_translate("MainWindow", "xplico"))
        self.XplicoB1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; color:#ffffff;\">The goal of Xplico is extract from an internet traffic capture the applications data contained. For </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">example, from a pcap file Xplico extracts each email (POP, IMAP, and SMTP protocols), all HTTP </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">contents, each VoIP call (SIP, MGCP, H323), FTP, TFTP, and so on. Xplico is not a network </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">protocol analyzer. </span></p><p><span style=\" font-size:18pt;\"><br/></span><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Author:</span><span style=\" font-size:18pt; color:#ffffff;\"> Gianluca Costa, Andre de Franceschi </span></p><p><br/></p></body></html>"))
        self.XplicoTitle.setText(_translate("MainWindow", "Xplico"))
        self.XplicoH4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#39b5ff;\">RUN ON TERMINAL :</span></p></body></html>"))
        self.XplicoB2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">xplico -h<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">xplico v1.0.1<br />Internet Traffic Decoder (NFAT).<br />See http://www.xplico.org for more information.<br /><br />Copyright 2007-2012 Gianluca Costa &amp; Andrea de Franceschi and contributors.<br />This is free software; see the source for copying conditions. There is NO<br />warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /><br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; color:#ffffff;\">This product includes GeoLite data created by MaxMind, available from http://www.maxmind.com/.</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br /><br />usage: xplico [-v] [-c &lt;config_file&gt;] [-h] [-g] [-l] [-i &lt;prot&gt;] -m &lt;capute_module&gt;<br />    -v </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">version</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />    -c </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">config file</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />    -h </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">this help</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />    -i</span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\"> info</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#ffffff;\"> </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">of protocol \'prot\'</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />    -g </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">display graph-tree of protocols</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />    -l </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">print all log in the screen</span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"><br />    -m </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">capture type module<br /></span><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\">    </span><span style=\" font-family:\'Times New Roman\'; font-size:18pt; color:#ffffff;\">NOTE: parameters MUST respect this order!</span><span style=\" font-size:18pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:18pt; font-weight:600; color:#00b0f0;\"> </span><span style=\" font-size:18pt;\"> </span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.XplicoTab), _translate("MainWindow", "Xplico"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Kali Tools"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "Information Gathering"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "acccheck"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "ace-voip"))
        self.treeWidget.topLevelItem(0).child(2).setText(0, _translate("MainWindow", "Amap"))
        self.treeWidget.topLevelItem(0).child(3).setText(0, _translate("MainWindow", "Automater"))
        self.treeWidget.topLevelItem(0).child(4).setText(0, _translate("MainWindow", "bing-ip2hosts"))
        self.treeWidget.topLevelItem(0).child(5).setText(0, _translate("MainWindow", "braa"))
        self.treeWidget.topLevelItem(0).child(6).setText(0, _translate("MainWindow", "CaseFile"))
        self.treeWidget.topLevelItem(0).child(7).setText(0, _translate("MainWindow", "CDPSnarf"))
        self.treeWidget.topLevelItem(0).child(8).setText(0, _translate("MainWindow", "cisco-torch"))
        self.treeWidget.topLevelItem(0).child(9).setText(0, _translate("MainWindow", "Cookie Cadger"))
        self.treeWidget.topLevelItem(0).child(10).setText(0, _translate("MainWindow", "copy-router-config"))
        self.treeWidget.topLevelItem(0).child(11).setText(0, _translate("MainWindow", "DMitry"))
        self.treeWidget.topLevelItem(0).child(12).setText(0, _translate("MainWindow", "dnmap"))
        self.treeWidget.topLevelItem(0).child(13).setText(0, _translate("MainWindow", "dsenum"))
        self.treeWidget.topLevelItem(0).child(14).setText(0, _translate("MainWindow", "dnsmap"))
        self.treeWidget.topLevelItem(0).child(15).setText(0, _translate("MainWindow", "DNSRecon"))
        self.treeWidget.topLevelItem(0).child(16).setText(0, _translate("MainWindow", "dnstracer"))
        self.treeWidget.topLevelItem(0).child(17).setText(0, _translate("MainWindow", "dnswalk"))
        self.treeWidget.topLevelItem(0).child(18).setText(0, _translate("MainWindow", "DotDotPwn"))
        self.treeWidget.topLevelItem(0).child(19).setText(0, _translate("MainWindow", "enum4linux"))
        self.treeWidget.topLevelItem(0).child(20).setText(0, _translate("MainWindow", "enumIAX"))
        self.treeWidget.topLevelItem(0).child(21).setText(0, _translate("MainWindow", "Faraday"))
        self.treeWidget.topLevelItem(0).child(22).setText(0, _translate("MainWindow", "Fierce"))
        self.treeWidget.topLevelItem(0).child(23).setText(0, _translate("MainWindow", "Firewalk"))
        self.treeWidget.topLevelItem(0).child(24).setText(0, _translate("MainWindow", "fragroute"))
        self.treeWidget.topLevelItem(0).child(25).setText(0, _translate("MainWindow", "fragrouter"))
        self.treeWidget.topLevelItem(0).child(26).setText(0, _translate("MainWindow", "Ghost Phisher"))
        self.treeWidget.topLevelItem(0).child(27).setText(0, _translate("MainWindow", "GoLismero"))
        self.treeWidget.topLevelItem(0).child(28).setText(0, _translate("MainWindow", "goofile"))
        self.treeWidget.topLevelItem(0).child(29).setText(0, _translate("MainWindow", "hping3"))
        self.treeWidget.topLevelItem(0).child(30).setText(0, _translate("MainWindow", "ident-user-enum"))
        self.treeWidget.topLevelItem(0).child(31).setText(0, _translate("MainWindow", "InTrace"))
        self.treeWidget.topLevelItem(0).child(32).setText(0, _translate("MainWindow", "iSMTP"))
        self.treeWidget.topLevelItem(0).child(33).setText(0, _translate("MainWindow", "Ibd"))
        self.treeWidget.topLevelItem(0).child(34).setText(0, _translate("MainWindow", "Maltego Teeth"))
        self.treeWidget.topLevelItem(0).child(35).setText(0, _translate("MainWindow", "masscan"))
        self.treeWidget.topLevelItem(0).child(36).setText(0, _translate("MainWindow", "Metagoofil"))
        self.treeWidget.topLevelItem(0).child(37).setText(0, _translate("MainWindow", "Miranda"))
        self.treeWidget.topLevelItem(0).child(38).setText(0, _translate("MainWindow", "nbtscan-unixwiz"))
        self.treeWidget.topLevelItem(0).child(39).setText(0, _translate("MainWindow", "Nmap"))
        self.treeWidget.topLevelItem(0).child(40).setText(0, _translate("MainWindow", "ntop"))
        self.treeWidget.topLevelItem(0).child(41).setText(0, _translate("MainWindow", "p0f"))
        self.treeWidget.topLevelItem(0).child(42).setText(0, _translate("MainWindow", "Parsero"))
        self.treeWidget.topLevelItem(0).child(43).setText(0, _translate("MainWindow", "Recon-ng"))
        self.treeWidget.topLevelItem(0).child(44).setText(0, _translate("MainWindow", "SET"))
        self.treeWidget.topLevelItem(0).child(45).setText(0, _translate("MainWindow", "smtp-user-enum"))
        self.treeWidget.topLevelItem(0).child(46).setText(0, _translate("MainWindow", "snmp-check"))
        self.treeWidget.topLevelItem(0).child(47).setText(0, _translate("MainWindow", "SPARTA"))
        self.treeWidget.topLevelItem(0).child(48).setText(0, _translate("MainWindow", "sslcaudit"))
        self.treeWidget.topLevelItem(0).child(49).setText(0, _translate("MainWindow", "SSLsplit"))
        self.treeWidget.topLevelItem(0).child(50).setText(0, _translate("MainWindow", "sslstrip"))
        self.treeWidget.topLevelItem(0).child(51).setText(0, _translate("MainWindow", "SSLyze"))
        self.treeWidget.topLevelItem(0).child(52).setText(0, _translate("MainWindow", "THC-IPV6"))
        self.treeWidget.topLevelItem(0).child(53).setText(0, _translate("MainWindow", "theHarvester"))
        self.treeWidget.topLevelItem(0).child(54).setText(0, _translate("MainWindow", "TLSSLed"))
        self.treeWidget.topLevelItem(0).child(55).setText(0, _translate("MainWindow", "twofi"))
        self.treeWidget.topLevelItem(0).child(56).setText(0, _translate("MainWindow", "URLCrazy"))
        self.treeWidget.topLevelItem(0).child(57).setText(0, _translate("MainWindow", "Wireshark"))
        self.treeWidget.topLevelItem(0).child(58).setText(0, _translate("MainWindow", "WOL-E"))
        self.treeWidget.topLevelItem(0).child(59).setText(0, _translate("MainWindow", "Xplico"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "Sniffing & Spoofing"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "Burp Suite"))
        self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "DNSChef"))
        self.treeWidget.topLevelItem(1).child(2).setText(0, _translate("MainWindow", "fiked"))
        self.treeWidget.topLevelItem(1).child(3).setText(0, _translate("MainWindow", "hamster-sidejack"))
        self.treeWidget.topLevelItem(1).child(4).setText(0, _translate("MainWindow", "HexInject"))
        self.treeWidget.topLevelItem(1).child(5).setText(0, _translate("MainWindow", "iaxflood"))
        self.treeWidget.topLevelItem(1).child(6).setText(0, _translate("MainWindow", "inviteflood"))
        self.treeWidget.topLevelItem(1).child(7).setText(0, _translate("MainWindow", "iSMTP"))
        self.treeWidget.topLevelItem(1).child(8).setText(0, _translate("MainWindow", "isr-evilgrade"))
        self.treeWidget.topLevelItem(1).child(9).setText(0, _translate("MainWindow", "mitmproxy"))
        self.treeWidget.topLevelItem(1).child(10).setText(0, _translate("MainWindow", "ohrwurm"))
        self.treeWidget.topLevelItem(1).child(11).setText(0, _translate("MainWindow", "protos-sip"))
        self.treeWidget.topLevelItem(1).child(12).setText(0, _translate("MainWindow", "rebind"))
        self.treeWidget.topLevelItem(1).child(13).setText(0, _translate("MainWindow", "responder"))
        self.treeWidget.topLevelItem(1).child(14).setText(0, _translate("MainWindow", "rtpbreak"))
        self.treeWidget.topLevelItem(1).child(15).setText(0, _translate("MainWindow", "rtpinsertsound"))
        self.treeWidget.topLevelItem(1).child(16).setText(0, _translate("MainWindow", "rtpmixsound"))
        self.treeWidget.topLevelItem(1).child(17).setText(0, _translate("MainWindow", "sctpscan"))
        self.treeWidget.topLevelItem(1).child(18).setText(0, _translate("MainWindow", "SIPArmyKnife"))
        self.treeWidget.topLevelItem(1).child(19).setText(0, _translate("MainWindow", "SIPp"))
        self.treeWidget.topLevelItem(1).child(20).setText(0, _translate("MainWindow", "SIPVicious"))
        self.treeWidget.topLevelItem(1).child(21).setText(0, _translate("MainWindow", "SniffJoke"))
        self.treeWidget.topLevelItem(1).child(22).setText(0, _translate("MainWindow", "SSLsplit"))
        self.treeWidget.topLevelItem(1).child(23).setText(0, _translate("MainWindow", "sslstrip"))
        self.treeWidget.topLevelItem(1).child(24).setText(0, _translate("MainWindow", "THC-IPV6"))
        self.treeWidget.topLevelItem(1).child(25).setText(0, _translate("MainWindow", "VoIPHopper"))
        self.treeWidget.topLevelItem(1).child(26).setText(0, _translate("MainWindow", "WebScabar"))
        self.treeWidget.topLevelItem(1).child(27).setText(0, _translate("MainWindow", "Wifi Honey"))
        self.treeWidget.topLevelItem(1).child(28).setText(0, _translate("MainWindow", "Wireshark"))
        self.treeWidget.topLevelItem(1).child(29).setText(0, _translate("MainWindow", "xspy"))
        self.treeWidget.topLevelItem(1).child(30).setText(0, _translate("MainWindow", "Yersinia"))
        self.treeWidget.topLevelItem(1).child(31).setText(0, _translate("MainWindow", "zaproxy"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "Vulnerability Analysis"))
        self.treeWidget.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "BBQSQL"))
        self.treeWidget.topLevelItem(2).child(1).setText(0, _translate("MainWindow", "BED"))
        self.treeWidget.topLevelItem(2).child(2).setText(0, _translate("MainWindow", "cisco-auditing-tool"))
        self.treeWidget.topLevelItem(2).child(3).setText(0, _translate("MainWindow", "cisco-global-exploiter"))
        self.treeWidget.topLevelItem(2).child(4).setText(0, _translate("MainWindow", "cisco-ocs"))
        self.treeWidget.topLevelItem(2).child(5).setText(0, _translate("MainWindow", "cisco-torch"))
        self.treeWidget.topLevelItem(2).child(6).setText(0, _translate("MainWindow", "copy-router-config"))
        self.treeWidget.topLevelItem(2).child(7).setText(0, _translate("MainWindow", "DBPwAudit"))
        self.treeWidget.topLevelItem(2).child(8).setText(0, _translate("MainWindow", "Doona"))
        self.treeWidget.topLevelItem(2).child(9).setText(0, _translate("MainWindow", "DotDotPwn"))
        self.treeWidget.topLevelItem(2).child(10).setText(0, _translate("MainWindow", "Greenbone Security Assistant"))
        self.treeWidget.topLevelItem(2).child(11).setText(0, _translate("MainWindow", "GSD"))
        self.treeWidget.topLevelItem(2).child(12).setText(0, _translate("MainWindow", "HexorBase"))
        self.treeWidget.topLevelItem(2).child(13).setText(0, _translate("MainWindow", "Inguma"))
        self.treeWidget.topLevelItem(2).child(14).setText(0, _translate("MainWindow", "jSQL"))
        self.treeWidget.topLevelItem(2).child(15).setText(0, _translate("MainWindow", "Lynis"))
        self.treeWidget.topLevelItem(2).child(16).setText(0, _translate("MainWindow", "Nmap"))
        self.treeWidget.topLevelItem(2).child(17).setText(0, _translate("MainWindow", "ohrwurm"))
        self.treeWidget.topLevelItem(2).child(18).setText(0, _translate("MainWindow", "openvas-adminstrator"))
        self.treeWidget.topLevelItem(2).child(19).setText(0, _translate("MainWindow", "openvas-scanner"))
        self.treeWidget.topLevelItem(2).child(20).setText(0, _translate("MainWindow", "Oscanner"))
        self.treeWidget.topLevelItem(2).child(21).setText(0, _translate("MainWindow", "sfuzz"))
        self.treeWidget.topLevelItem(2).child(22).setText(0, _translate("MainWindow", "SidGuesser"))
        self.treeWidget.topLevelItem(2).child(23).setText(0, _translate("MainWindow", "SIPArmyKnife"))
        self.treeWidget.topLevelItem(2).child(24).setText(0, _translate("MainWindow", "sqlmap"))
        self.treeWidget.topLevelItem(2).child(25).setText(0, _translate("MainWindow", "Sqlninja"))
        self.treeWidget.topLevelItem(2).child(26).setText(0, _translate("MainWindow", "sqlsus"))
        self.treeWidget.topLevelItem(2).child(27).setText(0, _translate("MainWindow", "THC-IPV6"))
        self.treeWidget.topLevelItem(2).child(28).setText(0, _translate("MainWindow", "tnscmd10g"))
        self.treeWidget.topLevelItem(2).child(29).setText(0, _translate("MainWindow", "unix-privesc-check"))
        self.treeWidget.topLevelItem(2).child(30).setText(0, _translate("MainWindow", "Yersinia"))
        self.treeWidget.topLevelItem(3).setText(0, _translate("MainWindow", "Exploitation"))
        self.treeWidget.topLevelItem(3).child(0).setText(0, _translate("MainWindow", "Armitage"))
        self.treeWidget.topLevelItem(3).child(1).setText(0, _translate("MainWindow", "Backdoor Factory"))
        self.treeWidget.topLevelItem(3).child(2).setText(0, _translate("MainWindow", "BeEF"))
        self.treeWidget.topLevelItem(3).child(3).setText(0, _translate("MainWindow", "cisco-auditing-tool"))
        self.treeWidget.topLevelItem(3).child(4).setText(0, _translate("MainWindow", "cisco-global-exploiter"))
        self.treeWidget.topLevelItem(3).child(5).setText(0, _translate("MainWindow", "cisco-ocs"))
        self.treeWidget.topLevelItem(3).child(6).setText(0, _translate("MainWindow", "cisco-torch"))
        self.treeWidget.topLevelItem(3).child(7).setText(0, _translate("MainWindow", "Commix"))
        self.treeWidget.topLevelItem(3).child(8).setText(0, _translate("MainWindow", "crackle"))
        self.treeWidget.topLevelItem(3).child(9).setText(0, _translate("MainWindow", "jboss-autopwn"))
        self.treeWidget.topLevelItem(3).child(10).setText(0, _translate("MainWindow", "Linux Exploit Suggester"))
        self.treeWidget.topLevelItem(3).child(11).setText(0, _translate("MainWindow", "Maltego Teeth"))
        self.treeWidget.topLevelItem(3).child(12).setText(0, _translate("MainWindow", "SET"))
        self.treeWidget.topLevelItem(3).child(13).setText(0, _translate("MainWindow", "ShellNoob"))
        self.treeWidget.topLevelItem(3).child(14).setText(0, _translate("MainWindow", "sqlmap"))
        self.treeWidget.topLevelItem(3).child(15).setText(0, _translate("MainWindow", "THC-IPV6"))
        self.treeWidget.topLevelItem(3).child(16).setText(0, _translate("MainWindow", "Yersinia"))
        self.treeWidget.topLevelItem(4).setText(0, _translate("MainWindow", "Password Attacks"))
        self.treeWidget.topLevelItem(4).child(0).setText(0, _translate("MainWindow", "acccheck"))
        self.treeWidget.topLevelItem(4).child(1).setText(0, _translate("MainWindow", "Burp Suite"))
        self.treeWidget.topLevelItem(4).child(2).setText(0, _translate("MainWindow", "CeWL"))
        self.treeWidget.topLevelItem(4).child(3).setText(0, _translate("MainWindow", "chnptw"))
        self.treeWidget.topLevelItem(4).child(4).setText(0, _translate("MainWindow", "cisco-auditing-tool"))
        self.treeWidget.topLevelItem(4).child(5).setText(0, _translate("MainWindow", "CmosPwd"))
        self.treeWidget.topLevelItem(4).child(6).setText(0, _translate("MainWindow", "creddump"))
        self.treeWidget.topLevelItem(4).child(7).setText(0, _translate("MainWindow", "crunch"))
        self.treeWidget.topLevelItem(4).child(8).setText(0, _translate("MainWindow", "DBPwAudit"))
        self.treeWidget.topLevelItem(4).child(9).setText(0, _translate("MainWindow", "findmyhash"))
        self.treeWidget.topLevelItem(4).child(10).setText(0, _translate("MainWindow", "gpp-decrypt"))
        self.treeWidget.topLevelItem(4).child(11).setText(0, _translate("MainWindow", "hash-identifier"))
        self.treeWidget.topLevelItem(4).child(12).setText(0, _translate("MainWindow", "HexorBase"))
        self.treeWidget.topLevelItem(4).child(13).setText(0, _translate("MainWindow", "THC-Hydra"))
        self.treeWidget.topLevelItem(4).child(14).setText(0, _translate("MainWindow", "John the Ripper"))
        self.treeWidget.topLevelItem(4).child(15).setText(0, _translate("MainWindow", "Johnny"))
        self.treeWidget.topLevelItem(4).child(16).setText(0, _translate("MainWindow", "keimpx"))
        self.treeWidget.topLevelItem(4).child(17).setText(0, _translate("MainWindow", "Maltego Teeth"))
        self.treeWidget.topLevelItem(4).child(18).setText(0, _translate("MainWindow", "Maskprocessor"))
        self.treeWidget.topLevelItem(4).child(19).setText(0, _translate("MainWindow", "multiforcer"))
        self.treeWidget.topLevelItem(4).child(20).setText(0, _translate("MainWindow", "Ncrack"))
        self.treeWidget.topLevelItem(4).child(21).setText(0, _translate("MainWindow", "oclgausscrack"))
        self.treeWidget.topLevelItem(4).child(22).setText(0, _translate("MainWindow", "PACK"))
        self.treeWidget.topLevelItem(4).child(23).setText(0, _translate("MainWindow", "patator"))
        self.treeWidget.topLevelItem(4).child(24).setText(0, _translate("MainWindow", "phrasendrescher"))
        self.treeWidget.topLevelItem(4).child(25).setText(0, _translate("MainWindow", "polenum"))
        self.treeWidget.topLevelItem(4).child(26).setText(0, _translate("MainWindow", "RainbowCrack"))
        self.treeWidget.topLevelItem(4).child(27).setText(0, _translate("MainWindow", "rcracki-mt"))
        self.treeWidget.topLevelItem(4).child(28).setText(0, _translate("MainWindow", "RSMangler"))
        self.treeWidget.topLevelItem(4).child(29).setText(0, _translate("MainWindow", "SQLdict"))
        self.treeWidget.topLevelItem(4).child(30).setText(0, _translate("MainWindow", "Statsprocessor"))
        self.treeWidget.topLevelItem(4).child(31).setText(0, _translate("MainWindow", "THC-pptp-bruter"))
        self.treeWidget.topLevelItem(4).child(32).setText(0, _translate("MainWindow", "TrueCrack"))
        self.treeWidget.topLevelItem(4).child(33).setText(0, _translate("MainWindow", "WebScarab"))
        self.treeWidget.topLevelItem(4).child(34).setText(0, _translate("MainWindow", "wordlists"))
        self.treeWidget.topLevelItem(4).child(35).setText(0, _translate("MainWindow", "zaproxy"))
        self.treeWidget.topLevelItem(5).setText(0, _translate("MainWindow", "Wireless Attacks"))
        self.treeWidget.topLevelItem(5).child(0).setText(0, _translate("MainWindow", "Aircrack-ng"))
        self.treeWidget.topLevelItem(5).child(1).setText(0, _translate("MainWindow", "Asleap"))
        self.treeWidget.topLevelItem(5).child(2).setText(0, _translate("MainWindow", "Bluelog"))
        self.treeWidget.topLevelItem(5).child(3).setText(0, _translate("MainWindow", "BlueMaho"))
        self.treeWidget.topLevelItem(5).child(4).setText(0, _translate("MainWindow", "Bluepot"))
        self.treeWidget.topLevelItem(5).child(5).setText(0, _translate("MainWindow", "BlueRanger"))
        self.treeWidget.topLevelItem(5).child(6).setText(0, _translate("MainWindow", "Bluesnarfer"))
        self.treeWidget.topLevelItem(5).child(7).setText(0, _translate("MainWindow", "Bully"))
        self.treeWidget.topLevelItem(5).child(8).setText(0, _translate("MainWindow", "coWPAtty"))
        self.treeWidget.topLevelItem(5).child(9).setText(0, _translate("MainWindow", "crackle"))
        self.treeWidget.topLevelItem(5).child(10).setText(0, _translate("MainWindow", "eapmd5pass"))
        self.treeWidget.topLevelItem(5).child(11).setText(0, _translate("MainWindow", "Fern Wifi Cracker"))
        self.treeWidget.topLevelItem(5).child(12).setText(0, _translate("MainWindow", "Ghost Phisher"))
        self.treeWidget.topLevelItem(5).child(13).setText(0, _translate("MainWindow", "GISKismet"))
        self.treeWidget.topLevelItem(5).child(14).setText(0, _translate("MainWindow", "Gqrx"))
        self.treeWidget.topLevelItem(5).child(15).setText(0, _translate("MainWindow", "gr-scan"))
        self.treeWidget.topLevelItem(5).child(16).setText(0, _translate("MainWindow", "hostapd-wpe"))
        self.treeWidget.topLevelItem(5).child(17).setText(0, _translate("MainWindow", "kalibrate-rtl"))
        self.treeWidget.topLevelItem(5).child(18).setText(0, _translate("MainWindow", "KillerBee"))
        self.treeWidget.topLevelItem(5).child(19).setText(0, _translate("MainWindow", "Kismet"))
        self.treeWidget.topLevelItem(5).child(20).setText(0, _translate("MainWindow", "mdk3"))
        self.treeWidget.topLevelItem(5).child(21).setText(0, _translate("MainWindow", "mfcuk"))
        self.treeWidget.topLevelItem(5).child(22).setText(0, _translate("MainWindow", "mfoc"))
        self.treeWidget.topLevelItem(5).child(23).setText(0, _translate("MainWindow", "mfterm"))
        self.treeWidget.topLevelItem(5).child(24).setText(0, _translate("MainWindow", "Multimon-NG"))
        self.treeWidget.topLevelItem(5).child(25).setText(0, _translate("MainWindow", "PixieWPS"))
        self.treeWidget.topLevelItem(5).child(26).setText(0, _translate("MainWindow", "Reaver"))
        self.treeWidget.topLevelItem(5).child(27).setText(0, _translate("MainWindow", "redfang"))
        self.treeWidget.topLevelItem(5).child(28).setText(0, _translate("MainWindow", "RTLSDR Scanner"))
        self.treeWidget.topLevelItem(5).child(29).setText(0, _translate("MainWindow", "Spooftooph"))
        self.treeWidget.topLevelItem(5).child(30).setText(0, _translate("MainWindow", "Wifi Honey"))
        self.treeWidget.topLevelItem(5).child(31).setText(0, _translate("MainWindow", "wifiphisher"))
        self.treeWidget.topLevelItem(5).child(32).setText(0, _translate("MainWindow", "Wifitap"))
        self.treeWidget.topLevelItem(5).child(33).setText(0, _translate("MainWindow", "Wifite"))
        self.treeWidget.topLevelItem(6).setText(0, _translate("MainWindow", "Forensics"))
        self.treeWidget.topLevelItem(6).child(0).setText(0, _translate("MainWindow", "Binwalk"))
        self.treeWidget.topLevelItem(6).child(1).setText(0, _translate("MainWindow", "bulk-extractor"))
        self.treeWidget.topLevelItem(6).child(2).setText(0, _translate("MainWindow", "Capstone"))
        self.treeWidget.topLevelItem(6).child(3).setText(0, _translate("MainWindow", "chntpw"))
        self.treeWidget.topLevelItem(6).child(4).setText(0, _translate("MainWindow", "Cuckoo"))
        self.treeWidget.topLevelItem(6).child(5).setText(0, _translate("MainWindow", "dc3dd"))
        self.treeWidget.topLevelItem(6).child(6).setText(0, _translate("MainWindow", "ddrescue"))
        self.treeWidget.topLevelItem(6).child(7).setText(0, _translate("MainWindow", "DFF"))
        self.treeWidget.topLevelItem(6).child(8).setText(0, _translate("MainWindow", "diStorm3"))
        self.treeWidget.topLevelItem(6).child(9).setText(0, _translate("MainWindow", "Dumpzilla"))
        self.treeWidget.topLevelItem(6).child(10).setText(0, _translate("MainWindow", "extundelete"))
        self.treeWidget.topLevelItem(6).child(11).setText(0, _translate("MainWindow", "Foremost"))
        self.treeWidget.topLevelItem(6).child(12).setText(0, _translate("MainWindow", "Galleta"))
        self.treeWidget.topLevelItem(6).child(13).setText(0, _translate("MainWindow", "Guymager"))
        self.treeWidget.topLevelItem(6).child(14).setText(0, _translate("MainWindow", "iPhone Backup Analyzer"))
        self.treeWidget.topLevelItem(6).child(15).setText(0, _translate("MainWindow", "p0f"))
        self.treeWidget.topLevelItem(6).child(16).setText(0, _translate("MainWindow", "pdf-parser"))
        self.treeWidget.topLevelItem(6).child(17).setText(0, _translate("MainWindow", "pdfid"))
        self.treeWidget.topLevelItem(6).child(18).setText(0, _translate("MainWindow", "pdgmail"))
        self.treeWidget.topLevelItem(6).child(19).setText(0, _translate("MainWindow", "peepdf"))
        self.treeWidget.topLevelItem(6).child(20).setText(0, _translate("MainWindow", "RegRipper"))
        self.treeWidget.topLevelItem(6).child(21).setText(0, _translate("MainWindow", "Volatility"))
        self.treeWidget.topLevelItem(6).child(22).setText(0, _translate("MainWindow", "Xplico"))
        self.treeWidget.topLevelItem(7).setText(0, _translate("MainWindow", "Maintaining Access"))
        self.treeWidget.topLevelItem(7).child(0).setText(0, _translate("MainWindow", "CryptCat"))
        self.treeWidget.topLevelItem(7).child(1).setText(0, _translate("MainWindow", "Cymothoa"))
        self.treeWidget.topLevelItem(7).child(2).setText(0, _translate("MainWindow", "dbd"))
        self.treeWidget.topLevelItem(7).child(3).setText(0, _translate("MainWindow", "dns2tcp"))
        self.treeWidget.topLevelItem(7).child(4).setText(0, _translate("MainWindow", "http-tunnel"))
        self.treeWidget.topLevelItem(7).child(5).setText(0, _translate("MainWindow", "HTTPTunnel"))
        self.treeWidget.topLevelItem(7).child(6).setText(0, _translate("MainWindow", "Intersect"))
        self.treeWidget.topLevelItem(7).child(7).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(7).child(8).setText(0, _translate("MainWindow", "Nishang"))
        self.treeWidget.topLevelItem(7).child(9).setText(0, _translate("MainWindow", "polenum"))
        self.treeWidget.topLevelItem(7).child(10).setText(0, _translate("MainWindow", "PowerSploit"))
        self.treeWidget.topLevelItem(7).child(11).setText(0, _translate("MainWindow", "pwnat"))
        self.treeWidget.topLevelItem(7).child(12).setText(0, _translate("MainWindow", "RidEnum"))
        self.treeWidget.topLevelItem(7).child(13).setText(0, _translate("MainWindow", "sbd"))
        self.treeWidget.topLevelItem(7).child(14).setText(0, _translate("MainWindow", "U3-Pwn"))
        self.treeWidget.topLevelItem(7).child(15).setText(0, _translate("MainWindow", "Webshells"))
        self.treeWidget.topLevelItem(7).child(16).setText(0, _translate("MainWindow", "Weevely"))
        self.treeWidget.topLevelItem(7).child(17).setText(0, _translate("MainWindow", "Winexe"))
        self.treeWidget.topLevelItem(8).setText(0, _translate("MainWindow", "Hardware Hacking"))
        self.treeWidget.topLevelItem(8).child(0).setText(0, _translate("MainWindow", "android-sdk"))
        self.treeWidget.topLevelItem(8).child(1).setText(0, _translate("MainWindow", "apktool"))
        self.treeWidget.topLevelItem(8).child(2).setText(0, _translate("MainWindow", "Arduino"))
        self.treeWidget.topLevelItem(8).child(3).setText(0, _translate("MainWindow", "dex2jar"))
        self.treeWidget.topLevelItem(8).child(4).setText(0, _translate("MainWindow", "Sakis3G"))
        self.treeWidget.topLevelItem(8).child(5).setText(0, _translate("MainWindow", "smali"))
        self.treeWidget.topLevelItem(9).setText(0, _translate("MainWindow", "Web Applications"))
        self.treeWidget.topLevelItem(9).child(0).setText(0, _translate("MainWindow", "apache-users"))
        self.treeWidget.topLevelItem(9).child(1).setText(0, _translate("MainWindow", "Arachni"))
        self.treeWidget.topLevelItem(9).child(2).setText(0, _translate("MainWindow", "BBQSQL"))
        self.treeWidget.topLevelItem(9).child(3).setText(0, _translate("MainWindow", "BlindElephant"))
        self.treeWidget.topLevelItem(9).child(4).setText(0, _translate("MainWindow", "Burp Suite"))
        self.treeWidget.topLevelItem(9).child(5).setText(0, _translate("MainWindow", "CutyCapt"))
        self.treeWidget.topLevelItem(9).child(6).setText(0, _translate("MainWindow", "DAVTest"))
        self.treeWidget.topLevelItem(9).child(7).setText(0, _translate("MainWindow", "deblaze"))
        self.treeWidget.topLevelItem(9).child(8).setText(0, _translate("MainWindow", "DIRB"))
        self.treeWidget.topLevelItem(9).child(9).setText(0, _translate("MainWindow", "DirBuster"))
        self.treeWidget.topLevelItem(9).child(10).setText(0, _translate("MainWindow", "fimap"))
        self.treeWidget.topLevelItem(9).child(11).setText(0, _translate("MainWindow", "FunkLoad"))
        self.treeWidget.topLevelItem(9).child(12).setText(0, _translate("MainWindow", "Gobuster"))
        self.treeWidget.topLevelItem(9).child(13).setText(0, _translate("MainWindow", "Grabber"))
        self.treeWidget.topLevelItem(9).child(14).setText(0, _translate("MainWindow", "jboss-autopwn"))
        self.treeWidget.topLevelItem(9).child(15).setText(0, _translate("MainWindow", "joomscan"))
        self.treeWidget.topLevelItem(9).child(16).setText(0, _translate("MainWindow", "jSQL"))
        self.treeWidget.topLevelItem(9).child(17).setText(0, _translate("MainWindow", "Maltego Teeth"))
        self.treeWidget.topLevelItem(9).child(18).setText(0, _translate("MainWindow", "PadBuster"))
        self.treeWidget.topLevelItem(9).child(19).setText(0, _translate("MainWindow", "Paros"))
        self.treeWidget.topLevelItem(9).child(20).setText(0, _translate("MainWindow", "Parsero"))
        self.treeWidget.topLevelItem(9).child(21).setText(0, _translate("MainWindow", "plecost"))
        self.treeWidget.topLevelItem(9).child(22).setText(0, _translate("MainWindow", "Powerfuzzer"))
        self.treeWidget.topLevelItem(9).child(23).setText(0, _translate("MainWindow", "ProxyStrike"))
        self.treeWidget.topLevelItem(9).child(24).setText(0, _translate("MainWindow", "Recon-ng"))
        self.treeWidget.topLevelItem(9).child(25).setText(0, _translate("MainWindow", "Skipfish"))
        self.treeWidget.topLevelItem(9).child(26).setText(0, _translate("MainWindow", "sqlmap"))
        self.treeWidget.topLevelItem(9).child(27).setText(0, _translate("MainWindow", "Sqlninja"))
        self.treeWidget.topLevelItem(9).child(28).setText(0, _translate("MainWindow", "sqlsus"))
        self.treeWidget.topLevelItem(9).child(29).setText(0, _translate("MainWindow", "ua-tester"))
        self.treeWidget.topLevelItem(9).child(30).setText(0, _translate("MainWindow", "Uniscan"))
        self.treeWidget.topLevelItem(9).child(31).setText(0, _translate("MainWindow", "Vega"))
        self.treeWidget.topLevelItem(9).child(32).setText(0, _translate("MainWindow", "w3af"))
        self.treeWidget.topLevelItem(9).child(33).setText(0, _translate("MainWindow", "WebScarab"))
        self.treeWidget.topLevelItem(9).child(34).setText(0, _translate("MainWindow", "Webshag"))
        self.treeWidget.topLevelItem(9).child(35).setText(0, _translate("MainWindow", "WebSlayer"))
        self.treeWidget.topLevelItem(9).child(36).setText(0, _translate("MainWindow", "WebSploit"))
        self.treeWidget.topLevelItem(9).child(37).setText(0, _translate("MainWindow", "Wfuzz"))
        self.treeWidget.topLevelItem(9).child(38).setText(0, _translate("MainWindow", "WPScan"))
        self.treeWidget.topLevelItem(9).child(39).setText(0, _translate("MainWindow", "XSSer"))
        self.treeWidget.topLevelItem(9).child(40).setText(0, _translate("MainWindow", "zaproxy"))
        self.treeWidget.topLevelItem(10).setText(0, _translate("MainWindow", "Stress Testing"))
        self.treeWidget.topLevelItem(10).child(0).setText(0, _translate("MainWindow", "DHCPig"))
        self.treeWidget.topLevelItem(10).child(1).setText(0, _translate("MainWindow", "FunkLoad"))
        self.treeWidget.topLevelItem(10).child(2).setText(0, _translate("MainWindow", "iaxflood"))
        self.treeWidget.topLevelItem(10).child(3).setText(0, _translate("MainWindow", "Inundator"))
        self.treeWidget.topLevelItem(10).child(4).setText(0, _translate("MainWindow", "inviteflood"))
        self.treeWidget.topLevelItem(10).child(5).setText(0, _translate("MainWindow", "ipv6-toolkit"))
        self.treeWidget.topLevelItem(10).child(6).setText(0, _translate("MainWindow", "mdk3"))
        self.treeWidget.topLevelItem(10).child(7).setText(0, _translate("MainWindow", "Reaver"))
        self.treeWidget.topLevelItem(10).child(8).setText(0, _translate("MainWindow", "rtpflood"))
        self.treeWidget.topLevelItem(10).child(9).setText(0, _translate("MainWindow", "SlowHTTPTest"))
        self.treeWidget.topLevelItem(10).child(10).setText(0, _translate("MainWindow", "t50"))
        self.treeWidget.topLevelItem(10).child(11).setText(0, _translate("MainWindow", "Termineter"))
        self.treeWidget.topLevelItem(10).child(12).setText(0, _translate("MainWindow", "THC-IPV6"))
        self.treeWidget.topLevelItem(10).child(13).setText(0, _translate("MainWindow", "THC-SSL-DOS"))
        self.treeWidget.topLevelItem(11).setText(0, _translate("MainWindow", "Reverse Engineering"))
        self.treeWidget.topLevelItem(11).child(0).setText(0, _translate("MainWindow", "apktool"))
        self.treeWidget.topLevelItem(11).child(1).setText(0, _translate("MainWindow", "dex2jar"))
        self.treeWidget.topLevelItem(11).child(2).setText(0, _translate("MainWindow", "diStorm3"))
        self.treeWidget.topLevelItem(11).child(3).setText(0, _translate("MainWindow", "edb-debugger"))
        self.treeWidget.topLevelItem(11).child(4).setText(0, _translate("MainWindow", "jad"))
        self.treeWidget.topLevelItem(11).child(5).setText(0, _translate("MainWindow", "javasnoop"))
        self.treeWidget.topLevelItem(11).child(6).setText(0, _translate("MainWindow", "JD-GUI"))
        self.treeWidget.topLevelItem(11).child(7).setText(0, _translate("MainWindow", "OllyDbg"))
        self.treeWidget.topLevelItem(11).child(8).setText(0, _translate("MainWindow", "smali"))
        self.treeWidget.topLevelItem(11).child(9).setText(0, _translate("MainWindow", "Valgrind"))
        self.treeWidget.topLevelItem(11).child(10).setText(0, _translate("MainWindow", "YARA"))
        self.treeWidget.topLevelItem(12).setText(0, _translate("MainWindow", "Reporting"))
        self.treeWidget.topLevelItem(12).child(0).setText(0, _translate("MainWindow", "CaseFile"))
        self.treeWidget.topLevelItem(12).child(1).setText(0, _translate("MainWindow", "CutyCapt"))
        self.treeWidget.topLevelItem(12).child(2).setText(0, _translate("MainWindow", "dos2unix"))
        self.treeWidget.topLevelItem(12).child(3).setText(0, _translate("MainWindow", "Dradis"))
        self.treeWidget.topLevelItem(12).child(4).setText(0, _translate("MainWindow", "KeepNote"))
        self.treeWidget.topLevelItem(12).child(5).setText(0, _translate("MainWindow", "MagicTree"))
        self.treeWidget.topLevelItem(12).child(6).setText(0, _translate("MainWindow", "Metagoofil"))
        self.treeWidget.topLevelItem(12).child(7).setText(0, _translate("MainWindow", "Nipper-ng"))
        self.treeWidget.topLevelItem(12).child(8).setText(0, _translate("MainWindow", "pipal"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew_Window.setText(_translate("MainWindow", "New Window"))
        self.actionClose_Window.setText(_translate("MainWindow", "Close Window"))
        self.actionClose_Tab.setText(_translate("MainWindow", "Close Tab"))
        self.actionNew_Tab.setText(_translate("MainWindow", "New Tab"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionSelect_All.setText(_translate("MainWindow", "Select All"))
        self.actionEnable_Dark_Mode.setText(_translate("MainWindow", "Enable Dark Mode"))
        self.actionMinimize.setText(_translate("MainWindow", "Minimize"))
        self.actionEnter_Full_Screen.setText(_translate("MainWindow", "Enter Full Screen"))
        self.actionSelect_Next_Tab.setText(_translate("MainWindow", "Select Next Tab"))
        self.actionSelect_Previous_Tab.setText(_translate("MainWindow", "Select Previous Tab"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))

