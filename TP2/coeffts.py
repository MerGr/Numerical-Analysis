import numpy as np

def coeffts(xData,yData):
    m=len(xData)
    a=yData.copy()
    for k in range(1,m):
        a[k]=(a[k]-a[k-1])/(xData[k]-xData[k-1])
    return a

xData=[-5,2,0,3,4]
yData=[2,0,3,8,7,6]
print(coeffts(xData,yData))