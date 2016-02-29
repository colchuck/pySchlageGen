# pySchlageGen
Pythonic GUI and CLI Schlage master key system generation. The GUI is written in Qt, and requires PyQt5 and Python3 to be installed, where the CLI requires only the Python3 interpreter to be installed. 

Essentially:
Input: A master key and the number of tenant keys.
Output: All found avaliable tenant keys, within the requested number and spaced by the requested increment.
This program is in its early stages, so having submaster keys is planned but not currently supported.

GUI Usage: python3 gui.py
The GUI allows users to generate, save, and load master key systems as well as store and modify relievant information about the system. Printing the system is now supported but only includes basic information. Options and customized printing are planned as well. 

CLI Usage: python3 cli.py
CLI will then prompt for needed information. Flags are also planned to be available as well.
System saving is not supported by the CLI; This is a feature that will be included in future releases. 

