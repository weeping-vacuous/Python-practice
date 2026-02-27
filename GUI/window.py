import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,QLabel
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First GUI")
        self.setGeometry(100, 100, 600, 400)
        self.setWindowIcon(QIcon("D:\\python\\GUI\\logo.png"))

        label = QLabel("Hello",self)
        label.setFont(QFont("Ariral",40))
        label.setGeometry(0,0,600,100)
        label.setStyleSheet("color:red;"
                            "background-color: yellow;"
                            "font-weight: bold;"
                            "font-style: italic;")
        
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

def main():
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()