from mind_mapper.models.node import Node
from mind_mapper.models.annotation import Annotation
from mind_mapper.models.text import Text


class Controller(object):

    NODE_IDS = 0

    def __init__(self, view_manager):
        self.view_manager = view_manager
        self.node_shape = 0
        self.node_size = 100
        self.node_padding = 0
        self.node_background = "#cc0000"
        self.nodes = []

    def create_node(self, x, y):
        node = Node(x=x, y=y, background=self.node_background,
                    shape=self.node_shape, size=self.node_size,
                    padding=self.node_padding, id=self.NODE_IDS, text=Text(),
                    annotation=Annotation())
        self.nodes.append(node)
        self.NODE_IDS += 1
        self.view_manager.create_node(node)

    def node_text_changed(self, id, text):
        self.nodes[id].text = Text(text=text, size=self.text_size,
                                   color=self.text_color, font=self.text_font)
        self.view_manager.node_text_changed(id, text)

    def node_annot_changed(self, id, text):
        self.nodes[id].annotation = Annotation(text=text)
        self.view_manager.node_annot_changed(id, text)

    def position_changed(self, id, x, y):
        self.nodes[id].x = x
        self.nodes[id].y = y
        self.view_manager.node_annot_changed(id, x, y)
