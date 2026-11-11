"""Open two connector reliefs in wrist.STL, measured in the original STL coordinates (mm)."""

from pathlib import Path
import hashlib
import shutil

import trimesh


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "STL （三维打印模型）" / "WRIST （腕部）" / "wrist.STL"
OUTPUT = SOURCE.with_name("wrist_C_B_connector_relief_25x25.STL")
PRINT_DIR = ROOT / "3D打印" / "分锅STL" / "锅07_腕部急停盒与J2"
PRINT_OLD = PRINT_DIR / "wrist.STL"
BACKUP = ROOT / "3D打印" / "备份" / "wrist_原版.STL"

mesh = trimesh.load_mesh(SOURCE)
if not mesh.is_watertight:
    raise RuntimeError("Original wrist STL is not watertight")

# The open end is at minimum Z. The square cavity is centered near X=30.05,
# Y=29.10; C is the +Y wall and B is the +X wall in the open-end view.
x_center = 30.05
y_center = 29.10
z_open = float(mesh.bounds[0, 2])
slot_width = 25.0
slot_depth = 25.0
z_bottom = z_open - 2.0
z_top = z_open + slot_depth

# Cutters extend slightly beyond both sides of each wall so no membrane remains.
c_cut = trimesh.creation.box(extents=(slot_width, 15.0, z_top - z_bottom))
c_cut.apply_translation((x_center, 54.0, (z_bottom + z_top) / 2.0))
b_cut = trimesh.creation.box(extents=(15.0, slot_width, z_top - z_bottom))
b_cut.apply_translation((56.0, y_center, (z_bottom + z_top) / 2.0))

result = trimesh.boolean.difference([mesh, c_cut, b_cut], engine="manifold")
if result is None or not result.is_watertight or result.volume >= mesh.volume:
    raise RuntimeError("Boolean cut failed validation")

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
result.export(OUTPUT)
PRINT_DIR.mkdir(parents=True, exist_ok=True)
BACKUP.parent.mkdir(parents=True, exist_ok=True)
if PRINT_OLD.exists():
    if hashlib.sha256(PRINT_OLD.read_bytes()).digest() != hashlib.sha256(SOURCE.read_bytes()).digest():
        raise RuntimeError("Printing copy differs from original; refusing to replace it")
    shutil.move(PRINT_OLD, BACKUP)
shutil.copy2(OUTPUT, PRINT_DIR / OUTPUT.name)
print(f"source_volume={mesh.volume:.3f} mm^3")
print(f"result_volume={result.volume:.3f} mm^3")
print(f"result_watertight={result.is_watertight}, faces={len(result.faces)}")
print(f"output={OUTPUT}")
print(f"print={PRINT_DIR / OUTPUT.name}")
