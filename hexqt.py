# hexqt.py -- HexQT a pretty QT hext editor.

import sys
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QVBoxLayout, QAction, QMainWindow, QFileDialog, QGridLayout, QGroupBox, QTextEdit, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class FileSelector(QFileDialog):
    def __init__(self):
        super().__init__()

        self.selectFile()      
        self.show()

    def selectFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Directory View", "","All Files (*)", options=options)
        
        self.fileName = fileName
        

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window options!
        self.title = 'HexQT'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def openFile(self):
        fileSelect = FileSelector()
        fileName = fileSelect.fileName

    def createTextArea(self):
        groupBox = QGroupBox('Text Area')
        qhBox = QHBoxLayout()

        textArea = QTextEdit('Load File: Ctrl + O...')
        qhBox.addWidget(textArea)

        groupBox.setLayout(qhBox)

        return groupBox

    def createHexArea(self):
        groupBox = QGroupBox('Hex Area')
        qhBox = QHBoxLayout()

        hexArea = QTextEdit('Hex Area...')
        qhBox.addWidget(hexArea)

        groupBox.setLayout(qhBox)

        return groupBox

    def initUI(self):
        # Initialize basic window options.
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        mainMenu = self.menuBar() # Creates a menu bar, (file, edit, options, etc...)

        # Menus for window.
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')
        helpMenu = mainMenu.addMenu('Help')

        # Open menu.
        openButton = QAction(QIcon(), 'Open', self)
        openButton.setShortcut('Ctrl+O')
        openButton.setStatusTip('Open file')
        openButton.triggered.connect(self.openFile)

        # Optional exit stuff.
        exitButton = QAction(QIcon(), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        
        fileMenu.addAction(openButton)
        fileMenu.addAction(exitButton)

        # Creating a groupbox layout.
        
        gBox = QGroupBox()

        qLayout = QHBoxLayout()
        qLayout.addWidget(self.createTextArea())
        qLayout.addWidget(self.createHexArea())
        
        gBox.setLayout(qLayout)
        self.setCentralWidget(gBox)

        # Show our masterpiece.
        self.show()

def main():
    app = QApplication(sys.argv)    
    hexqt = App()
    sys.exit(app.exec_())

# Initialize the brogram.
if __name__ == '__main__':
    main()