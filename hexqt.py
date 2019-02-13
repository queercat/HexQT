# hexqt.py -- HexQT a pretty QT hext editor.

import sys, os
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QAction, QMainWindow, QFileDialog, QGridLayout, QGroupBox, QTextEdit, QDesktopWidget
from PyQt5.QtGui import QIcon, QPalette, QColor, QFont, QFontDatabase
from PyQt5.QtCore import Qt, pyqtSlot

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
        self.left = 0
        self.top = 0
        self.width = 1024
        self.height = 640
        self.initUI()

    def readFile(self, fileName):
        fileData = ''
        
        with open(fileName, 'rb') as fileObj:
            fileData = fileObj.read()

        options = {
            'rowSpacing': 4,
            'rowLength': 16
        }

        self.generateView(fileData, options)

        # generateView ... Generates text view for hexdump likedness.
    def generateView(self, text, options):
        # Standard spacing.
        space = ' '
        bigSpace = ' ' * 4 

        rowSpacing = options['rowSpacing']
        rowLength = options['rowLength']

        offset = 0

        offsetText = ''
        mainText = ''
        asciiText = ''

        for chars in range(1, len(text) + 1):
            byte = text[chars - 1]
            char = chr(text[chars - 1])

            offsetText += format(offset, '08x') + '\n'
            offset += rowLength

            if char is ' ':
                asciiText += '.'

            else:
                asciiText += char

            mainText += format(byte, '04x') + space

            if chars % rowSpacing is 0:
                mainText += space

            if chars % rowLength is 0:
                mainText += bigSpace + '\n'
            
        self.offsetTextArea.setText(offsetText)
        self.mainTextArea.setText(mainText)
        self.asciiTextArea.setText(asciiText)
        
    def openFile(self):
        fileSelect = FileSelector()
        fileName = fileSelect.fileName

        self.readFile(fileName)

    def saveFile(self):
        print('Saved!')

    def createMainView(self):
        qhBox = QHBoxLayout()

        self.mainTextArea = QTextEdit()
        self.offsetTextArea = QTextEdit()
        self.asciiTextArea = QTextEdit()

        # Initialize them all to read only.
        self.mainTextArea.setReadOnly(True)
        self.asciiTextArea.setReadOnly(True)
        self.offsetTextArea.setReadOnly(True)

        # Create the fonts and styles to be used and then apply them.
        font = QFont("DejaVu Sans Mono", 8, QFont.Normal, True)
        
        self.mainTextArea.setFont(font)
        self.asciiTextArea.setFont(font)
        self.offsetTextArea.setFont(font)

        qhBox.addWidget(self.offsetTextArea, 1)
        qhBox.addWidget(self.mainTextArea, 4)
        qhBox.addWidget(self.asciiTextArea, 2)

        return qhBox

    def initUI(self):
        # Initialize basic window options.
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Center the window.
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        
        # Creates a menu bar, (file, edit, options, etc...)
        mainMenu = self.menuBar() 

        # Menus for window.
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')
        helpMenu = mainMenu.addMenu('Help')

        # Open button.
        openButton = QAction(QIcon(), 'Open', self)
        openButton.setShortcut('Ctrl+O')
        openButton.setStatusTip('Open file')
        openButton.triggered.connect(self.openFile)

        # Save button.
        saveButton = QAction(QIcon(), 'Save', self)
        saveButton.setShortcut('Ctrl+S')
        saveButton.setStatusTip('Open file')
        saveButton.triggered.connect(self.saveFile)

        # Optional exit stuff.
        exitButton = QAction(QIcon(), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        
        fileMenu.addAction(openButton)
        fileMenu.addAction(saveButton)
        fileMenu.addAction(exitButton)

        # Creating a widget for the central widget thingy.
        centralWidget = QWidget()
        centralWidget.setLayout(self.createMainView())
        
        self.setCentralWidget(centralWidget)

        # Show our masterpiece.
        self.show()

# setStyle ... Sets the style of the QT Application. Right now using edgy black.
def setStyle(qApp):
    qApp.setStyle("Fusion")

    dark_palette = QPalette()

    dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.WindowText, Qt.white)
    dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
    dark_palette.setColor(QPalette.ToolTipText, Qt.white)
    dark_palette.setColor(QPalette.Text, Qt.white)
    dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ButtonText, Qt.white)
    dark_palette.setColor(QPalette.BrightText, Qt.white)
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, Qt.black)

    qApp.setPalette(dark_palette)

    qApp.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

def main():
    app = QApplication(sys.argv)
    setStyle(app)
    
    hexqt = App()
    sys.exit(app.exec_())

# Initialize the brogram.
if __name__ == '__main__':
    main()