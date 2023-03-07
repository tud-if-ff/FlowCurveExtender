import os

from DIC_Exchange.convert_to import load_from
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QFileDialog
from FlowCurveExtender.gui.ui_convertHdf5Popup import Ui_ConvertHDF5Popup


class ConvertHdf5Popup(Ui_ConvertHDF5Popup, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.setupUi(self)
        self.pushButton_addFiles.clicked.connect(self.add_files)
        self.pushButton_removeFiles.clicked.connect(self.remove_files)
        self.pushButton_convert.clicked.connect(self.convert)
        self.progressBar.setFormat("%v of %m")
        self.progressBar.setVisible(False)

    def add_files(self):
        self.progressBar.setVisible(False)
        paths = QFileDialog.getOpenFileNames(self, "Open Image", "~", "Aramis XML File (*.xml)")[0]
        if len(paths) == 0:
            return

        for path in paths:
            path_dir = os.path.dirname(path)
            self.listWidget.addItem(os.path.join(path_dir, path))

    def remove_files(self):
        self.listWidget.takeItem(self.listWidget.currentRow())

    def convert(self):
        if self.listWidget.count() == 0:
            return

        self.progressBar.setVisible(True)
        self.progressBar.setMaximum(self.listWidget.count())
        self.progressBar.setValue(self.progressBar.minimum())

        done_count = 0
        while self.listWidget.count() > 0:
            text = self.listWidget.takeItem(0).text()
            dic_res = load_from(text, force_rupture_ratio=.8)
            dic_res.save_to_hdf5(text[:-4] + ".hdf5")
            print("saved " + str(text[:-4] + ".hdf5"))
            done_count += 1
            self.progressBar.setValue(done_count)
