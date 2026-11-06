## 第76页
肩部装配（Shoulder assembly）

- 零件：`J2_bearing_backplate`、`J2_cover`
- 使用 4 颗 M3 × 12 mm 螺钉。
- `J2_cover` 和 `bearing_backplate` 都带有螺纹。

## 第77页
肩部装配（Shoulder assembly）

- 零件：`J1_belt_cover`、`J1_wires_cover`
- 使用 M2 × 10 mm 螺钉。
- 将 J1 步进电机的导线穿过 `J1_belt_cover` 上的孔，再穿过 `J1_rotation_shaft`。
- 此阶段不要把 `J1_belt_cover` 拧紧固定！
- 用 2 颗 M2 螺钉固定线缆盖（wires cover）。

## 第78页
肩部装配（Shoulder assembly）

- 将其余所有导线继续穿过 `J1_rotation_shaft`。

## 第79页
底座装配（Base assembly）

## 第80页
底座装配（Base assembly）

- 零件：`Main_base`、2 个 3 号轴承（bearing 3）、传感器 3（Sensor 3）。
- 使用 1 颗 M3 × 25 mm 螺钉。
- 传感器 3 必须与主底座表面齐平。使用随附螺母从两侧各固定一个。
- 在红色标记的孔中将 M3 × 20 mm 螺钉拧到底。它用作 J1 的旋转限位。
- **如果没有安装旋转限位块，底座中的 J1 转动超过一圈可能损坏机械臂！**
- PAROL6 使用开环步进驱动器，需要执行回零。J1、J4、J6 使用电感式传感器回零。回零由小螺钉靠近传感器并触发完成。需要找到能可靠触发传感器的合适位置（sweet spot）。

## 第81页
底座装配（Base assembly）

- 零件：J1 带轮（J1 pulley）、J1 皮带（J1 belt）。
- 将 J1 皮带放到位。除了 J1 传感器的线以外，将所有导线穿过底座部件；随后缓慢地将底座向上套到 `J1_rotation_shaft` 上。
- 此时皮带应绕在底座周围。之后可以拧上盖板并安装带轮。带轮侧面有紧定螺钉孔，盖件上也有对应孔。
- 如有需要，在红色标记处增加皮带张紧轴承。

## 第82页
底座装配（Base assembly）

- 零件：`J1_backplate`。
- 使用 6 颗 M4 × 16 mm 螺钉。
- 将除 J1 传感器线以外的所有导线穿过 `J1_backplate`。

## 第83页
底座装配（Base assembly）

所有机械臂线缆都必须穿过孔 1 和孔 2。为减少线束杂乱并减轻线缆受力，请按以下方式布线：

- **孔 1：**J1、J3、J5 步进电机线；限位开关 2、1、5 的线。
- **孔 2：**J2、J4、J6 步进电机线；限位开关 6、3、4 的线；CAN 线；气动管。

## 第84页
底座装配（Base assembly）

- PAROL6 主控板（control board）。原手册提供购买链接：<https://source-robotics.com/products/parol6-control-board>，也可联系 `info@source-robotics.com`。
- 按图示方向放置控制板。按照本手册或项目文档中的接线说明连接机械臂。

## 第85页
按照左侧图片为机械臂接线。

- 步进电机必须正确连接 A、B 两相。若只交换其中一相的两根线（例如 A+ 和 A−），方向可在软件中处理。
- 限位开关不区分方向：一根线接 24 V，另一根线接信号端。
- 电感式传感器线色：
  - 黑色（Black）：信号
  - 蓝色（Blue）：负极
  - 棕色（Brown）：正极

## 第86页
将夹爪 CAN 连接线接到 POWER 电源接口的 24 V 和 GND（图中红色箭头）。将夹爪的 CANH、CANL 线分别接到 CANBUS 接口的 CAN1H、CAN1L（图中蓝色箭头）。

## 第87页
底座装配（Base assembly）

- 零件：电子设备外壳（`Electronics case`）。
- 使用 8 颗 M3 × 12 mm 螺钉。
- 从控制板下方滑入电子设备外壳，并用 8 颗 M3 螺钉固定到机械臂上。拆下 USB 旁绿色接线端子上的端子部件。

## 第88页
准备线缆（Prepare the wires）

