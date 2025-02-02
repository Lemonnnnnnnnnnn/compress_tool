# 安全文件压缩工具

![Python版本](https://img.shields.io/badge/Python-3.8%2B-blue)
![许可证](https://img.shields.io/badge/License-MIT-green)

用于百度云盘存储敏感资源开发的文件批量压缩工具：
- 🔒 7Z文件密码保护（AES-256加密）
- 🔑 文件名哈希加密（MD5）
- 📁 自动生成解密元数据

## 主要功能

- 交互式CLI界面
- 双重压缩
- 文件名哈希加密
- 大文件自动分卷（>2GB）
- 详细的操作日志
- 支持Windows/Linux/macOS

## 快速开始

### 环境要求
- Python 3.8+
- pip包管理器
- 7-Zip命令行工具

### 安装步骤

```bash
# 克隆仓库
git clone https://github.com/yourusername/secure-compressor.git
cd secure-compressor

# 创建虚拟环境（推荐）
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 使用说明

```bash
# 运行程序
python src/main.py

# 按照提示输入：
# 1. 源文件夹路径
# 2. 输出文件夹路径 
# 3. 第一层压缩密码（需二次确认）
# 4. 第二层压缩密码（需二次确认）
# 5. 元数据文件名（可选）
```

### 打包可执行文件

```bash
# 使用PyInstaller打包
pyinstaller build.spec

# 生成的可执行文件位于 dist/ 目录
# Windows: compress_tool.exe
# Linux/macOS: compress_tool
```

## 项目结构

```
secure-compressor/
├── src/                 # 源代码
│   ├── main.py         # 主程序
│   ├── compression.py  # 压缩模块
│   ├── utils.py        # 工具函数
│   └── logger.py       # 日志模块
├── resources/          # 资源文件
│   ├── 7z.exe         # 7-Zip可执行文件
│   └── 7z.dll         # 7-Zip依赖库
├── requirements.txt    # 依赖清单
├── build.spec          # 打包配置
├── README.md          # 说明文档
└── .gitignore         # 版本控制忽略配置
```

## 功能特性

| 功能                | 描述                                                                 |
|---------------------|----------------------------------------------------------------------|
| 双重加密           | 两层7Z密码保护                                                      |
| 文件名加密         | MD5哈希算法                                                         |
| 大文件处理         | 自动2GB分卷                                                         |
| 元数据管理         | 自动生成包含解密信息的meta.json文件                                 |
| 错误处理           | 详细的错误日志记录和用户友好提示                                    |
| 跨平台支持         | 兼容Windows/Linux/macOS系统                                         |

## 安全警告

⚠️ 请务必妥善保存以下信息：
1. 生成的`meta.json`文件
2. 第一层压缩密码
3. 第二层压缩密码

丢失以上信息将**无法恢复**加密文件！

## 开发指南

1. 提交Issue报告问题
2. Fork仓库进行功能开发
3. 创建Pull Request时包含：
   - 功能描述
   - 测试结果
   - 相关文档更新

## 许可证

本项目采用 [MIT License](LICENSE) 开源协议
