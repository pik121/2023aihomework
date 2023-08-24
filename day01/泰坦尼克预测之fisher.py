import pandas as pd
import numpy as np
import math
data = pd.read_csv('train.csv')
data = np.array(data[["Survived", "Pclass", "Sex", "Age"]])
data_deal = []
for i in range(0, len(data)):
    if 0 <= data[i][3] <= 1000:
        data_deal.append(data[i])
    else:
        continue

for i in range(0, len(data_deal)):
    if data_deal[i][2] == 'male':
        data_deal[i][2] = 1
    else:
        data_deal[i][2] = 2

    if 0 <= data_deal[i][3] <= 6:
        data_deal[i][3] = 1
    elif 7 <= data_deal[i][3] <= 12:
        data_deal[i][3] = 2
    elif 13 <= data_deal[i][3] <= 17:
        data_deal[i][3] = 3
    elif 18 <= data_deal[i][3] <= 45:
        data_deal[i][3] = 4
    elif 46 <= data_deal[i][3] <= 69:
        data_deal[i][3] = 5
    else:
        data_deal[i][3] = 6

data = pd.DataFrame(data_deal)
sample_size = int(len(data_deal) * 0.8)
sample_data = data.sample(n=sample_size)
rest_data = data.drop(sample_data.index)
sample_data = np.array(sample_data)
test_data = np.array(rest_data)

s = []
d = []
for i in range(0, len(sample_data)):
    if sample_data[i][0] == 1:
        s.append(np.delete(sample_data[i], 0))
    else:
        d.append(np.delete(sample_data[i], 0))
for i in range(0, len(s)):
    if s[i][1] == 'male':
        s[i][1] = 1
    else:
        s[i][1] = 2
for i in range(0, len(d)):
    if d[i][1] == 'female':
        d[i][1] = 1
    else:
        d[i][1] = 2
s_x = s_y = s_z = 0
d_x = d_y = d_z = 0
for i in range(0, len(s)):
    s_x += s[i][0]
    s_y += s[i][1]
    s_z += s[i][2]
for i in range(0, len(d)):
    d_x += d[i][0]
    d_y += d[i][1]
    d_z += d[i][2]
s_x /= len(s)
s_y /= len(s)
s_z /= len(s)
d_x /= len(d)
d_y /= len(d)
d_z /= len(d)
predict = []
for i in range(0, len(test_data)):
    distance_s = math.sqrt((test_data[i][0] - s_x) ** 2 + (test_data[i][1] - s_y) ** 2 + (test_data[i][2] - s_z) ** 2)
    distance_d = math.sqrt((test_data[i][0] - d_x) ** 2 + (test_data[i][1] - d_y) ** 2 + (test_data[i][2] - d_z) ** 2)
    if distance_s >= distance_d:
        predict.append(1)
    else:
        predict.append(0)
precision = 0
for i in range(0, len(predict)):
    precision += abs(predict[i] - test_data[i][0])
precision /= len(test_data)
print(precision)