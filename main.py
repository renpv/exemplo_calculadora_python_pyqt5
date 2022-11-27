import sys 
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy

class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora')
        self.setFixedSize(400,400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.criar_display()
        
        self.botoes_na_linha(1, '7', '8', '9', '+')
        self.botoes_na_linha(2, '4', '5', '6', '-')
        self.botoes_na_linha(3, '1', '2', '3', '/', '')
        self.botoes_na_linha(4, '.', '0', '', '*')

        self.add_btn('C', 1, 4, 1,1, self.limpar_tudo, 'background: #fff1cc')
        self.add_btn('<-', 2, 4, 1,1, self.limpar_ultimo_caractere)
        self.add_btn('=', 4, 4, 1,1, self.eval_igual)

        self.grid.addWidget(self.display, 0,0,1,5)
        
        self.setCentralWidget(self.cw)

    def criar_display(self):
        self.display = QLineEdit()
        self.display.setDisabled(True)
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.display.setStyleSheet('background: white; font-size: 28px')

    def add_btn(self, label, row, col, rowspan, colspan, funcao=None, style=None):
        btn = QPushButton(label)
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        if not funcao:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(funcao)

        if style:
            btn.setStyleSheet(style)
            
    def botoes_na_linha(self, linha, *args):
        for i, label in enumerate(args):
            self.add_btn(label, linha, i, 1,1)

    def limpar_tudo(self):
        self.display.setText('')

    def limpar_ultimo_caractere(self):
        self.display.setText(self.display.text()[:-1])

    def eval_igual(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        except Exception as e:
            self.display.setText('Conta inválida')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
