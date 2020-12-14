from items.item import DiagramItem

class Rectangle(DiagramItem):
    def __init__(self, diagramType, contextMenu, parent=None, scene=None):
        super(DiagramItem, self).__init__(parent, scene)