- 电源开关（On/off button）
- JST PH 2.0 mm、4 针导线
- 按导线颜色标记将 JST 导线接到按钮上。**只有在导线和按钮型号完全相同时，才照颜色对应连接。**
- JST 线长应为 80 mm。

## 第89页
准备线缆（Prepare the wires）

- GX16 2 针插头（GX16 2PIN）
- XT30 母头（XT30 female connector）
- 在至少 110 mm 长的导线上连接 GX16 2 针公头与 XT30 母头。
- **务必按图片所示核对极性！**

## 第90页
底座装配（Base assembly）

- 2 个气动接头（Pneumatic connector 1）、电源开关、电源连接器。
- 使用 8 颗 M3 × 8 mm 螺钉。
- 气动管从机械臂底座穿出后，长度至少应为 150 mm。
- 如有需要，缩短冷却风扇导线。注意风扇的正负极性。

## 第91页
底座装配（Base assembly）

- 零件：`Lid_electronics`、风扇盖（Fan cover）、冷却风扇（Cooling fan）。
- 使用 2 颗 M3 × 8 mm 螺钉。
- 使用随附螺钉安装冷却风扇。若风扇线过长则缩短。不同风扇可能需要不同规格的螺钉。
- **将 24 V 电源接入机械臂时，务必确认连接器接线极性正确！**

## 第92页
底座装配（Base assembly）

- 零件：底盖（Bottom lid）。
- 使用 3 颗 M3 × 8 mm 螺钉；螺钉头高度为 2 mm。

## 第93页
安装 J5 皮带（Attaching J5 belt）

- 零件：J5 带轮（J5 Pulley）、J5 皮带（J5 belt）。
- 将皮带安装在 J5 带轮与 `HTD3_48_J5_pulley` 之间。

## 第94页
安装 J3 皮带（Attaching J3 belt）

- 4 个 3 × 8 mm 轴承、`42_pulley`、法兰联轴器（shaft coupler）。
- 使用 4 颗 M4 × 10 mm 螺钉将法兰联轴器安装到带轮上。
- 减速器上有一个供键使用的键槽。本方案不使用键，因此确保法兰联轴器的紧定螺钉对准键槽！此处使用螺纹锁固剂（threadlocker）。

## 第95页
法兰联轴器（shaft couplers）！

> 本页为图示/提醒页；文字层仅提及法兰联轴器。

## 第96页
安装关节盖（Attaching joint covers）

- 使用：2 颗 M3 × 12 mm、2 颗 M3 × 8 mm、8 颗 M3 × 14 mm 螺钉，以及 8 个 4 × 8 × 3 mm 球轴承。
- 每侧皮带各安装 2 个轴承作为张紧轴承。使用 M3 × 14 mm 螺钉安装。
- 图中还标注 M3 × 12 mm、M3 × 8 mm、M3 × 14 mm 及张紧轴承（tension bearings）。

## 第97页
气动夹爪（Pneumatic gripper）

- 法兰联轴器（shaft coupler）、4 颗 M4 × 10 mm 螺钉、气动夹爪支架（Pneumatic gripper holder）、M3 × 14 mm 螺钉。
- 将法兰联轴器安装到气动夹爪支架上。确保法兰联轴器紧定螺钉孔与支架上的孔对齐。

## 第98页
气动夹爪（Pneumatic gripper）

- M3 × 14 mm 螺钉、气动夹爪、4 颗 M4 × 10 mm 螺钉。
- 用 4 颗 M4 螺钉将夹爪安装到支架上。若夹爪尚未安装气动接头，则加装接头。
- 将回零螺钉（M3 × 14 mm）安装到箭头所示的孔中，确认该螺钉能触发传感器。
- 拧紧法兰联轴器上的紧定螺钉。

## 第99页
急停装配（Estop assembly）

- 急停按钮（Estop）、急停盒底部（Estop bottom）、急停盒顶部（Estop top）、PG7 电缆密封接头（Cable gland PG7）。
- 使用 4 颗 M3 × 25 mm 螺钉及 4 个 M3 黄铜热熔嵌件。

## 第100页
SSG48 夹爪（SSG48 gripper）

如果你想为 PAROL6 制作 SSG 电动夹爪，请参考指南：<https://github.com/PCrnjak/SSG-48-adaptive-electric-gripper>。

## 第101页
恭喜完成！

请前往项目文档，了解如何启动并使用机械臂：<https://source-robotics.github.io/PAROL-docs/>。
