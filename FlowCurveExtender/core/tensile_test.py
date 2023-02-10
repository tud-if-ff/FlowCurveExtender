from abc import ABC

import matplotlib.pyplot as plt
import numpy as np
from DIC_Exchange import HDF5Exchange

from FlowCurveExtender.core.cut_line_simplified_analysis import tensile_evaluate_cut_line
from FlowCurveExtender.core.iso_analysis import traditional_stress_from_tensile


class TensileTest(ABC):
    def __init__(self, dic_results, name=""):
        assert isinstance(dic_results, HDF5Exchange.DIC_Result)

        self.dic_results = dic_results
        self.name = name
        self.analysed = False
        self.analysis = None

    def center(self, timestep=0):
        center = np.average(self.dic_results.coords[timestep, :], axis=0)
        self.dic_results.translate(-center)

    def rot_90(self, pos=True):
        if pos:
            mat_rot = np.array([[0, -1, 0],
                                [1, 0, 0],
                                [0, 0, 1]])
        else:
            mat_rot = np.array([[0, 1, 0],
                                [-1, 0, 0],
                                [0, 0, 1]])

        self.dic_results.rotate(mat_rot)

    def rot_z(self, theta):
        theta *= 2 * np.pi / 360
        mat_rot = np.array([[np.cos(theta), -np.sin(theta), 0],
                            [np.sin(theta), np.cos(theta), 0],
                            [0, 0, 1]])

        self.dic_results.rotate(mat_rot)

    def orient_z(self, timestep=0):
        center = np.average(self.dic_results.coords[timestep, :], axis=0)
        points = self.dic_results.coords[timestep]
        points -= center
        u, d, vh = np.linalg.svd(points.T @ points)
        e_z = u[:, -1]
        e_z = e_z / np.linalg.norm(e_z)
        e_y = np.cross(e_z, [0, 1, 0])
        e_x = np.cross(e_z, e_y)
        mat_rot = np.stack((e_x, e_y, e_z))
        self.dic_results.rotate(mat_rot)

    def orient_vertical(self, timestep=0):
        points_xy = self.dic_results.coords[timestep, :, [0, 1]]
        cov = np.cov(points_xy)
        eig_val, eig_vect = np.linalg.eig(cov)
        eig_vect = eig_vect[np.argsort(eig_val)]
        e_y = np.array([eig_vect[0, 1], eig_vect[1, 1], 0])
        e_z = np.array([0, 0, 1])
        e_x = np.cross(e_y, e_z)
        mat_rot = np.stack((e_x, e_y, e_z))
        self.dic_results.rotate(mat_rot)

    def plot_on_ax(self, ax, keyword=None, timestep=0, kwargs=None):
        if timestep >= len(self.dic_results.time):
            timestep = -1
        elif timestep <= -len(self.dic_results.time):
            timestep = 0
        plot = None
        if kwargs is None:
            kwargs = {}
        if keyword is None or keyword == "None":
            plot = ax.triplot(self.dic_results.coords[timestep, :, 0], self.dic_results.coords[timestep, :, 1],
                              triangles=self.dic_results.mesh)
        elif keyword == "eps_xx":
            plot = ax.tripcolor(self.dic_results.coords[timestep, :, 0], self.dic_results.coords[timestep, :, 1],
                                self.dic_results.strains[timestep, :, 0],
                                triangles=self.dic_results.mesh)
            c_bar = plt.colorbar(plot, ax=ax)
            c_bar.set_label(r"$\varepsilon_{xx}$")
        elif keyword == "eps_yy":
            plot = ax.tripcolor(self.dic_results.coords[timestep, :, 0], self.dic_results.coords[timestep, :, 1],
                                self.dic_results.strains[timestep, :, 1],
                                triangles=self.dic_results.mesh)
            c_bar = plt.colorbar(plot, ax=ax)
            c_bar.set_label(r"$\varepsilon_{yy}$")
        elif keyword == "eps_xy":
            plot = ax.tripcolor(self.dic_results.coords[timestep, :, 0], self.dic_results.coords[timestep, :, 1],
                                self.dic_results.strains[timestep, :, 2],
                                triangles=self.dic_results.mesh)
            c_bar = plt.colorbar(plot, ax=ax)
            c_bar.set_label(r"$\varepsilon_{xy}$")
        return plot

    def analyse(self, args: dict):
        if args["method"] == "cut_line":
            self.analysis = tensile_evaluate_cut_line(self, **args)
        elif args["method"] == "ISO":
            self.analysis = traditional_stress_from_tensile(self, **args)

        self.analysed = True
