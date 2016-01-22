import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QGridLayout,QAction, qApp, QMainWindow, QHBoxLayout,QApplication, QVBoxLayout, QFileDialog,
    QPushButton, QApplication, QTextBrowser, QTableWidget, QLineEdit, QListWidgetItem, QListWidget, QLabel)
from PyQt5.QtGui import QFont
from schlageGen import schlageGen
from os.path import expanduser
from PyQt5.QtCore import *


class Gui(QMainWindow):
    mainText = None
    mast = None
    tenants = None
    inc = None
    rowStore = None
    Gen = None

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #menubar
        openFile = QAction('Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.fileOpen)
        saveFile = QAction('Save', self)
        saveFile.setShortcut('Ctrl+S')
        saveFile.setStatusTip('Save new File')
        saveFile.triggered.connect(self.fileSave)
        exitAction = QAction('Exit',self)
        exitAction.triggered.connect(self.extAction)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)
        fileMenu.addAction(exitAction)
        #widgets
        QToolTip.setFont(QFont('SansSerif', 10))
        grid = QGridLayout()
        horiz = QVBoxLayout()
        window = QWidget()
        window.setLayout(horiz)
        self.setCentralWidget(window);
        btn = QPushButton('Generate', self)
        btn.clicked.connect(lambda: self.runGen())
        btn.setToolTip('')
        clearBtn = QPushButton("Clear",self)
        clearBtn.clicked.connect(self.clearList)
        self.mainText = QListWidget(self)
        self.mainText.itemClicked.connect(self.listItemClicked)
        self.mast = QLineEdit()
        self.tenants = QLineEdit()
        self.inc = QLineEdit()
        label = QLabel("Master Cuts")
        incLabel = QLabel("Increment")
        tenantLabel = QLabel("Tenants")
        grid.addWidget(incLabel,3,0)
        grid.addWidget(tenantLabel,2,0)
        grid.addWidget(label,1,0)
        grid.addWidget(btn,0,0)
        horiz.addWidget(self.mainText)
        horiz.addLayout(grid)
        grid.addWidget(clearBtn,0,1)
        grid.addWidget(self.tenants,2,1)
        grid.addWidget(self.inc,3,1)
        grid.addWidget(self.mast,1,1)
        self.setGeometry(300, 300, 400, 600)
        self.setWindowTitle('PySchlageGen')
        self.show()

    def runGen(self):
        self.mainText.clear()
        text = self.mast.text()
        try:
            mastCuts = self.mast.text().rstrip().split(" ")
            tenants = int(self.tenants.text())
            inc = int(self.inc.text())
            mastCuts = list(map(int, mastCuts))
            self.gen = schlageGen()
            self.gen.addMasterKey(mastCuts)
            output = self.gen.genSystem(tenants,inc)
            i=0
            for o in output:
                f=""
                for e in o:
                  f = f+ str(e) + " "
                self.mainText.insertItem(i,f)
                i=i+1
        except:
            pass
        
    def displayKeys(self,output):
        i=0
        for o in output:
            f=""
            for e in o:
              f = f+ str(e) + " "
            self.mainText.insertItem(i,f)
            i=i+1

    def formatText(self,flist,space=True,inj=" "):
        out = ""
        for e in flist[:-1]:
            out= out+str(e)
            if space:
                out = out + inj
        out=out+str(flist[-1])
        return out

    def clearList(self):
        self.mainText.clear()

    def listItemClicked(self,item):
        flags = item.flags()
        if flags & Qt.ItemIsEnabled:
            if self.rowStore != None:
                self.mainText.takeItem(self.rowStore+1)
                self.mainText.takeItem(self.rowStore+1)
            tenCuts = item.text().rstrip().split(" ")
            tenCuts = list(map(int, tenCuts))
            output = self.gen.bittingCalc(tenCuts)
            row = self.mainText.currentRow()
            self.rowStore = row
            flags = item.flags()
            flags ^= Qt.ItemIsEnabled
            item = QListWidgetItem(self.formatText(output[0]))
            item.setFlags(flags)
            item2 = QListWidgetItem(self.formatText(output[1]))
            item2.setFlags(flags)
            self.mainText.insertItem(row+1,item)
            self.mainText.insertItem(row+2,item2)

    def fileOpen(self):
        home = expanduser("~")
        fname = QFileDialog.getOpenFileName(self, 'Open file', home,"*.mks")
        data = None
        if fname[0] != '':
            with open(fname[0], 'r') as infile:
                data = infile.read()
            sys = data.split(",")
            self.gen=schlageGen()
            master = list(map(int, sys[0]))
            self.gen.addMasterKey(master)
            del sys[0]
            self.gen.setTenants(sys)
            self.displayKeys(sys)
            self.mast.setText(self.formatText(master))
            self.tenants.setText(str(len(sys)))
            #self.inc

    def fileSave(self):
        home = expanduser("~")
        fname = QFileDialog.getSaveFileName(self, 'Open file', home,"*.mks")
        if fname[0]:
            with open(fname[0],"w") as thefile:
                thefile.write("%s," % self.formatText(self.gen.getMasterKey(),False))
                for e in self.gen.getSystem()[:-1]:
                    thefile.write("%s," % self.formatText(e,False))
                thefile.write("%s" % self.formatText(e,False))

    def extAction(self):
        sys.exit(app.exec_())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Gui()
    sys.exit(app.exec_())