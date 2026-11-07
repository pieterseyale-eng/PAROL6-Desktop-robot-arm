# PAROL6 制造版本 BOM（J5 加长 / 自研主控）

更新日期：2026-11-07。本表由原版 `BOM.md` 复制，供当前机械臂制造与采购核对；原版 BOM 保持不变。

## 本版改动与采购状态

| 项目 | 本制造版本 | 状态与说明 |
| :--- | :--- | :--- |
| J5 主体 | `J5_part_J6_plus30mm_v2.STL` | 上方横板加长 30 mm；以改版 STL 为准 |
| J5 同步带 | **HTD3 306-6，102 齿，1 条** | 代替原版 HTD3 246-6；理论节线长 304.793 mm，306 mm 带需核对张紧行程 |
| J1 / J3 / J4 同步带 | 396-3M-6 / 342-3M-6 / 201-3M-6，各 1 条 | 沿用原版规格 |
| 电机与驱动 | 张大头闭环步进 + X 固件，拟通过 CAN 控制 | 实际电机与驱动板型号、轴径、长度、接口以已购实物为准；原版电机表仅供对照 |
| 主控 | 自研 STM32 + CAN 收发器，电脑侧预留 USB | 具体最小系统板及电源方案尚待定；不采购原版 PAROL 主控板和 TMC5160 |
| 气动 / 真空夹爪 | 当前不纳入首轮制造 | 原版表中的相关条目仅供后续参考 |

J5 皮带测算与张紧注意事项见 [`J5_part_J6加长30mm_修改记录.md`](../Docs%20%EF%BC%88%E9%A1%B9%E7%9B%AE%E6%96%87%E6%A1%A3%EF%BC%89/J5_part_J6%E5%8A%A0%E9%95%BF30mm_%E4%BF%AE%E6%94%B9%E8%AE%B0%E5%BD%95.md)。本表保留原 BOM 的供应商链接作为零件参考，不代表当前商品规格已核实。

---

Most items have links where you can buy the item, and some of them are affiliate links. Items like screws, belts and bearings can be bought locally or from many other vendors.

