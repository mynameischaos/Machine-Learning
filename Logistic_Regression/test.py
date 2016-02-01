
import logRegres
from numpy import *

if __name__ == '__main__':
    dataArr, labelMat = logRegres.loadDataSet()
    weights = logRegres.gradAscent(dataArr, labelMat)
    logRegres.plotBestFit(weights.getA())
    weights1 = logRegres.stocGradAscent0(array(dataArr), labelMat)
    logRegres.plotBestFit(weights1)
    weights2 = logRegres.stocGradAscent1(array(dataArr), labelMat)
    logRegres.plotBestFit(weights2)
