import sys
from PyQt5.QtWidgets import (QWidget, QDialog, QTextEdit, QMessageBox, QFormLayout, QSpinBox, QToolTip, QGridLayout, QAction, qApp, QMainWindow, QHBoxLayout, QApplication, QVBoxLayout, QFileDialog,
                             QPushButton, QApplication, QCheckBox, QTextBrowser, QTableWidget, QLineEdit, QListWidgetItem, QListWidget, QLabel)
from PyQt5.QtGui import (QFont, QFontDatabase, QIcon)
from schlageGen import schlageGen
from os.path import expanduser
from PyQt5.QtCore import *
from PyQt5 import *


class PrintSetup(QDialog):

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.initUI()

    def initUI(self):
        #icon
        app_icon = QIcon()
        app_icon.addFile("key.png", QSize(256, 256))
        self.setWindowIcon(app_icon)
        #text preview
        self.Gen = self.parent.getGen()
        self.preview = QTextEdit()
        self.preview.setReadOnly(True)
        #gui elements
        pntBtn = QPushButton("Print", self)
        pntBtn.clicked.connect(self.printMKS)
        previewBtn = QPushButton("Preview", self)
        previewBtn.clicked.connect(self.previewMKS)
        #showBittings = QCheckBox("Master Bittings")
        #showTitlePage = QCheckBox("Title Page")
        showContact = QCheckBox("Contact Information")
        showContact.setEnabled(False)
        vert = QVBoxLayout()
        self.setLayout(vert)
        #vert.addWidget(showBittings)
        #vert.addWidget(showTitlePage)
        vert.addWidget(showContact)
        vert.addWidget(self.preview)
        vert.addWidget(pntBtn)
        vert.addWidget(previewBtn)
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Print')
        self.formatPrint()
        self.show()

    #print without preview
    def printMKS(self):
        printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
        diag = QtPrintSupport.QPrintDialog(printer, self)
        if diag.exec_() == QDialog.Accepted:
            self.preview.print_(diag.printer())

    #formats data for printing
    def formatPrint(self):
        output = self.Gen.getSystem()
        html = ""
        i = 1
        html += "<div align='center' font-size='120%'>" + self.parent.title.text() + \
            "</div>"
        html += "<div align='center'>" + self.parent.address.text() + "</div>"
        html += "<div align='center'> Master Key: " + \
            " ".join(map(str,self.Gen.getMasterKey())) + "</div>"
        html += "<br><table>"
        for e in output:
            e = list(map(int, e))
            html += "<tr><td style='width:30px'>" + \
                str(i) + ": </td><td width='90%'>"
            for f in e:
                html += str(f) + " "
            html += "</td></tr><hr width='100%'>"
            bitting = self.Gen.bittingCalc(e)
            html += "<tr><td></td><td>"
            for f in bitting[0]:
                if f == 0:
                    f = "x"
                html += "" + str(f) + " "
            html += "</td></tr>"
            html += "<tr><td></td><td>"
            for l in bitting[1]:
                html += str(l) + " "
            html += "</td></tr><br>"
            i = i + 1
        html += "</table>"
        self.preview.insertHtml(html)
        self.preview.moveCursor (QtGui.QTextCursor.Start) ;
        self.preview.ensureCursorVisible();

    #preview print dialog
    def previewMKS(self):
        printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
        preview = QtPrintSupport.QPrintPreviewDialog(printer, self)
        preview.paintRequested.connect(self.printPreview)
        preview.exec_()

    #helper function for print preview
    def printPreview(self, printer):
        self.preview.print_(printer)
