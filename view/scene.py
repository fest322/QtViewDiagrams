import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem,
                             QGridLayout, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QGraphicsTextItem)
from items.item import DiagramItem

class Scene(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.view.show()

    def item_insert(self, item: DiagramItem):
        ...

    def text_inserted(self, item: QGraphicsTextItem):
        ...

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Scene()
    sys.exit(app.exec_())
