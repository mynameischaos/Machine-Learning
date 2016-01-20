# encoding=utf8
import tree
import treePlotter

if __name__ == '__main__':
    myDat, labels = tree.createDataSet()
    # print myDat
    # shannonEnt = tree.calcShannonEnt(myDat)
    # print shannonEnt
    # 熵越高，混合的数据越多，也就是种类越多
    # myDat[0][-1] = 'maybe'
    # print tree.calcShannonEnt(myDat)
    # print tree.splitDataSet(myDat, 1, 1)
    # print tree.chooseBestFeatureToSplit(myDat)
    myTree = tree.createTree(myDat, labels)
    print myTree
    print treePlotter.getNumLeafs(myTree)
    print treePlotter.getTreeDepth(myTree)
    # treePlotter.createPlot()