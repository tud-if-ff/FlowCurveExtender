import os
from functools import wraps

import matplotlib.patches as mpatches
import numpy as np
from DIC_Exchange.convert_to import load_from
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from FlowCurveExtender.core.tensile_test_series import TensileTestSeries
from FlowCurveExtender.gui.mplwidget import MplWidget
from FlowCurveExtender.gui.popup_widget import PopupWidget
from FlowCurveExtender.gui.ui_mainwindow import Ui_MainWindow


def status_setter(message):
    def decorate(method):
        @wraps(method)
        def _impl(self, *method_args, **method_kwargs):
            self.set_status_msg(message, update=True)
            method_output = method(self, *method_args, **method_kwargs)
            self.set_status_msg("Ready", update=False)
            return method_output

        return _impl

    return decorate


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.setupUi(self)
        self.show()

        self.TestSeries = None
        self.mpl_widget_orient = None
        self.mpl_widget_analyse = None

        # %%% Connection
        # %% Toolbar
        self.actionLoad.triggered.connect(self.load_files)
        self.actionconvert_xml_to_hdf5.triggered.connect(self.convert_xml_to_hdf5)

        # %% Orient Tab
        self.pushButton_Orient_UpdatePlot.clicked.connect(self.update_orient_plot)
        self.pushButton_Orient_RotatePos.clicked.connect(self.rotate_p90)
        self.pushButton_Orient_RotateNeg.clicked.connect(self.rotate_n90)
        self.pushButton_Orient_OrientVertical.clicked.connect(self.orient_vertical)
        self.pushButton_Orient_OrientZ.clicked.connect(self.orient_z)
        self.pushButton_Orient_RotatePos_2.clicked.connect(self.rotate_theta)
        self.pushButton_Orientvalidate.clicked.connect(self.validate_orient)
        self.pushButton_Orient_time_force.clicked.connect(self.pop_up_force_time_plot)

        # %% Analyse Tab
        self.activate_methods()
        self.comboBox_A_methodchoice.currentIndexChanged.connect(self.activate_methods)
        self.pushButton_A_compute.clicked.connect(self.analyse)
        self.pushButton_A_update_plot.clicked.connect(self.update_analyse_plot)
        self.pushButton_A_stress_strain_pop.clicked.connect(self.pop_up_stress_strain_plot)
        self.pushButton_A_strain_rate_pop.clicked.connect(self.pop_up_stress_strain_rate)
        self.pushButton_A_C_strain_line_plot.clicked.connect(self.pop_up_strain_line_plot)
        self.comboBox_A_C_SL_name.currentIndexChanged.connect(self.combo_timesteps_adapt)

        # %% Fitting Tab
        validator = QDoubleValidator()
        validator.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.lineEdit_FY_lw_strain.setValidator(validator)
        self.lineEdit_FY_lw_stress.setValidator(validator)
        self.lineEdit_FY_up_strain.setValidator(validator)
        self.lineEdit_FY_up_stress.setValidator(validator)
        self.poissonCoefLineEdit.setValidator(validator)
        self.youngModLineEdit.setValidator(validator)

        self.pushButton_FY_compute.clicked.connect(self.compute_elastics)
        self.checkBox_FY_lw_stress.stateChanged.connect(self.enable_box_bound_young)
        self.checkBox_FY_up_stress.stateChanged.connect(self.enable_box_bound_young)
        self.checkBox_FY_up_strain.stateChanged.connect(self.enable_box_bound_young)
        self.checkBox_FY_lw_strain.stateChanged.connect(self.enable_box_bound_young)

        self.pushButton_FH_plot.clicked.connect(self.plot_plastics)
        self.pushButton_FY_strain_diagram.clicked.connect(self.plot_strain_diagram)

        # %%% Status bar
        self.Qstatus_label = QLabel(parent=self.statusbar)
        self.Qstatus_label.setMinimumSize(QSize(100, 0))
        self.statusbar.addWidget(self.Qstatus_label)

        # %%% Prepare Popup
        self.pop_up = MplWidget(parent=None)

        # %%% Set Activation Status
        self.set_status_msg("Ready")

    def set_status_msg(self, status, update=True):
        self.Qstatus_label.setText(status)
        if update:
            self.Qstatus_label.repaint()
            self.statusbar.repaint()

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%     Action for toolbar
    @status_setter(message="Loading Files...")
    def load_files(self, paths=None):
        if paths is None:
            paths = QFileDialog.getOpenFileNames(self, "Open Image", "~", "DIC Exchange Files (*.hf5, *.hdf5)")[0]

        if len(paths) != 0:
            self.TestSeries = TensileTestSeries.load_from_paths(paths)
            self.spinBox_Orient_timestep.setMinimum(-1 * self.TestSeries.get_timestep_safe_index())
            self.spinBox_Orient_timestep.setMaximum(self.TestSeries.get_timestep_safe_index())
            self.spinBox_A_plottimestep.setMinimum(-1 * self.TestSeries.get_timestep_safe_index())
            self.spinBox_A_plottimestep.setMaximum(self.TestSeries.get_timestep_safe_index())
            self.update_orient_plot()

    @status_setter(message="Loading Files...")
    def convert_xml_to_hdf5(self):

        path = QFileDialog.getOpenFileName(self, "Open Image", "~", "Aramis XML File (*.xml)")[0]

        if len(path) ==0:
            return

        path_dir = os.path.dirname(path)

        dic_res = load_from(os.path.join(path_dir, path), force_rupture_ratio=.8)
        dic_res.save_to_hdf5(os.path.join(path_dir, path[:-4] + ".hdf5"))
        print("saved " + str(os.path.join(path_dir, path[:-4] + ".hdf5")))

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%      Action for Orient
    def update_orient_plot(self):
        keyword = self.comboBox_Orient_Field.currentText()
        timestep = self.spinBox_Orient_timestep.value()
        if self.mpl_widget_orient is None:
            self.mpl_widget_orient = []
        if len(self.mpl_widget_orient) != len(self.TestSeries.tensile_tests):
            names = self.TestSeries.get_names()
            for i in range(len(self.mpl_widget_orient), len(self.TestSeries.tensile_tests)):
                self.mpl_widget_orient.append(MplWidget())
                self.tabWidget_orient.addTab(self.mpl_widget_orient[-1], names[i])

        [a_mpl_wdiget.plot_clear() for a_mpl_wdiget in self.mpl_widget_orient]
        self.TestSeries.get_plot_all([a_mpl_wdiget.get_ax() for a_mpl_wdiget in self.mpl_widget_orient],
                                     keyword=keyword, timestep=timestep)
        [a_mpl_wdiget.get_ax().set_aspect("equal") for a_mpl_wdiget in self.mpl_widget_orient]
        [a_mpl_wdiget.get_ax().set_xlabel("X axis") for a_mpl_wdiget in self.mpl_widget_orient]
        [a_mpl_wdiget.get_ax().set_ylabel("Y axis") for a_mpl_wdiget in self.mpl_widget_orient]
        [a_mpl_wdiget.draw() for a_mpl_wdiget in self.mpl_widget_orient]

    @status_setter(message="Orienting...")
    def orient_vertical(self):
        self.TestSeries.orient_vertical_all()
        self.update_orient_plot()

    @status_setter(message="Orienting...")
    def orient_z(self):
        self.TestSeries.orient_z_all()
        self.update_orient_plot()

    @status_setter(message="Rotating...")
    def rotate_p90(self):
        self.TestSeries.rotate_all_90(pos=True)
        self.update_orient_plot()

    @status_setter(message="Rotating...")
    def rotate_n90(self):
        self.TestSeries.rotate_all_90(pos=False)
        self.update_orient_plot()

    @status_setter(message="Rotating...")
    def rotate_theta(self):
        theta = self.doubleSpinBox_Orient_rotatevalue.value()
        self.TestSeries.rotate_all_theta(theta)
        self.update_orient_plot()

    def validate_orient(self):
        self.actionLoad.setDisabled(True)
        self.tab_Orient.setDisabled(True)
        self.tabWidget.setCurrentIndex(1)

        self.comboBox_A_C_SL_name.insertItems(0, self.TestSeries.get_names())

    def pop_up_force_time_plot(self):
        self.pop_up = MplWidget(parent=None)
        self.pop_up.plot_clear()
        self.TestSeries.get_plot_force_time(self.pop_up.get_ax())
        self.pop_up.setVisible(True)

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%     Action for Analyse

    def combo_timesteps_adapt(self):
        name = self.comboBox_A_C_SL_name.currentText()
        len_ts = len(self.TestSeries.tensile_tests[self.TestSeries.get_names().index(name)].dic_results.time)
        self.spinBox_A_C_SL_timesteps.setMinimum(-1 * len_ts)
        self.spinBox_A_C_SL_timesteps.setMaximum(len_ts)

    def activate_methods(self):
        val_combo = self.comboBox_A_methodchoice.currentText()
        if val_combo == "Cut Line":
            self.Widget_Analyse_Cut.setDisabled(False)
            self.Widget_Analyse_Iso.setDisabled(True)
        elif val_combo == "ISO-DIN":
            self.Widget_Analyse_Cut.setDisabled(True)
            self.Widget_Analyse_Iso.setDisabled(False)

    @status_setter(message="Analyzing...")
    def analyse(self):
        if self.Widget_Analyse_Cut.isEnabled():
            args = {
                "method": "cut_line",
                "offset_line": float(self.DoubleSpinBox_A_C_offset.value()),
                "res_side": int(self.SpinBox_A_C_side_res.value()),
                "res_cut_line": int(self.SpinBox_A_C_line_res.value()),
                "kernel_size": float(self.DoubleSpinBox_A_C_kernel_size.value()),
                "initial_width": float(self.doubleSpinBox_A_spec_width.value()),
                "initial_thickness": float(self.doubleSpinBox_A_spec_thickness.value())}
        else:
            args = {
                "method": "ISO",
                "offset": float(self.doubleSpinBox_A_ISO_Offset.value()),
                "lenght": float(self.DoubleSpinBox_A_ISO_lengh.value()),
                "initial_width": float(self.doubleSpinBox_A_spec_width.value()),
                "initial_thickness": float(self.doubleSpinBox_A_spec_thickness.value())
            }

        self.TestSeries.analyse(args)

    @status_setter(message="Plotting...")
    def update_analyse_plot(self):
        if not self.TestSeries.analysed:
            keyword = self.comboBox_A_plotvalue.currentText()
            timestep = self.spinBox_A_plottimestep.value()
            if self.mpl_widget_analyse is None:
                self.mpl_widget_analyse = []
            if len(self.mpl_widget_analyse) != len(self.TestSeries.tensile_tests):
                names = self.TestSeries.get_names()
                for i in range(len(self.mpl_widget_analyse), len(self.TestSeries.tensile_tests)):
                    self.mpl_widget_analyse.append(MplWidget())
                    self.tabWidget_Analyse_plot.addTab(self.mpl_widget_analyse[-1], names[i])

            [a_mpl_wdiget.plot_clear() for a_mpl_wdiget in self.mpl_widget_analyse]
            self.TestSeries.get_plot_all([a_mpl_wdiget.get_ax() for a_mpl_wdiget in self.mpl_widget_analyse],
                                         keyword=keyword, timestep=timestep)
            [a_mpl_wdiget.get_ax().set_aspect("equal") for a_mpl_wdiget in self.mpl_widget_analyse]
            [a_mpl_wdiget.get_ax().set_xlabel("X axis") for a_mpl_wdiget in self.mpl_widget_analyse]
            [a_mpl_wdiget.get_ax().set_ylabel("Y axis") for a_mpl_wdiget in self.mpl_widget_analyse]
            [a_mpl_wdiget.draw() for a_mpl_wdiget in self.mpl_widget_analyse]
        else:
            keyword = self.comboBox_A_plotvalue.currentText()
            timestep = self.spinBox_A_plottimestep.value()
            if self.mpl_widget_analyse is None:
                self.mpl_widget_analyse = []
            if len(self.mpl_widget_analyse) != len(self.TestSeries.tensile_tests):
                names = self.TestSeries.get_names()
                for i in range(len(self.mpl_widget_analyse), len(self.TestSeries.tensile_tests)):
                    self.mpl_widget_analyse.append(MplWidget())
                    self.tabWidget_Analyse_plot.addTab(self.mpl_widget_analyse[-1], names[i])

            [a_mpl_wdiget.plot_clear() for a_mpl_wdiget in self.mpl_widget_analyse]
            self.TestSeries.get_plot_results([a_mpl_wdiget.get_ax() for a_mpl_wdiget in self.mpl_widget_analyse],
                                             keyword=keyword, timestep=timestep)
            [a_mpl_wdiget.get_ax().set_aspect("equal") for a_mpl_wdiget in self.mpl_widget_analyse]
            [a_mpl_wdiget.get_ax().set_xlabel("X axis") for a_mpl_wdiget in self.mpl_widget_analyse]
            [a_mpl_wdiget.get_ax().set_ylabel("Y axis") for a_mpl_wdiget in self.mpl_widget_analyse]
            [a_mpl_wdiget.draw() for a_mpl_wdiget in self.mpl_widget_analyse]

    def pop_up_stress_strain_rate(self):
        self.pop_up = PopupWidget(self.TestSeries,"stress_strain_rate",parent=None)
        self.pop_up.setVisible(True)

    def pop_up_stress_strain_plot(self):
        self.pop_up = PopupWidget( self.TestSeries,"stress_strain", parent=None )
        self.pop_up.setVisible(True)

    def pop_up_strain_line_plot(self):
        timestep = int(self.spinBox_A_C_SL_timesteps.value())
        name = self.comboBox_A_C_SL_name.currentText()
        which = self.comboBox_A_C_SL_which.currentText()
        self.pop_up = MplWidget(parent=None)
        self.pop_up.plot_clear()
        self.TestSeries.plot_strain_lines(self.pop_up.get_ax(), timestep=timestep, name=name, which=which)
        self.pop_up.setVisible(True)

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%     Action for Fitting

    def enable_box_bound_young(self):
        self.lineEdit_FY_lw_strain.setEnabled(self.checkBox_FY_lw_strain.isChecked())
        self.lineEdit_FY_lw_stress.setEnabled(self.checkBox_FY_lw_stress.isChecked())
        self.lineEdit_FY_up_strain.setEnabled(self.checkBox_FY_up_strain.isChecked())
        self.lineEdit_FY_up_stress.setEnabled(self.checkBox_FY_up_stress.isChecked())

    def compute_elastics(self):

        if self.checkBox_FY_lw_strain.isChecked():
            bounds_lw_strain = float(self.lineEdit_FY_lw_strain.text())
        else:
            bounds_lw_strain = -np.inf

        if self.checkBox_FY_lw_stress.isChecked():
            bounds_lw_stress = float(self.lineEdit_FY_lw_stress.text())
        else:
            bounds_lw_stress = -np.inf

        if self.checkBox_FY_up_strain.isChecked():
            bounds_up_strain = float(self.lineEdit_FY_up_strain.text())
        else:
            bounds_up_strain = np.inf

        if self.checkBox_FY_up_stress.isChecked():
            bounds_up_stress = float(self.lineEdit_FY_up_stress.text())
        else:
            bounds_up_stress = np.inf

        self.TestSeries.fit_elastics(upper_stress=bounds_up_stress,
                                     lower_stress=bounds_lw_stress,
                                     upper_strain=bounds_up_strain,
                                     lower_strain=bounds_lw_strain)

        self.textBrowser_FY_output.setText(self.TestSeries.get_str_fit_elastics())
        self.plot_elastics()
        self.youngModLineEdit.setText("{:.0f}".format(self.TestSeries.elastics["E"]))
        self.poissonCoefLineEdit.setText("{:.4f}".format(self.TestSeries.elastics["v"]))

    def elastics_overwrite(self):
        self.TestSeries.elastics["E"] = self.youngModLineEdit.text()
        self.TestSeries.elastics["v"] = self.poissonCoefLineEdit.text()

    def plot_elastics(self):
        self.mplwidget_FY_plot.plot_clear()
        self.TestSeries.plot_elastic_fit(self.mplwidget_FY_plot.get_ax())

        if self.checkBox_FY_lw_strain.isChecked():
            u_lw_strain = float(self.lineEdit_FY_lw_strain.text())
            b_lw_strain = True
        else:
            u_lw_strain = self.mplwidget_FY_plot.get_ax().get_xlim()[0]
            b_lw_strain = False

        if self.checkBox_FY_lw_stress.isChecked():
            u_lw_stress = float(self.lineEdit_FY_lw_stress.text())
            b_lw_stress = True
        else:
            u_lw_stress = self.mplwidget_FY_plot.get_ax().get_ylim()[0]
            b_lw_stress = False

        if self.checkBox_FY_up_strain.isChecked():
            u_up_strain = float(self.lineEdit_FY_up_strain.text())
            b_up_strain = True
        else:
            u_up_strain = self.mplwidget_FY_plot.get_ax().get_xlim()[1]
            b_up_strain = False

        if self.checkBox_FY_up_stress.isChecked():
            u_up_stress = float(self.lineEdit_FY_up_stress.text())
            b_up_stress = True
        else:
            u_up_stress = self.mplwidget_FY_plot.get_ax().get_ylim()[1]
            b_up_stress = False

        if b_lw_strain or b_up_strain:
            delta = abs((u_up_strain - u_lw_strain) * 0.15)
            if b_lw_strain:
                b_lw_strain = u_lw_strain
                u_lw_strain = u_lw_strain - delta
            else:
                b_lw_strain = u_lw_strain
            if b_up_strain:
                b_up_strain = u_up_strain
                u_up_strain = u_up_strain + delta
            else:
                b_up_strain = u_up_strain
        else:
            b_up_strain = u_up_strain
            b_lw_strain = u_lw_strain

        if b_lw_stress or b_up_stress:
            delta = abs((u_up_stress - u_lw_stress) * 0.15)
            if b_lw_stress:
                b_lw_stress = u_lw_stress
                u_lw_stress = u_lw_stress - delta
            else:
                b_lw_stress = u_lw_stress
            if b_up_stress:
                b_up_stress = u_up_stress
                u_up_stress = u_up_stress + delta
            else:
                b_up_stress = u_up_stress
        else:
            b_up_stress = u_up_stress
            b_lw_stress = u_lw_stress

        points = np.array([[b_lw_strain, b_lw_stress],
                           [b_up_strain, b_lw_stress],
                           [b_up_strain, b_up_stress],
                           [b_lw_strain, b_up_stress],
                           [b_lw_strain, b_lw_stress]])

        self.mplwidget_FY_plot.get_ax().add_patch(mpatches.Polygon(points,
                                                                   facecolor="k",
                                                                   edgecolor="k",
                                                                   alpha=0.1))

        self.mplwidget_FY_plot.draw()

    def plot_strain_diagram(self):
        self.pop_up = MplWidget(parent=None)
        self.pop_up.plot_clear()
        self.pop_up.plot_clear()
        self.TestSeries.plot_strain_diagram(self.pop_up.get_ax())
        self.pop_up.get_ax().grid()
        self.pop_up.draw()
        self.pop_up.setVisible(True)

    def plot_plastics(self):
        self.mplwidget_FH.plot_clear()
        self.TestSeries.compute_plastics()
        self.TestSeries.plot_plastic(self.mplwidget_FH.get_ax())
        self.mplwidget_FH.get_ax().grid()
        self.mplwidget_FH.draw()
