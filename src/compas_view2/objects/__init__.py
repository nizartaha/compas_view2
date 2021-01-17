from compas.datastructures import Network
from compas.datastructures import Mesh
from compas.geometry import Box
from compas.geometry import Sphere
from compas.geometry import Torus

from .viewobject import ViewObject

from .viewnetwork import ViewNetwork
from .viewmesh import ViewMesh
from .viewbox import ViewBox
from .viewsphere import ViewSphere
from .viewtorus import ViewTorus

ViewObject.register(Network, ViewNetwork)
ViewObject.register(Mesh, ViewMesh)
ViewObject.register(Box, ViewBox)
ViewObject.register(Sphere, ViewSphere)
ViewObject.register(Torus, ViewTorus)
