"""Close two unused cable holes and open a motor connector notch in J5 v2.

All dimensions use the STL's own millimetre coordinates. The script always
starts from the 30 mm extended v2 model, never from a previously edited copy.
"""
from pathlib import Path

import numpy as np
import trimesh

HERE = Path(__file__).resolve().parent
source = HERE / "J5_part_J6_plus30mm_v2.STL"
output = HERE / "J5_part_J6_plus30mm_v3_closed_holes_connector20.STL"
original = trimesh.load(source, force="mesh")

# The two visible round holes are through the +Y outer wall. At Y=70 their
# measured boundaries are about X=120.8..133.2 and X=138.8..151.2,
# Z=2.8..15.3. Fill them with overlapping cylinders, flush with outer Y.
hole_centers_x = (127.0, 145.0)
hole_center_z = 9.05
plug_radius = 6.4   # observed opening radius ~6.2 mm; 0.2 mm weld overlap
wall_inner_y = 64.0
wall_outer_y = float(original.bounds[1, 1])
plug_min_y = wall_inner_y - 0.1
plug_length = wall_outer_y - plug_min_y
plugs = []
for x in hole_centers_x:
    plug = trimesh.creation.cylinder(radius=plug_radius, height=plug_length, sections=128)
    plug.apply_transform(trimesh.transformations.rotation_matrix(np.pi/2, [1, 0, 0]))
    plug.apply_translation([x, (plug_min_y + wall_outer_y)/2, hole_center_z])
    plugs.append(plug)
closed = trimesh.boolean.union([original, *plugs], engine="manifold")

# Motor axis in the original STL is X=134.5, Y=42.918. The 42 mm motor spans
# X=113.5..155.5, so the requested 20 mm notch is X=124.5..144.5.
# The motor's underside mounting plane is Z=58.1. Its requested notch floor
# is 25 mm away toward the exposed motor back: Z=33.1. Open to the Z=0 edge.
motor_center_x = 134.5
notch_width_x = 20.0
mounting_plane_z = 58.1
notch_floor_z = mounting_plane_z - 25.0
cut_min = np.array([motor_center_x - notch_width_x/2, wall_inner_y - 0.5, -1.0])
cut_max = np.array([motor_center_x + notch_width_x/2, wall_outer_y + 1.0, notch_floor_z])
tool = trimesh.creation.box(extents=cut_max-cut_min)
tool.apply_translation((cut_min+cut_max)/2)
result = trimesh.boolean.difference([closed, tool], engine="manifold")

assert result.is_watertight and result.is_winding_consistent
assert len(result.split(only_watertight=True)) == 1
assert np.allclose(result.bounds, original.bounds, atol=0.01)
result.export(output)
print(f"source_volume={original.volume:.2f} mm3")
print(f"filled_volume={closed.volume:.2f} mm3")
print(f"result_volume={result.volume:.2f} mm3")
print(f"notch={cut_min.round(2).tolist()} to {cut_max.round(2).tolist()}")
print(f"bounds={result.bounds.round(2).tolist()}")
