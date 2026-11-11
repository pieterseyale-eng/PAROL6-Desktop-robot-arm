"""Cut a local connector exit from the previously deepened Elbow STL.

Coordinate dimensions are in mm in the original STL's coordinate system.
"""
from pathlib import Path

import numpy as np
import trimesh

HERE = Path(__file__).resolve().parent
source = HERE / "Elbow_part_motor_cavity_deeper30mm.STL"
output = HERE / "Elbow_part_motor_cavity_deeper30mm_connector_relief_left_28_25.STL"

# Motor mounting plane: Z≈83.7. The user requested the near edge of the
# window 28 mm from that plane, and a 25 mm axial opening toward lower Z.
# On the Bambu Studio screenshot, the circled side is the -X wall.
# Extend through the complete wall (its inner boundary is near X=16).
mounting_face_z = 83.7
near_edge_z = mounting_face_z - 28.0
far_edge_z = near_edge_z - 25.0
cut_min = np.array([-1.0, -1.0, far_edge_z])
cut_max = np.array([16.6, 30.0, near_edge_z])

mesh = trimesh.load(source, force="mesh")
tool = trimesh.creation.box(extents=cut_max-cut_min)
tool.apply_translation((cut_min+cut_max)/2)
result = trimesh.boolean.difference([mesh, tool], engine="manifold")

assert result.is_watertight
assert len(result.split(only_watertight=True)) == 1
assert np.allclose(result.bounds, mesh.bounds, atol=0.01)
assert result.volume < mesh.volume

result.export(output)
print(f"source_volume={mesh.volume:.2f} mm3")
print(f"result_volume={result.volume:.2f} mm3")
print(f"removed={mesh.volume-result.volume:.2f} mm3")
print(f"bounds={result.bounds.round(2).tolist()}")
print(f"watertight={result.is_watertight}; components={len(result.split(only_watertight=True))}")
