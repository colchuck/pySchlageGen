import sys
from PyQt5.QtWidgets import (QWidget, QTextEdit, QMessageBox, QFormLayout, QSpinBox,QToolTip, QGridLayout,QAction, qApp, QMainWindow, QHBoxLayout,QApplication, QVBoxLayout, QFileDialog,
    QPushButton, QApplication, QTextBrowser, QTableWidget, QLineEdit, QListWidgetItem, QListWidget, QLabel)
from PyQt5.QtGui import (QFont, QFontDatabase,QIcon)
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
    mastInput = None
    keyNum=1

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        app_icon = QIcon()
        app_icon.addFile("key.png",QSize(256,256))
        self.setWindowIcon(app_icon)
        #open
        openFile = QAction('Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.fileOpen)
        #save
        saveFile = QAction('Save', self)
        saveFile.setShortcut('Ctrl+S')
        saveFile.setStatusTip('Save new File')
        saveFile.triggered.connect(self.fileSave)
        #exit
        exitAction = QAction('Exit',self)
        exitAction.triggered.connect(self.closeEvent)
        #menu object
        menubar = self.menuBar()
        #file drop down
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)
        fileMenu.addAction(exitAction)
        #widgets
        grid = QGridLayout()
        horiz = QVBoxLayout()
        bigHoriz = QHBoxLayout()
        horizLayout = QHBoxLayout()
        window = QWidget()
        window.setLayout(bigHoriz)
        leftPane = QFormLayout()
        bigHoriz.addLayout(leftPane)
        bigHoriz.addLayout(horiz)
        self.setCentralWidget(window)
        btn = QPushButton('Generate', self)
        btn.clicked.connect(lambda: self.runGen())
        clearBtn = QPushButton("Clear",self)
        clearBtn.clicked.connect(self.clearList)
        self.mainText = QListWidget(self)
        self.mainText.itemSelectionChanged.connect(self.listItemClicked)
        self.mainText.setFont(QFontDatabase.systemFont(QFontDatabase.FixedFont))
        self.mastInput =[]
        i=0
        while i<6:
            t = QLineEdit()
            t.setMaxLength(1)
            t.setAlignment(Qt.AlignHCenter)
            t.textChanged.connect(self.textInputed)
            self.mastInput.append(t)
            i=i+1
        for e in self.mastInput:
            horizLayout.addWidget(e)
        self.mast = QLineEdit()
        self.tenants = QLineEdit()
        self.inc = QLineEdit()
        self.title =QLineEdit()
        self.title.setMinimumWidth(200)
        self.desc = QLineEdit()
        self.address = QLineEdit()
        self.contact = QLineEdit()
        self.phone = QLineEdit()
        self.email = QLineEdit()
        self.notes = QTextEdit()
        self.keyway = QLineEdit()
        label = QLabel("Master Cuts")
        incLabel = QLabel("Increment")
        tenantLabel = QLabel("Tenants")
        #add widgets to layouts
        leftPane.addRow(QLabel("Title"),self.title)
        leftPane.addRow(QLabel("Description"),self.desc)
        leftPane.addRow(QLabel("Keyway"),self.keyway)
        leftPane.addRow(QLabel("Address"),self.address)
        leftPane.addRow(QLabel("contact"),self.contact)
        leftPane.addRow(QLabel("Phone"),self.phone)
        leftPane.addRow(QLabel("Email"),self.email)
        leftPane.addRow(QLabel("Notes"),self.notes)
        grid.addWidget(incLabel,3,0)
        grid.addWidget(tenantLabel,2,0)
        grid.addWidget(label,1,0)
        grid.addWidget(btn,0,0)
        horiz.addWidget(self.mainText)
        horiz.addLayout(grid)
        #horiz.addLayout(horizLayout)
        grid.addWidget(clearBtn,0,1)
        grid.addWidget(self.tenants,2,1)
        grid.addWidget(self.inc,3,1)
        grid.addLayout(horizLayout,1,1)
        #window properties
        self.setGeometry(300, 300, 500, 425)
        self.setWindowTitle('PySchlageGen')
        self.show()

    def textInputed(self,string):
        if len(string) == 1:
            self.focusNextChild()
            
    def runGen(self):
        self.mainText.clear()
        self.keyNum=1
        text = self.mast.text()
        mastCuts = []
        try:
            for e in self.mastInput:
                if e.text():   
                    mastCuts.append(int(e.text()))
            tenants = int(self.tenants.text())
            inc = int(self.inc.text())
            mastCuts = list(map(int, mastCuts))
            self.gen = schlageGen()
            self.gen.addMasterKey(mastCuts)
            output = self.gen.genSystem(tenants,inc)
            self.displayKeys(output)
        except:
            pass
        
    def displayKeys(self,output):
        i=0
        for o in output:
            if self.keyNum < 10:
                f= str(self.keyNum) + ":     "
            elif self.keyNum < 100:
                f= str(self.keyNum) + ":   "
            elif self.keyNum < 1000:
                f= str(self.keyNum) + ": "
            else:
                f = str(self.keyNum)+":"
            for e in o:
              f = f+ str(e) + " "
            item = QListWidgetItem(f)
            self.mainText.insertItem(i,item)
            i=i+1
            self.keyNum = self.keyNum+1
               
    def formatText(self,flist,space=True,inj=" "):
        out = ""
        for e in flist[:-1]:
            out= out+str(e)
            if space:
                out = out + inj
        out=out+str(flist[-1])
        return out

    def clearList(self):
        self.keyNum = 1
        self.mainText.clear()
        self.tenants.clear()
        self.inc.clear()
        for e in self.mastInput:
            e.clear()

    def listItemClicked(self):
        item = self.mainText.currentItem()
        flags = item.flags()
        if flags & Qt.ItemIsEnabled:
            if self.rowStore != None:
                self.mainText.takeItem(self.rowStore+1)
                self.mainText.takeItem(self.rowStore+1)
            tenCuts = self.gen.getSystem()[int(item.text().split(":")[0])-1]
            tenCuts = list(map(int, tenCuts))
            output = self.gen.bittingCalc(tenCuts)
            row = self.mainText.currentRow()
            self.rowStore = row
            flags = item.flags()
            flags ^= Qt.ItemIsEnabled
            item = QListWidgetItem("        "+self.formatText(output[0]))
            item.setFlags(flags)
            item2 = QListWidgetItem("        "+self.formatText(output[1]))
            item2.setFlags(flags)
            self.mainText.insertItem(row+1,item)
            self.mainText.insertItem(row+2,item2)

    def fileOpen(self):
        self.clearList()
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
            self.inc.setText(str(sys[0]))
            del sys[0]
            self.title.setText(str(sys[0]))
            del sys[0]
            self.desc.setText(str(sys[0]))
            del sys[0]
            self.keyway.setText(str(sys[0]))
            del sys[0]
            self.address.setText(str(sys[0]))
            del sys[0]
            self.contact.setText(str(sys[0]))
            del sys[0]
            self.phone.setText(str(sys[0]))
            del sys[0]
            self.email.setText(str(sys[0]))
            del sys[0]
            self.notes.setPlainText(str(sys[0]))
            del sys[0]
            self.gen.setTenants(sys)
            self.displayKeys(sys)
            i=0
            while i<len(master):
                self.mastInput[i].setText(str(master[i]))
                i=i+1
            self.tenants.setText(str(len(sys)))

    def fileSave(self):
        home = expanduser("~")
        fname = QFileDialog.getSaveFileName(self, 'Open file', home,"*.mks")
        if fname[0]:
            with open(fname[0],"w") as thefile:
                thefile.write("%s," % self.formatText(self.gen.getMasterKey(),False))
                thefile.write("%s," % self.inc.text())
                thefile.write("%s," % self.title.text())
                thefile.write("%s," % self.desc.text())
                thefile.write("%s," % self.keyway.text())
                thefile.write("%s," % self.address.text())
                thefile.write("%s," % self.contact.text())
                thefile.write("%s," % self.phone.text())
                thefile.write("%s," % self.email.text())
                thefile.write("%s," % self.notes.toPlainText())
                for e in self.gen.getSystem()[:-1]:
                    thefile.write("%s," % self.formatText(e,False))
                thefile.write("%s" % self.formatText(self.gen.getSystem()[-1],False))

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            sys.exit()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Gui()
    sys.exit(app.exec_())