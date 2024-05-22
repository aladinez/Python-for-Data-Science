import sys
sys.path.append('/workspaces/Python-for-Data-Science/Python0')

from ex06.ft_filter import ft_filter


original = filter.__doc__
copy = ft_filter.__doc__
print(copy) # output: docstring
print(original == copy) # output: True