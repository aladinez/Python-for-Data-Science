import sys
sys.path.append('/workspaces/Python-for-Data-Science/Python0')
from ex08.Loadin import ft_tqdm
from time import sleep
from tqdm import tqdm

for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()
for elem in tqdm(range(333)):
    sleep(0.005)