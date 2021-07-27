from sympy import *
from sympy.parsing.latex import parse_latex
import os
import subprocess
# import random
from PyQt5.QtWidgets import QDialog


class vh_bbt_b2(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

    def bbt_b2(self):
        # bien = self.lne_bien.text()
        x = symbols('x')
        hs1 = self.lne_nhap.text()
        hs2 = parse_latex(hs1)

        with open('data/bbt/bangbienthien.tex', 'w', encoding='utf-8') as file:
            #########
            # bắt đầu câu hỏi

            # phương trình
            x = symbols('x')
            pt = 2 * x ** 2 - 3 * x + 3
            # kq = solveset(pt, x)
            ##############

            file.write("Bảng biến thiên hàm số $y=" + str(hs1) + "$\n")
            # file.write("Bảng biến thiên hàm số $y=3x^2-x+1$\n")

            # hết câu hỏi
            # kết thúc file
            ####################
        # Mở file pdf khi hoàn thành
        kt = subprocess.call('pdflatex -synctex=1 --shell-escape -interaction=nonstopmode data/bbt/bbt_main.tex')
        if kt != 0:
            print('Exit-code not 0, check result!')
        else:
            os.system('start bbt_main.pdf')
