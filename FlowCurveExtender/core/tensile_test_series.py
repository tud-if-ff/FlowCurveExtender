import os

import numpy as np

from FlowCurveExtender.core import tensile_test
from DIC_Exchange.HDF5Exchange import DIC_Result
import matplotlib
import matplotlib.pyplot as plt


class TensileTestSeries:

    def __init__(self, the_tensile_tests:list[tensile_test.TensileTest]):
        self.tensile_tests = the_tensile_tests
        self.analysed = False
        self.elastics = {"E":0.0, "v":0.0}

    def __len__(self):
        return len(self.tensile_tests)

    @classmethod
    def load_from_paths(cls, paths:list[str]):

        tensile_test_list = []
        for a_path in paths:
            dic_results = DIC_Result.load_from_hdf5(a_path)
            tensile_test_list.append(tensile_test.TensileTest(dic_results, name=os.path.basename(a_path)))

        return cls(tensile_test_list)

    def get_names(self):
        return [self.tensile_tests[i].name for i in range(len(self.tensile_tests))]

    def rotate_all_90(self, pos=True):
        for i in range((len(self.tensile_tests))):
            self.tensile_tests[i].rot_90(pos)

    def rotate_all_theta(self, theta):
        for i in range((len(self.tensile_tests))):
            self.tensile_tests[i].rot_z(theta)

    def orient_z_all(self, timestep=0):
        for i in range((len(self.tensile_tests))):
            self.tensile_tests[i].orient_z(timestep=0)

    def orient_vertical_all(self, timestep=0):
        for i in range((len(self.tensile_tests))):
            self.tensile_tests[i].orient_vertical(timestep=0)

    def orient_vertical_one(self, index, timestep=0):
        self.tensile_tests[index].orient_vertical(timestep=0)

    def get_plot_results(self, axes:list[plt.Axes], keyword=None, timestep=0):
        if isinstance(axes, list):
            if len(axes) != len(self.tensile_tests):
                raise TypeError("Incorrect list size")
            plots = []
            for i in range(len(axes)):
                plots.append(self.tensile_tests[i].analysis.plot(axes[i], keyword=keyword, timestep=timestep))
        return plots

    def get_plot_all(self, axes:list[plt.Axes], keyword=None, timestep=0):
        if isinstance(axes, list):
            if len(axes) != len(self.tensile_tests):
                raise TypeError("Incorrect list size")
            plots = []
            for i in range(len(axes)):
                plots.append(self.tensile_tests[i].plot_on_ax(axes[i], keyword=keyword, timestep=timestep))
        return plots

    def get_timestep_number(self, name=None, index=None):
        timesteps = [len(self.tensile_tests[i].dic_results.time) for i in range(len(self.tensile_tests))]
        if name is None and index is None:
            return timesteps
        elif index is None:
            index = self.get_names().index(name)
            return timesteps[index]
        else:
            return timesteps[index]

    def get_timestep_safe_index(self):
        lens = [len(self.tensile_tests[i].dic_results.time) for i in range(len(self.tensile_tests))]
        return np.min(lens)

    def analyse(self, args):
        for i in range((len(self.tensile_tests))):
            print("Analysing test " + self.get_names()[i] + " ...")
            self.tensile_tests[i].analyse(args)

        print("Done Analysing")
        self.analysed = True

    def get_plot_force_time(self, axes):
        for i in range(len(self.tensile_tests)):
            time = self.tensile_tests[i].dic_results.time
            force = self.tensile_tests[i].dic_results.force
            axes.plot(time, force, label=self.get_names()[i])
            axes.set_xlabel("Time")
            axes.set_ylabel("Force")
        axes.legend()

    def get_plot_stress_strain_alt(self, axes):
        for i in range(len(self.tensile_tests)):
            stress = self.tensile_tests[i].analysis.stress
            strain = self.tensile_tests[i].analysis.strain[0, :]
            axes.plot(strain, stress, label=self.get_names()[i])
            axes.set_xlabel(r"Strain ($\varepsilon_{yy}$)")
            axes.set_ylabel(r"Stress ($\sigma_{yy}$)")
        axes.legend()

    def get_plot_stress_strain(self, axes):
        for i in range(len(self.tensile_tests)):
            time_rate = np.diff(self.tensile_tests[i].dic_results.time)
            strain_rate = np.diff(self.tensile_tests[i].analysis.strain[0, :])
            strain = self.tensile_tests[i].analysis.strain[0, :]
            axes.plot(strain[1:], np.nan_to_num(strain_rate/time_rate), label=self.get_names()[i])
            axes.set_xlabel(r"Strain ($\varepsilon_{yy}$)")
            axes.set_ylabel(r"Stress ($\sigma_{yy}$)")
        axes.legend()

    def plot_strain_lines(self, axes, name, timestep=-1, which="Upper"):
        i = self.get_names().index(name)
        self.tensile_tests[i].analysis.plot_strain_line(axes, which, timestep)

    def fit_elastics(self, lower_stress=-np.inf, upper_stress=np.inf, lower_strain=-np.inf, upper_strain=np.inf):
        for i in range(len(self.tensile_tests)):
            self.tensile_tests[i].analysis.fit_elastics(lower_stress, upper_stress, lower_strain, upper_strain)

        E_mod = np.average([self.tensile_tests[i].analysis.young_mod for i in range(len(self.tensile_tests))])
        p_coe = np.average([self.tensile_tests[i].analysis.poisson for i in range(len(self.tensile_tests))])
        self.elastics = {"E":E_mod, "v":p_coe}

    def get_str_fit_elastics(self):
        buff = ""
        for i in range(len(self.tensile_tests)):
            buff += self.tensile_tests[i].analysis.get_elast_reg_string_result()
        return buff

    def plot_elastic_fit(self, axes):
        for i in range(len(self.tensile_tests)):
            stress = self.tensile_tests[i].analysis.stress
            strain = self.tensile_tests[i].analysis.strain[1, :]
            axes.plot(strain, stress, label=self.get_names()[i])

        axes.set_xlabel(r"Strain ($\varepsilon_{yy}$)")
        axes.set_ylabel(r"Stress ($\sigma_{yy}$)")
        axes.legend()


    def compute_plastics(self):
        for i in range(len(self.tensile_tests)):
            self.tensile_tests[i].analysis.compute_plastic(self.elastics)

    def plot_plastic(self, axes):
        for i in range(len(self.tensile_tests)):
            stress = self.tensile_tests[i].analysis.stress_pl
            strain = self.tensile_tests[i].analysis.strain_pl[1, :]
            axes.plot(strain, stress, label=self.get_names()[i])

        axes.set_xlabel(r"Strain ($\varepsilon_{yy}$)")
        axes.set_ylabel(r"Stress ($\sigma_{yy}$)")
        axes.legend()

