import monkdata as m
import dtree as d
import drawtree_qt5 as dt
import random
import matplotlib.pyplot as plt



def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]


t1_2 = d.buildTree(m.monk1, m.attributes, 2)
t1 = d.buildTree(m.monk1, m.attributes)
t2 = d.buildTree(m.monk2, m.attributes)
t3 = d.buildTree(m.monk3, m.attributes)
# dt.drawTree(t1_2)


def prune_result(train_dataset, final_validation_dataset, fraction):
    new_train, new_val = partition(train_dataset, fraction)
    best_pruned_tree = d.buildTree(new_train, m.attributes)
    best = d.check(best_pruned_tree, new_val)
    found_better = True
    while found_better:
        found_better = False
        possiblePrunedTrees = d.allPruned(best_pruned_tree)
        for prunedTree in possiblePrunedTrees:
            if d.check(prunedTree, new_val) > best:
                best_pruned_tree = prunedTree
                best = d.check(prunedTree, new_val)
                found_better = True

    return 1 - d.check(best_pruned_tree, final_validation_dataset)

import numpy as np

# Example data

fractions = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
means = []  # Mean values for each category
std_devs = []  # Standard deviations for each category
for fraction in fractions:
    l = list()
    for i in range(1000):
        l.append(prune_result(m.monk3, m.monk3test, fraction))
    means.append(np.mean(l))
    std_devs.append((np.std(l)))


# Plotting the dot plot with error bars
plt.errorbar(fractions, means, yerr=std_devs, fmt='o', color='blue', ecolor='red', capsize=5, capthick=2)

# Adding labels and title
plt.xlabel('Fraction of test size used')
plt.ylabel('Classification Error')
plt.title('Classification mean error for best pruned tree Monk-3 (1000 runs)')
plt.grid(True, linestyle='--', alpha=0.7)

plt.legend(['mean error with std marked'])

# Show the plot
plt.show()
