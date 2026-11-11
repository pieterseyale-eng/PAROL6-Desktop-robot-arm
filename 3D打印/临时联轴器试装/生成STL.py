"""Generate the fit-check STL from the parameters mirrored in the SCAD source."""
from pathlib import Path
import math
import numpy as np
import trimesh

HERE = Path(__file__).resolve().parent
FLANGE_D, FLANGE_H = 32.0, 3.0
HUB_D, HUB_H = 16.0, 10.0
BORE_D, MOUNT_D, PILOT_D = 8.2, 4.2, 3.3
PCD, SET_SCREW_Z = 24.0, 8.0

def cylinder(diameter, height, center):
    mesh = trimesh.creation.cylinder(radius=diameter / 2, height=height, sections=128)
    mesh.apply_translation(center)
    return mesh

flange = cylinder(FLANGE_D, FLANGE_H, (0, 0, FLANGE_H / 2))
hub = cylinder(HUB_D, HUB_H, (0, 0, FLANGE_H + HUB_H / 2))
solid = trimesh.boolean.union([flange, hub], engine="manifold")

cuts = [cylinder(BORE_D, FLANGE_H + HUB_H + 2, (0, 0, (FLANGE_H + HUB_H) / 2))]
for angle in (0, 90, 180, 270):
    rad = math.radians(angle)
    cuts.append(cylinder(MOUNT_D, FLANGE_H + 2,
                         (PCD / 2 * math.cos(rad), PCD / 2 * math.sin(rad), FLANGE_H / 2)))
for angle in (0, 90):
    cut = cylinder(PILOT_D, HUB_D / 2 + 1, (0, 0, 0))
    cut.apply_transform(trimesh.transformations.rotation_matrix(math.pi / 2, [0, 1, 0]))
    cut.apply_transform(trimesh.transformations.rotation_matrix(math.radians(angle), [0, 0, 1]))
    cut.apply_translation(((HUB_D / 4 + 0.5) * math.cos(math.radians(angle)),
                           (HUB_D / 4 + 0.5) * math.sin(math.radians(angle)), SET_SCREW_Z))
    cuts.append(cut)

mesh = trimesh.boolean.difference([solid, *cuts], engine="manifold")
mesh.export(HERE / "8mm法兰联轴器_试装.stl")
print(f"watertight={mesh.is_watertight}, bounds={np.round(mesh.bounds, 3).tolist()}, volume={mesh.volume:.1f} mm3")
