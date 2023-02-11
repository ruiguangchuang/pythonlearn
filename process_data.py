import xarray as xa
import numpy as np

## 命名格式： test_00001_07_06.npy  =  (12,24,72,4)
## label: test_00001_07_06.npy    =  (24,)
##

## godas_train: E:\tianchi\case1\AI-competition-main\tianchi-enso-prediction\data_48\GODAS_train_48.nc
## 4*(33,48,24,72)  ->  (12,24,72,4)

path1 = "E:\\tianchi\case1\AI-competition-main\\tianchi-enso-prediction\data_48\GODAS_train_48.nc"
path2 = '../data_48/GODAS_label_48.nc'
data = xa.open_dataset(path1, decode_times=False)
data = np.array([np.array(data[i]) for i in ['sst', 't300', 'ua', 'va']])
print(data.shape)  ## (4, 33, 48, 24, 72)

label = xa.open_dataset(path2, decode_times=False)
label = np.array(label['nino'])
print(label.shape)  ## (33,48)

samples = []
samples_label = []
for i in range(33):
    for j in range(12):
        data_x = data[:, i, j:j+12, :, :]
        label_x = label[i, j+12:j+12+24]
        samples.append(data_x)
        samples_label.append(label_x)

samples = np.array(samples)
print(samples.shape)  ## (396, 4, 12, 24, 72)
print((samples[0, 0, :12, :, :] == data[0, 0, :12,:, :]).all())

# samples=(396,4,12,24,72)
# samples1=(396,12,24,72,4)
samples1 = samples.reshape(-1, 12,24,72,4)
samples2 = samples.transpose(0,2,3,4,1)
samples = np.around(samples, 2)
samples1 = np.around(samples1, 2)
samples2 = np.around(samples2, 2)
print((samples[0, 0, 0, :, :] == samples1[0,0,:,:, 0]).all())


import csv
with open('samples.csv', mode='a', newline='')as f:
    writer = csv.writer(f)
    writer.writerows(samples[0, 0, 0, :, :])

with open('samples_reshape.csv', mode='a', newline='')as f:
    writer = csv.writer(f)
    writer.writerows(samples1[0,0,:,:, 0])

with open('samples_transpose.csv', mode='a', newline='')as f:
    writer = csv.writer(f)
    writer.writerows(samples2[0,0,:,:, 0])





