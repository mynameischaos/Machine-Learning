import operator

from numpy import *


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    #print 'tile:', tile(inX, (dataSetSize, 1))
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    #print 'diffMat:', diffMat
    sqDiffMat = diffMat ** 2
    #print 'sqDiffMat:', sqDiffMat
    sqDistances = sqDiffMat.sum(axis=1)
    #print 'sqDistances:', sqDistances
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    #print 'sortedDistIndicies', sortedDistIndicies

    classCount = {}
    for i in range(k):
        votellabel = labels[sortedDistIndicies[i]]
        #print votellabel
        classCount[votellabel] = classCount.get(votellabel, 0) + 1
        #print classCount[votellabel]
    sortedClassCount = sorted(classCount.iteritems(),
                              key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def file2matrix(filename):
    fr = open(filename)
    arrayOfLines = fr.readlines()
    numberOfLines = len(arrayOfLines)
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayOfLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1

    return returnMat, classLabelVector

def autoNorm(dataSet):
    minValue = dataSet.min(0)
    maxValue = dataSet.max(0)
    ranges = maxValue - minValue
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minValue, (m, 1))
    normDataSet = normDataSet/tile(ranges, (m, 1))

    return normDataSet, ranges, minValue

def classifyPerson():
    resultList = ['not at all', 'in small doses', 'in large doses']
    percentTats = float(raw_input(\
                  "percentage of time spent playing video games?"))
    ffMiles = float(raw_input("frequent flier miles earned per year?"))
    iceCream = float(raw_input("liters of ice cream consumed per year?"))
    datingDataMat, datingLables = file2matrix('datingTestSet.txt')
    normMat, ranges, minValue = autoNorm(datingDataMat)
    inArr = array([ffMiles, percentTats, iceCream])
    classifierResult = classify0((inArr - \
                                  minValue) / ranges, normMat, datingLables, 3)
    print 'You will probably like this person: ', \
        resultList[classifierResult - 1]


