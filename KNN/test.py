import matplotlib.pyplot as plt
from numpy import *

import kNN


def paintDataSet():
    datingDataMat, datingLabels = kNN.file2matrix('datingTestSet.txt')

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 20.0*array(datingLabels), 20.0*array(datingLabels))
    plt.show()

if __name__ == '__main__':
    kNN.classifyPerson()


