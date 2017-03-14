from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('Driverstation.pyw', base=base)
]

setup(name='MiniFRC Driver Station',
      version = '3.3',
      description = 'Driver Station',
      options = dict(build_exe = buildOptions),
      executables = executables)
