from cx_Freeze import *
includefiles = ['cal.ico']
excludes = []
packages = []
base = None
if sys.platform == "win32":
    base = "Win32GUI"

shortcut_table = [
    ("DesktopShortcut", # Shortcut
    "DesktopFolder", # Directory_
    "My Calculator", # Name
    "TARGETDIR", # Component_
    "[TARGETDIR]\calculator.exe", # Target
    None, # Arguments
    None, # Description
    None, # Hotkey
    None, # Icon
    None, # IconIndex
    None, # ShowCmd
    "TARGETDIR", #WkDir
    )
]
msi_data = {"Shortcut": shortcut_table}

#change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {'data': msi_data}
setup(
    version = "0.1",
    description = "My Calculator",
    author = "Sanjay Dahal",
    name = "Calculator",
    options = {'build_exe': {'include_files': includefiles}, "bdist_msi":bdist_msi_options},
    executables = [
        Executable(
            script= "calculator.py",
            base= base,
            icon = 'cal.ico',
        )
    ]

)