> [!NOTE]
> If any product links are broken, unavailable, or no longer point to the correct item, please [open an issue](https://github.com/PCrnjak/PAROL6-Desktop-robot-arm/issues/new). You can also use the reference images to find the same or an equivalent part from another supplier.

---

## Screws and Nuts

| Diameter / Type | Length | Quantity | Description |
| :--- | :--- | :--- | :--- |
| M4 | 10 mm | 20 | DIN 912 / ISO 4762 (hexagon socket head cap) |
| M3 | 8 mm | 10 | 2 mm head height |
| M3 | 8 mm | 50 | DIN 912 / ISO 4762 (hexagon socket head cap) |
| M3 | 14 mm | 30 | DIN 912 / ISO 4762 (hexagon socket head cap) |
| M3 nut | — | 10 | DIN 934 / ISO 4032 (hexagon nut) |
| M3 | 25 mm | 10 | DIN 912 / ISO 4762 (hexagon socket head cap) |
| M2 | 10 mm | 10 | DIN 912 / ISO 4762 (hexagon socket head cap) |
| M3 | 16 mm | 10 | DIN 912 / ISO 4762 (hexagon socket head cap) |
| M3 | 6 mm | 10 | Pan head phillips |
| M3 | 12 mm | 30 | DIN 912 / ISO 4762 (hexagon socket head cap) |
| M3 | 35 mm | 10 | DIN 912 / ISO 4762 (hexagon socket head cap) |
| M4 | 16 mm | 30 | DIN 912 / ISO 4762 (hexagon socket head cap) |
| M4 | 14 mm | 10 | DIN 912 / ISO 4762 (hexagon socket head cap) |
| M4 | 50 mm | 10 | DIN 912 / ISO 4762 (hexagon socket head cap) |
| M3 | 15 mm | 2 | Tapered screw head |

---

## Gearboxes

> [!NOTE]
> For cheaper gearbox options you can use MG series planetary gearboxes. They have bigger backlash but are cheaper. [Link](https://www.omc-stepperonline.com/mg-series-planetary-gearbox) — [Aliexpress Link](https://s.click.aliexpress.com/e/_oBYBoUP)

| Name | Type | Quantity | Description | Link | ALT link | Reference Image |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Gearbox 20:1 | Nema 17 20:1 | 2 | EG precision planetary | [Link](https://www.omc-stepperonline.com/eg-series-planetary-gearbox-gear-ratio-20-1-backlash-20-arc-min-for-nema-17-stepper-motor-eg17-g20?tracking=6543849d6ff69) | [Alt Link](https://s.click.aliexpress.com/e/_oEhMNU5) | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/stepper%2020_1.jpg) |
| Gearbox 10:1 | Nema 17 10:1 | 1 | EG precision planetary | [Link](https://www.omc-stepperonline.com/eg-series-planetary-gearbox-gear-ratio-10-1-backlash-15-arc-min-for-nema-17-stepper-motor-eg17-g10?tracking=6543849d6ff69) | [Alt Link](https://s.click.aliexpress.com/e/_oEhMNU5) | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/stepper%2010_1.jpg) |

---

## Motors — 原版电机参考（当前不按此表采购）

当前改用张大头闭环步进及 X 固件；电机型号、机身长度与 CAN 接口按已购实物填写，不把下列开环电机数量当作现行采购单。


| Name | Type | Quantity | Description | Link | ALT link | Reference Image |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Stepper 1 | Nema 17 | 1 | 16Ncm, 42x42x20mm | [Link](https://www.omc-stepperonline.com/nema-17-bipolar-1-8deg-16ncm-22-6oz-in-1a-3-7v-42x42x20mm-4-wires-17hs08-1004s?tracking=6543849d6ff69) | [Alt Link](https://s.click.aliexpress.com/e/_oo1LTs7) | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/stepper%2021_5mm.jpg) |
| Stepper 2 | Nema 17 | 3 | 45Ncm, 42x42x40mm | [Link](https://www.omc-stepperonline.com/nema-17-bipolar-45ncm-64oz-in-2a-42x42x40mm-4-wires-w-1m-cable-connector-17hs16-2004s1?tracking=6543849d6ff69) | [Alt Link](https://s.click.aliexpress.com/e/_oC1Ii0v) | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/stepper%2040mm.jpg) |
| Stepper 3 | Nema 17 | 2 | 65Ncm, 42x42x60mm | [Link](https://www.omc-stepperonline.com/nema-17-bipolar-1-8deg-65ncm-92oz-in-2-1a-3-36v-42x42x60mm-4-wires-17hs24-2104s?tracking=6543849d6ff69) | [Alt Link](https://s.click.aliexpress.com/e/_opq2ugp) | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/stepper%2060mm.jpg) |

---

## Belts

| Name | Type | Quantity | Description | Link | ALT link | Reference Image |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Joint 1 belt | HTD3 396 | 1 | 6 mm width | [Link](https://s.click.aliexpress.com/e/_c3LnffKl) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/HTD%203M%20belt.png) |
| Joint 3 belt | HTD3 342 | 1 | 6 mm width | [Link](https://s.click.aliexpress.com/e/_c4O7CHOd) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/HTD%203M%20belt.png) |
| Joint 4 belt | HTD3 201 | 1 | 6 mm width | [Link](https://s.click.aliexpress.com/e/_c4NiUycd) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/HTD%203M%20belt.png) |
| Joint 5 belt（制造版） | **HTD3 306** | **1** | **6 mm width；102 齿；需核对张紧量** | 原版 246 规格链接不适用 | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/HTD%203M%20belt.png) |

---

## Pulleys

| Name | Type | Quantity | Description | Link | ALT link | Reference Image |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| J4 pulley, J5 pulley | HTD3M 12 tooth | 2 | 5mm bore, 10mm width | [Link](https://s.click.aliexpress.com/e/_DFYERWX) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/HTD%203M%20pulley.png) |
| J1 pulley | HTD3M 15 tooth | 1 | 5mm bore, 10mm width | [Link](https://s.click.aliexpress.com/e/_DBVgkVp) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/HTD%203M%20pulley.png) |

---

## Shaft couplers

| Name | Type | Quantity | Description | Link | ALT link | Reference Image |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Shaft coupler | Shaft coupler | 3 | 8 mm hole shaft, M4 screw holes | [Link](https://s.click.aliexpress.com/e/_c2xnQgI7) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/shaft%20coupler%20gripper.png) |

---

## Bearings

| Name | Type | Quantity | Description | Link | ALT link | Reference Image |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Bearing 1 | AXK3552 | 1 | 35X52X4, needs to have top and bottom plate | [Link](https://s.click.aliexpress.com/e/_Dk4bHg7) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/AXK3552%20needle%20bearing.png) |
| Bearing 2 | NSK HR32906J | 5 | Joint 5, 4 and 3 | [Link](https://s.click.aliexpress.com/e/_DcJMtBl) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/Tapered%20bearing.png) |
| Bearing 3 | NSK HR32907J | 4 | Joint 1 and 2 | [Link](https://s.click.aliexpress.com/e/_DcJMtBl) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/Tapered%20bearing.png) |
| Tension bearing | Ball bearing 3x8x4 | 20 | Used for belt tension | [Link](https://s.click.aliexpress.com/e/_DCjfgFV) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/small%20tension%20bearings.png) |
| Tension bearing | Ball bearing 3x10x4 | 20 | Used for belt tension | [Link](https://s.click.aliexpress.com/e/_DlA33Af) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/small%20tension%20bearings.png) |

---

## Electronics — 原版电控参考（当前不按此表采购）

以下原厂主控板、TMC5160、USB-B 线和原版电源等条目仅用于追溯原项目。当前 STM32 + CAN 方案见 `../Control/PAROL6_STM32_X固件_CAN六轴控制方案.md`；传感器和急停件须按自研电路核定接口。


| Name | Type | Quantity | Description | Link | ALT link | Reference Image |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| PAROL control board | | 1 | [source-robotics.com](http://source-robotics.com/) | [Link](https://source-robotics.com/products/parol6-control-board) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/PAROL6%20control%20board.jpg) |
| TMC5160 | | 6 | Drivers from the links are tested. Use any other at own risk | [Link](https://s.click.aliexpress.com/e/_c3Jc52V9) | [Alt Link](https://s.click.aliexpress.com/e/_Dd8Cjkb) | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/TMC5160%20driver.jpg) |
| Thermal paste / cement | | 2 | Needed only if your control board has no drivers! | [Link](https://s.click.aliexpress.com/e/_c2u86OEn) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/Thermal%20cement.jpg) |
| On/Off button | | 1 | 12mm 3-6V | [Link](https://s.click.aliexpress.com/e/_DBpZV3h) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/button.png) |
| JST PH 2.0mm 200mm 4PIN | | 1 | For power button | [Link](https://s.click.aliexpress.com/e/_DeObQ1D) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/JST_PH.png) |
| Noctua NF-A4x20 5V 40mm | | 1 | or any 40mm 5V fan| | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/Noctua%20NF-A4x20%20fan.jpg) |
| Power connector - male + female | | 1 | GX16 2PIN | [Link](https://s.click.aliexpress.com/e/_DcHjMfN) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/GX16.jpg) |
| Gripper connector (electric) | | 1 | M8 sensor Female 4 pin | [Link](https://s.click.aliexpress.com/e/_DDQz9iP) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/M8%20connector%20female%204pin.png) |
| Power supply | | 1 | Any 24V 5A supply | [Link](https://www.omc-stepperonline.com/edr-120-24-mean-well-120w-24vdc-5a-115-230vac-din-rail-power-supply-edr-120-24?tracking=6543849d6ff69) | [Alt Link](https://s.click.aliexpress.com/e/_olFOM5Z) | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/Power%20supply%20EDR-120-24.jpg) |
| Limit switches | | 3 | Type ZW12-3 | [Link](https://s.click.aliexpress.com/e/_DBq6eeF) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/LIMIT_SWITCH.png) |
| Inductive sensor 1 | | 1 | 4mm NPN NO | [Link](https://s.click.aliexpress.com/e/_c40MRkk5) | [Alt Link](https://s.click.aliexpress.com/e/_c3CMbO1h) | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/INDUCTIVE_4MM.png) |
| Inductive sensor 2 | | 1 | GX-F8A | [Link](https://s.click.aliexpress.com/e/_c4VxLtW3) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/GX-F8A.png) |
| Inductive sensor 3 | | 1 | M5, NPN NO | [Link](https://s.click.aliexpress.com/e/_c3zGvxrP) | [Alt Link](https://s.click.aliexpress.com/e/_c3CMbO1h) | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/INDUCTIVE_5MM.png) |
| Estop | | 1 | Any NC estop | [Link](https://s.click.aliexpress.com/e/_c3Bn4RR5) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/19mm%20ESTOP.png) |
| Cable gland for estop | | 1 | PG7 type | [Link](https://s.click.aliexpress.com/e/_DdJj62p) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/CABLE_GLAND.png) |
| M3 brass insert | | 4 | M3, 6mm lenght | [Link](https://s.click.aliexpress.com/e/_DmZR9AN) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/brass_insert.png) |
| Pneumatic connector - robot | | 4 | 4 mm type PM | [Link](https://s.click.aliexpress.com/e/_c3GpN5cR) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/PM4.png) |
| Pneumatic Gripper | | 1 | MHZ2-16D | [Link](https://s.click.aliexpress.com/e/_c4EJl0Qr) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/MHZ.png) |
| Pneumatic gripper connector | | 2 | PC4 - M5 | [Link](https://s.click.aliexpress.com/e/_DkCJqUL) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/PC4-M5.png) |
| Pneumatic tube | | 5 meters | 1 meter, 4x2.5mm | [Link](https://s.click.aliexpress.com/e/_DEhvFyJ) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/Pneumatic_tube.png) |
| xt30 connector female | | 1 | Used to deliver power to PAROL6 PCB | [Link](https://s.click.aliexpress.com/e/_DllR7eL) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/XT30%20female%20connector.jpg) |
| Stlink / programming adapter | | 1 | Use our [Official programming adapter](https://source-robotics.com/products/parol6-programming-adapter) for ease of use! Pin order needs to be: SWCLK, SWDIO, GND, 3V3, 5V | [Link](https://s.click.aliexpress.com/e/_c38Ao641) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/PAROL6%20programming%20adapter.jpg) |
| USB B cable | | 1 | Comms to the PC | | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/USB%20B%20cable.jpg) |
| 5/2 solenoid air valve | | 1 | 4mm tube connectors, 5/2, 24V | [Link](https://s.click.aliexpress.com/e/_DDrw0Ux) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/solenoid_valve.png) |

---

## Vacuum gripper — 后续可选（首轮不采购）

| Name | Type | Quantity | Description | Link | ALT link | Reference Image |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Suction cup gripper | | 1 | | [Link](https://s.click.aliexpress.com/e/_c3bSPdVZ) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/Suction%20cup%20gripper.jpg) |
| Vacuum generator | | 1 | | [Link](https://s.click.aliexpress.com/e/_c2zw8dHh) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/Vacuum%20generator.jpg) |
| 4mm to 6mm coupler | | 1 | | [Link](https://s.click.aliexpress.com/e/_c3wvdY99) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/Pneumatic%20coupler%204%20to%206%20mm.jpg) |

---

## Small print bed modification

> [!NOTE]
> These parts are only needed if your printer bed is too small for `J1_turret_rework_blocker` and `Upper_arm`. Both parts are split in two and joined with dowel pins and epoxy after printing. STL files are in [STL/SMALL_PRINT_BED](../STL%20%EF%BC%88%E4%B8%89%E7%BB%B4%E6%89%93%E5%8D%B0%E6%A8%A1%E5%9E%8B%EF%BC%89/SMALL_PRINT_BED%20%EF%BC%88%E5%B0%8F%E5%B0%BA%E5%AF%B8%E6%89%93%E5%8D%B0%E5%B9%B3%E5%8F%B0%EF%BC%89). Nothing else in the build changes.

| Name | Type | Quantity | Description | Link | ALT link | Reference Image |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| J1 turret dowel pin | Dowel pin 4 x 18 mm | 3 | Solid cylindrical, stainless or hardened steel | [Link](https://www.aliexpress.com/item/1005009401701158.html) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/Dowel%20pin.jpg) |
| Upper arm dowel pin | Dowel pin 6 x 22 mm | 4 | Solid cylindrical, stainless or hardened steel | [Link](https://www.aliexpress.com/item/1005009401701158.html) | | [Link](BOM%20reference%20images%20%EF%BC%88%E7%89%A9%E6%96%99%E5%8F%82%E8%80%83%E5%9B%BE%E7%89%87%EF%BC%89/Dowel%20pin.jpg) |
| Two part epoxy | Epoxy adhesive | 1 | 1:1 mix, slow setting | [Link](https://www.aliexpress.com/item/1005012397836514.html) | | |
