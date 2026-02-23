import scipy.io as sio

def load_mat(filepath):
    mat = sio.loadmat(filepath)
    return mat

if __name__ == "__main__":
    mat = load_mat("data/raw/B0005.mat")
    print(mat.keys())
    battery = mat['B0005']
    print(type(battery))
    print(battery.shape)
    battery = mat['B0005']
    cycles = battery[0, 0]
    print(type(cycles))
    print(cycles.dtype.names)
    cycle_data = cycles['cycle']
    print(type(cycle_data))
    print(cycle_data.shape)
    first_cycle = cycle_data[0, 0]
    print(type(first_cycle))
    print(first_cycle.dtype.names)
    print(first_cycle['type'][0])
    for i in range(616):
        cycle = cycle_data[0, i]
        ctype = cycle['type'][0]
        if 'impedance' in str(ctype):
            print(i, ctype)
            break


