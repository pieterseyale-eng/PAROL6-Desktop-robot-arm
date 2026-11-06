
<div align="center">

# PAROL6-Desktop-robot-arm

</div>

## 本地改装项目入口

| 内容 | 位置 |
| --- | --- |
| 正在使用的 P1S 分锅打印文件与说明 | [3D打印](<3D打印/README.md>) |
| STM32 + 张大头 X 固件 CAN 控制方案 | [Control](<Control/PAROL6_STM32_X固件_CAN六轴控制方案.md>) |
| 项目进度、采购资料与财务台账 | [Docs（项目文档）](<Docs （项目文档）/项目进度.md>) |
| 原版与改版 STL、J5 加长修改记录 | [STL（模型）](<STL （三维打印模型）/FOREARM （前臂）/J5_part_J6_plus30mm_v2.STL>) · [修改记录](<Docs （项目文档）/J5_part_J6加长30mm_修改记录.md>) |
| 装配手册、中文版 PDF 与翻译底稿 | [Building instructions（装配说明）](<Building instructions （装配说明）/PAROL6装配说明_中文.pdf>) |
| 电机、减速器资料 | [硬件资料](<硬件资料/张大头/PAROL6选型与控制方案.md>) |
| 原仓库附带的 ST-LINK Windows 驱动包 | [STM32 开发工具](<硬件资料/STM32开发工具/en.stsw-link009.zip>) |

打印用文件以 `3D打印/分锅STL` 中的当前版本为准；正在打印期间先核对对应锅次的 `本锅零件.txt`。

## URDF and MuJoCo models

**[Open the PAROL6 model guide and downloads](parol6_description%20%EF%BC%88%E6%9C%BA%E5%99%A8%E4%BA%BA%E6%A8%A1%E5%9E%8B%E8%AF%B4%E6%98%8E%EF%BC%89)**

