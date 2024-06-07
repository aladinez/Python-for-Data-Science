import sys
sys.path.append('/workspaces/Python-for-Data-Science/Python1')

from ex01.array2D import slice_me

family = [[2.10, 78.45],
 [4.15, 6.70],
 [2.10, 98.5],
 [1.88, 75.2]]
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))