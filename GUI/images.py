import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel
from PyQt5.QtGui import QPixmap,QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,600,600)
        self.setWindowTitle("Pokemon Dictionary")
        self.setWindowIcon(QIcon("D:\python\GUI\pokemonlogo.png"))

        label = QLabel(self)
        label.setGeometry(0,0,600,600)
        label.setPixmap(QPixmap("D:\\python\\GUI\\pikachu.png"))
        label.setScaledContents(True)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
   