# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popUpWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

from FlowCurveExtender.gui.mplwidget import MplWidget

class Ui_PopupWidget(object):
    def setupUi(self, PopupWidget):
        if not PopupWidget.objectName():
            PopupWidget.setObjectName(u"PopupWidget")
        PopupWidget.resize(559, 470)
        self.verticalLayoutWidget = QWidget(PopupWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(-1, 0, 561, 451))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mplWidget = MplWidget(self.verticalLayoutWidget)
        self.mplWidget.setObjectName(u"mplWidget")

        self.verticalLayout.addWidget(self.mplWidget)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.horizontalLayout_windowSize = QHBoxLayout()
        self.horizontalLayout_windowSize.setObjectName(u"horizontalLayout_windowSize")
        self.horizontalLayout_windowSize.setContentsMargins(10, 10, 10, 10)
        self.label_windowSize = QLabel(self.verticalLayoutWidget)
        self.label_windowSize.setObjectName(u"label_windowSize")

        self.horizontalLayout_windowSize.addWidget(self.label_windowSize)

        self.spinBox_windowSize = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_windowSize.setObjectName(u"spinBox_windowSize")
        self.spinBox_windowSize.setMinimum(1)
        self.spinBox_windowSize.setMaximum(50)
        self.spinBox_windowSize.setValue(10)

        self.horizontalLayout_windowSize.addWidget(self.spinBox_windowSize)


        self.gridLayout.addLayout(self.horizontalLayout_windowSize, 1, 1, 1, 1)

        self.pushButton_updatePlot = QPushButton(self.verticalLayoutWidget)
        self.pushButton_updatePlot.setObjectName(u"pushButton_updatePlot")

        self.gridLayout.addWidget(self.pushButton_updatePlot, 0, 2, 1, 1)

        self.pushButton_exportData = QPushButton(self.verticalLayoutWidget)
        self.pushButton_exportData.setObjectName(u"pushButton_exportData")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_exportData.sizePolicy().hasHeightForWidth())
        self.pushButton_exportData.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_exportData, 1, 2, 1, 1)

        self.checkBox_smoothingEnabled = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_smoothingEnabled.setObjectName(u"checkBox_smoothingEnabled")

        self.gridLayout.addWidget(self.checkBox_smoothingEnabled, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(PopupWidget)

        QMetaObject.connectSlotsByName(PopupWidget)
    # setupUi

    def retranslateUi(self, PopupWidget):
        PopupWidget.setWindowTitle(QCoreApplication.translate("PopupWidget", u"Form", None))
        self.label_windowSize.setText(QCoreApplication.translate("PopupWidget", u"Window Size Smoothing", None))
        self.pushButton_updatePlot.setText(QCoreApplication.translate("PopupWidget", u"Update Plot", None))
        self.pushButton_exportData.setText(QCoreApplication.translate("PopupWidget", u"Export data", None))
        self.checkBox_smoothingEnabled.setText(QCoreApplication.translate("PopupWidget", u"Enable Smoothing", None))
    # retranslateUi

