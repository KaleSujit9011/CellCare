import scipy.io as sio
import pandas as pd


def load_mat(filepath):
    mat = sio.loadmat(filepath)
    return mat

def extract_discharge_cycles(mat):
    records = []
    battery = mat['B0005']
    cycles = battery[0, 0]
    cycle_data = cycles['cycle']

    for i in range(616):
        cycle = cycle_data[0, i]
        ctype = str(cycle['type'][0])

        if 'discharge' in ctype:
            data = cycle['data'][0, 0]
            capacity = float(data['Capacity'][0][0])
            temp = data['Temperature_measured'][0]
            voltage = data['Voltage_measured'][0]
            current = data['Current_measured'][0]

            records.append({
                'cycle_number': i,
                'capacity': capacity,
                'max_temp': temp.max(),
                'min_voltage': voltage.min(),
                'mean_current': current.mean()
            })

    df_cycles = pd.DataFrame(records)
    return df_cycles

if __name__ == "__main__":
    mat = load_mat("data/raw/B0005.mat")
    df = extract_discharge_cycles(mat)
    print(df.shape)
    print(df.head())