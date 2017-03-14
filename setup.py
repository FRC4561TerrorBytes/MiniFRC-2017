import sys
from cx_Freeze import setup, Executable

if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "MiniFRC Driver Station",
        version = "3.3",
        description = "Driver Station",
        options = 
