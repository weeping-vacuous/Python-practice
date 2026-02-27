import sys
from PyQt5.QtWidgets import (QMainWindow,QApplication,QLabel,QWidget,
                             QVBoxLayout,QHBoxLayout,QGridLayout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,600,600)
        self.initUI()

    def initUI(self):
        Central_Widget = QWidget()
        self.setCentralWidget(Central_Widget)

        label1 = QLabel("1",self)
        label2 = QLabel("2",self)
        label3 = QLabel("3",self)
        label4 = QLabel("4",self)
        label5 = QLabel("5",self)

        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: blue;")
        label3.setStyleSheet("background-color: green;")
        label4.setStyleSheet("background-color: yellow;")
        label5.setStyleSheet("background-color: purple;")

        Grid=QGridLayout()

        Grid.addWidget(label1,0,0)
        Grid.addWidget(label2,0,1)
        Grid.addWidget(label3,1,0)
        Grid.addWidget(label4,1,1)
        Grid.addWidget(label5,2,2)

        Central_Widget.setLayout(Grid)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
   