from proj_generic import GenericProjection
import math

class SinusoidalProjection(GenericProjection):
	
	def __init__(self):
		self.projection_type = self.ProjectionType.PseudoCylindric

	def get_coords(self, x, y):
		return 70 * x * math.cos(y), 2 * math.degrees(y)

