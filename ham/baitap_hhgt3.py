# from sympy import *
# import os
# import subprocess
# import random
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi
from ham.bt_hhgt3.bt_hhgt3_ptmp import *
from ham.bt_hhgt3.bt_hhgt3_ptdt import *


class bt_hhgt3_ptmp_Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/baitap_dialog.ui", self)
        self.setWindowTitle("Phương trình mặt phẳng")
        self.setFixedSize(self.size())

        self.listw_dang.addItem('1. Phương trình mặt phẳng đầy đủ')
        self.listw_dang.addItem('2. Phương trình mặt phẳng khuyết D')
        self.listw_dang.addItem('3. Phương trình mặt phẳng (Oxy)')
        self.listw_dang.addItem('4. Phương trình mặt phẳng (Oxy)')
        self.listw_dang.addItem('5. Phương trình mặt phẳng (Oxy)')
        self.listw_dang.addItem('6. Phương trình mặt phẳng (Oxy)')
        self.listw_dang.addItem('7. Phương trình mặt phẳng (Oxy)')
        self.listw_dang.addItem('8. Phương trình mặt phẳng (Oxy)')
        self.listw_dang.addItem('9. Phương trình mặt phẳng (Oxy)')

        self.listw_dang.itemClicked.connect(self.themmota)

        self.radio_tn.setChecked(True)

        self.btn_tao.clicked.connect(self.thuchien)

    def themmota(self):
        self.tbr_mota.setText(self.listw_dang.currentItem().text())

    def thuchien(self):
        chon = self.listw_dang.currentRow()
        # Báo lỗi nếu chưa chọn dạng
        if chon == -1:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Thông báo")
            msg.setText("Đã có lỗi!")
            msg.setInformativeText("Chưa chọn dạng.")
            msg.exec_()
        else:
            bt_hhgt3_ptmp.ptmp_1(self)


class bt_hhgt3_ptdt_Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/baitap_dialog.ui", self)
        self.setWindowTitle("Phương trình đường thẳng")
        self.setFixedSize(self.size())

        self.listw_dang.addItem('1. Phương trình đường thẳng đầy đủ')
        self.listw_dang.addItem('2. Phương trình đường thẳng khuyết D')
        self.listw_dang.addItem('3. Phương trình đường thẳng (Oxy)')
        self.listw_dang.addItem('4. Phương trình đường thẳng (Oxy)')
        self.listw_dang.addItem('5. Phương trình đường thẳng (Oxy)')
        self.listw_dang.addItem('6. Phương trình đường thẳng (Oxy)')
        self.listw_dang.addItem('7. Phương trình đường thẳng (Oxy)')
        self.listw_dang.addItem('8. Phương trình đường thẳng (Oxy)')
        self.listw_dang.addItem('9. Phương trình đường thẳng (Oxy)')

        self.listw_dang.itemClicked.connect(self.themmota)

        self.radio_tn.setChecked(True)

        self.btn_tao.clicked.connect(self.thuchien)

    def themmota(self):
        self.tbr_mota.setText(self.listw_dang.currentItem().text())

    def thuchien(self):
        chon = self.listw_dang.currentRow()
        # Báo lỗi nếu chưa chọn dạng
        if chon == -1:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Thông báo")
            msg.setText("Đã có lỗi!")
            msg.setInformativeText("Chưa chọn dạng.")
            msg.exec_()
        else:
            bt_hhgt3_ptdt.ptdt_1(self)
