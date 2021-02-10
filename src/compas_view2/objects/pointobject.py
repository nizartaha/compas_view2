import ctypes as ct
from OpenGL import GL
from compas.utilities import flatten

from ..buffers import make_index_buffer, make_vertex_buffer

from .object import Object
from ..forms import PointEditForm


class PointObject(Object):
    """Object for displaying COMPAS point geometry."""

    default_color = [0.1, 0.1, 0.1]

    def __init__(self, data, name=None, is_selected=False, color=None, size=10):
        super().__init__(data, name=name, is_selected=is_selected)
        self._points = None
        self.color = color
        self.size = size

    @property
    def points(self):
        return self._points

    def init(self):
        positions = [self._data]
        colors = [self.color or self.default_color]
        elements = [0]
        self._points = {
            'positions': make_vertex_buffer(list(flatten(positions)), True),
            'colors': make_vertex_buffer(list(flatten(colors))),
            'elements': make_index_buffer(elements),
            'n': 1
        }

    def edit(self, on_update=None):
        self.editform = PointEditForm(self, on_update=on_update)
        self.editform.show()

    def update(self):
        data = list(self._data)
        n = len(data)
        size = n * ct.sizeof(ct.c_float)
        data = (ct.c_float * n)(* data)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self._points['positions'])
        GL.glBufferSubData(GL.GL_ARRAY_BUFFER, 0, size, data)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, 0)

    def draw(self, shader):
        shader.enable_attribute('position')
        shader.enable_attribute('color')
        shader.uniform1i('is_selected', self.is_selected)
        shader.bind_attribute('position', self.points['positions'])
        shader.bind_attribute('color', self.points['colors'])
        shader.draw_points(size=self.size, elements=self.points['elements'], n=self.points['n'])
        shader.uniform1i('is_selected', 0)
        shader.disable_attribute('position')
        shader.disable_attribute('color')

    def draw_instance(self, shader):
        shader.enable_attribute('position')
        shader.enable_attribute('color')
        shader.uniform1i('is_instance_mask', 1)
        shader.uniform3f('instance_color', self.instance_color)
        shader.bind_attribute('position', self.points['positions'])
        shader.draw_points(size=self.size, elements=self.points['elements'], n=self.points['n'])
        shader.uniform1i('is_instance_mask', 0)
        shader.uniform3f('instance_color', [0, 0, 0])
        shader.disable_attribute('position')
        shader.disable_attribute('color')
