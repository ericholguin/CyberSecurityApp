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
