import numpy as np

def calculate(list):
    array_as=np.asarray(list)
    arrnum=array_as.reshape(3,3)
    np.set_printoptions(precision=16, suppress=False)

    meanax0=arrnum.mean(axis=0)
    meanax1=arrnum.mean(axis=1)
    meanax=arrnum.mean()

    varax0=arrnum.var(axis=0)
    varax1=arrnum.var(axis=1)
    varax=arrnum.var()

    stdax0=arrnum.std(axis=0)
    stdax1=arrnum.std(axis=1,dtype=np.double)
    stdax=arrnum.std()
    
    minax0=arrnum.min(axis=0)
    minax1=arrnum.min(axis=1)
    minax=arrnum.min()

    maxax0=arrnum.max(axis=0)
    maxax1=arrnum.max(axis=1)
    maxax=arrnum.max()

    sumax0=arrnum.sum(axis=0)
    sumax1=arrnum.sum(axis=1)
    sumax=arrnum.sum()    
    calculations =f" {{ \n'mean': [{meanax0}, {meanax1}, {meanax}],\n'variance': [{varax0}, {varax1}, {varax}],\n'standard deviation': [{stdax0}, {stdax1}, {stdax}],\n 'max': [{maxax0}, {maxax1}, {maxax}],\n'min': [{minax0}, {minax1}, {minax}],\n'sum': [{sumax0}, {sumax1},{sumax}] \n}}"
    return calculations