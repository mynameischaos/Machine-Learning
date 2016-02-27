# encoding=utf-8

import adaboost
from numpy import  *

datMat, classLabels = adaboost.loadSimData()
#print datMat
#print classLabels
D = mat(ones((5, 1)) / 5)
bestStump, minError, bestClasEst = adaboost.buildStump(datMat, classLabels, D)
#print bestStump
#print minError
#print bestClasEst
classifierArray = adaboost.adaBoostTrainDS(datMat, classLabels, 30)
adaboost.adaClassify([0, 0], classifierArray)
