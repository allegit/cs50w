"""currentPath.py

This program prints the current path
"""

import os

thisdir = os.path.dirname(__file__)
print('Current Directory: ' + os.path.abspath(os.path.join(thisdir, '.')))
