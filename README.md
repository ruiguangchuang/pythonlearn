# pythonlearn
about python's refusing part
## python 中的numpy使用reshape和transpose的结果是不同的
## 使用reshape可能会将数组的原始顺序打乱。得到的结果可能只是shape一样，但内容不一样。
## 使用transpose则不会将数组的原始顺序打乱。得到的结果不仅shape一样，内容也一样。

### 比如 海洋数据 data=(4,100,12,24,72)表示4个特征，100年，12个月。大小为24*72.如果想获得(100,12,24,72,4)的数据，也就是将特征4放在最后一维。
### 使用data_reshape = data.reshape(100,12,24,72,4)
### 使用data_transpose = data.teanspose(1,2,3,4,0)
### 通过对比得到的数据
### data[0,0,0,:,:] == data_reshape[0,0,:,:,0]    false
### data[0,0,0,:,:] == data_transpose[0,0,:,:,0]  true


