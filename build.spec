# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules
import platform

block_cipher = None

# 根据平台决定是否包含7z相关文件
system = platform.system().lower()
if system == 'windows':
    binaries = [
        ('resources/7z.exe', 'resources'),
        ('resources/7z.dll', 'resources'),
    ]
else:
    binaries = []

a = Analysis(
    ['./src/main.py'],
    pathex=[],
    binaries=binaries,
    datas=[],
    hiddenimports=['src', 'src.logger', 'src.utils', 'src.compression'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='compress_tool',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
) 