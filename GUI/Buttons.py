import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QPushButton
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Click Me",self)
        self.setGeometry(100,100,600,600)
        self.label = QLabel("Hello",self)
        self.initUI()
    
    def initUI(self):
        
        self.button.setGeometry(150,200,200,100)
        self.button.setStyleSheet("font-size: 30px")
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(150,300,200,100)
        self.label.setStyleSheet("font-size :50px")

    def on_click(self):
        self.label.setText("Goodbye")
        self.button.setDisabled(True)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
   