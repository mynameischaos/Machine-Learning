# encoding=utf-8

import bayes

if __name__ == '__main__':
    # listOPosts, listClasses = bayes.loadDataSet()
    # myVocabList = bayes.createVocabList(listOPosts)
    # print myVocabList
    # print bayes.setOfWord2Vec(myVocabList, listOPosts[0])
    # print bayes.setOfWord2Vec(myVocabList, listOPosts[3])
    # trainMat = []
    # for postinDoc in listOPosts:
        # trainMat.append(bayes.setOfWord2Vec(myVocabList, postinDoc))
    # p0V, p1V, pAb = bayes.trainNB0(trainMat, listClasses)
    bayes.testingNB()
