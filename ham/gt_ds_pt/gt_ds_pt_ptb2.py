from sympy import *
from sympy.parsing.latex import parse_latex
# import os
# import subprocess
# import random
from PyQt5.QtWidgets import QDialog


class gt_ds_pt_ptb2(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

    def ptb2_1(self):
        bien = self.lne_bien.text()
        x = symbols(bien)
        pt1 = self.lne_nhap.text()
        pt2 = parse_latex(pt1)

        dang = self.cbo_dang.currentIndex()

        if dang == 1:
            kq1 = solveset(pt2, x)
            kq2 = latex(kq1)

            ketqua = """
                <!DOCTYPE html>
                <html>
                <head>
    
                <script>
                MathJax = {
                  tex: {
                    inlineMath: [['$', '$'], ['\\(', '\\)']]
                  }
                };
                </script>
                <script type="text/javascript" id="MathJax-script" async 
                src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
                </script>
    
                </head>
                <body>
    
                <p>
                $$ S= %s $$
                </p>
    
                </body>
                </html>
            """ % kq2

            self.webkq.setHtml(ketqua)
            self.webkq.show()

            giaichitiet = """
                <!DOCTYPE html>
                <html>
                <head>
    
                <script>
                MathJax = {
                  tex: {
                    inlineMath: [['$', '$'], ['\\(', '\\)']]
                  }
                };
                </script>
                <script type="text/javascript" id="MathJax-script" async 
                src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
                </script>
    
                </head>
                <body>
    
                Tập nghiệm của hương trình đã cho là: $S=%s$
    
                </body>
                </html>
            """ % kq2

            self.webgiai.setHtml(giaichitiet)
            self.webgiai.show()

        if dang == 2:
            kq1 = solveset(pt2, x)
            kq2 = latex(kq1)

            ketqua = """
                <!DOCTYPE html>
                <html>
                <head>

                <script>
                MathJax = {
                  tex: {
                    inlineMath: [['$', '$'], ['\\(', '\\)']]
                  }
                };
                </script>
                <script type="text/javascript" id="MathJax-script" async 
                src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
                </script>

                </head>
                <body>

                <p>
                $$ S= %s $$
                </p>

                </body>
                </html>
            """ % kq2

            self.webkq.setHtml(ketqua)
            self.webkq.show()

            giaichitiet = """
                <!DOCTYPE html>
                <html>
                <head>

                <script>
                MathJax = {
                  tex: {
                    inlineMath: [['$', '$'], ['\\(', '\\)']]
                  }
                };
                </script>
                <script type="text/javascript" id="MathJax-script" async 
                src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
                </script>

                </head>
                <body>

                Đây là phương trình bậc 2 có chứa tham số.<br> 
                Phương trình đã cho có nghiệm là: $x_1=m_1$ và $x_2=m_2$

                </body>
                </html>
            """

            self.webgiai.setHtml(giaichitiet)
            self.webgiai.show()