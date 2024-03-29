#  Copyright (c) 2023. Chair of Forming and Machining Processes, TU Dresden
#   FlowCurveExtender, analysing tensile test beyond necking point
#   This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU Affero General Public License as
#       published by the Free Software Foundation, either version 3 of the
#       License, or (at your option) any later version.
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU Affero General Public License for more details.
#       You should have received a copy of the GNU Affero General Public License
#       along with this program.  If not, see <https://www.gnu.org/licenses/>.

import numpy as np

from FlowCurveExtender.core.test_results import ISOAnalysisResult


def traditional_stress_from_tensile(tensile_test, offset=0, lenght=50,
                                    initial_width=20, initial_thickness=1, **kwargs):
    """
    get the traditional stress/strain curve from a tensile test
    :param args: path to the aramis export or (time, force, coords, strain)
    :param initial_thickness: initial thickness of the sheet
    :param initial_width: initial width of the probe
    :return: dataframe with stress, force, time, strains as series with A, Ag and Rm as
    """
    time = tensile_test.dic_results.time
    force = tensile_test.dic_results.force
    coords = tensile_test.dic_results.coords
    strain = tensile_test.dic_results.strains

    av_y = np.average(coords[0, :, 1]) + offset
    y_coords = coords[0, :, 1]
    loc_coords = np.logical_and(y_coords <= av_y + lenght / 2, y_coords >= av_y - lenght / 2)
    y_min = np.min(coords[:, loc_coords, 1], axis=1)
    y_max = np.max(coords[:, loc_coords, 1], axis=1)

    eps_xx = np.average(strain[:, loc_coords, 0], axis=1)
    eps_yy = np.average(strain[:, loc_coords, 1], axis=1)
    eps_xy = np.average(strain[:, loc_coords, 2], axis=1)

    eps_zz = -(eps_xx + eps_yy)
    thickness = initial_thickness * np.exp(eps_zz)
    width = initial_width * np.exp(eps_yy)
    stress = force / (thickness * width)
    strain = np.stack([eps_xx, eps_yy, eps_xy])
    print(strain.shape)

    return ISOAnalysisResult(test_parent=tensile_test, stress=stress,
                             strain=strain, bound=(y_min, y_max), time=time)
