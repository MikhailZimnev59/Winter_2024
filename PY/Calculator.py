from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit, QTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")

        w, h = 200, 25

        self.line1 = QLineEdit()
        self.line1.setFixedSize(QSize(w, h))

        self.line2 = QLineEdit()
        self.line2.setFixedSize(QSize(w, h))

        self.button_add = QPushButton("+")
        self.button_add.setFixedSize(QSize(w, h))
        self.button_add.clicked.connect(self.the_button_add)

        self.button_sub = QPushButton("-")
        self.button_sub.setFixedSize(QSize(w, h))
        self.button_sub.clicked.connect(self.the_button_sub)

        self.button_mul = QPushButton("*")
        self.button_mul.setFixedSize(QSize(w, h))
        self.button_mul.clicked.connect(self.the_button_mul)

        self.button_div = QPushButton("/")
        self.button_div.setFixedSize(QSize(w, h))
        self.button_div.clicked.connect(self.the_button_div)

        self.button_div_int = QPushButton("//")
        self.button_div_int.setFixedSize(QSize(w, h))
        self.button_div_int.clicked.connect(self.the_button_div_int)

        self.te = QTextEdit()
        self.te.setFixedSize(QSize(w, w))

        self.label = QLabel("=")
        self.label.setFixedSize(QSize(w, h))
        font = self.label.font()
        font.setPointSize(10)
        self.label.setFont(font)
        # self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        layout = QVBoxLayout()
        widgets = [self.line1, self.line2, self.label, self.te,
                   self.button_add, self.button_sub, self.button_mul, self.button_div, self.button_div_int,
                   ]
        for w in widgets:
            layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def the_button_add(self):
        try:
            res = '=' + str(eval(self.line1.text() + '+' + self.line2.text()))
        except:
            res = 'Mistake!'
        self.label.setText(res)
        self.te.append(res)

    def the_button_sub(self):
        try:
            res = '=' + str(eval(self.line1.text() + '-' + self.line2.text()))
        except:
            res = 'Mistake!'
        self.label.setText(res)
        self.te.append(res)

    def the_button_mul(self):
        try:
            res = '=' + str(eval(self.line1.text() + '*' + self.line2.text()))
        except:
            res = 'Mistake!'
        self.label.setText(res)
        self.te.append(res)

    def the_button_div(self):
        try:
            res = '=' + str(eval(self.line1.text() + '/' + self.line2.text()))
        except:
            res = 'Mistake!'
        self.label.setText(res)
        self.te.append(res)

    def the_button_div_int(self):
        try:
            res = '=' + str(eval(self.line1.text() + '//' + self.line2.text()))
        except:
            res = 'Mistake!'
        self.label.setText(res)
        self.te.append(res)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
