from sympy import *
from sympy.parsing.latex import parse_latex
import sys
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random


class vh_dths_b3(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that
        # displays the 'figure'it takes the
        # 'figure' instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to 'plot' method
        self.luu = QPushButton('Lưu ảnh')
        self.thoat = QPushButton('Thoát')

        # random data
        data = [random.random() for i in range(10)]

        # clearing old figure
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(111)

        # plot data
        ax.plot(data, '*-')

        # refresh canvas
        self.canvas.draw()

        # creating a Vertical Box layout
        layout = QVBoxLayout()

        # adding tool bar to the layout
        # layout.addWidget(self.toolbar)

        # adding canvas to the layout
        layout.addWidget(self.canvas)

        # adding push button to the layout
        layout.addWidget(self.luu)
        layout.addWidget(self.thoat)
        self.luu.clicked.connect(self.save)
        self.thoat.clicked.connect(self.reject)

        # setting layout to the main window
        self.setLayout(layout)

    def save(self):
        filename = QFileDialog.getSaveFileName(self, "Save As", "plot.png", "*.png ;; *.pdf ")
        savename = filename[0]
        if savename:
            self.figure.savefig(savename)
