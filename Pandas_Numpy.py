"""from  pandas import read_csv 

path="D:\K1023ML\Iris.csv"
data=read_csv(path)
print(data.shape)#ROWS AND COLUMN
print(data[:-1])
"""

from numpy import loadtxt,genfromtxt
path="D:\K1023ML\Iris.csv"
datapath=open(path,'r').readlines()
data=genfromtxt(datapath,delimiter=" ,")
print(data.shape)
