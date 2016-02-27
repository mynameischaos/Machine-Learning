# encoding=utf-8
import regression
from numpy import *

xArr, yArr = regression.loadDataSet("filename")
ws = regression.standRegres(xArr, yArr)

'''
# 绘图
xMat = mat(xArr)
yMat = mat(yArr)
yHat = xMat * ws
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(xMat[:, 1].flatten().A[0], yMat.T[:, 0].flatten().A[0])
xCopy = xMat.copy()
xCopy.sort(0)
yHat = xCopy * ws
ax.plot(xCopy[:, 1], yHat)
plt.show()
#相关系数:用来衡量预测值和真实值的匹配程序
corrcoef(yHat.T, yMat)
'''
# 得到数据集中所有点的估计
yHat = regression.lwlrTest(xArr, xArr, yArr, 0.003)
