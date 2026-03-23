
import numpy as np
import scipy.io as sio
from scipy.stats import skew, kurtosis

def compute_didt(current, time):
    didt = np.diff(current)/np.diff(time)
    return didt

def compute_load_features(current, time):
    didt = compute_didt(current,time)

    C1 = didt.mean()
    C2 = didt.std()
    C3 = skew(didt)
    C4 = kurtosis(didt)
    return C1,C2,C3,C4

if __name__ == "__main__":
    from data_loader import load_mat #only for testing
    mat = load_mat("data/raw/B0005.mat")
    battery = mat['B0005']
    cycles = battery[0,0]
    cycle_data = cycles['cycle']

    # 1st discharge
    for i in range(616):
        cycle = cycle_data[0,i]
        ctype = str(cycle['type'][0])
        if 'discharge' in ctype:
            data = cycle['data'][0,0]
            current = data['Current_measured'][0]
            time = data['Time'][0]
            break

    didt = compute_didt(current,time)
    print(f"didt(shape): {didt.shape}")
    print(f"didt max: {didt.max():.5f}")
    print(f"didt max: { didt.min():.5f}")

    C1,C2,C3,C4 = compute_load_features(current,time)
    print(f"C1(mean): {C1:.5f}")
    print(f"C2(std): {C2:.5f}")
    print(f"C3(skew): {C3:.5f}")
    print(f"C4(kurtosis): {C4:.5f}")


