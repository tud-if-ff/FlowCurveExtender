from abc import ABC

import numpy as np
from scipy import stats
from scipy.stats import t


class AnalysisResult(ABC):
    def __init__(self, test_parent, stress: np.ndarray, time: np.ndarray, strain: np.ndarray):
        self.stress_el = None
        self.strain_el = None
        self.stress_pl = None
        self.poisson = None
        self.poisson_reg = None
        self.young_conf = None
        self.young_inter = None
        self.young_mod = None
        self.young_reg = None
        self.poisson_inter = None
        self.poisson_conf = None
        self.strain_pl = None
        self.stress = stress
        self.strain = strain
        self.time = time
        self.test_parent = test_parent
        self.elastic_mask = np.ones_like(stress, dtype=bool)

    def export(self):
        pass

    def plot(self, ax, keyword=None, timestep=-1):
        raise NotImplementedError

    def fit_elastics(self, lower_stress=-np.inf, upper_stress=np.inf, lower_strain=-np.inf, upper_strain=np.inf):
        loc_stress = np.logical_and(self.stress <= upper_stress, self.stress >= lower_stress)
        loc_strain = np.logical_and(self.strain[1] <= upper_strain, self.strain[1] >= lower_strain)

        loc = np.logical_and(loc_stress, loc_strain)
        self.strain_el = self.strain[:, loc]
        self.stress_el = self.stress[loc]

        self.young_reg = stats.linregress(self.strain[1, loc], self.stress[loc])
        self.young_mod = self.young_reg.slope
        self.young_inter = self.young_reg.intercept
        tinv = lambda p, df: abs(t.ppf(p / 2, df))
        self.young_conf = tinv(0.05, len(self.stress[loc]) - 2) * self.young_reg.stderr

        self.poisson_reg = stats.linregress(self.strain[1, loc], self.strain[0, loc])
        self.poisson = -self.poisson_reg.slope
        self.poisson_inter = self.poisson_reg.intercept
        self.poisson_conf = tinv(0.05, len(self.stress[loc]) - 2) * self.poisson_reg.stderr

    def get_elast_reg_string_result(self):
        buff = self.test_parent.name + "\n"

        buff += "fitted young modulus: {mod:.0f} ±{conf:.0f} (±{confp:.3f}%)\n".format(
            mod=self.young_mod, conf=self.young_conf, confp=self.young_conf / self.young_mod)

        buff += "regression quality: R²={R_sq:.4f}\n".format(
            R_sq=self.young_reg.rvalue ** 2)

        buff += "fitted poisson coeff: {mod:.3f} ±{conf:5f} (±{confp:.3f}%)\n".format(
            mod=self.poisson, conf=self.poisson_conf, confp=self.poisson_conf / self.poisson)

        buff += "regression quality: R²={R_sq:.4f}\n".format(
            R_sq=self.poisson_reg.rvalue ** 2)
        return buff

    def compute_plastic(self, elastics):
        E_mod = elastics["E"]
        pcoe = elastics["v"]
        self.strain_pl = self.strain - np.stack([self.stress * pcoe / E_mod, self.stress / E_mod, self.stress * 0])
        max_strain = np.argmax(self.stress)
        min_strain = np.max(np.where(self.strain_pl[1] <= 0)) + 1
        self.strain_pl = self.strain_pl[:, min_strain:max_strain]
        self.stress_pl = self.stress[min_strain:max_strain]


class CutLineAnalysisResult(AnalysisResult):

    def __init__(self, test_parent, time: np.ndarray, stress: np.ndarray, strain_cut_line: np.ndarray,
                 cutlines: np.ndarray):

        strain = np.stack([np.average(strain_cut_line[:, 0, :, :], axis=(0, 2)),
                           np.average(strain_cut_line[:, 1, :, :], axis=(0, 2)),
                           np.average(strain_cut_line[:, 2, :, :], axis=(0, 2))])

        super().__init__(test_parent=test_parent, stress=stress, time=time, strain=strain)
        self.cutlines = cutlines
        self.strain_cut_line = strain_cut_line

    def plot(self, ax, keyword=None, timestep=-1):
        plot = self.test_parent.plot_on_ax(ax, keyword, timestep)

        x_up = self.cutlines[0, timestep, :, 0]
        y_up = self.cutlines[0, timestep, :, 1]
        x_dw = self.cutlines[1, timestep, :, 0]
        y_dw = self.cutlines[1, timestep, :, 1]

        ax.plot(x_up, y_up, "-m")
        ax.plot(x_dw, y_dw, "-m")

        return plot

    def plot_strain_line(self, ax, which="Upper", timestep=-1):
        if which == "Upper":
            which_line = 0
        else:
            which_line = 1

        print(self.strain_cut_line.shape)

        ax.plot(self.cutlines[which_line, timestep, :, 0], self.strain_cut_line[which_line, 0, timestep, :],
                label="eps_xx")
        ax.plot(self.cutlines[which_line, timestep, :, 0], self.strain_cut_line[which_line, 1, timestep, :],
                label="eps_yy")
        ax.plot(self.cutlines[which_line, timestep, :, 0], self.strain_cut_line[which_line, 2, timestep, :],
                label="eps_xy")

        ax.set_xlabel("X coordinate")
        ax.set_ylabel("Strain")

        ax.legend()


class ISOAnalysisResult(AnalysisResult):
    def __init__(self, test_parent, time: np.ndarray, stress: np.ndarray, strain: np.ndarray, bound):
        super().__init__(test_parent=test_parent, stress=stress, time=time, strain=strain)

        self.bound = bound

    def plot(self, ax, keyword=None, timestep=-1):
        plot = self.test_parent.plot_on_ax(ax, keyword, timestep)
        ax.plot([-15, 15], [self.bound[0][timestep], self.bound[0][timestep]], "-r")
        ax.plot([-15, 15], [self.bound[1][timestep], self.bound[1][timestep]], "-r")

        return plot