The `parol6_description （机器人模型说明）/` folder contains the product README, preview images and
download links for all six robot/end-effector configurations.
All maintained model files live in [robot_descriptions](https://github.com/Source-Robotics/robot_descriptions).
Download the model ZIP for your product and simulator from the guide, then
extract it into your working directory. This hardware repository needs no
model submodule or recursive clone.





<img src="Images%20%EF%BC%88%E5%9B%BE%E7%89%87%E8%B5%84%E6%96%99%EF%BC%89/img3.png" alt="drawing" width="5000"/>

<div align="center">

</div>

<div align="center">

[![License: CERN-OHL-S-2.0](https://img.shields.io/badge/license-CERN--OHL--S--2.0-blue)](LICENSE) [![Firmware: GPL-3.0](https://img.shields.io/badge/firmware-GPL--3.0-blue)](PAROL6%20control%20board%20main%20software/LICENSE)    ![Issues](https://img.shields.io/github/issues/Source-Robotics/PAROL6-Desktop-robot-arm) ![release](https://img.shields.io/github/v/release/Source-Robotics/PAROL6-Desktop-robot-arm) [![Powered by the Robotics Toolbox](https://raw.githubusercontent.com/petercorke/robotics-toolbox-python/master/.github/svg/rtb_powered.min.svg)](https://github.com/petercorke/robotics-toolbox-python) 

<p align="center">
  <a href="https://docs.source-robotics.com/PAROL-docs/"><img src="https://img.shields.io/badge/doc-page-orange" alt="Documentation"></a>
  <a href="http://discord.gg/prjUvjmGpZ"><img src="https://img.shields.io/discord/1072498136284667955?logo=discord&color=blue" alt="Discord"></a>
  <a href="https://source-robotics.com/"><img src="https://img.shields.io/badge/Shop-shopping-purple?logo=shopify" alt="Shop"></a>
  <a href="https://www.linkedin.com/company/source-robotics/"><img src="https://img.shields.io/badge/LinkedIn-Follow-blue?logo=linkedin" alt="LinkedIn"></a>
  <a href="https://x.com/SourceRobotics"><img src="https://img.shields.io/badge/X-Follow-black?logo=x" alt="X"></a>
  <a href="https://www.youtube.com/@source-robotics"><img src="https://img.shields.io/badge/YouTube-Subscribe-red?logo=youtube" alt="YouTube"></a>
</p>

## [▶️YouTube🔴 Video of Robot in Action!](https://youtu.be/bbrFn3aFLaA)

</div>



## 📖 Project Overview
PAROL6 is a high-performance 3D-printed desktop robotic arm. The design approach of PAROL6 was to be similar to industrial robots in terms of mechanical design, control software, and usability. Control software, GUI, and robots STL files are open-source. 

## How to build / Where to buy?

You can buy the PAROL6 robotic arm on our website: https://source-robotics.com

If you want to Source all the parts yourself and build your own follow these steps:

* Source all the parts from the [BOM](https://github.com/Source-Robotics/PAROL6-Desktop-robot-arm/tree/main/BOM)
* Follow [Building instructions](https://github.com/Source-Robotics/PAROL6-Desktop-robot-arm/tree/main/Building%20instructions) to assemble your robot
* Follow [DOCS](https://docs.source-robotics.com/PAROL-docs/) to get your robot up and running.

## 📚 Resources
- [Official website](https://source-robotics.com)
- [Commander software](https://github.com/Source-Robotics/PAROL-commander-software) ------ [Minimal hardware specs!](https://github.com/Source-Robotics/PAROL-commander-software/blob/main/confirmed_working_systems.md)
- [PAROL-Web-Commander](https://github.com/Jepson2k/PAROL-Web-Commander) — alternative web-based commander software
- [Python API](https://github.com/PCrnjak/PAROL6-python-API) ; [Python API legacy](https://github.com/PCrnjak/PAROL6-python-API-Alvar)
- [Building instructions](https://github.com/Source-Robotics/PAROL6-Desktop-robot-arm/tree/main/Building%20instructions)
- [BOM](https://github.com/Source-Robotics/PAROL6-Desktop-robot-arm/tree/main/BOM)
- [DOCS](https://docs.source-robotics.com/PAROL-docs/)
- [Video tutorials](https://youtube.com/playlist?list=PLSueoDrBt5MMTL9O8qAWZiJrNIf8-29Qz&si=Zca3UZKENje9ifow)
- [ROS2 / Moveit simulation](https://github.com/Source-Robotics/PAROL6-ROS2-MOVEIT)

- [Community projects](community_projects.md) — GUIs, vision/AI demos, and hardware mods built by the community

## 🌐 More about PAROL6 robotic arm

| YouTube | Instagram | Twitter | LinkedIn |
|--------|-----------|---------|----------|
| [![YouTube](https://img.shields.io/badge/YouTube-FF0000?logo=youtube&logoColor=white)](https://www.youtube.com/@source-robotics) | [![Instagram](https://img.shields.io/badge/Instagram-E4405F?logo=instagram&logoColor=white)](https://www.instagram.com/source_robotics/) | [![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?logo=twitter&logoColor=white)](https://twitter.com/SourceRobotics) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/company/source-robotics) |


| Discord | Forum | Hackaday | Blog |
|--------|-------|------| ------|
| [![Discord](https://img.shields.io/badge/Discord-5865F2?logo=discord&logoColor=white)](https://discord.com/invite/prjUvjmGpZ) | [![Discussions](https://img.shields.io/badge/Discussions-0A0A0A?logo=github)](https://github.com/orgs/Source-Robotics/discussions) | [![Hackaday](https://img.shields.io/badge/Hackaday-000000?logo=hackaday&logoColor=white)](https://hackaday.io/project/191860-parol6-desktop-robotic-arm) | [![Blog](https://img.shields.io/badge/Blog-Source%20Robotics-blue)](https://source-robotics.com/blogs/blog) 


## ⚠️ Safety, Liability & Disclaimer
This project includes experimental software, hardware designs, and assembly documentation that are still under development and may contain bugs, errors, or incomplete features. By using, building, or modifying this project, you acknowledge that:

* You use this project entirely at your own risk
* You are solely responsible for safe assembly, testing, and operation
* No guarantee is made regarding correctness, safety, or reliability
* The authors are not responsible for any damage, injury, or loss resulting from the use or misuse of this project
* Hardware performance and safety depend on user assembly, component quality, calibration, and handling, which cannot be guaranteed
* This project is provided “as is.” If you choose to build a device yourself using these files, designs, or instructions, you do so without any warranties or guarantees, including regarding safety, reliability, or suitability for any particular purpose.

THIS PROJECT INVOLVES LETHAL VOLTAGES AND OTHER SERIOUS HAZARDS THAT CAN CAUSE SEVERE INJURY. YOU MUST READ THE FULL [SAFETY WARNING AND DISCLAIMER DOCUMENT](SAFETY_WARNING_AND_DISCLAIMER.md)  BEFORE USING ANY PROJECT FILES. BY PROCEEDING, YOU ACKNOWLEDGE AND ACCEPT ALL RISKS AND AGREE TO USE THIS PROJECT ENTIRELY AT YOUR OWN RESPONSIBILITY.

## 🛡️ Licensing
The hardware, everything in this repository except the firmware, is under the [CERN Open Hardware Licence Version 2 - Strongly Reciprocal](LICENSE) (CERN-OHL-S-2.0): the STL files, the BOM, the building instructions, the print table and the robot models. The firmware in `PAROL6 control board main software （主控正式固件）` and `PAROL6 control board test code （主控测试固件）` is under [GPL-3.0](PAROL6%20control%20board%20main%20software%20%EF%BC%88%E4%B8%BB%E6%8E%A7%E6%AD%A3%E5%BC%8F%E5%9B%BA%E4%BB%B6%EF%BC%89/LICENSE), and the libraries in their `lib` folders keep their own licences. Until 4 November 2026 the whole repository was under GPL-3.0.
