# from sympy import *
# import os
# import subprocess
# import random
from PyQt5.QtWidgets import QDialog


class bt_hhgt_3_ptdt(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

    def ptdt_1(self):
        print("BT Phuong trinh duong thang")
        # print(self.listw_dang.currentRow())
        print(self.listw_dang.currentItem().text())
        print(self.spin_socau.text())
