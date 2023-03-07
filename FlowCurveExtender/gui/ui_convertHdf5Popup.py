# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'convertHdf5Popup.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QProgressBar, QPushButton, QSizePolicy, QWidget)

class Ui_ConvertHDF5Popup(object):
    def setupUi(self, ConvertHDF5Popup):
        if not ConvertHDF5Popup.objectName():
            ConvertHDF5Popup.setObjectName(u"ConvertHDF5Popup")
        ConvertHDF5Popup.resize(779, 300)
        self.listWidget = QListWidget(ConvertHDF5Popup)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(30, 30, 581, 191))
        self.pushButton_addFiles = QPushButton(ConvertHDF5Popup)
        self.pushButton_addFiles.setObjectName(u"pushButton_addFiles")
        self.pushButton_addFiles.setGeometry(QRect(640, 40, 101, 20))
        self.pushButton_removeFiles = QPushButton(ConvertHDF5Popup)
        self.pushButton_removeFiles.setObjectName(u"pushButton_removeFiles")
        self.pushButton_removeFiles.setGeometry(QRect(640, 70, 101, 20))
        self.pushButton_convert = QPushButton(ConvertHDF5Popup)
        self.pushButton_convert.setObjectName(u"pushButton_convert")
        self.pushButton_convert.setGeometry(QRect(640, 170, 101, 41))
        self.label = QLabel(ConvertHDF5Popup)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 231, 16))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.progressBar = QProgressBar(ConvertHDF5Popup)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(190, 250, 281, 23))
        self.progressBar.setValue(24)

        self.retranslateUi(ConvertHDF5Popup)

        QMetaObject.connectSlotsByName(ConvertHDF5Popup)
    # setupUi

    def retranslateUi(self, ConvertHDF5Popup):
        ConvertHDF5Popup.setWindowTitle(QCoreApplication.translate("ConvertHDF5Popup", u"Form", None))
        self.pushButton_addFiles.setText(QCoreApplication.translate("ConvertHDF5Popup", u"Add Files", None))
        self.pushButton_removeFiles.setText(QCoreApplication.translate("ConvertHDF5Popup", u"Remove Files", None))
        self.pushButton_convert.setText(QCoreApplication.translate("ConvertHDF5Popup", u"Convert to HDF5", None))
        self.label.setText(QCoreApplication.translate("ConvertHDF5Popup", u"Selected Files", None))
    # retranslateUi

