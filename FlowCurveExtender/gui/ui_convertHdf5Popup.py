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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_ConvertHDF5Popup(object):
    def setupUi(self, ConvertHDF5Popup):
        if not ConvertHDF5Popup.objectName():
            ConvertHDF5Popup.setObjectName(u"ConvertHDF5Popup")
        ConvertHDF5Popup.resize(779, 360)
        self.widget = QWidget(ConvertHDF5Popup)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 761, 342))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Open Sans"])
        font.setPointSize(12)
        font.setBold(False)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listWidget = QListWidget(self.widget)
        self.listWidget.setObjectName(u"listWidget")

        self.horizontalLayout.addWidget(self.listWidget)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_addFiles = QPushButton(self.widget)
        self.pushButton_addFiles.setObjectName(u"pushButton_addFiles")

        self.verticalLayout_2.addWidget(self.pushButton_addFiles)

        self.pushButton_removeFiles = QPushButton(self.widget)
        self.pushButton_removeFiles.setObjectName(u"pushButton_removeFiles")

        self.verticalLayout_2.addWidget(self.pushButton_removeFiles)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.pushButton_convert = QPushButton(self.widget)
        self.pushButton_convert.setObjectName(u"pushButton_convert")

        self.verticalLayout_2.addWidget(self.pushButton_convert)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)


        self.retranslateUi(ConvertHDF5Popup)

        QMetaObject.connectSlotsByName(ConvertHDF5Popup)
    # setupUi

    def retranslateUi(self, ConvertHDF5Popup):
        ConvertHDF5Popup.setWindowTitle(QCoreApplication.translate("ConvertHDF5Popup", u"Form", None))
        self.label.setText(QCoreApplication.translate("ConvertHDF5Popup", u"Selected Files", None))
        self.pushButton_addFiles.setText(QCoreApplication.translate("ConvertHDF5Popup", u"Add Files", None))
        self.pushButton_removeFiles.setText(QCoreApplication.translate("ConvertHDF5Popup", u"Remove Files", None))
        self.pushButton_convert.setText(QCoreApplication.translate("ConvertHDF5Popup", u"Convert to HDF5", None))
    # retranslateUi

