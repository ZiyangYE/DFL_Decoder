#%% import

file_src = 'C:/Users/JackC/OneDrive/ICTA/PN/ChannelSsa Buffers'

import xml.etree.ElementTree as ET
import base64
import struct
import matplotlib.pyplot as plt
import numpy as np

#%% read xml file
tree = ET.parse(file_src)
root = tree.getroot()

# %% get datas of Trace_XShared & NoiseFloor_X

x_shared = []
Y_mea = []

for prop in root.findall('.//Prop'):
    name = prop.get('Name')
    if name == 'Trace_XShared':
        x_shared_value = prop.get('Value')
        x_shared.append(x_shared_value)
    elif name == 'Y':
        Y_value = prop.get('Value')
        Y_mea.append(Y_value)

# %% decode base64

x_shared_data = []
Y_data = []

for x_shared_value in x_shared:
    x_shared_data.append(base64.b64decode(x_shared_value))

for noise_floor_value in Y_mea:
    Y_data.append(base64.b64decode(noise_floor_value))

# %% X shared data is 8 bytes, Y is 4 bytes

x_shared_all = b"".join(x_shared_data)
Y_all = b"".join(Y_data)



x_shared_double = []
for i in range(0, len(x_shared_all), 8):
    uint64 = struct.unpack('<d', x_shared_all[i:i+8])[0]
    x_shared_double.append(uint64)

Y_single = []
for i in range(0, len(Y_all), 4):
    uint64 = struct.unpack('<f', Y_all[i:i+4])[0]
    Y_single.append(uint64)

# %% plot data

# log x axis

plt.plot(x_shared_double,Y_single)
plt.xscale('log')
plt.grid()

plt.show()

# %% save to output.npy & output.csv

result = np.array([x_shared_double, Y_single], dtype='double').T
np.save('output.npy', result)
np.savetxt('output.csv', result, delimiter=',')

# %%
