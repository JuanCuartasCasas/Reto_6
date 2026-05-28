from typing import List
import math
# from Space.Line import Line 
# from Space.Point import Point
 

class InvalidShapeError(Exception):
    pass


class Shape:
    
    def __init__(self, vertices: List):
        self._vertices: List = vertices
        self._initialize_attributes()

    def _initialize_attributes(self):
        if len(self._vertices) < 3:
            self._edges: List = []
            self.inner_angles: List = []
            self.__is_regular: bool = False
        else:
            self._edges: List = self.set_edges()
            self.inner_angles: List = self.compute_inner_angles(self._vertices)
            self.__is_regular: bool = self.set_is_regular()

    def get_is_regular(self):
        return self.__is_regular
    
    def get_vertices(self):
        return self._vertices
    
    def set_edges(self):
        list_edges = []
        if not self._vertices:
            return list_edges
        try:
            for i in range(len(self._vertices)):
                edge = Line(self._vertices[i], self._vertices[(i + 1) % len(self._vertices)])
                list_edges.append(edge)
        except Exception as e:
            raise InvalidShapeError("Error construyendo aristas a partir de los vértices") from e
        return list_edges

    def set_vertices(self, new_vertices: List[Point]):
        try:
            self._vertices = new_vertices
            self._initialize_attributes()
        except InvalidShapeError:
            raise
        except Exception as e:
            raise InvalidShapeError("Vertices inválidos proporcionados") from e
        finally:
            self._edges = []
    
    
    def set_is_regular(self):
        if len(self._vertices) < 3:
            self.__is_regular = False
            return self.__is_regular

        try:
            side_lengths = [edge.length for edge in self._edges]
            first_length = side_lengths[0]
            sides_equal = all(abs(length - first_length) < 1e-9 for length in side_lengths)

            angles = self.inner_angles
            first_angle = angles[0]
            angles_equal = all(abs(angle - first_angle) < 1e-9 for angle in angles)

            self.__is_regular = sides_equal and angles_equal
            return self.__is_regular
        except Exception:
            self.__is_regular = False
            return self.__is_regular

    def compute_area(self):

        raise NotImplementedError("Debe implementarse un método 'compute_area()' a cáda subclase específica")

    def compute_perimeter(self):
        raise NotImplementedError("Debe implementarse un método 'compute_perimeter()' a cáda subclase específica")

    def compute_inner_angles(self, vertices):
        n = len(vertices)
        angles = []

        if n < 3:
            return angles

        for i in range(n):
            try:
                p_prev = vertices[(i - 1) % n]
                p = vertices[i]
                p_next = vertices[(i + 1) % n]

                ux = p_prev._x - p._x
                uy = p_prev._y - p._y
                vx = p_next._x - p._x
                vy = p_next._y - p._y

                dot = ux * vx + uy * vy

                norm_u = math.hypot(ux, uy)
                norm_v = math.hypot(vx, vy)
                if norm_u == 0 or norm_v == 0:
                    angles.append(0.0)
                    continue

                cos_theta = dot / (norm_u * norm_v)
                cos_theta = max(-1.0, min(1.0, cos_theta))
                angles.append(math.degrees(math.acos(cos_theta)))
            except Exception:
                angles.append(0.0)
                continue

        return angles
       


