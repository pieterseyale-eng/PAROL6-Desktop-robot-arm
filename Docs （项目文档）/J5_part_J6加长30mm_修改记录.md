# J5_part 为 J6 电机组件加长 30 mm：修改记录

记录日期：2026-11-06

## 修改目的与范围

J6 更换为新的电机、减速器和控制板组合后，电机尾部预计比原设计向外突出约 23 mm。因此先给 J5_part 增加 30 mm 轴向空间，留下约 7 mm 的名义余量。这个余量只是按目前提供的突出量估算，尚未经过实物装配验证。

初次修改仅改变 `J5_part.STL` 的长度，原版保留。**2026-11-11 起当前打印版为 `J5_part_J6_plus30mm_v3_closed_holes_connector20.STL`**，在 v2 加长版上进一步补孔和避让电机插头。曾生成过一版会错误延长下方竖板的模型，已删除；不要从旧的打印队列或切片工程中使用它。各文件位置见文末。

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

### J5 同步带长度

原 BOM 的 **J5 皮带为 HTD3 246，宽 6 mm（82 齿）**；J5 电机带轮为 **12 齿**，输出带轮 `HTD3_48_J5_pulley` 为 **48 齿**。本版把右侧电机安装结构整体后移 30 mm，因此在带轮轴线仍平行、且中心距确实增加 30 mm 的前提下，原 246 mm 皮带无法继续使用。

直接量 STL 在 Z = 70 mm 截面的两个主要同轴孔：左侧中心约 **(28.5, 42.918)**，原版右侧中心约 **(104.5, 42.918)**，v2 右侧中心约 **(134.5, 42.918)**。据此，原版轴心距 **76.00 mm**，v2 轴心距 **106.00 mm**，确实增加 30.00 mm。计算假设这两个孔就是 J5 的 48 齿输出带轮和 12 齿电机带轮的轴心，且两带轮在同一平面。

按 HTD3 节距 3 mm，48 齿/12 齿带轮节圆半径分别为 `48×3/(2π) ≈ 22.918 mm`、`12×3/(2π) ≈ 5.730 mm`。两轮开口带的理论节线长为 `L = 2√(C²−(R−r)²) + π(R+r) + 2(R−r)asin((R−r)/C)`。代入原版 `C = 76 mm` 得 **245.904 mm**，与 BOM 的 246 mm 接近；代入 v2 `C = 106 mm` 得 **304.793 mm**。

推荐先按 **HTD3 306-6（102 齿，节线周长 306 mm，宽 6 mm）**采购和试装。它比理论需求长 **1.207 mm**；若没有张紧轮或可调轴距，306 mm 带在固定的 106 mm 轴距上可能偏松。让 306 mm 带按上述几何刚好张紧，轴距需约 **106.611 mm**，比当前模型大 **0.611 mm**。相邻的 303 mm 带则要求轴距约 **105.091 mm**，在当前 106 mm 固定轴距下可能装不上。打印与装配前须确认原结构的张紧行程；若无法调整，应重新设计轴距或张紧结构，而不能把 306 mm 当作已验证的即装即用尺寸。

这里改变的是 **J5 皮带**；原 BOM 中 J1 396、J3 342、J4 201 不因这次 J5_part 加长而直接改长。原版 `J5_belt_lid.STL` 也应检查是否覆盖加长后的带路，不应仅凭带长正确就直接打印使用。

1. 用实物测 J6 电机、减速器、控制板及接线插头在该方向的总外形，确认 30 mm 加长量和装配余量。
2. 在 CAD 或 Bambu Studio 中检查 J5_part 与相邻盖板、皮带、同步轮及螺钉的配合。右端孔位虽保持相对关系，但它们在整机中的位置整体变了 30 mm；相邻零件可能也需加长。
3. 先用少量材料或局部试打印验证接口位置，再决定最终打印参数。

## 文件位置

- 原版：`STL （三维打印模型）/FOREARM （前臂）/J5_part.STL`
- 加长版 v2（保留作后续修改基线）：`STL （三维打印模型）/FOREARM （前臂）/J5_part_J6_plus30mm_v2.STL`
- 修正版底部对比预览：`STL （三维打印模型）/FOREARM （前臂）/J5_part_J6_plus30mm_v2_底部对比预览.png`

## 2026-11-11：补孔并开电机插头避让口

用户实物照片显示，新 42 mm 电机后部的插头和线束与 J5 端部外壁干涉。用户要求将原外壁两个圆孔补上，开口宽度由 18 mm 改为 **20 mm**，以 42 mm 电机一边的 21 mm 中线为中心；避让口底面距电机安装面 **25 mm**。

本版始终从 **v2 加长 30 mm 的模型**生成，不改变已确认的横板加长量和皮带轴心距。坐标和操作如下：

- 两旧圆孔位于 `+Y` 外壁，约 `Y=64.0～71.418 mm`，圆心 `(X,Z)=(127.0,9.05)` 和 `(145.0,9.05) mm`，孔径约 12.4 mm。用略大于孔径的圆柱与壁体布尔合并，外表面齐平。
- 电机轴线约 `X=134.5 mm`，20 mm 开口横向范围为 `X=124.5～144.5 mm`。壁体沿 Y 方向全厚切穿，刀具 `Y=63.5～72.418 mm`。
- 电机安装面取上横板下表面 `Z=58.1 mm`。开口底面为 `Z=33.1 mm`，两者相差 25.0 mm。刀具向零件原 `Z=0` 边缘开通，范围 `Z=−1.0～33.1 mm`。该开口会覆盖第一旧圆孔位置，因此先补孔、再开口，最终外观只留矩形避让口。
- 用户在 Bambu Studio 截图中标出的 **A 面**为避让口底面 `Z=33.1 mm`，**B 面**为电机装配面 `Z=58.1 mm`。两平面沿法向相距 **25.0 mm = 2.5 cm**，不是 25 cm。此项已在 2026-11-11 与用户核对。
- v2 体积 `161316.49 mm³`；补孔后 `163162.94 mm³`；开口后 `158246.10 mm³`。最终网格封闭、法向一致、单连通实体，外包围盒仍为 `163.8 × 71.418 × 74 mm`。

当前文件：

- 打印：`3D打印/分锅STL/锅06_前臂与J5/J5_part_J6_plus30mm_v3_closed_holes_connector20.STL`
- 源模型：`STL （三维打印模型）/FOREARM （前臂）/J5_part_J6_plus30mm_v3_closed_holes_connector20.STL`
- 对比图：`STL （三维打印模型）/FOREARM （前臂）/J5_part_J6_plus30mm_v3_孔洞与避让对比.png`
- 再生成脚本：`STL （三维打印模型）/FOREARM （前臂）/生成J5插头避让版.py`
- 上一版打印副本备份：`3D打印/备份/J5_part_J6_plus30mm_v2_旧打印版.STL`

插头及线束外形还需用实物试装核对。若后续变更安装基准面，应重新标注 A、B 平面并更新生成脚本，不能直接沿用当前的 `Z=33.1 mm` 切口底面。
