import matplotlib
from PySide6 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib.figure import Figure

# Ensure using PyQt5 backend
matplotlib.use('QT5Agg')


# Matplotlib canvas class to create figure
class MplCanvas(Canvas):
    def __init__(self):
        self.fig = Figure()
        self.fig.set_tight_layout(True)
        self.ax = self.fig.add_subplot(111)
        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)

    def plot_clear(self):
        self.fig.clear()
        self.ax = self.fig.add_subplot(111)
        self.draw()

    def plot_data(self, data):
        for a_key in list(data.keys()):
            self.ax.plot(data[a_key][0], data[a_key][1], label=a_key)
        self.ax.legend()
        self.draw()


# Matplotlib widget
class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)  # Inherit from QWidget
        self.canvas = MplCanvas()  # Create canvas object
        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        self.vbl = QtWidgets.QVBoxLayout()  # Set box for plotting
        self.vbl.addWidget(self.toolbar)
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)

    def get_ax(self):
        return self.canvas.ax

    def draw(self):
        self.canvas.draw()

    def plot_clear(self):
        self.canvas.plot_clear()
