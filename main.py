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
        def commandEvent1():
                    os.system("ace")
        def commandEvent2():
                    os.system("amap")
        def commandEvent3():
                    os.system("automater")
        def commandEvent4():
                    os.system("bing-ip2hosts")
        def commandEvent5():
                    os.system("braa")
        def commandEvent6():
                    os.system("casefile")
        def commandEvent7():
                    os.system("cdpsnarf")
        def commandEvent8():
                    os.system("cisco-torch")
        def commandEvent9():
                    os.system("cookiecadger")
        def commandEvent10():
                    os.system("copy-router-config.pl")
        def commandEvent11():
                    os.system("dmitry")
        def commandEvent12():
                    os.system("dnmap_client")
        def commandEvent13():
                    os.system("dnsenum")
        def commandEvent14():
                    os.system("dnsmap")
        def commandEvent15():
                    os.system("dnsrecon")
        def commandEvent16():
                    os.system("dnstracer")
        def commandEvent17():
                    os.system("dnswalk")
        def commandEvent18():
                    os.system("dotdotpwn.pl")
        def commandEvent19():
                    os.system("enum4linux")
        def commandEvent20():
                    os.system("enumiax")
        def commandEvent21():
                    os.system("python-faraday")
        def commandEvent22():
                    os.system("fierce")
        def commandEvent23():
                    os.system("firewalk")
        def commandEvent24():
                    os.system("fragroute")
        def commandEvent25():
                    os.system("fragrouter")
        def commandEvent26():
                    os.system("ghost-phisher")
        def commandEvent27():
                    os.system("golismero")
        def commandEvent28():
                    os.system("goofile")
        def commandEvent29():
                    os.system("hping3")
        def commandEvent30():
                    os.system("ident-user-enum")
        def commandEvent31():
                    os.system("intrace")
        def commandEvent32():
                    os.system("ismtp")
        def commandEvent33():
                    os.system("lbd")
        def commandEvent34():
                    os.system("cat /opt/Teeth/README.txt")
        def commandEvent35():
                    os.system("masscan")
        def commandEvent36():
                    os.system("metagoofil")
        def commandEvent37():
                    os.system("miranda")
        def commandEvent38():
                    os.system("nbtscan-unixwiz")
        def commandEvent39():
                    os.system("nmap")
        def commandEvent40():
                    os.system("ntop")
        def commandEvent41():
                    os.system("p0f")
        def commandEvent42():
                    os.system("parsero")
        def commandEvent43():
                    os.system("recon-ng")
        def commandEvent44():
                    os.system("settoolkit")
        def commandEvent45():
                    os.system("smtp-user-enum")
        def commandEvent46():
                    os.system("snmp-check")
        def commandEvent47():
                    os.system("sparta")
        def commandEvent48():
                    os.system("sslcaudit")
        def commandEvent49():
                    os.system("sslsplit")
        def commandEvent50():
                    os.system("sslstrip")
        def commandEvent51():
                    os.system("sslyze")
        def commandEvent52():
                    os.system("thc-ipv6")
        def commandEvent53():
                    os.system("theharvester")
        def commandEvent54():
                    os.system("tlssled")
        def commandEvent55():
                    os.system("twofi")
        def commandEvent56():
                    os.system("urlcrazy")
        def commandEvent57():
                    os.system("wireshark")
        def commandEvent58():
                    os.system("wol-e")
        def commandEvent59():
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
