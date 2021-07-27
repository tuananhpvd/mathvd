# import os
# import subprocess
# import random

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.uic import loadUi
from ham.vh_bbt.vh_bbt_b2 import *
from ham.vh_bbt.vh_bbt_b3 import *


class vh_bbt_b2_Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/bangbienthien_dialog.ui", self)
        #self.setWindowTitle("Phương trình bậc 2")
        self.setFixedSize(self.size())

        huongdan = """
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
    
            Hướng dẫn ve BBT bac 2:
            $$y=a x^2+bx+c$$
    
            </body>
            </html>
        """
        self.webhd.setHtml(huongdan)
        self.webhd.show()

        dang = """
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
            $$y=a x^2+bx+c$$
            </p>

            </body>
            </html>
        """

        self.webdang.setHtml(dang)
        self.webdang.show()

        self.btn_kt.clicked.connect(self.kiemtra)
        self.btn_vebbt.clicked.connect(self.thuchien)

    def kiemtra(self):
        nhap1 = self.lne_nhap.text()
        # Báo lỗi nếu chưa chọn dạng
        if nhap1 == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Thông báo")
            msg.setText("Đã có lỗi!")
            msg.setInformativeText("Chưa nhập hàm số.")
            msg.exec_()
        else:
            xemtruoc = """
                <!DOCTYPE html>
                <html>
                <head>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/brython/3.9.0/brython.js"></script>
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
                   $$ y=%s $$
                </body>
                </html>
                    """ % nhap1
            self.webxem.setHtml(xemtruoc)
            self.webxem.show()

    def thuchien(self):
        nhap1 = self.lne_nhap.text()
        # Báo lỗi nếu chưa chọn dạng
        if nhap1 == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Thông báo")
            msg.setText("Đã có lỗi!")
            msg.setInformativeText("Chưa nhập hàm số.")
            msg.exec_()
        else:
            vh_bbt_b2.bbt_b2(self)


class vh_bbt_b3_Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/bangbienthien_dialog.ui", self)
        # self.setWindowTitle("Phương trình bậc 2")
        self.setFixedSize(self.size())

        huongdan = """
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

            Hướng dẫn ve BBT bac 3:
            $$y=a x^3+bx^2+cx+d$$

            </body>
            </html>
        """
        self.webhd.setHtml(huongdan)
        self.webhd.show()

        dang = """
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
            $$y=a x^3+bx^2+cx+d$$
            </p>

            </body>
            </html>
        """

        self.webdang.setHtml(dang)
        self.webdang.show()

        self.btn_kt.clicked.connect(self.kiemtra)
        self.btn_vebbt.clicked.connect(self.thuchien)

    def kiemtra(self):
        nhap1 = self.lne_nhap.text()
        # Báo lỗi nếu chưa chọn dạng
        if nhap1 == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Thông báo")
            msg.setText("Đã có lỗi!")
            msg.setInformativeText("Chưa nhập hàm số.")
            msg.exec_()
        else:
            xemtruoc = """
                <!DOCTYPE html>
                <html>
                <head>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/brython/3.9.0/brython.js"></script>
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
                   $$ y=%s $$
                </body>
                </html>
                    """ % nhap1
            self.webxem.setHtml(xemtruoc)
            self.webxem.show()

    def thuchien(self):
        nhap1 = self.lne_nhap.text()
        # Báo lỗi nếu chưa chọn dạng
        if nhap1 == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Thông báo")
            msg.setText("Đã có lỗi!")
            msg.setInformativeText("Chưa nhập hàm số.")
            msg.exec_()
        else:
            vh_bbt_b3.bbt_b3(self)