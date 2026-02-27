import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,600,600)
        self.checkbox = QCheckBox("Do you like pizza?",self)

        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(10,0,500,100)
        self.checkbox.setStyleSheet("font-size: 30px;"
                                    "font-family: Arial;")
        self.checkbox.stateChanged.connect(self.check_state)
        

    def check_state(self,state):
        if state == Qt.Checked:
            print("You like pizza")
        else:
            print("You do not like pizza")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
   