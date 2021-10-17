import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from Models.read_RE import getStatus 

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./Views/main.ui', self)
        self.button_ok.clicked.connect(self.isClickedButtonOk)
    
    def isClickedButtonOk(self):
        text = self.input_text.text()
        status = getStatus(text)

        if(status and len(text)==18):
            self.label_status.setText('CLABE VÁLIDA')
            self.label_status.setStyleSheet('background-color: green; color: white; font-size: 12px; font-weight: bold')
        else:
            self.label_status.setText('CLABE INVÁLIDA!')
            self.label_status.setStyleSheet('background-color: red; color: white; font-size: 12px; font-weight: bold')

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Window()
    demo.show()

    try: 
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')