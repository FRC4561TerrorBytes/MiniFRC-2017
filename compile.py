import cx_Freeze

executables = [cx_Freeze.Executable("Driverstation.pyw")]

cx_Freeze.setup(
    name = "MiniFRC 2017",
    executables = executables
)
