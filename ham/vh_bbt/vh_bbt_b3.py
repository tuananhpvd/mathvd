from sympy import *
from sympy.parsing.latex import parse_latex
import os
import subprocess
# import random
from PyQt5.QtWidgets import QDialog


class vh_bbt_b3(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

    def bbt_b3(self):
        # bien = self.lne_bien.text()
        # lay thong tin ham so
        x = symbols('x')
        hs1 = self.lne_nhap.text()  # ham so kieu latex khi nhap
        hs2 = parse_latex(hs1)  # ham so kieu sympy
        bt = poly(hs2, x)  # chuyen hs ve dang da thuc
        heso = bt.all_coeffs()  # lay cac he so cua bt
        a = heso[0]
        dh2 = diff(hs2, x)  # dao ham hs2
        gptdh2 = solveset(dh2, x, domain=S.Reals)  # giai pt dh2
        songhiem = len(gptdh2)

        with open('bbt_hs.tex', 'w', encoding='utf-8') as file:
            file.write("\\documentclass{standalone}\n")
            file.write("\\usepackage{amsmath}\n")
            file.write("\\usepackage{luamplib}\n")
            file.write("\\begin{document}\n")
            file.write("\\input{bbt}\n")
            if songhiem == 2:
                x_1 = gptdh2.args[0]
                x_2 = gptdh2.args[1]
                y_1 = hs2.subs(x, x_1)
                y_2 = hs2.subs(x, x_2)
                if a > 0:
                    file.write("\\hsbbd{"+str(latex(x_1))+"}{"+str(latex(x_2))+"}{"+str(latex(y_1))+"}{"+str(latex(y_2))+"}\n")
                if a < 0:
                    file.write("\\hsbba{"+str(latex(x_1))+"}{"+str(latex(x_2))+"}{"+str(latex(y_1))+"}{"+str(latex(y_2))+"}\n")
            if songhiem == 1:
                x_1 = gptdh2.args[0]
                y_1 = hs2.subs(x, x_1)
                if a > 0:
                    file.write("\\hsbbdt{"+str(latex(x_1))+"}{"+str(latex(y_1))+"}\n")
                if a < 0:
                    file.write("\\hsbbdg{"+str(latex(x_1))+"}{"+str(latex(y_1))+"}\n")
            if songhiem == 0:
                if a > 0:
                    file.write("\\hsbbngt\n")
                if a < 0:
                    file.write("\\hsbbngg\n")
            file.write("\\end{document}\n")

        # Mở file pdf khi hoàn thành
        kt = subprocess.call('pdflatex -synctex=1 --shell-escape -interaction=nonstopmode bbt_hsb3.tex')
        if kt != 0:
            print('Exit-code not 0, check result!')
        else:
            os.system('start bbt_hsb3.pdf')
