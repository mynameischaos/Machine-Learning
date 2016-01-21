import tree

fr = open('lenses.txt')
lenses = [inst.strip().split('  ') for inst in fr.readlines()]
print lenses
lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
lensesTree = tree.createTree(lenses, lensesLabels)
print lensesTree