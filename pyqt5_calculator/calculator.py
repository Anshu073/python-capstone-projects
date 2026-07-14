import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QLabel
from PyQt5.QtCore import Qt
class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)

        self.label1 = QLabel(self)

        self.button0 = QPushButton("0",self)
        self.button1 = QPushButton("1",self)
        self.button2 = QPushButton("2",self)
        self.button3 = QPushButton("3",self)
        self.button4 = QPushButton("4",self)
        self.button5 = QPushButton("5",self)
        self.button6 = QPushButton("6",self)
        self.button7 = QPushButton("7",self)
        self.button8 = QPushButton("8",self)
        self.button9 = QPushButton("9",self)
        self.button10 = QPushButton("+",self)
        self.button11 = QPushButton("-",self)
        self.button12 = QPushButton("*",self)
        self.button13 = QPushButton("/",self)
        self.button14 = QPushButton("=",self)
        self.button15 = QPushButton("AC",self)
        self.button16 = QPushButton("⌫",self)

        self.expression = ""
        

        self.initUI()
    
    def initUI(self):

        central_widget = QWidget()
        self.setCentralWidget(central_widget)


        #self.label1.setStyleSheet("background-color: grey;")
        

        self.button0.setStyleSheet("font-size: 25px;"
                                   "background-color: pink;")
        self.button1.setStyleSheet("font-size: 25px;"
                                   "background-color: pink;")
        self.button2.setStyleSheet("font-size: 25px;"
                                   "background-color: pink;")
        self.button3.setStyleSheet("font-size: 25px;"
                                   "background-color: pink;")
        self.button4.setStyleSheet("font-size: 25px;"
                                   "background-color: pink;")
        self.button5.setStyleSheet("font-size: 25px;"
                                   "background-color: pink;")
        self.button6.setStyleSheet("font-size: 25px;"
                                   "background-color: pink;")
        self.button7.setStyleSheet("font-size: 25px;"
                                   "background-color: pink;")
        self.button8.setStyleSheet("font-size: 25px;"
                                   "background-color: pink;")
        self.button9.setStyleSheet("font-size: 25px;"
                                   "background-color: pink;")
        self.button10.setStyleSheet("font-size: 25px;"
                                   "background-color: orange;")
        self.button11.setStyleSheet("font-size: 25px;"
                                   "background-color: orange;")
        self.button12.setStyleSheet("font-size: 25px;"
                                   "background-color: orange;")
        self.button13.setStyleSheet("font-size: 25px;"
                                   "background-color: orange;")
        self.button14.setStyleSheet("font-size: 25px;"
                                   "background-color: green;")
        self.button15.setStyleSheet("font-size: 25px;"
                                   "background-color: yellow;;")
        self.button16.setStyleSheet("font-size: 25px;"
                                    "background-color:red;")
        
        self.label1.setFixedHeight(60)
        self.label1.setStyleSheet("font-size: 30px;"
                                  "color: white;"
                                  "background-color: black;"
                                  "font-weight: bold;"
                                  )
        self.label1.setAlignment(Qt.AlignRight | Qt.AlignCenter)

        grid = QGridLayout()
        
        grid.addWidget(self.label1,0,0,1,4)
        grid.addWidget(self.button1,1,0)
        grid.addWidget(self.button2,1,1)
        grid.addWidget(self.button3,1,2)
        grid.addWidget(self.button10,1,3)
        grid.addWidget(self.button4,2,0)
        grid.addWidget(self.button5,2,1)
        grid.addWidget(self.button6,2,2)
        grid.addWidget(self.button11,2,3)
        grid.addWidget(self.button7,3,0)
        grid.addWidget(self.button8,3,1)
        grid.addWidget(self.button9,3,2)
        grid.addWidget(self.button12,3,3)
        grid.addWidget(self.button0,4,1)
        grid.addWidget(self.button13,4,3)
        grid.addWidget(self.button15,5,0)
        grid.addWidget(self.button16,5,1)
        grid.addWidget(self.button14,5,2)

        central_widget.setLayout(grid)

        self.button0.clicked.connect(self.button_clicked)
        self.button1.clicked.connect(self.button_clicked)
        self.button2.clicked.connect(self.button_clicked)
        self.button3.clicked.connect(self.button_clicked)
        self.button4.clicked.connect(self.button_clicked)
        self.button5.clicked.connect(self.button_clicked)
        self.button6.clicked.connect(self.button_clicked)
        self.button7.clicked.connect(self.button_clicked)
        self.button8.clicked.connect(self.button_clicked)
        self.button9.clicked.connect(self.button_clicked)
        self.button10.clicked.connect(self.button_clicked)
        self.button11.clicked.connect(self.button_clicked)
        self.button12.clicked.connect(self.button_clicked)
        self.button13.clicked.connect(self.button_clicked)
        self.button14.clicked.connect(self.button_clicked)
        self.button15.clicked.connect(self.button_clicked)
        self.button16.clicked.connect(self.button_clicked)


    def button_clicked(self):
        button = self.sender()
        symbols = ["+","*","/","=","AC","⌫"]
        operators = ["+","-","*","/"]

        if button.text() == "=":
            if self.expression == "" or self.expression[-1] in operators:
                pass
            else:
                result = eval(self.expression)
                self.label1.setText(str(result))
                self.expression = str(self.label1.text())
            
        elif button.text() == "AC":
            self.expression = ""
            self.label1.setText(self.expression)

        elif button.text() == "⌫":
            self.expression = self.expression[:-1]
            self.label1.setText(self.expression)
        else:
            if button.text() in operators:
                if self.expression == "":
                    if button.text() == "-":
                        self.expression += button.text()
                        self.label1.setText(self.expression)
                    pass
                elif self.expression[-1] in operators:
                    if self.expression == "-":
                        pass
                    else:
                        self.expression = self.expression[:-1] + button.text()
                        self.label1.setText(self.expression)
                else:
                    self.expression += button.text()
                    self.label1.setText(self.expression)
            else:
                self.expression += button.text()
            
                index = 0
                if self.expression[index] == "0":
                    self.expression = self.expression[index+1:]
                
                self.label1.setText(self.expression)

        
        

def main():
    app = QApplication(sys.argv)
    Calc = Calculator()
    Calc.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()