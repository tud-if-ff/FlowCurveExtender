import numpy as np
from scipy.interpolate import interp1d
from FlowCurveExtender.core.test_results import CutLineAnalysisResult
import shapely as shp


def search_striction(dic_result, initial_width=20, res_line=100):
    x = dic_result.coords[-1, :, 0]
    left_side = x <= x.min() + initial_width/4
    right_side = x >= x.max() - initial_width/4
    all = np.ones_like(x, dtype=bool)
    avg_x_l = np.average(x[left_side])
    avg_x_r = np.average(x[right_side])
    y_middle = []

    for a_loc in [left_side, right_side, all]:
        y = dic_result.coords[-1, a_loc, 1]
        e_yy = dic_result.strains[-1, a_loc, 1]
        y_min, y_max = np.min(dic_result.coords[-1, :, 1]), np.max(dic_result.coords[-1, :, 1])
        y_iter = np.linspace(y_min, y_max, num=100, endpoint=True)
        s_w = 0.75
        norm_r = (np.outer(np.ones_like(y), y_iter) - np.outer(y, np.ones_like(y_iter))) ** 2
        W_line_r = 1 / (s_w * np.sqrt(2 * np.pi)) * np.exp(-norm_r / (2 * s_w ** 2))
        e_yy_iter = np.einsum("ij, i -> j", W_line_r, e_yy) / np.sum(W_line_r, axis=0)
        y_middle.append(y_iter[np.argmax(e_yy_iter)])

    dx = avg_x_l - avg_x_r
    dy = y_middle[0] - y_middle[1]
    m = dy / dx

    item = 0
    len_item = -1
    for i in range(len(dic_result.mesh_holes)):
        if len(dic_result.mesh_holes[i]) > len_item:
            item = i
            len_item = len(dic_result.mesh_holes[i])

    mesh_outside_boundary = dic_result.mesh_holes[item]
    mesh_outside_boundary = np.array(mesh_outside_boundary)[:, 0]
    x_bound = dic_result.coords[-1, mesh_outside_boundary][:, [0, 1]]
    shape = shp.Polygon(x_bound)

    x_strict = np.array((x.min(), x.max()))
    y_strict = y_middle[-1] + m * x_strict
    line = shp.LineString(np.array((x_strict, y_strict)).T)
    line = line.intersection(shape)
    x_strict = np.linspace(line.coords[0][0], line.coords[-1][0], endpoint=True, num=res_line)
    y_strict = np.linspace(line.coords[0][1], line.coords[-1][1], endpoint=True, num=res_line)

    x = dic_result.coords[:, :, 0]
    y = dic_result.coords[:, :, 1]

    y_strict_all = [y_strict, ]
    x_strict_all = [x_strict, ]

    duy = np.diff(dic_result.coords[:, :, 1], axis=0)
    dux = np.diff(dic_result.coords[:, :, 0], axis=0)

    for i in range(len(duy) - 1, -1, -1):
        y_cut_prec = y_strict_all[-1]
        x_cut_prec = x_strict_all[-1]
        norm_r = (np.outer(np.ones_like(x[i]), x_cut_prec) - np.outer(x[i], np.ones_like(x_cut_prec))) ** 2 + \
                 (np.outer(np.ones_like(y[i]), y_cut_prec) - np.outer(y[i], np.ones_like(y_cut_prec))) ** 2
        W_line_r = 1 / (s_w * np.sqrt(2 * np.pi)) * np.exp(-norm_r / (2 * s_w ** 2))
        y_cut_actual = y_cut_prec - np.einsum("ij, i -> j", W_line_r, duy[i]) / np.sum(W_line_r, axis=0)
        x_cut_actual = x_cut_prec - np.einsum("ij, i -> j", W_line_r, dux[i]) / np.sum(W_line_r, axis=0)
        y_strict_all.append(y_cut_actual)
        x_strict_all.append(x_cut_actual)

    y_strict_all = np.array(y_strict_all[::-1])
    x_strict_all = np.array(x_strict_all[::-1])

    return x_strict_all, y_strict_all


def get_cut_lines(dic_results, offset=4, res_side=20, res_line=50, initial_width=20):
    """
    Find the parameter the cut line coordinates
    :param coords: the coordinate of the points cloud
    :param loc_right: mask for the right side
    :param loc_left: mask for the left side
    :param offset: offset for the cut line
    :param res_side: number point on the side (edges) lines
    :param res_line: resolution of the cut line
    :param initial_width: initial width of the probe
    :return: cut lines coordinates for every time step
    """


    return True, True


