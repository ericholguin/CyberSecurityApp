import os
import sys  #We need the sys module to pass argv to QApplication
import design   #Holds the MainWindow and all design related items
from PyQt5 import QtGui #Importing the PyQt5 module we need
from PyQt5.QtCore import *
from PyQt5.QtWidgets import * #Import QMainWindow, QApplication, QAction, qApp, QWidget



class ExampleApp(QMainWindow, design.Ui_MainWindow):
    def openTab(self):
        self.tabWidget.addTab(self.infoGatheringTab, "Information Gathering")

    def __init__(self, parent=None):
        #using super to access variable, methods, etc. in design.py
        super(ExampleApp, self).__init__(parent)
        #Defined in the design file, sets up layout and widgets
        self.setupUi(self)

        #allow tabs to be closed
        self.tabWidget.setTabsClosable(1)
        #if the tab is closed, remove the tab
        self.tabWidget.tabCloseRequested.connect(self.tabWidget.removeTab)
        #Welcome Tab is always open
        self.tabWidget.tabBar().setTabButton(0, QTabBar.LeftSide, None)

        for x in range(61):
            self.tabWidget.removeTab(1)

        def openTab():

            if (self.item_0.isSelected() == True):
                self.tabWidget.addTab(self.infoGatheringTab, "Information Gathering")
            elif (self.Click1.isSelected() == True):
                 self.tabWidget.addTab(self.acccheckTab, "acccheck")
            elif (self.Click2.isSelected() == True):
                 self.tabWidget.addTab(self.acevoipTab, "ace-voip")
            elif (self.Click3.isSelected() == True):
                 self.tabWidget.addTab(self.amapTab, "amap")
            elif (self.Click4.isSelected() == True):
                 self.tabWidget.addTab(self.automaterTab, "Automater")
            elif (self.Click5.isSelected() == True):
                 self.tabWidget.addTab(self.bingip2hostsTab, "bing-ip2hosts")
            elif (self.Click6.isSelected() == True):
                 self.tabWidget.addTab(self.braaTab, "braa")
            elif (self.Click7.isSelected() == True):
                 self.tabWidget.addTab(self.CaseFileTab, "CaseFile")
            elif (self.Click8.isSelected() == True):
                 self.tabWidget.addTab(self.CDPSnarfTab, "CDPSnarf")
            elif (self.Click9.isSelected() == True):
                 self.tabWidget.addTab(self.ciscoTorchTab, "cisco-torch")
            elif (self.Click10.isSelected() == True):
                 self.tabWidget.addTab(self.CookieCadgerTab, "Cookie Cadger")
            elif (self.Click11.isSelected() == True):
                 self.tabWidget.addTab(self.copyRouterConfigTab, "copy-router-config")
            elif (self.Click12.isSelected() == True):
                 self.tabWidget.addTab(self.DMitryTab, "DMitry")
            elif (self.Click13.isSelected() == True):
                 self.tabWidget.addTab(self.dnmapTab, "dnmap")
            elif (self.Click14.isSelected() == True):
                 self.tabWidget.addTab(self.dnsenumTab, "dnsenum")
            elif (self.Click15.isSelected() == True):
                 self.tabWidget.addTab(self.dnsmapTab, "dnsmap")
            elif (self.Click16.isSelected() == True):
                 self.tabWidget.addTab(self.DNSReconTab, "DNSRecon")
            elif (self.Click17.isSelected() == True):
                 self.tabWidget.addTab(self.dnstracerTab, "dnstracer")
            elif (self.Click18.isSelected() == True):
                 self.tabWidget.addTab(self.dnswalkTab, "dnswalk")
            elif (self.Click19.isSelected() == True):
                 self.tabWidget.addTab(self.DotDotPwnTab, "DotDotPwn")
            elif (self.Click20.isSelected() == True):
                 self.tabWidget.addTab(self.enum4linuxTab, "enum4linux")
            elif (self.Click21.isSelected() == True):
                 self.tabWidget.addTab(self.enumIAXTab, "enumIAX")
            elif (self.Click22.isSelected() == True):
                 self.tabWidget.addTab(self.Faraday, "Faraday")
            elif (self.Click23.isSelected() == True):
                 self.tabWidget.addTab(self.FierceTab, "Fierce")
            elif (self.Click24.isSelected() == True):
                 self.tabWidget.addTab(self.FireWalkTab, "Firewalk")
            elif (self.Click25.isSelected() == True):
                 self.tabWidget.addTab(self.fragRouteTab, "fragroute")
            elif (self.Click26.isSelected() == True):
                 self.tabWidget.addTab(self.fragRouterTab, "fragrouter")
            elif (self.Click27.isSelected() == True):
                 self.tabWidget.addTab(self.GhostPhisherTab, "Ghost Phisher")
            elif (self.Click28.isSelected() == True):
                 self.tabWidget.addTab(self.GoLismeroTab, "GoLismero")
            elif (self.Click29.isSelected() == True):
                 self.tabWidget.addTab(self.goofileTab, "goofile")
            elif (self.Click30.isSelected() == True):
                 self.tabWidget.addTab(self.hping3Tab, "hping3")
            elif (self.Click31.isSelected() == True):
                 self.tabWidget.addTab(self.identUserEnumTab, "ident-user-enum")
            elif (self.Click32.isSelected() == True):
                 self.tabWidget.addTab(self.InTraceTab, "InTrace")
            elif (self.Click33.isSelected() == True):
                 self.tabWidget.addTab(self.iSMTPTab, "iSMTP")
            elif (self.Click34.isSelected() == True):
                 self.tabWidget.addTab(self.IbdTab, "Ibd")
            elif (self.Click35.isSelected() == True):
                 self.tabWidget.addTab(self.MaltegoTeethTab, "Maltego Teeth")
            elif (self.Click36.isSelected() == True):
                 self.tabWidget.addTab(self.masscanTab, "masscan")
            elif (self.Click37.isSelected() == True):
                 self.tabWidget.addTab(self.MetagoofilTab, "Metagoofil")
            elif (self.Click38.isSelected() == True):
                 self.tabWidget.addTab(self.MirandaTab, "Miranda")
            elif (self.Click39.isSelected() == True):
                 self.tabWidget.addTab(self.nbtscanUnixwizTab, "nbtscan-unix")
            elif (self.Click40.isSelected() == True):
                 self.tabWidget.addTab(self.NmapTab, "Nmap")
            elif (self.Click41.isSelected() == True):
                 self.tabWidget.addTab(self.ntopTab, "ntop")
            elif (self.Click42.isSelected() == True):
                 self.tabWidget.addTab(self.p0fTab, "p0f")
            elif (self.Click43.isSelected() == True):
                 self.tabWidget.addTab(self.PareseroTab, "Parsero")
            elif (self.Click44.isSelected() == True):
                 self.tabWidget.addTab(self.ReconNgTab, "Recon-ng")
            elif (self.Click45.isSelected() == True):
                 self.tabWidget.addTab(self.SETTab, "SET")
            elif (self.Click46.isSelected() == True):
                 self.tabWidget.addTab(self.smtpUserEnumTab, "smtp-user-enum")
            elif (self.Click47.isSelected() == True):
                 self.tabWidget.addTab(self.snmpChecktab, "snmp-check")
            elif (self.Click48.isSelected() == True):
                 self.tabWidget.addTab(self.spartaTab, "SPARTA")
            elif (self.Click49.isSelected() == True):
                 self.tabWidget.addTab(self.sscaudittab, "sslcaudit")
            elif (self.Click50.isSelected() == True):
                 self.tabWidget.addTab(self.SSLsplitab, "SSLsplit")
            elif (self.Click51.isSelected() == True):
                 self.tabWidget.addTab(self.sslstripTab, "sslstrip")
            elif (self.Click52.isSelected() == True):
                 self.tabWidget.addTab(self.SSLyzeTab, "SSLyze")
            elif (self.Click53.isSelected() == True):
                 self.tabWidget.addTab(self.THCIPV6Tab, "THC-IPV6")
            elif (self.Click54.isSelected() == True):
                 self.tabWidget.addTab(self.theHarvesterTab, "theHarvester")
            elif (self.Click55.isSelected() == True):
                 self.tabWidget.addTab(self.TLSSLedTab, "TLSSLed")
            elif (self.Click56.isSelected() == True):
                 self.tabWidget.addTab(self.twofiTab, "twofi")
            elif (self.Click57.isSelected() == True):
                 self.tabWidget.addTab(self.urlCrazyTab, "UrlCrazy")
            elif (self.Click58.isSelected() == True):
                 self.tabWidget.addTab(self.WiresharkTab, "Wireshark")
            elif (self.Click59.isSelected() == True):
                 self.tabWidget.addTab(self.WOLETab, "WOL-E")
            elif (self.Click60.isSelected() == True):
                 self.tabWidget.addTab(self.XplicoTab, "Xplico")

        def commandEvent():
                os.system("acccheck")

        self.treeWidget.itemClicked.connect(openTab)

        self.acccheckButton.clicked.connect(commandEvent)
        #os.system("xterm -hold -e scipt.sh")

def main():
    #new instance of QApplication
    app = QApplication(sys.argv)
    #set form to be our ExampleApp(design)
    form = ExampleApp()
    #show the form
    form.show()
    #execute the app
    app.exec_()

#if we're running directly and not importing
if __name__ == '__main__':
    #run the main function
    main()
