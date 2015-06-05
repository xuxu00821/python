# -*- mode: python -*-
a = Analysis(['today_QB.py'],
             pathex=['/home/xxux/python/spider'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='today_QB',
          debug=False,
          strip=None,
          upx=True,
          console=True )
