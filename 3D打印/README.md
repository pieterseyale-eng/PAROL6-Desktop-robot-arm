# PAROL6 三维打印操作说明（拓竹 P1S）

实验室打印机：Bambu Lab P1S。切片软件：Bambu Studio。此文件夹中的 `分锅STL` 是按建议锅次整理的模型输入包，**还不是可直接启动打印的 G-code 文件**。每锅一个子目录，目录内全部 STL 属于同一锅，可一次性多选导入 Bambu Studio。

## 文件结构

- `分锅STL/锅01_底座主件` 至 `锅08_小辅件`：每个目录含本锅 STL 和 `本锅零件.txt` 清单。
- `锅03_J1改装限位件_可选` 仅在采用该 J1 rework 结构时打印；标准 J1 版本不要和它同时打印。
- 锅04采用整件上臂 `Upper_arm.STL`。小平台分体上臂 A/B 是替代方案，不要重复打印。
- 锅06使用 `J5_part_J6_plus30mm_v2.STL`，上方横板加长 30 mm，下方竖板保持原形。原版 `J5_part.STL` 已从分锅目录移至 `备份/J5_part_原版.STL`，不要把备份件与锅06一同导入。修改方法见 `../Docs （项目文档）/J5_part_J6加长30mm_修改记录.md`。
- `分锅STL.zip` 与当前分锅目录同步，锅06只含加长版 J5 主体；备份件不在压缩包中。
- 气动夹爪附件、真空夹爪附件未加入本批次。锅06的 J5 主体已为 J6 电机组件预留 30 mm；J6 周边件及相邻盖板的实际配合仍需装配核对。
- 原始 STL 在 `../STL （三维打印模型）`，整理包为副本，不覆盖原文件。

## 在 Bambu Studio 中切片

1. 打开对应锅次文件夹，全选其中 STL，一次性拖入 Bambu Studio；选择 P1S 和实际喷嘴。
2. 使用自动摆放后逐个检查模型未超出平台、对象间有足够间隙，关键孔、轴承座和装配基准面没有被支撑封住。自动摆盘可能需要手动调整；检查长件边缘余量。
3. 按实际耗材线轴选择材料配置。PAROL6 原说明建议 PETG，但材料品牌和型号尚未提供。Bambu Studio 中的 Generic PETG HF 只是软件配置候选，**只有线轴规格适配该预设时才能使用**，不得把预设视为实验室已确认耗材。按线轴厂商说明干燥耗材并设置温度。
4. 检查方向、支撑、首层、零件间隔、打印时间与耗材估算后点击“切片”。大型承力零件建议先打样检查尺寸和层间强度。
5. 切片完成后导出板切片文件，保存为 `.gcode.3mf`；另存普通 `.3mf` 项目文件以便调整。普通 `.3mf` 和 STL 都不是已切片打印文件。
6. 将 `.gcode.3mf` 放到机器或存储介质后，由操作者核对耗材、打印板和首层情况，再开始打印。

## CLI 状态

Bambu Studio 官方 CLI 文档提供 `--orient`、`--arrange`、`--slice`、`--export-3mf` 参数（[官方 Command Line Usage](https://github.com/bambulab/BambuStudio/wiki/Command-Line-Usage)）。本机安装路径为 `D:\Software\bambu_LAB\Bambu Studio\bambu-studio.exe`。目前尝试在 Windows 下执行 CLI 时只启动/聚焦 GUI，没有得到导出的 G-code；因此本目录没有伪造或标记任何未切片文件为打印就绪。配置文件来源：Bambu Studio 安装/用户数据中的 P1S 0.4 mm 喷嘴机型与 Generic PETG HF 配置；实际耗材仍需按线轴确认。成功前应先对一个小件做 CLI 冒烟测试，并验证生成文件确实包含 G-code 与正确 P1S 参数，再批量切片。

推荐 CLI 命令形式（待本机验证成功后再用于批量输出）：

```powershell
& 'D:\Software\bambu_LAB\Bambu Studio\bambu-studio.exe' `
  --orient --arrange 1 `
  --load-settings 'machine-full.json;process-full.json' `
  --load-filaments 'filament-full.json' `
  --slice 0 --export-3mf '锅01.gcode.3mf' '锅01.3mf'
```

Bambu 官方文档要求 CLI 所用 settings 为完整配置；仅有 `inherits` 的原始 profile 不一定可直接传入。多零件同板优先使用 Bambu Studio 项目 3MF 输入，避免把多个 STL 当作多个独立板。当前阶段每锅 STL 均可一起导入后再切片。

## 方案限制

8 锅是基于 STL 包围盒和零件组合的候选分组，不等于已在切片器确认可摆放。方向、支撑、Brim、部件碰撞、承力层向以及耗材时间均需 Bambu Studio 预览确认。开始正式批量打印前，请复核版本选择和分锅清单。
