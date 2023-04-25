# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\julie\\OneDrive\\Documents\\Python-F\\App Bureau\\9 App\\PyCrypto\\src\\main\\python\\main.py'],
             pathex=['C:\\Users\\julie\\OneDrive\\Documents\\Python-F\\App Bureau\\9 App\\PyCrypto\\target\\PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['C:\\Users\\julie\\anaconda3\\envs\\qtpyenv\\lib\\site-packages\\fbs\\freeze\\hooks'],
             runtime_hooks=['C:\\Users\\julie\\OneDrive\\Documents\\Python-F\\App Bureau\\9 App\\PyCrypto\\target\\PyInstaller\\fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Crypto 2S3',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , version='C:\\Users\\julie\\OneDrive\\Documents\\Python-F\\App Bureau\\9 App\\PyCrypto\\target\\PyInstaller\\version_info.py', icon='C:\\Users\\julie\\OneDrive\\Documents\\Python-F\\App Bureau\\9 App\\PyCrypto\\src\\main\\icons\\Icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='Crypto 2S3')
