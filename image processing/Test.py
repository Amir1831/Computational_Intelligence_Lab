import numpy as np


test = np.arange(0,120).reshape((5,4,3,2,1))



print(test)

test[0]

test[:,0]


test_2 = np.arange(0,6).reshape((1,2,3))
test_2 , test_2.shape

test_2.swapaxes(0,1)  ,test_2.swapaxes(0,1).shape


test_2.swapaxes(0,-1) , test_2.swapaxes(0,-1).shape

test_2.reshape(3,2,1) , test_2.reshape(3,2,1).shape
test_2.view((3,2,1))
test_2.transpose((-1,1,0))


test_3 = np.arange(0,8).reshape(2,2,2)
test_3

test_3[0,1]

import torch

sample = torch.tensor(np.random.randint(50,size=(1,3,5,5)),dtype=torch.float32)

sample_conv = torch.nn.Conv2d(3,6,(3,3))(sample)

torch.nn.MaxPool2d((3,3))(sample_conv).shape

sample_2 = torch.tensor(np.random.randint(50,size=(1,9)),dtype=torch.float32)
sample_2

torch.nn.MaxPool1d(2)(sample_2)
