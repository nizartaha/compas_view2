from random import random

from compas_view2.app import App
from compas_view2.shapes import Arrow

viewer = App()

for x in range(5):
    for y in range(5):
        arrow = Arrow([x, y, 0], [0, 0, 1], head_portion=0.2, head_width=0.07, body_width=0.02)
        viewer.add(arrow, u=16, show_edges=False, color=(random(), random(), random()))

viewer.show()
