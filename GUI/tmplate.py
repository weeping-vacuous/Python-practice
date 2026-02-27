import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,600,600)
        self.initUI()

        
    def initUI(self):
        pass

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
   