# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QLocale,
                            QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QAction, QFont)
from PySide6.QtWidgets import (QCheckBox, QComboBox, QDoubleSpinBox,
                               QFormLayout, QFrame, QGridLayout, QHBoxLayout,
                               QLabel, QLineEdit, QMenu,
                               QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
                               QSpinBox, QStatusBar, QTabWidget, QTextBrowser,
                               QVBoxLayout, QWidget)

from FlowCurveExtender.gui.mplwidget import MplWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 900)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1200, 900))
        MainWindow.setMaximumSize(QSize(1200, 900))
        font = QFont()
        font.setFamilies([u"Open Sans"])
        MainWindow.setFont(font)
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.actionLoad = QAction(MainWindow)
        self.actionLoad.setObjectName(u"actionLoad")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave.setEnabled(False)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionExit.setEnabled(False)
        self.actionAramis_XML = QAction(MainWindow)
        self.actionAramis_XML.setObjectName(u"actionAramis_XML")
        self.actionAramis_XML.setEnabled(False)
        self.actionhelp = QAction(MainWindow)
        self.actionhelp.setObjectName(u"actionhelp")
        self.actionhelp.setEnabled(False)
        self.actionLicense = QAction(MainWindow)
        self.actionLicense.setObjectName(u"actionLicense")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 1181, 841))
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tab_Orient = QWidget()
        self.tab_Orient.setObjectName(u"tab_Orient")
        self.horizontalLayoutWidget = QWidget(self.tab_Orient)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 1151, 791))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_orient = QTabWidget(self.horizontalLayoutWidget)
        self.tabWidget_orient.setObjectName(u"tabWidget_orient")
        self.tabWidget_orient.setEnabled(True)
        self.tabWidget_orient.setAutoFillBackground(False)
        self.tabWidget_orient.setTabPosition(QTabWidget.South)
        self.tabWidget_orient.setTabShape(QTabWidget.Rounded)
        self.tabWidget_orient.setElideMode(Qt.ElideLeft)
        self.tabWidget_orient.setUsesScrollButtons(True)
        self.tabWidget_orient.setDocumentMode(True)
        self.tabWidget_orient.setTabsClosable(False)
        self.tabWidget_orient.setMovable(False)
        self.tabWidget_orient.setTabBarAutoHide(False)

        self.horizontalLayout.addWidget(self.tabWidget_orient)

        self.line_2 = QFrame(self.horizontalLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_10 = QLabel(self.horizontalLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        font1 = QFont()
        font1.setFamilies([u"Open Sans"])
        font1.setPointSize(11)
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_10)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.spinBox_Orient_timestep = QSpinBox(self.horizontalLayoutWidget)
        self.spinBox_Orient_timestep.setObjectName(u"spinBox_Orient_timestep")
        self.spinBox_Orient_timestep.setMinimumSize(QSize(100, 0))

        self.gridLayout.addWidget(self.spinBox_Orient_timestep, 1, 1, 1, 1)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.comboBox_Orient_Field = QComboBox(self.horizontalLayoutWidget)
        self.comboBox_Orient_Field.addItem("")
        self.comboBox_Orient_Field.addItem("")
        self.comboBox_Orient_Field.addItem("")
        self.comboBox_Orient_Field.addItem("")
        self.comboBox_Orient_Field.setObjectName(u"comboBox_Orient_Field")
        self.comboBox_Orient_Field.setEditable(True)

        self.gridLayout.addWidget(self.comboBox_Orient_Field, 3, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.pushButton_Orient_UpdatePlot = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Orient_UpdatePlot.setObjectName(u"pushButton_Orient_UpdatePlot")

        self.verticalLayout.addWidget(self.pushButton_Orient_UpdatePlot)

        self.pushButton_Orient_time_force = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Orient_time_force.setObjectName(u"pushButton_Orient_time_force")

        self.verticalLayout.addWidget(self.pushButton_Orient_time_force)

        self.line = QFrame(self.horizontalLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.line_3 = QFrame(self.horizontalLayoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.label_11 = QLabel(self.horizontalLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_11)

        self.pushButton_Orient_Center = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Orient_Center.setObjectName(u"pushButton_Orient_Center")

        self.verticalLayout.addWidget(self.pushButton_Orient_Center)

        self.pushButton_Orient_OrientZ = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Orient_OrientZ.setObjectName(u"pushButton_Orient_OrientZ")

        self.verticalLayout.addWidget(self.pushButton_Orient_OrientZ)

        self.pushButton_Orient_OrientVertical = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Orient_OrientVertical.setObjectName(u"pushButton_Orient_OrientVertical")

        self.verticalLayout.addWidget(self.pushButton_Orient_OrientVertical)

        self.pushButton_Orient_RotateNeg = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Orient_RotateNeg.setObjectName(u"pushButton_Orient_RotateNeg")

        self.verticalLayout.addWidget(self.pushButton_Orient_RotateNeg)

        self.pushButton_Orient_RotatePos = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Orient_RotatePos.setObjectName(u"pushButton_Orient_RotatePos")

        self.verticalLayout.addWidget(self.pushButton_Orient_RotatePos)

        self.line_5 = QFrame(self.horizontalLayoutWidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_5)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.doubleSpinBox_Orient_rotatevalue = QDoubleSpinBox(self.horizontalLayoutWidget)
        self.doubleSpinBox_Orient_rotatevalue.setObjectName(u"doubleSpinBox_Orient_rotatevalue")
        self.doubleSpinBox_Orient_rotatevalue.setMinimum(-180.000000000000000)
        self.doubleSpinBox_Orient_rotatevalue.setMaximum(180.000000000000000)

        self.gridLayout_2.addWidget(self.doubleSpinBox_Orient_rotatevalue, 0, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout_2)

        self.pushButton_Orient_RotatePos_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Orient_RotatePos_2.setObjectName(u"pushButton_Orient_RotatePos_2")

        self.verticalLayout.addWidget(self.pushButton_Orient_RotatePos_2)

        self.line_4 = QFrame(self.horizontalLayoutWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_4)

        self.pushButton_Orientvalidate = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Orientvalidate.setObjectName(u"pushButton_Orientvalidate")

        self.verticalLayout.addWidget(self.pushButton_Orientvalidate)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.tabWidget.addTab(self.tab_Orient, "")
        self.tab_Analyse = QWidget()
        self.tab_Analyse.setObjectName(u"tab_Analyse")
        self.horizontalLayoutWidget_2 = QWidget(self.tab_Analyse)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 10, 1151, 791))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_Analyse_plot = QTabWidget(self.horizontalLayoutWidget_2)
        self.tabWidget_Analyse_plot.setObjectName(u"tabWidget_Analyse_plot")
        self.tabWidget_Analyse_plot.setEnabled(True)
        self.tabWidget_Analyse_plot.setAutoFillBackground(False)
        self.tabWidget_Analyse_plot.setTabPosition(QTabWidget.South)
        self.tabWidget_Analyse_plot.setTabShape(QTabWidget.Rounded)
        self.tabWidget_Analyse_plot.setElideMode(Qt.ElideLeft)
        self.tabWidget_Analyse_plot.setUsesScrollButtons(True)
        self.tabWidget_Analyse_plot.setDocumentMode(True)
        self.tabWidget_Analyse_plot.setTabsClosable(False)
        self.tabWidget_Analyse_plot.setMovable(False)
        self.tabWidget_Analyse_plot.setTabBarAutoHide(False)

        self.horizontalLayout_2.addWidget(self.tabWidget_Analyse_plot)

        self.line_6 = QFrame(self.horizontalLayoutWidget_2)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_6)

        self.verticalLayout_A_Tools = QVBoxLayout()
        self.verticalLayout_A_Tools.setObjectName(u"verticalLayout_A_Tools")
        self.label_12 = QLabel(self.horizontalLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_A_Tools.addWidget(self.label_12)

        self.gridLayout_A_plot = QGridLayout()
        self.gridLayout_A_plot.setObjectName(u"gridLayout_A_plot")
        self.comboBox_A_plotvalue = QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox_A_plotvalue.addItem("")
        self.comboBox_A_plotvalue.addItem("")
        self.comboBox_A_plotvalue.addItem("")
        self.comboBox_A_plotvalue.addItem("")
        self.comboBox_A_plotvalue.setObjectName(u"comboBox_A_plotvalue")

        self.gridLayout_A_plot.addWidget(self.comboBox_A_plotvalue, 3, 1, 1, 1)

        self.label_14 = QLabel(self.horizontalLayoutWidget_2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_A_plot.addWidget(self.label_14, 3, 0, 1, 1)

        self.label_13 = QLabel(self.horizontalLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_A_plot.addWidget(self.label_13, 2, 0, 1, 1)

        self.spinBox_A_plottimestep = QSpinBox(self.horizontalLayoutWidget_2)
        self.spinBox_A_plottimestep.setObjectName(u"spinBox_A_plottimestep")

        self.gridLayout_A_plot.addWidget(self.spinBox_A_plottimestep, 2, 1, 1, 1)

        self.verticalLayout_A_Tools.addLayout(self.gridLayout_A_plot)

        self.pushButton_A_update_plot = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_A_update_plot.setObjectName(u"pushButton_A_update_plot")

        self.verticalLayout_A_Tools.addWidget(self.pushButton_A_update_plot)

        self.line_9 = QFrame(self.horizontalLayoutWidget_2)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_A_Tools.addWidget(self.line_9)

        self.label_6 = QLabel(self.horizontalLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_A_Tools.addWidget(self.label_6)

        self.gridLayout_A_Speciment = QGridLayout()
        self.gridLayout_A_Speciment.setObjectName(u"gridLayout_A_Speciment")
        self.label_8 = QLabel(self.horizontalLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_A_Speciment.addWidget(self.label_8, 3, 0, 1, 1)

        self.comboBox_A_methodchoice = QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox_A_methodchoice.addItem("")
        self.comboBox_A_methodchoice.addItem("")
        self.comboBox_A_methodchoice.setObjectName(u"comboBox_A_methodchoice")

        self.gridLayout_A_Speciment.addWidget(self.comboBox_A_methodchoice, 5, 1, 1, 1)

        self.label_7 = QLabel(self.horizontalLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_A_Speciment.addWidget(self.label_7, 4, 0, 1, 1)

        self.label_9 = QLabel(self.horizontalLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_A_Speciment.addWidget(self.label_9, 5, 0, 1, 1)

        self.doubleSpinBox_A_spec_width = QDoubleSpinBox(self.horizontalLayoutWidget_2)
        self.doubleSpinBox_A_spec_width.setObjectName(u"doubleSpinBox_A_spec_width")
        self.doubleSpinBox_A_spec_width.setMinimum(2.000000000000000)
        self.doubleSpinBox_A_spec_width.setMaximum(100.000000000000000)
        self.doubleSpinBox_A_spec_width.setValue(20.000000000000000)

        self.gridLayout_A_Speciment.addWidget(self.doubleSpinBox_A_spec_width, 3, 1, 1, 1)

        self.doubleSpinBox_A_spec_thickness = QDoubleSpinBox(self.horizontalLayoutWidget_2)
        self.doubleSpinBox_A_spec_thickness.setObjectName(u"doubleSpinBox_A_spec_thickness")
        self.doubleSpinBox_A_spec_thickness.setMinimum(0.010000000000000)
        self.doubleSpinBox_A_spec_thickness.setMaximum(10.000000000000000)
        self.doubleSpinBox_A_spec_thickness.setSingleStep(25.000000000000000)
        self.doubleSpinBox_A_spec_thickness.setValue(1.000000000000000)

        self.gridLayout_A_Speciment.addWidget(self.doubleSpinBox_A_spec_thickness, 4, 1, 1, 1)

        self.verticalLayout_A_Tools.addLayout(self.gridLayout_A_Speciment)

        self.line_7 = QFrame(self.horizontalLayoutWidget_2)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_A_Tools.addWidget(self.line_7)

        self.horizontalLayout_A_methods = QHBoxLayout()
        self.horizontalLayout_A_methods.setObjectName(u"horizontalLayout_A_methods")
        self.Widget_Analyse_Cut = QWidget(self.horizontalLayoutWidget_2)
        self.Widget_Analyse_Cut.setObjectName(u"Widget_Analyse_Cut")
        self.verticalLayout_3 = QVBoxLayout(self.Widget_Analyse_Cut)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.Widget_Analyse_Cut)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(170, 0))
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_5)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.offsetLabel = QLabel(self.Widget_Analyse_Cut)
        self.offsetLabel.setObjectName(u"offsetLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.offsetLabel)

        self.lineResolutionLabel = QLabel(self.Widget_Analyse_Cut)
        self.lineResolutionLabel.setObjectName(u"lineResolutionLabel")
        self.lineResolutionLabel.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lineResolutionLabel)

        self.sideResolutionLabel = QLabel(self.Widget_Analyse_Cut)
        self.sideResolutionLabel.setObjectName(u"sideResolutionLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.sideResolutionLabel)

        self.kernelSizeLabel = QLabel(self.Widget_Analyse_Cut)
        self.kernelSizeLabel.setObjectName(u"kernelSizeLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.kernelSizeLabel)

        self.DoubleSpinBox_A_C_kernel_size = QDoubleSpinBox(self.Widget_Analyse_Cut)
        self.DoubleSpinBox_A_C_kernel_size.setObjectName(u"DoubleSpinBox_A_C_kernel_size")
        self.DoubleSpinBox_A_C_kernel_size.setDecimals(3)
        self.DoubleSpinBox_A_C_kernel_size.setSingleStep(0.050000000000000)
        self.DoubleSpinBox_A_C_kernel_size.setValue(0.750000000000000)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.DoubleSpinBox_A_C_kernel_size)

        self.DoubleSpinBox_A_C_offset = QDoubleSpinBox(self.Widget_Analyse_Cut)
        self.DoubleSpinBox_A_C_offset.setObjectName(u"DoubleSpinBox_A_C_offset")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.DoubleSpinBox_A_C_offset.sizePolicy().hasHeightForWidth())
        self.DoubleSpinBox_A_C_offset.setSizePolicy(sizePolicy1)
        self.DoubleSpinBox_A_C_offset.setMinimumSize(QSize(0, 0))
        self.DoubleSpinBox_A_C_offset.setMaximum(15.000000000000000)
        self.DoubleSpinBox_A_C_offset.setSingleStep(0.250000000000000)
        self.DoubleSpinBox_A_C_offset.setValue(4.000000000000000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.DoubleSpinBox_A_C_offset)

        self.SpinBox_A_C_line_res = QSpinBox(self.Widget_Analyse_Cut)
        self.SpinBox_A_C_line_res.setObjectName(u"SpinBox_A_C_line_res")
        self.SpinBox_A_C_line_res.setEnabled(False)
        self.SpinBox_A_C_line_res.setMaximum(250)
        self.SpinBox_A_C_line_res.setSingleStep(10)
        self.SpinBox_A_C_line_res.setValue(50)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.SpinBox_A_C_line_res)

        self.SpinBox_A_C_side_res = QSpinBox(self.Widget_Analyse_Cut)
        self.SpinBox_A_C_side_res.setObjectName(u"SpinBox_A_C_side_res")
        self.SpinBox_A_C_side_res.setMaximum(250)
        self.SpinBox_A_C_side_res.setSingleStep(10)
        self.SpinBox_A_C_side_res.setValue(100)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.SpinBox_A_C_side_res)

        self.verticalLayout_3.addLayout(self.formLayout)

        self.line_10 = QFrame(self.Widget_Analyse_Cut)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_10)

        self.label_16 = QLabel(self.Widget_Analyse_Cut)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(170, 0))
        self.label_16.setFont(font1)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_16)

        self.comboBox_A_C_SL_name = QComboBox(self.Widget_Analyse_Cut)
        self.comboBox_A_C_SL_name.setObjectName(u"comboBox_A_C_SL_name")

        self.verticalLayout_3.addWidget(self.comboBox_A_C_SL_name)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_15 = QLabel(self.Widget_Analyse_Cut)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_3.addWidget(self.label_15)

        self.spinBox_A_C_SL_timesteps = QSpinBox(self.Widget_Analyse_Cut)
        self.spinBox_A_C_SL_timesteps.setObjectName(u"spinBox_A_C_SL_timesteps")

        self.horizontalLayout_3.addWidget(self.spinBox_A_C_SL_timesteps)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.comboBox_A_C_SL_which = QComboBox(self.Widget_Analyse_Cut)
        self.comboBox_A_C_SL_which.addItem("")
        self.comboBox_A_C_SL_which.addItem("")
        self.comboBox_A_C_SL_which.setObjectName(u"comboBox_A_C_SL_which")

        self.verticalLayout_3.addWidget(self.comboBox_A_C_SL_which)

        self.pushButton_A_C_strain_line_plot = QPushButton(self.Widget_Analyse_Cut)
        self.pushButton_A_C_strain_line_plot.setObjectName(u"pushButton_A_C_strain_line_plot")

        self.verticalLayout_3.addWidget(self.pushButton_A_C_strain_line_plot)

        self.line_11 = QFrame(self.Widget_Analyse_Cut)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_11)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.horizontalLayout_A_methods.addWidget(self.Widget_Analyse_Cut)

        self.line_8 = QFrame(self.horizontalLayoutWidget_2)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_A_methods.addWidget(self.line_8)

        self.Widget_Analyse_Iso = QWidget(self.horizontalLayoutWidget_2)
        self.Widget_Analyse_Iso.setObjectName(u"Widget_Analyse_Iso")
        self.verticalLayout_2 = QVBoxLayout(self.Widget_Analyse_Iso)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.Widget_Analyse_Iso)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(170, 0))
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.offsetCenterLabel = QLabel(self.Widget_Analyse_Iso)
        self.offsetCenterLabel.setObjectName(u"offsetCenterLabel")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.offsetCenterLabel)

        self.doubleSpinBox_A_ISO_Offset = QDoubleSpinBox(self.Widget_Analyse_Iso)
        self.doubleSpinBox_A_ISO_Offset.setObjectName(u"doubleSpinBox_A_ISO_Offset")
        self.doubleSpinBox_A_ISO_Offset.setMinimum(-50.000000000000000)
        self.doubleSpinBox_A_ISO_Offset.setMaximum(50.000000000000000)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.doubleSpinBox_A_ISO_Offset)

        self.lenghLabel = QLabel(self.Widget_Analyse_Iso)
        self.lenghLabel.setObjectName(u"lenghLabel")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lenghLabel)

        self.DoubleSpinBox_A_ISO_lengh = QDoubleSpinBox(self.Widget_Analyse_Iso)
        self.DoubleSpinBox_A_ISO_lengh.setObjectName(u"DoubleSpinBox_A_ISO_lengh")
        self.DoubleSpinBox_A_ISO_lengh.setValue(50.000000000000000)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.DoubleSpinBox_A_ISO_lengh)

        self.verticalLayout_2.addLayout(self.formLayout_2)

        self.line_15 = QFrame(self.Widget_Analyse_Iso)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.HLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_15)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_A_methods.addWidget(self.Widget_Analyse_Iso)

        self.verticalLayout_A_Tools.addLayout(self.horizontalLayout_A_methods)

        self.pushButton_A_compute = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_A_compute.setObjectName(u"pushButton_A_compute")

        self.verticalLayout_A_Tools.addWidget(self.pushButton_A_compute)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_A_stress_strain_pop = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_A_stress_strain_pop.setObjectName(u"pushButton_A_stress_strain_pop")

        self.horizontalLayout_6.addWidget(self.pushButton_A_stress_strain_pop)

        self.pushButton_A_strain_rate_pop = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_A_strain_rate_pop.setObjectName(u"pushButton_A_strain_rate_pop")

        self.horizontalLayout_6.addWidget(self.pushButton_A_strain_rate_pop)

        self.verticalLayout_A_Tools.addLayout(self.horizontalLayout_6)

        self.pushButton_A_validate = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_A_validate.setObjectName(u"pushButton_A_validate")
        self.pushButton_A_validate.setEnabled(False)

        self.verticalLayout_A_Tools.addWidget(self.pushButton_A_validate)

        self.horizontalLayout_2.addLayout(self.verticalLayout_A_Tools)

        self.tabWidget.addTab(self.tab_Analyse, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget_2 = QTabWidget(self.tab)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(-6, -1, 1181, 811))
        self.tab_Young = QWidget()
        self.tab_Young.setObjectName(u"tab_Young")
        self.layoutWidget = QWidget(self.tab_Young)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 1160, 761))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.mplwidget_FY_plot = MplWidget(self.layoutWidget)
        self.mplwidget_FY_plot.setObjectName(u"mplwidget_FY_plot")
        self.mplwidget_FY_plot.setMinimumSize(QSize(850, 0))
        self.mplwidget_FY_plot.setMaximumSize(QSize(850, 759))

        self.horizontalLayout_4.addWidget(self.mplwidget_FY_plot)

        self.line_13 = QFrame(self.layoutWidget)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.VLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_13)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_21 = QLabel(self.layoutWidget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font1)
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_21)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.checkBox_FY_up_strain = QCheckBox(self.layoutWidget)
        self.checkBox_FY_up_strain.setObjectName(u"checkBox_FY_up_strain")
        self.checkBox_FY_up_strain.setEnabled(True)
        self.checkBox_FY_up_strain.setMaximumSize(QSize(70, 200))

        self.gridLayout_4.addWidget(self.checkBox_FY_up_strain, 0, 2, 1, 1)

        self.label_18 = QLabel(self.layoutWidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_4.addWidget(self.label_18, 2, 0, 1, 1)

        self.label_17 = QLabel(self.layoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_4.addWidget(self.label_17, 0, 0, 1, 1)

        self.checkBox_FY_lw_strain = QCheckBox(self.layoutWidget)
        self.checkBox_FY_lw_strain.setObjectName(u"checkBox_FY_lw_strain")
        self.checkBox_FY_lw_strain.setEnabled(True)
        self.checkBox_FY_lw_strain.setMaximumSize(QSize(70, 200))

        self.gridLayout_4.addWidget(self.checkBox_FY_lw_strain, 2, 2, 1, 1)

        self.lineEdit_FY_up_strain = QLineEdit(self.layoutWidget)
        self.lineEdit_FY_up_strain.setObjectName(u"lineEdit_FY_up_strain")
        self.lineEdit_FY_up_strain.setEnabled(False)

        self.gridLayout_4.addWidget(self.lineEdit_FY_up_strain, 0, 1, 1, 1)

        self.lineEdit_FY_lw_strain = QLineEdit(self.layoutWidget)
        self.lineEdit_FY_lw_strain.setObjectName(u"lineEdit_FY_lw_strain")
        self.lineEdit_FY_lw_strain.setEnabled(False)

        self.gridLayout_4.addWidget(self.lineEdit_FY_lw_strain, 2, 1, 1, 1)

        self.verticalLayout_4.addLayout(self.gridLayout_4)

        self.label_22 = QLabel(self.layoutWidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_22)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkBox_FY_lw_stress = QCheckBox(self.layoutWidget)
        self.checkBox_FY_lw_stress.setObjectName(u"checkBox_FY_lw_stress")
        self.checkBox_FY_lw_stress.setMaximumSize(QSize(70, 200))
        self.checkBox_FY_lw_stress.setChecked(True)

        self.gridLayout_3.addWidget(self.checkBox_FY_lw_stress, 2, 2, 1, 1)

        self.checkBox_FY_up_stress = QCheckBox(self.layoutWidget)
        self.checkBox_FY_up_stress.setObjectName(u"checkBox_FY_up_stress")
        self.checkBox_FY_up_stress.setMaximumSize(QSize(70, 200))
        self.checkBox_FY_up_stress.setChecked(True)

        self.gridLayout_3.addWidget(self.checkBox_FY_up_stress, 0, 2, 1, 1)

        self.label_19 = QLabel(self.layoutWidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_3.addWidget(self.label_19, 0, 0, 1, 1)

        self.label_20 = QLabel(self.layoutWidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_3.addWidget(self.label_20, 2, 0, 1, 1)

        self.lineEdit_FY_up_stress = QLineEdit(self.layoutWidget)
        self.lineEdit_FY_up_stress.setObjectName(u"lineEdit_FY_up_stress")

        self.gridLayout_3.addWidget(self.lineEdit_FY_up_stress, 0, 1, 1, 1)

        self.lineEdit_FY_lw_stress = QLineEdit(self.layoutWidget)
        self.lineEdit_FY_lw_stress.setObjectName(u"lineEdit_FY_lw_stress")

        self.gridLayout_3.addWidget(self.lineEdit_FY_lw_stress, 2, 1, 1, 1)

        self.verticalLayout_4.addLayout(self.gridLayout_3)

        self.pushButton_FY_compute = QPushButton(self.layoutWidget)
        self.pushButton_FY_compute.setObjectName(u"pushButton_FY_compute")

        self.verticalLayout_4.addWidget(self.pushButton_FY_compute)

        self.line_12 = QFrame(self.layoutWidget)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_12)

        self.label_23 = QLabel(self.layoutWidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_23)

        self.textBrowser_FY_output = QTextBrowser(self.layoutWidget)
        self.textBrowser_FY_output.setObjectName(u"textBrowser_FY_output")

        self.verticalLayout_4.addWidget(self.textBrowser_FY_output)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.youngModLabel = QLabel(self.layoutWidget)
        self.youngModLabel.setObjectName(u"youngModLabel")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.youngModLabel)

        self.youngModLineEdit = QLineEdit(self.layoutWidget)
        self.youngModLineEdit.setObjectName(u"youngModLineEdit")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.youngModLineEdit)

        self.poissonCoefLabel = QLabel(self.layoutWidget)
        self.poissonCoefLabel.setObjectName(u"poissonCoefLabel")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.poissonCoefLabel)

        self.poissonCoefLineEdit = QLineEdit(self.layoutWidget)
        self.poissonCoefLineEdit.setObjectName(u"poissonCoefLineEdit")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.poissonCoefLineEdit)

        self.verticalLayout_4.addLayout(self.formLayout_3)

        self.pushButton_FY_overwrite = QPushButton(self.layoutWidget)
        self.pushButton_FY_overwrite.setObjectName(u"pushButton_FY_overwrite")

        self.verticalLayout_4.addWidget(self.pushButton_FY_overwrite)

        self.line_14 = QFrame(self.layoutWidget)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_14)

        self.pushButton_FY_strain_diagram = QPushButton(self.layoutWidget)
        self.pushButton_FY_strain_diagram.setObjectName(u"pushButton_FY_strain_diagram")

        self.verticalLayout_4.addWidget(self.pushButton_FY_strain_diagram)

        self.line_17 = QFrame(self.layoutWidget)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.HLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_17)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)

        self.verticalLayout_4.addWidget(self.pushButton)

        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.tabWidget_2.addTab(self.tab_Young, "")
        self.tab_Hardening = QWidget()
        self.tab_Hardening.setObjectName(u"tab_Hardening")
        self.layoutWidget1 = QWidget(self.tab_Hardening)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(3, 10, 1171, 761))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.mplwidget_FH = MplWidget(self.layoutWidget1)
        self.mplwidget_FH.setObjectName(u"mplwidget_FH")
        self.mplwidget_FH.setMinimumSize(QSize(0, 700))

        self.verticalLayout_6.addWidget(self.mplwidget_FH)

        self.line_16 = QFrame(self.layoutWidget1)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.HLine)
        self.line_16.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_16)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.pushButton_FH_plot = QPushButton(self.layoutWidget1)
        self.pushButton_FH_plot.setObjectName(u"pushButton_FH_plot")
        self.pushButton_FH_plot.setMinimumSize(QSize(100, 0))
        self.pushButton_FH_plot.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_5.addWidget(self.pushButton_FH_plot)

        self.pushButton_FH_export = QPushButton(self.layoutWidget1)
        self.pushButton_FH_export.setObjectName(u"pushButton_FH_export")
        self.pushButton_FH_export.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.pushButton_FH_export)

        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.tabWidget_2.addTab(self.tab_Hardening, "")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 23))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuconvert_to = QMenu(self.menuTools)
        self.menuconvert_to.setObjectName(u"menuconvert_to")
        self.menuhelp = QMenu(self.menubar)
        self.menuhelp.setObjectName(u"menuhelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuTools.addAction(self.menuconvert_to.menuAction())
        self.menuconvert_to.addAction(self.actionAramis_XML)
        self.menuhelp.addAction(self.actionhelp)
        self.menuhelp.addAction(self.actionLicense)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_orient.setCurrentIndex(-1)
        self.tabWidget_Analyse_plot.setCurrentIndex(-1)
        self.tabWidget_2.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionLoad.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionAramis_XML.setText(QCoreApplication.translate("MainWindow", u"Aramis_XML", None))
        self.actionhelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionLicense.setText(QCoreApplication.translate("MainWindow", u"License", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Plotting", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Timestep:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Value:", None))
        self.comboBox_Orient_Field.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.comboBox_Orient_Field.setItemText(1, QCoreApplication.translate("MainWindow", u"eps_xx", None))
        self.comboBox_Orient_Field.setItemText(2, QCoreApplication.translate("MainWindow", u"eps_yy", None))
        self.comboBox_Orient_Field.setItemText(3, QCoreApplication.translate("MainWindow", u"eps_xy", None))

        self.pushButton_Orient_UpdatePlot.setText(QCoreApplication.translate("MainWindow", u"Update Plot", None))
        self.pushButton_Orient_time_force.setText(QCoreApplication.translate("MainWindow", u"Plot time force", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Orient and rotate", None))
        self.pushButton_Orient_Center.setText(QCoreApplication.translate("MainWindow", u"Center", None))
        self.pushButton_Orient_OrientZ.setText(QCoreApplication.translate("MainWindow", u"Orient Z", None))
        self.pushButton_Orient_OrientVertical.setText(
            QCoreApplication.translate("MainWindow", u"Orient vertical", None))
        self.pushButton_Orient_RotateNeg.setText(QCoreApplication.translate("MainWindow", u"Rotate x -90", None))
        self.pushButton_Orient_RotatePos.setText(QCoreApplication.translate("MainWindow", u"Rotate x +90", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Angle", None))
        self.pushButton_Orient_RotatePos_2.setText(QCoreApplication.translate("MainWindow", u"Rotate", None))
        self.pushButton_Orientvalidate.setText(QCoreApplication.translate("MainWindow", u"Validate", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Orient),
                                  QCoreApplication.translate("MainWindow", u"Orient", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Plotting", None))
        self.comboBox_A_plotvalue.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.comboBox_A_plotvalue.setItemText(1, QCoreApplication.translate("MainWindow", u"eps_xx", None))
        self.comboBox_A_plotvalue.setItemText(2, QCoreApplication.translate("MainWindow", u"eps_yy", None))
        self.comboBox_A_plotvalue.setItemText(3, QCoreApplication.translate("MainWindow", u"eps_xy", None))

        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Value:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Timestep:", None))
        self.pushButton_A_update_plot.setText(QCoreApplication.translate("MainWindow", u"Update plot", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Initial  specimen geometry", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Width:", None))
        self.comboBox_A_methodchoice.setItemText(0, QCoreApplication.translate("MainWindow", u"ISO-DIN", None))
        self.comboBox_A_methodchoice.setItemText(1, QCoreApplication.translate("MainWindow", u"Cut Line", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Thickness:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Evaluations Method:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Cut Line Evaluation", None))
        self.offsetLabel.setText(QCoreApplication.translate("MainWindow", u"Offset:", None))
        self.lineResolutionLabel.setText(QCoreApplication.translate("MainWindow", u"Line resolution:", None))
        self.sideResolutionLabel.setText(QCoreApplication.translate("MainWindow", u"Side resolution:", None))
        self.kernelSizeLabel.setText(QCoreApplication.translate("MainWindow", u"Kernel size:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Plot strain line", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Timestep:", None))
        self.comboBox_A_C_SL_which.setItemText(0, QCoreApplication.translate("MainWindow", u"Upper", None))
        self.comboBox_A_C_SL_which.setItemText(1, QCoreApplication.translate("MainWindow", u"Lower", None))

        self.pushButton_A_C_strain_line_plot.setText(
            QCoreApplication.translate("MainWindow", u"Plot cut line strains", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ISO Evaluation", None))
        self.offsetCenterLabel.setText(QCoreApplication.translate("MainWindow", u"Offset Center", None))
        self.lenghLabel.setText(QCoreApplication.translate("MainWindow", u"Lengh:", None))
        self.pushButton_A_compute.setText(QCoreApplication.translate("MainWindow", u"Compute", None))
        self.pushButton_A_stress_strain_pop.setText(
            QCoreApplication.translate("MainWindow", u"Plot stress strain diagram", None))
        self.pushButton_A_strain_rate_pop.setText(QCoreApplication.translate("MainWindow", u"Plot strain rate", None))
        self.pushButton_A_validate.setText(QCoreApplication.translate("MainWindow", u"Validate", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Analyse),
                                  QCoreApplication.translate("MainWindow", u"Analyse", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Strain", None))
        self.checkBox_FY_up_strain.setText(QCoreApplication.translate("MainWindow", u"Active", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Lower bound", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Upper bound", None))
        self.checkBox_FY_lw_strain.setText(QCoreApplication.translate("MainWindow", u"Active", None))
        self.lineEdit_FY_up_strain.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.lineEdit_FY_lw_strain.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Stress", None))
        self.checkBox_FY_lw_stress.setText(QCoreApplication.translate("MainWindow", u"Active", None))
        self.checkBox_FY_up_stress.setText(QCoreApplication.translate("MainWindow", u"Active", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Upper bound", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Lower bound", None))
        self.lineEdit_FY_up_stress.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.lineEdit_FY_lw_stress.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_FY_compute.setText(QCoreApplication.translate("MainWindow", u"Compute", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        self.youngModLabel.setText(QCoreApplication.translate("MainWindow", u"Young mod.", None))
        self.poissonCoefLabel.setText(QCoreApplication.translate("MainWindow", u"Poisson coef.", None))
        self.pushButton_FY_overwrite.setText(QCoreApplication.translate("MainWindow", u"Overwrite", None))
        self.pushButton_FY_strain_diagram.setText(
            QCoreApplication.translate("MainWindow", u"Plot strain diagram", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Validate", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_Young),
                                    QCoreApplication.translate("MainWindow", u"Young's modulus", None))
        self.pushButton_FH_plot.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.pushButton_FH_export.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_Hardening),
                                    QCoreApplication.translate("MainWindow", u"Hardening", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                  QCoreApplication.translate("MainWindow", u"Fitting", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuconvert_to.setTitle(QCoreApplication.translate("MainWindow", u"convert_to", None))
        self.menuhelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi
