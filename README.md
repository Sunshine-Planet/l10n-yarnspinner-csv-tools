# 适用于 Yarn Spinner 对话系统下 Yarn Scripts 对话脚本的本地化工具

## 功能
1. 提取 Yarn Scripts 对话脚本文件中含有 line id 的行，并导出为 CSV 文件。
2. 将翻译后的 CSV 文件重新导入 Yarn Scripts 对话脚本文件。

## 运行环境
本工具使用 Python3 编写。

## 使用方法

本工具需要与 UnityEX 配合使用才能在游戏中看到实际修改效果。

### 1. 获取 Yarn Scripts 对话脚本文件

如果没有要本地化游戏的 Yarn Scripts 对话脚本文件，请使用 UnityEX 导出游戏的 Yarn Scripts 对话脚本文件。
然后将导出的 Unity_Assets_Files 文件复制至本项目目录下。

### 2. 导出 Yarn Scripts 对话脚本文件至 CSV 文件

执行 ExportToYarnTxt.bat ，导出的 CSV 文件储存在 output/vanillaCSV 下。

### 3. 导入翻译后 CSV 文件至 Yarn Scripts 对话脚本文件
下载项目至本地电脑，在本项目目录下创建名为 utf8 的空文件夹。将需要翻译后的 CSV 文件（不包含文件夹）复制到 utf8 文件夹下.
执行 ExportToYarnTxt.bat ，重新导入后的 Yarn Scripts 对话脚本文件储存在 output/Unity_Assets_Files 文件夹下。

