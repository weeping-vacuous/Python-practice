import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton,QWidget,QHBoxLayout
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()

        
    def initUI(self):
        CW = QWidget()
        self.setCentralWidget(CW)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        CW.setLayout(hbox)
        self.button1.setObjectName("b1")
        self.button2.setObjectName("b2")
        self.button3.setObjectName("b3")

        self.setStyleSheet("""
            QPushButton{
                           font-size: 40px;
                           font-family: Arial;
                           padding: 15px 75px;
                           margin: 20px;
                           border: 3px solid;
                           border-radius: 15px;
                           }
            QPushButton#b1{
                           background-color: hsl(5, 88%, 52%);}
            QPushButton#b2{
                           background-color: hsl(111, 87%, 20%);}
            QPushButton#b3{
                           background-color: hsl(212, 94%, 32%);}
            QPushButton#b1:hover{
                           background-color: hsl(5, 88%, 72%);}
            QPushButton#b2:hover{
                           background-color: hsl(111, 87%, 40%);}
            QPushButton#b3:hover{
                           background-color: hsl(212, 94%, 52%);}
   """)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
   