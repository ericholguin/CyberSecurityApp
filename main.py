import sys  #We need the sys module to pass argv to QApplication
import design   #Holds the MainWindow and all design related items
from PyQt5 import QtGui #Importing the PyQt5 module we need
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

        self.treeWidget.itemSelectionChanged.connect(self.openTab)

        for x in range(61):
            self.tabWidget.removeTab(1)

        if (self.Click1.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click2.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click3.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click4.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click5.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click6.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click7.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click8.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click9.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click10.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click11.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click12.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click13.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click14.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click15.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click16.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click17.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click18.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click19.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click20.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click21.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click22.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click23.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click24.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click25.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click26.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click27.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click28.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click29.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click30.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click31.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click32.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click33.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click34.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click35.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click36.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click37.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click38.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click39.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click40.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click41.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click42.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click43.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click44.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click45.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click46.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click47.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click48.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click49.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click50.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click51.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click52.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click53.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click54.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click55.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click56.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click57.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click58.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click59.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
        if (self.Click60.isSelected):
            {
                self.tabWidget.addTab(self.acccheckTab, "acccheck")
            }
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
