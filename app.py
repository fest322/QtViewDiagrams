import sys
from PyQt5.QtWidgets import QApplication
from view.scene import Scene

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Scene()
    sys.exit(app.exec_())