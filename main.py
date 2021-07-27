import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from ham.baitap_hhgt_3 import*
from ham.giaitoan_ds_pt import*
from ham.vehinh_bbt import*
from ham.vehinh_dths import*
from main_win import Ui_MainWindow  # import file main_win.py


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.action_gioithieu.triggered.connect(self.gioithieu)
        self.action_thoat.triggered.connect(self.close)
        self.action_bt_hhgt3_ptmp.triggered.connect(self.bt_hhgt_3_ptmp)
        self.action_bt_hhgt3_ptdt.triggered.connect(self.bt_hhgt_3_ptdt)
        self.action_gt_ds_pt_ptb2.triggered.connect(self.gt_ds_pt_ptb2)
        self.action_vh_bbt_b2.triggered.connect(self.vh_bbt_b2)
        self.action_vh_bbt_b3.triggered.connect(self.vh_bbt_b3)
        self.action_vh_dths_b3.triggered.connect(self.vh_dths_b3)

    def gioithieu(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Xin chào!")
        msg.setInformativeText("Đây là giới thiệu phần mềm")
        msg.setWindowTitle("Giới thiệu phần mềm")
        msg.exec_()

    def bt_hhgt_3_ptmp(self):
        dialog = bt_hhgt_3_ptmp_Dialog(self)
        dialog.exec()

    def bt_hhgt_3_ptdt(self):
        dialog = bt_hhgt_3_ptdt_Dialog(self)
        dialog.exec()

    def gt_ds_pt_ptb2(self):
        dialog = gt_ds_pt_ptb2_Dialog(self)
        dialog.exec()

    def vh_bbt_b2(self):
        dialog = vh_bbt_b2_Dialog(self)
        dialog.exec()

    def vh_bbt_b3(self):
        dialog = vh_bbt_b3_Dialog(self)
        dialog.exec()

    def vh_dths_b3(self):
        dialog = vh_dths_b3_Dialog(self)
        dialog.exec()

# main


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
