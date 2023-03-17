import os

from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget
from FlowCurveExtender.gui.ui_popup_widget import Ui_PopupWidget
from FlowCurveExtender.gui.mplwidget import MplWidget
import pandas as pd


class PopupWidget(Ui_PopupWidget, QWidget):
    def __init__(self, testSerie, plot_type, parent=None):
        super().__init__(parent=parent)

        self.setupUi(self)
        self.testSerie = testSerie
        self.plot_type = plot_type

        self.plots = []

        self.pushButton_updatePlot.clicked.connect(self.update_plot)
        self.pushButton_exportData.clicked.connect(self.export_plot)
        self.mplWidget.plot_clear()
        self.update_plot()

    def update_plot(self):
        self.mplWidget.plot_clear()
        if self.plot_type == "stress_strain":
            self.plots =  self.testSerie.get_plot_stress_strain(self.mplWidget.get_ax(), self.spinBox_windowSize.value(), self.checkBox_smoothingEnabled.isChecked())
            self.mplWidget.draw()
            return

        if self.plot_type == "stress_strain_rate":
            self.plots =  self.testSerie.get_plot_stress_strain_rate(self.mplWidget.get_ax(), self.spinBox_windowSize.value(), self.checkBox_smoothingEnabled.isChecked())
            self.mplWidget.draw()
            return

    def export_plot(self):
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')

        if len(folderpath)==0:
            return

        ax = self.mplWidget.get_ax()

        for plot in self.plots:
            line = plot[0]
            data = {ax.get_xlabel(): line.get_xdata(), ax.get_ylabel(): line.get_ydata()}
            df = pd.DataFrame(data)
            base_filename = line.get_label()
            base_filename = base_filename.split(".")[0]
            base_filename = base_filename+"_"+self.plot_type
            filePath = os.path.join(folderpath, base_filename + '.' + "csv")
            df.to_csv(filePath)