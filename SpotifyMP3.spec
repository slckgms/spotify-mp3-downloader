# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['spotify_gui.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['yt_dlp', 'requests', 'tkinter', 'PIL', 'PIL.Image', 'PIL.ImageTk'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='SpotifyMP3',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['SpotifyMP3.ico'],
)
```

**`.gitignore` içeriği** (yeni dosya oluştur):
```
dist/
build/
*.spec
installer.nsi
ffmpeg_bin/
*.exe
*.pkg
*.zip
build_log.txt
*.log
__pycache__/
*.pyc
*.pyo
*.pyd
.vscode/
.idea/
.DS_Store
Thumbs.db
desktop.ini
github-recovery-codes.txt
*.env
secrets.*
```

**`requirements.txt` içeriği** (yeni dosya oluştur):
```
yt-dlp>=2024.1.0
requests>=2.31.0
Pillow>=10.0.0
pyinstaller>=6.0.0
