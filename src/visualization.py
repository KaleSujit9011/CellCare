import matplotlib.pyplot as plt
from data_loader import load_mat, extract_discharge_cycles

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
os.chdir(os.path.join(os.path.dirname(__file__), '..'))
os.makedirs('../outputs/plots', exist_ok=True)

mat = load_mat("data/raw/B0005.mat")
df = extract_discharge_cycles(mat)

plt.plot(df['cycle_number'],df['capacity'])
plt.xlabel('Cycle Number')
plt.ylabel('Capacity(Ah)')
plt.title('Battery B0005 Degradation Curve')
plt.axhline(y=1.4, color='r', linestyle='--', label='End of Life (1.4Ah)')
plt.legend()
plt.savefig('./outputs/plots/degradation_curve.png')
