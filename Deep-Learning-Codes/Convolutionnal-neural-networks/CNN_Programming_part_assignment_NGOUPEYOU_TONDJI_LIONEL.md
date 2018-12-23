

```python
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
```


```python
class CNN(nn.Module):
    
    def __init__(self, input_size, n_feature, output_size, conv_kernel_size, pooling_kernel_size, stride_size, zero_padding, max_pooling):
        super(CNN, self).__init__()
        self.n_feature = n_feature
        
        if zero_padding :
            self.conv1 = nn.Conv2d(in_channels=1, out_channels=16, kernel_size=int(conv_kernel_size), stride = stride_size, padding = (int(conv_kernel_size)-1)//2)
            self.conv2 = nn.Conv2d(16, 32, kernel_size=int(conv_kernel_size), stride = stride_size, padding = (int(conv_kernel_size)-1)//2)
            self.sp = int(np.sqrt(input_size)/(pooling_kernel_size*pooling_kernel_size))
            self.fc1 = nn.Linear(32*self.sp*self.sp, 10)
        else:
            self.conv1 = nn.Conv2d(in_channels=1, out_channels=16, kernel_size=int(conv_kernel_size), stride = stride_size)
            self.conv2 = nn.Conv2d(16, 32, kernel_size=int(conv_kernel_size), stride = stride_size)
            self.s = int((np.sqrt(input_size) + pooling_kernel_size * (stride_size**2 - stride_size*conv_kernel_size) + stride_size - conv_kernel_size)/(stride_size*pooling_kernel_size)**2 )
            self.fc1 = nn.Linear(32*self.s*self.s, 10)
        
        
    def forward(self, x, verbose=False):
        x = self.conv1(x)
        if max_pooling :
            x = F.max_pool2d(x, kernel_size=int(pooling_kernel_size))
        else:
            x = F.avg_pool2d(x, kernel_size=int(pooling_kernel_size))
        x = self.conv2(x)
        if max_pooling : 
            x = F.max_pool2d(x, kernel_size=int(pooling_kernel_size))
        else:
            x = F.avg_pool2d(x, kernel_size=int(pooling_kernel_size))
            
        self.zero_padding =zero_padding
        if self.zero_padding :
            x = x.view(-1, 32*self.sp*self.sp)
        else:
            x =x.view(-1, 32*self.s*self.s)
        x = self.fc1(x)
        x = F.softmax(x, dim=1)
        return x
```

## 4.2 Zero Padding Model Tensors


```python
conv_kernel_size = 5
pooling_kernel_size = 2
stride_size = 1
zero_padding =True
max_pooling =True



input_size  = 28*28   # images are 28x28 pixels
output_size = 10      # there are 10 classes
n_feature = 6 # number of feature maps

kwargs = {'input_size': 28*28, 'n_feature': 6,'output_size':10, 'conv_kernel_size': 5, 'pooling_kernel_size': 2, 'stride_size': 1, 'zero_padding':True, 'max_pooling': True}
```


```python
model = CNN(**kwargs)
```


```python
print(model.conv1)
```

    Conv2d(1, 16, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2))



```python
print(model.conv2)
```

    Conv2d(16, 32, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2))



```python
for k in model.parameters():
    print(k.size())
```

    torch.Size([16, 1, 5, 5])
    torch.Size([16])
    torch.Size([32, 16, 5, 5])
    torch.Size([32])
    torch.Size([10, 1568])
    torch.Size([10])



```python
param_count = 0
for param in model.parameters():
  print(param.data.shape)
  param_count += np.product(param.data.shape)
print(param_count)
```

    torch.Size([16, 1, 5, 5])
    torch.Size([16])
    torch.Size([32, 16, 5, 5])
    torch.Size([32])
    torch.Size([10, 1568])
    torch.Size([10])
    28938



```python
print(model.parameters)
```

    <bound method Module.parameters of CNN(
      (conv1): Conv2d(1, 16, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2))
      (conv2): Conv2d(16, 32, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2))
      (fc1): Linear(in_features=1568, out_features=10, bias=True)
    )>



```python
print(dir(model))
```

## 4.3 Valid Padding Model Tensors


```python
conv_kernel_size = 5
pooling_kernel_size = 2
stride_size = 1
zero_padding = False
max_pooling = True


input_size  = 28*28   # images are 28x28 pixels
output_size = 10      # there are 10 classes
n_feature = 6 # number of feature maps

kwargs = {'input_size': 28*28, 'n_feature': 6,'output_size':10, 'conv_kernel_size': 5, 'pooling_kernel_size': 2, 'stride_size': 1, 'zero_padding':False, 'max_pooling': True}
```


```python
model1 = CNN(**kwargs)
```


```python
print(model1.parameters)
```

    <bound method Module.parameters of CNN(
      (conv1): Conv2d(1, 16, kernel_size=(5, 5), stride=(1, 1))
      (conv2): Conv2d(16, 32, kernel_size=(5, 5), stride=(1, 1))
      (fc1): Linear(in_features=512, out_features=10, bias=True)
    )>



```python
for k in model1.parameters():
    print(k.size())
```

    torch.Size([16, 1, 5, 5])
    torch.Size([16])
    torch.Size([32, 16, 5, 5])
    torch.Size([32])
    torch.Size([10, 512])
    torch.Size([10])



```python
param_count = 0
for param in model1.parameters():
  print(param.data.shape)
  param_count += np.product(param.data.shape)
print(param_count)
```

    torch.Size([16, 1, 5, 5])
    torch.Size([16])
    torch.Size([32, 16, 5, 5])
    torch.Size([32])
    torch.Size([10, 512])
    torch.Size([10])
    18378



```python
print(model1.conv1)
```

    Conv2d(1, 16, kernel_size=(5, 5), stride=(1, 1))



```python
print(model1.conv2)
```

    Conv2d(16, 32, kernel_size=(5, 5), stride=(1, 1))

