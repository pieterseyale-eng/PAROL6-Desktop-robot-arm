# Small print bed modification

These STL files are **replacements**, not additions.

`Upper_arm （上臂）` and `J1_turret_rework_blocker （J1转台限位件）` do not fit on a printer with a bed
smaller than about 175 mm. No rotation makes them fit: the smallest cube that
can contain the upper arm is 160.5 mm, and the turret blocker 154.1 mm.

Each part here is split into two halves that are joined with steel dowel pins
and two part epoxy after printing.

> [!IMPORTANT]
> Only use these files if your printer bed is too small for the standard parts.
> If the original parts fit, print those instead. A single moulded part is always
> stronger than a bonded one.

## Contents

| Folder | Replaces | Halves |
| :--- | :--- | :--- |
| `Upper_arm （上臂）` | `STL （三维打印模型）/UPPER_ARM （上臂）/Upper_arm.STL` | `Upper_arm_A_long_end.STL`, `Upper_arm_B_short_end.STL` |
| `J1_turret_rework_blocker （J1转台限位件）` | `STL （三维打印模型）/SHOULDER （肩部）/J1_turret_rework_blocker.STL` | `J1_turret_rework_blocker_A_turret_end.STL`, `J1_turret_rework_blocker_B_arm_end.STL` |

Print one folder or both, depending on which parts do not fit. Every other part
of the robot is unchanged.

## Before you print

Read `Building instructions （装配说明）/Parol small print bed modification.pdf` first. It
covers the reamers, dowel pins and epoxy you need, and the assembly steps for
both parts.

The extra hardware is listed under **Small print bed modification** in
`BOM （物料清单）/BOM.md`.
