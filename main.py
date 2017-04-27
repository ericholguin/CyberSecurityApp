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

        self.setGeometry(0, 0, 650, 650)

        #allow tabs to be closed
        self.tabWidget.setTabsClosable(1)
        #if the tab is closed, remove the tab
        self.tabWidget.tabCloseRequested.connect(self.tabWidget.removeTab)
        #Welcome Tab is always open
        self.tabWidget.tabBar().setTabButton(0, QTabBar.RightSide, None)

        for x in range(61):
            self.tabWidget.removeTab(1)

        def openTab():

            if (self.item_0.isSelected() == True):
                self.tabWidget.addTab(self.infoGatheringTab, "Information Gathering")
                self.tabWidget.setCurrentWidget(self.infoGatheringTab)
            elif (self.Click1.isSelected() == True):
                 self.tabWidget.addTab(self.acccheckTab, "acccheck")
                 self.tabWidget.setCurrentWidget(self.acccheckTab)
            elif (self.Click2.isSelected() == True):
                 self.tabWidget.addTab(self.acevoipTab, "ace-voip")
                 self.tabWidget.setCurrentWidget(self.acevoipTab)
            elif (self.Click3.isSelected() == True):
                 self.tabWidget.addTab(self.amapTab, "amap")
                 self.tabWidget.setCurrentWidget(self.amapTab)
            elif (self.Click4.isSelected() == True):
                 self.tabWidget.addTab(self.automaterTab, "Automater")
                 self.tabWidget.setCurrentWidget(self.automaterTab)
            elif (self.Click5.isSelected() == True):
                 self.tabWidget.addTab(self.bingip2hostsTab, "bing-ip2hosts")
                 self.tabWidget.setCurrentWidget(self.bingip2hostsTab)
            elif (self.Click6.isSelected() == True):
                 self.tabWidget.addTab(self.braaTab, "braa")
                 self.tabWidget.setCurrentWidget(self.braaTab)
            elif (self.Click7.isSelected() == True):
                 self.tabWidget.addTab(self.CaseFileTab, "CaseFile")
                 self.tabWidget.setCurrentWidget(self.CaseFileTab)
            elif (self.Click8.isSelected() == True):
                 self.tabWidget.addTab(self.CDPSnarfTab, "CDPSnarf")
                 self.tabWidget.setCurrentWidget(self.CDPSnarfTab)
            elif (self.Click9.isSelected() == True):
                 self.tabWidget.addTab(self.ciscoTorchTab, "cisco-torch")
                 self.tabWidget.setCurrentWidget(self.ciscoTorchTab)
            elif (self.Click10.isSelected() == True):
                 self.tabWidget.addTab(self.CookieCadgerTab, "Cookie Cadger")
                 self.tabWidget.setCurrentWidget(self.CookieCadgerTab)
            elif (self.Click11.isSelected() == True):
                 self.tabWidget.addTab(self.copyRouterConfigTab, "copy-router-config")
                 self.tabWidget.setCurrentWidget(self.copyRouterConfigTab)
            elif (self.Click12.isSelected() == True):
                 self.tabWidget.addTab(self.DMitryTab, "DMitry")
                 self.tabWidget.setCurrentWidget(self.DMitryTab)
            elif (self.Click13.isSelected() == True):
                 self.tabWidget.addTab(self.dnmapTab, "dnmap")
                 self.tabWidget.setCurrentWidget(self.dnmapTab)
            elif (self.Click14.isSelected() == True):
                 self.tabWidget.addTab(self.dnsenumTab, "dnsenum")
                 self.tabWidget.setCurrentWidget(self.dnsenumTab)
            elif (self.Click15.isSelected() == True):
                 self.tabWidget.addTab(self.dnsmapTab, "dnsmap")
                 self.tabWidget.setCurrentWidget(self.dnsmapTab)
            elif (self.Click16.isSelected() == True):
                 self.tabWidget.addTab(self.DNSReconTab, "DNSRecon")
                 self.tabWidget.setCurrentWidget(self.DNSReconTab)
            elif (self.Click17.isSelected() == True):
                 self.tabWidget.addTab(self.dnstracerTab, "dnstracer")
                 self.tabWidget.setCurrentWidget(self.dnstracerTab)
            elif (self.Click18.isSelected() == True):
                 self.tabWidget.addTab(self.dnswalkTab, "dnswalk")
                 self.tabWidget.setCurrentWidget(self.dnswalkTab)
            elif (self.Click19.isSelected() == True):
                 self.tabWidget.addTab(self.DotDotPwnTab, "DotDotPwn")
                 self.tabWidget.setCurrentWidget(self.DotDotPwnTab)
            elif (self.Click20.isSelected() == True):
                 self.tabWidget.addTab(self.enum4linuxTab, "enum4linux")
                 self.tabWidget.setCurrentWidget(self.enum4linuxTab)
            elif (self.Click21.isSelected() == True):
                 self.tabWidget.addTab(self.enumIAXTab, "enumIAX")
                 self.tabWidget.setCurrentWidget(self.enumIAXTab)
            elif (self.Click22.isSelected() == True):
                 self.tabWidget.addTab(self.Faraday, "Faraday")
                 self.tabWidget.setCurrentWidget(self.Faraday)
            elif (self.Click23.isSelected() == True):
                 self.tabWidget.addTab(self.FierceTab, "Fierce")
                 self.tabWidget.setCurrentWidget(self.FierceTab)
            elif (self.Click24.isSelected() == True):
                 self.tabWidget.addTab(self.FireWalkTab, "Firewalk")
                 self.tabWidget.setCurrentWidget(self.FireWalkTab)
            elif (self.Click25.isSelected() == True):
                 self.tabWidget.addTab(self.fragRouteTab, "fragroute")
                 self.tabWidget.setCurrentWidget(self.fragRouteTab)
            elif (self.Click26.isSelected() == True):
                 self.tabWidget.addTab(self.fragRouterTab, "fragrouter")
                 self.tabWidget.setCurrentWidget(self.fragRouterTab)
            elif (self.Click27.isSelected() == True):
                 self.tabWidget.addTab(self.GhostPhisherTab, "Ghost Phisher")
                 self.tabWidget.setCurrentWidget(self.GhostPhisherTab)
            elif (self.Click28.isSelected() == True):
                 self.tabWidget.addTab(self.GoLismeroTab, "GoLismero")
                 self.tabWidget.setCurrentWidget(self.GoLismeroTab)
            elif (self.Click29.isSelected() == True):
                 self.tabWidget.addTab(self.goofileTab, "goofile")
                 self.tabWidget.setCurrentWidget(self.goofileTab)
            elif (self.Click30.isSelected() == True):
                 self.tabWidget.addTab(self.hping3Tab, "hping3")
                 self.tabWidget.setCurrentWidget(self.hping3Tab)
            elif (self.Click31.isSelected() == True):
                 self.tabWidget.addTab(self.identUserEnumTab, "ident-user-enum")
                 self.tabWidget.setCurrentWidget(self.identUserEnumTab)
            elif (self.Click32.isSelected() == True):
                 self.tabWidget.addTab(self.InTraceTab, "InTrace")
                 self.tabWidget.setCurrentWidget(self.InTraceTab)
            elif (self.Click33.isSelected() == True):
                 self.tabWidget.addTab(self.iSMTPTab, "iSMTP")
                 self.tabWidget.setCurrentWidget(self.iSMTPTab)
            elif (self.Click34.isSelected() == True):
                 self.tabWidget.addTab(self.IbdTab, "Ibd")
                 self.tabWidget.setCurrentWidget(self.IbdTab)
            elif (self.Click35.isSelected() == True):
                 self.tabWidget.addTab(self.MaltegoTeethTab, "Maltego Teeth")
                 self.tabWidget.setCurrentWidget(self.MaltegoTeethTab)
            elif (self.Click36.isSelected() == True):
                 self.tabWidget.addTab(self.masscanTab, "masscan")
                 self.tabWidget.setCurrentWidget(self.masscanTab)
            elif (self.Click37.isSelected() == True):
                 self.tabWidget.addTab(self.MetagoofilTab, "Metagoofil")
                 self.tabWidget.setCurrentWidget(self.MetagoofilTab)
            elif (self.Click38.isSelected() == True):
                 self.tabWidget.addTab(self.MirandaTab, "Miranda")
                 self.tabWidget.setCurrentWidget(self.MirandaTab)
            elif (self.Click39.isSelected() == True):
                 self.tabWidget.addTab(self.nbtscanUnixwizTab, "nbtscan-unix")
                 self.tabWidget.setCurrentWidget(self.nbtscanUnixwizTab)
            elif (self.Click40.isSelected() == True):
                 self.tabWidget.addTab(self.NmapTab, "Nmap")
                 self.tabWidget.setCurrentWidget(self.NmapTab)
            elif (self.Click41.isSelected() == True):
                 self.tabWidget.addTab(self.ntopTab, "ntop")
                 self.tabWidget.setCurrentWidget(self.ntopTab)
            elif (self.Click42.isSelected() == True):
                 self.tabWidget.addTab(self.p0fTab, "p0f")
                 self.tabWidget.setCurrentWidget(self.p0fTab)
            elif (self.Click43.isSelected() == True):
                 self.tabWidget.addTab(self.PareseroTab, "Parsero")
                 self.tabWidget.setCurrentWidget(self.PareseroTab)
            elif (self.Click44.isSelected() == True):
                 self.tabWidget.addTab(self.ReconNgTab, "Recon-ng")
                 self.tabWidget.setCurrentWidget(self.ReconNgTab)
            elif (self.Click45.isSelected() == True):
                 self.tabWidget.addTab(self.SETTab, "SET")
                 self.tabWidget.setCurrentWidget(self.SETTab)
            elif (self.Click46.isSelected() == True):
                 self.tabWidget.addTab(self.smtpUserEnumTab, "smtp-user-enum")
                 self.tabWidget.setCurrentWidget(self.smtpUserEnumTab)
            elif (self.Click47.isSelected() == True):
                 self.tabWidget.addTab(self.snmpChecktab, "snmp-check")
                 self.tabWidget.setCurrentWidget(self.snmpChecktab)
            elif (self.Click48.isSelected() == True):
                 self.tabWidget.addTab(self.spartaTab, "SPARTA")
                 self.tabWidget.setCurrentWidget(self.spartaTab)
            elif (self.Click49.isSelected() == True):
                 self.tabWidget.addTab(self.sscaudittab, "sslcaudit")
                 self.tabWidget.setCurrentWidget(self.sscaudittab)
            elif (self.Click50.isSelected() == True):
                 self.tabWidget.addTab(self.SSLsplitab, "SSLsplit")
                 self.tabWidget.setCurrentWidget(self.SSLsplitab)
            elif (self.Click51.isSelected() == True):
                 self.tabWidget.addTab(self.sslstripTab, "sslstrip")
                 self.tabWidget.setCurrentWidget(self.sslstripTab)
            elif (self.Click52.isSelected() == True):
                 self.tabWidget.addTab(self.SSLyzeTab, "SSLyze")
                 self.tabWidget.setCurrentWidget(self.SSLyzeTab)
            elif (self.Click53.isSelected() == True):
                 self.tabWidget.addTab(self.THCIPV6Tab, "THC-IPV6")
                 self.tabWidget.setCurrentWidget(self.THCIPV6Tab)
            elif (self.Click54.isSelected() == True):
                 self.tabWidget.addTab(self.theHarvesterTab, "theHarvester")
                 self.tabWidget.setCurrentWidget(self.theHarvesterTab)
            elif (self.Click55.isSelected() == True):
                 self.tabWidget.addTab(self.TLSSLedTab, "TLSSLed")
                 self.tabWidget.setCurrentWidget(self.TLSSLedTab)
            elif (self.Click56.isSelected() == True):
                 self.tabWidget.addTab(self.twofiTab, "twofi")
                 self.tabWidget.setCurrentWidget(self.twofiTab)
            elif (self.Click57.isSelected() == True):
                 self.tabWidget.addTab(self.urlCrazyTab, "UrlCrazy")
                 self.tabWidget.setCurrentWidget(self.urlCrazyTab)
            elif (self.Click58.isSelected() == True):
                 self.tabWidget.addTab(self.WiresharkTab, "Wireshark")
                 self.tabWidget.setCurrentWidget(self.WiresharkTab)
            elif (self.Click59.isSelected() == True):
                 self.tabWidget.addTab(self.WOLETab, "WOL-E")
                 self.tabWidget.setCurrentWidget(self.WOLETab)
            elif (self.Click60.isSelected() == True):
                 self.tabWidget.addTab(self.XplicoTab, "Xplico")
                 self.tabWidget.setCurrentWidget(self.XplicoTab)

        def commandEvent():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("acccheck")
        def commandEvent1():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("ace")
        def commandEvent2():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("amap")
        def commandEvent3():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("automater")
        def commandEvent4():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("bing-ip2hosts")
        def commandEvent5():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("braa")
        def commandEvent6():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("casefile")
        def commandEvent7():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("cdpsnarf")
        def commandEvent8():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("cisco-torch")
        def commandEvent9():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("cookiecadger")
        def commandEvent10():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("copy-router-config.pl")
        def commandEvent11():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("dmitry")
        def commandEvent12():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("dnmap_client")
        def commandEvent13():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("dnsenum")
        def commandEvent14():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("dnsmap")
        def commandEvent15():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("dnsrecon")
        def commandEvent16():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("dnstracer")
        def commandEvent17():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("dnswalk")
        def commandEvent18():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("dotdotpwn.pl")
        def commandEvent19():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("enum4linux")
        def commandEvent20():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("enumiax")
        def commandEvent21():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("python-faraday")
        def commandEvent22():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("fierce")
        def commandEvent23():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("firewalk")
        def commandEvent24():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("fragroute")
        def commandEvent25():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("fragrouter")
        def commandEvent26():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("ghost-phisher")
        def commandEvent27():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("golismero")
        def commandEvent28():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("goofile")
        def commandEvent29():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("hping3")
        def commandEvent30():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("ident-user-enum")
        def commandEvent31():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("intrace")
        def commandEvent32():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("ismtp")
        def commandEvent33():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("lbd")
        def commandEvent34():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("cat /opt/Teeth/README.txt")
        def commandEvent35():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("masscan")
        def commandEvent36():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("metagoofil")
        def commandEvent37():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("miranda")
        def commandEvent38():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("nbtscan-unixwiz")
        def commandEvent39():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("nmap")
        def commandEvent40():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("ntop")
        def commandEvent41():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("p0f")
        def commandEvent42():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("parsero")
        def commandEvent43():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("recon-ng")
        def commandEvent44():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("settoolkit")
        def commandEvent45():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("smtp-user-enum")
        def commandEvent46():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("snmp-check")
        def commandEvent47():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("sparta")
        def commandEvent48():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("sslcaudit")
        def commandEvent49():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("sslsplit")
        def commandEvent50():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("sslstrip")
        def commandEvent51():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("sslyze")
        def commandEvent52():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("thc-ipv6")
        def commandEvent53():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("theharvester")
        def commandEvent54():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("tlssled")
        def commandEvent55():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("twofi")
        def commandEvent56():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("urlcrazy")
        def commandEvent57():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("wireshark")
        def commandEvent58():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("wol-e")
        def commandEvent59():
                    self.setWindowState(Qt.WindowMinimized)
                    os.system("xplico")

        self.treeWidget.itemClicked.connect(openTab)

        self.acccheckButton.clicked.connect(commandEvent)
        self.acevoipButton.clicked.connect(commandEvent1)
        self.amapButton.clicked.connect(commandEvent2)
        self.automaterButton.clicked.connect(commandEvent3)
        self.bingip2hostsButton.clicked.connect(commandEvent4)
        self.braaButton.clicked.connect(commandEvent5)
        self.CaseFileButton.clicked.connect(commandEvent6)
        self.CDPSnarfButton.clicked.connect(commandEvent7)
        self.ciscoTorchButton.clicked.connect(commandEvent8)
        self.CookieCadgerButton.clicked.connect(commandEvent9)
        self.copyRouterConfigButton.clicked.connect(commandEvent10)
        self.DMitryButton.clicked.connect(commandEvent11)
        self.dnmapButton.clicked.connect(commandEvent12)
        self.dnsenumButton.clicked.connect(commandEvent13)
        self.dnsmapButton.clicked.connect(commandEvent14)
        self.DNSReconButton.clicked.connect(commandEvent15)
        self.dnstracerButton.clicked.connect(commandEvent16)
        self.dnswalkButton.clicked.connect(commandEvent17)
        self.DotDotPwnButton.clicked.connect(commandEvent18)
        self.enum4linuxButton.clicked.connect(commandEvent19)
        self.enumIAXButton.clicked.connect(commandEvent20)
        self.FaradayButton.clicked.connect(commandEvent21)
        self.FierceButton.clicked.connect(commandEvent22)
        self.FireWalkButton.clicked.connect(commandEvent23)
        self.fragRouteButton.clicked.connect(commandEvent24)
        self.fragRouterButton.clicked.connect(commandEvent25)
        self.GhostPhisherButton.clicked.connect(commandEvent26)
        self.GoLismeroButton.clicked.connect(commandEvent27)
        self.goofileButton.clicked.connect(commandEvent28)
        self.hping3Button.clicked.connect(commandEvent29)
        self.identUserEnumButton.clicked.connect(commandEvent30)
        self.InTraceButton.clicked.connect(commandEvent31)
        self.iSMTPButton.clicked.connect(commandEvent32)
        self.IbdButton.clicked.connect(commandEvent33)
        self.MaltegoTeethButton.clicked.connect(commandEvent34)
        self.masscanButton.clicked.connect(commandEvent35)
        self.MetagoofilButton.clicked.connect(commandEvent36)
        self.MirandaButton.clicked.connect(commandEvent37)
        self.nbtscanUnixwizButton.clicked.connect(commandEvent38)
        self.NmapButton.clicked.connect(commandEvent39)
        self.ntopButton.clicked.connect(commandEvent40)
        self.p0fButton.clicked.connect(commandEvent41)
        self.ParseroButton.clicked.connect(commandEvent42)
        self.ReconNgButton.clicked.connect(commandEvent43)
        self.SETButton.clicked.connect(commandEvent44)
        self.smtpUserEnumButton.clicked.connect(commandEvent45)
        self.snmpCheckButton.clicked.connect(commandEvent46)
        self.spartaButton.clicked.connect(commandEvent47)
        self.sslcauditButton.clicked.connect(commandEvent48)
        self.SSLsplitButton.clicked.connect(commandEvent49)
        self.sslstripButton.clicked.connect(commandEvent50)
        self.SSLyzeButton.clicked.connect(commandEvent51)
        self.THCIPV6Button.clicked.connect(commandEvent52)
        self.theHarvesterButton.clicked.connect(commandEvent53)
        self.TLSSLedButton.clicked.connect(commandEvent54)
        self.twofiButton.clicked.connect(commandEvent55)
        self.urlCrazyButton.clicked.connect(commandEvent56)
        self.WiresharkButton.clicked.connect(commandEvent57)
        self.WOLEButton.clicked.connect(commandEvent58)
        self.XplicoButton.clicked.connect(commandEvent59)


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
