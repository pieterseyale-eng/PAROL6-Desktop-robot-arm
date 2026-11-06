# J5_part 为 J6 电机组件加长 30 mm：修改记录

记录日期：2026-11-06

## 修改目的与范围

J6 更换为新的电机、减速器和控制板组合后，电机尾部预计比原设计向外突出约 23 mm。因此先给 J5_part 增加 30 mm 轴向空间，留下约 7 mm 的名义余量。这个余量只是按目前提供的突出量估算，尚未经过实物装配验证。

本次仅修改 `J5_part.STL` 的长度。原版文件保留。**用于打印的加长版为 `J5_part_J6_plus30mm_v2.STL`。**曾生成过一版会错误延长下方竖板的模型，已删除；不要从旧的打印队列或切片工程中使用它。各文件位置见文末。

## 几何定义

坐标采用原 STL 自带坐标系，单位为 mm。X 方向是零件由左侧圆环通向右侧 J6 安装端的长度方向。根据用户对下方竖板的要求，在 **X = 82 mm** 处切开。这个截面仅有上方横板，Z 范围为 **58.1～74.0 mm**；在此插入 **30 mm** 长的等截面实体。

修改后的几何映射：

| 原零件位置 | 新零件位置 | 处理 |
| --- | --- | --- |
| X < 82 mm | 原位 | 左侧圆环和其余前段不动 |
| X = 82 mm 截面 | X = 82～112 mm | 只延长上方横板；中间新增区域没有下方竖板 |
| X > 82 mm | 原 X + 30 mm | 右侧 J6 安装端、两块下方竖板、孔位整体后移，形状不拉长 |

左右段分别封口后，与插入段做实体布尔合并，输出单一封闭网格。插入段并非独立打印件；STL 是完整的一件式零件。X = 82 mm 处的横板截面面积约 **906.300 mm²**。新模型在 X = 90、100、110 mm 的截面最低 Z 均为 58.1 mm，确认竖板没有被加长；到 X = 114 mm，右侧竖板重新出现。

## 修改前后数据

| 指标 | 原版 `J5_part.STL` | 修正版 `J5_part_J6_plus30mm_v2.STL` |
| --- | ---: | ---: |
| X 长度 | 133.800 mm | 163.800 mm |
| Y 宽度 | 71.418 mm | 71.418 mm |
| Z 高度 | 74.000 mm | 74.000 mm |
| 网格体积 | 134127.495 mm³ | 161316.486 mm³ |
| 体积增加 | — | 27188.990 mm³（约 20.3%） |
| 三角面数 | 131560 | 131582 |
| 是否封闭 / 法向一致 | 是 / 是 | 是 / 是 |
| 文件大小 | 6578084 字节 | 6579184 字节 |

两个文件的 X 最小值均约为 0.000 mm；X 最大值分别为 133.800 mm 和 163.800 mm。体积增加量与截面面积乘 30 mm 相符。新零件包围盒为 **163.8 × 71.418 × 74 mm**，尺寸上可以放入拓竹 P1S 的 256 × 256 × 256 mm 打印空间；实际朝向、支撑和打印强度仍需在 Bambu Studio 中确认。

文件 SHA-256：

```text
J5_part.STL                 a533ed726836d6d5a468bed34e515ce0f14014f1c67af8c522bf8f64b4989ef9
J5_part_J6_plus30mm_v2.STL  be6481b2a5029ff4e15a1fc8174e97d77601c97636aeb3b0fd573676f9977224
```

## 复现或再次改长度

在仓库根目录安装 Python 依赖：

```powershell
python -m pip install trimesh shapely mapbox_earcut manifold3d
```

下面的脚本从**原版**开始生成，改 `cut_x` 或 `extra_mm` 即可尝试其他版本。不要在已经加长的 STL 上重复执行，否则会再次增加长度。输出文件名应随参数修改，避免覆盖现有版本。

```python
from pathlib import Path
import trimesh

folder = Path("STL （三维打印模型）/FOREARM （前臂）")
source = folder / "J5_part.STL"
target = folder / "J5_part_J6_plus30mm_v2.STL"
cut_x = 82.0
extra_mm = 30.0

original = trimesh.load(source, force="mesh")
left = trimesh.intersections.slice_mesh_plane(
    original, [-1, 0, 0], [cut_x, 0, 0], cap=True
)
right = trimesh.intersections.slice_mesh_plane(
    original, [1, 0, 0], [cut_x, 0, 0], cap=True
)
right.apply_translation([extra_mm, 0, 0])

section = original.section(
    plane_origin=[cut_x, 0, 0], plane_normal=[1, 0, 0]
)
profile, transform = section.to_2D()
assert len(profile.polygons_full) == 1, "截面轮廓已变化，请检查切割位置"
bridge = trimesh.creation.extrude_polygon(
    profile.polygons_full[0], height=extra_mm, engine="earcut"
)
bridge.apply_transform(transform)

result = trimesh.boolean.union([left, bridge, right], engine="manifold")
assert result.is_watertight and result.is_winding_consistent
assert abs(result.extents[0] - (original.extents[0] + extra_mm)) < 0.01
result.export(target)
```

## 后续装配检查

1. 用实物测 J6 电机、减速器、控制板及接线插头在该方向的总外形，确认 30 mm 加长量和装配余量。
2. 在 CAD 或 Bambu Studio 中检查 J5_part 与相邻盖板、皮带、同步轮及螺钉的配合。右端孔位虽保持相对关系，但它们在整机中的位置整体变了 30 mm；相邻零件可能也需加长。
3. 先用少量材料或局部试打印验证接口位置，再决定最终打印参数。

## 文件位置

- 原版：`STL （三维打印模型）/FOREARM （前臂）/J5_part.STL`
- 修正版（推荐打印）：`STL （三维打印模型）/FOREARM （前臂）/J5_part_J6_plus30mm_v2.STL`
- 修正版底部对比预览：`STL （三维打印模型）/FOREARM （前臂）/J5_part_J6_plus30mm_v2_底部对比预览.png`
