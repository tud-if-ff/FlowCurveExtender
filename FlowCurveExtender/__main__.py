import sys

from PySide6.QtWidgets import QApplication

from FlowCurveExtender.gui.mainwindow import MainWindow


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