def tensile_evaluate_cut_line(tensile_test, offset_line=4, res_side=50, res_cut_line=50, kernel_size=0.75,
                              initial_width=20, initial_thickness=1, **kwargs):
    """
    :param args: path to the aramis export or (time, force, coords, strain)
    :param offset_line: offset for the cut line
    :param res_side: number point on the side (edges) lines
    :param res_cut_line: resolution of the cut line
    :return: stress, strain from the experiment
    """

    time = tensile_test.dic_results.time
    force = tensile_test.dic_results.force
    strain = tensile_test.dic_results.strains
    coords = tensile_test.dic_results.coords.swapaxes(-1, 0).swapaxes(-1, 1)
    simplices = tensile_test.dic_results.mesh

    x_strict, y_strict = search_striction(tensile_test.dic_results, initial_width=20, res_line=res_cut_line)

    eps_yy_list_up = []
    eps_yy_list_dw = []

    eps_xx_list_up = []
    eps_xx_list_dw = []

    eps_xy_list_up = []
    eps_xy_list_dw = []

    stress_up = []
    stress_dw = []
    s_w = kernel_size

    for i in range(len(time)):
        eps_yy = strain[i, :, 1]
        eps_xx = strain[i, :, 0]
        eps_xy = strain[i, :, 2]

        x_t = coords[0, i]
        y_t = coords[1, i]

        x_up = x_strict[i]
        y_up = y_strict[i] + offset_line

        norm = (np.einsum('i,j->ij', x_t, np.ones_like(x_up)) - x_up)**2 +\
               (np.einsum('i,j->ij', y_t, np.ones_like(y_up)) - y_up)**2
        W_line_up = 1/(s_w*np.sqrt(2*np.pi)) * np.exp(-norm/(2*s_w**2))
        eps_yy_up = np.einsum("ij, i -> j", W_line_up, eps_yy) / np.sum(W_line_up, axis=0)
        eps_xx_up = np.einsum("ij, i -> j", W_line_up, eps_xx) / np.sum(W_line_up, axis=0)
        eps_xy_up = np.einsum("ij, i -> j", W_line_up, eps_xy) / np.sum(W_line_up, axis=0)

        len_line_up = np.sqrt((x_up.max() - x_up.min())**2)
        thickness_up = initial_thickness*np.exp(np.average(-(eps_yy_up+eps_xx_up)))

        eps_yy_list_up.append(eps_yy_up)
        eps_xx_list_up.append(eps_xx_up)
        eps_xy_list_up.append(eps_xy_up)

        stress_up.append(force[i]/(len_line_up*thickness_up))

        x_dw = x_strict[i]
        y_dw = y_strict[i] - offset_line

        norm = (np.einsum('i,j->ij', x_t, np.ones_like(x_dw)) - x_dw)**2 \
               + (np.einsum('i,j->ij', y_t, np.ones_like(y_dw)) - y_dw)**2
        W_line_dw = 1/(s_w*np.sqrt(2*np.pi)) * np.exp(-norm/(2*s_w**2))

        eps_yy_dw = np.einsum("ij, i -> j", W_line_dw, eps_yy) / np.sum(W_line_dw, axis=0)
        eps_xx_dw = np.einsum("ij, i -> j", W_line_dw, eps_xx) / np.sum(W_line_dw, axis=0)
        eps_xy_dw = np.einsum("ij, i -> j", W_line_dw, eps_xy) / np.sum(W_line_dw, axis=0)

        thickness_dw = initial_thickness*np.exp(np.average(-(eps_yy_dw + eps_xx_dw)))
        len_line_dw = np.sqrt((x_dw.max() - x_dw.min())**2)

        eps_yy_list_dw.append(eps_yy_dw)
        eps_xx_list_dw.append(eps_xx_dw)
        eps_xy_list_dw.append(eps_xy_dw)

        stress_dw.append(force[i]/(np.average(len_line_dw*thickness_dw)))

    stress = (np.array(stress_dw) + np.array(stress_up))/2

    strain = np.stack([np.stack([eps_xx_list_up, eps_yy_list_up, eps_xy_list_up]),
                       np.stack([eps_xx_list_dw, eps_yy_list_dw, eps_xy_list_dw])])

    coords_line_up = np.stack((x_strict, y_strict - offset_line)).swapaxes(0, 1).swapaxes(1, -1)
    coords_line_down = np.stack((x_strict, y_strict - offset_line)).swapaxes(0, 1).swapaxes(1, -1)

    return CutLineAnalysisResult(test_parent=tensile_test,time=time, stress=stress, strain_cut_line=strain,
                                 cutlines=np.stack([coords_line_up, coords_line_down]))
