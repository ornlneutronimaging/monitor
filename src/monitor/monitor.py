from qtpy.QtWidgets import QMainWindow, QApplication
import sys
import os
import logging
from qtpy.QtGui import QIcon

from . import load_ui


class Monitor(QMainWindow):

	def __init__(self, parent=None):
		super(Monitor, self).__init__(parent)

		ui_full_path = os.path.join(os.path.dirname(__file__),
									os.path.join('ui',
												 'monitor.ui'))

		self.ui = load_ui(ui_full_path, baseinstance=self)


def main(args):
    app = QApplication(args)
    app.setStyle('Fusion')
    app.setApplicationDisplayName("Data Reduction Monitor")
    window = Monitor()
    window.show()
    sys.exit(app.exec_())
