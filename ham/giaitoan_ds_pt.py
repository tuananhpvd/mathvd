# import os
# import subprocess
# import random

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.uic import loadUi
from ham.gt_ds_pt.gt_ds_pt_ptb2 import *


class gt_ds_pt_ptb2_Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/giaitoan_dialog.ui", self)
        self.setWindowTitle("Phương trình bậc 2")
        self.setFixedSize(self.size())

        self.cbo_dang.addItem("--- Chọn dạng ---")
        self.cbo_dang.addItem("1. Dạng 1")
        self.cbo_dang.addItem("1. Dạng 2")

        self.cbo_dang.activated.connect(self.dang)

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
    
            Hướng dẫn phương trình bậc 2:
            $$a x^2+bx+c=0$$
    
            </body>
            </html>
        """
        self.webhd.setHtml(huongdan)
        self.webhd.show()

        self.lbl_nhap.setText("Nhập phương trình:")
        self.lne_bien.setText("x")

        self.btn_kt.clicked.connect(self.kiemtra)
        self.btn_giai.clicked.connect(self.thuchien)

    def dang(self):
        if self.cbo_dang.currentIndex() == 1:
            dang1 = """
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
                $$a x^2+bx+c=0$$
                </p>
    
                </body>
                </html>
            """

            self.webdang.setHtml(dang1)
            self.webdang.show()

        if self.cbo_dang.currentIndex() == 2:
            dang2 = """
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

                $$a x^2+bx=0$$

                </body>
                </html>
            """

            self.webdang.setHtml(dang2)
            self.webdang.show()

    def kiemtra(self):
        nhap1 = self.lne_nhap.text()
        # Báo lỗi nếu chưa chọn dạng
        if nhap1 == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Thông báo")
            msg.setText("Đã có lỗi!")
            msg.setInformativeText("Chưa nhập đề.")
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
                   $$ %s $$
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
            msg.setInformativeText("Chưa nhập đề.")
            msg.exec_()
        else:
            gt_ds_pt_ptb2.ptb2_1(self)
