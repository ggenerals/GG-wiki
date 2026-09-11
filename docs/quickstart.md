# 快速开始
这是一份面对零基础但是想参与开发的用户所编写的教程，不一定符合工程规范。

## Part1 准备工作

准备一个 github 账号，注册链接: <https://github.com/signup>

下载 git，ubuntu 下使用 `sudo apt update && sudo apt install git` 安装git。

在命令行中输入 `git clone https://github.com/ggenerals/GG-wiki.git` 将本仓库克隆到当前目录下的 GG-wiki 文件夹。

## Part2 编写

所有文档都在 `./GG-wiki/docs` 文件夹下。推荐使用 VScode 进行修改。

接下来将介绍如何使用 VScode 进行开发

用 VScode 打开文件夹进行编辑，在修改完对应的文件后，打开左侧边栏的源代码管理（默认从上往下第三个）或使用快捷键 `Ctrl+Shift+G`。

在更改下有一个提交按钮，再往下是你本次积累的修改。上面是你对本次修改的描述，输入描述（一般建议输入 `update`）。

提交之后点击 同步更改 按钮，如果出现提示，按照提示进行操作即可。

## Part3 更多
### 启动本地预览
请确保你的 python 版本不低于 3.8，推荐 3.11 或 3.12，这部分操作请自行上网搜索。

创建并激活虚拟环境（建议在 VScode 的终端中执行接下来的操作）：

1. 运行 `sudo apt install python3.12-venv` 安装虚拟环境。

2. 运行 `python3 -m venv .venv && source .venv/bin/activate` 激活虚拟环境。

3. 使用 `pip install -r requirements.txt` 安装依赖。

4. 使用 `mkdocs serve` 启动实时预览。