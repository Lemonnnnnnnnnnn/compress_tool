# 安全文件压缩工具

![Python版本](https://img.shields.io/badge/Python-3.8%2B-blue)
![许可证](https://img.shields.io/badge/License-MIT-green)

一个具备加密功能的文件压缩工具，提供双重保护：
- 🔒 ZIP文件密码保护（AES-256加密）
- 🔑 文件名加密（AES-CBC模式）
- 📁 自动生成解密元数据

## 主要功能

- 交互式CLI界面
- 密码二次验证机制
- 随机密钥生成与保存
- 压缩日志记录
- 支持Windows/Linux/macOS

## 快速开始

### 环境要求
- Python 3.8+
- pip包管理器

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
python main.py

# 按照提示输入：
# 1. 源文件夹路径
# 2. 输出文件夹路径 
# 3. 压缩密码（需二次确认）
# 4. 加密配置（推荐使用随机密钥）
```

### 打包可执行文件

```bash
# 使用PyInstaller打包
pyinstaller --onefile main.py

# 生成的可执行文件位于 dist/ 目录
# Windows: main.exe
# Linux/macOS: main
```

## 项目结构

```
secure-compressor/
├── src/                 # 源代码
│   └── main.py         
├── requirements.txt    # 依赖清单
├── build.spec          # 打包配置
├── README.md           # 说明文档
└── .gitignore          # 版本控制忽略配置
```

## 功能特性

| 功能                | 描述                                                                 |
|---------------------|----------------------------------------------------------------------|
| 双重加密          | ZIP密码保护 + 文件名AES加密                                         |
| 随机密钥生成      | 支持16/24/32字节密钥长度                                            |
| 元数据管理        | 自动生成包含解密信息的meta.json文件                                 |
| 错误处理          | 详细的错误日志记录和用户友好提示                                    |
| 跨平台支持        | 兼容Windows/Linux/macOS系统                                         |

## 安全警告

⚠️ 请务必妥善保存以下信息：
1. 生成的`meta.json`文件
2. 随机生成的AES密钥和IV
3. 压缩文件密码

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
