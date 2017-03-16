from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = ["numpy","aiohttp","fuckit","websockets","setuptools","pip","discord","pydub","wheel"])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('Driverstation.pyw', base=base)
]

setup(name='MiniFRC Drivers Station',
      version = '3.4',
      description = 'Driver Station',
      options = dict(build_exe = buildOptions),
      executables = executables)
