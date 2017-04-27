# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py', 'design.py'],
             pathex=['/media/sf_SharedVM/Documents/2016-2017/Spring/Cyber Security/CyberSecurityApplication/CyberSecurityApp'],
             binaries=[],
             datas=[],
             hiddenimports=['os', 'sys'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='TYRION',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='TYRION')
