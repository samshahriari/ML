# Lab 1: Decision Trees (DD2421)
Sam Shahriari
2024-01-31

### Assignment 0
All three datasets has factors that make them hard to predict, but I think that MONK-1 is probably the hardest since it 
has few training points together with a complex condition that involves to attributes to be the same.



### Assignment 1

| Dataset | Entropy |
|---------|---------|
| Monk-1  | 1.0     |
| Monk-2  | 0.9571  |
| Monk-3  | 0.9998  |





### Assignment 2
For a uniform dataset, every outcome has an equal likely probability to be the outcome this means that we are really 
unsure what the result will be and thus having high entropy. An example of this is flipping a fair coin. Each side has a 
50% probability so guessing is hard.

If we instead have a biased coin where heads is much more likely to happen we can predict the outcome easier and thus 
giving a lower entropy. 


### Assignment 3


| Dataset | a1      | a2      | a3      | a4      | a5      | a6      |
|---------|---------|---------|---------|---------|---------|---------|
| Monk-1  | 0.07527 | 0.00584 | 0.00471 | 0.02631 | 0.28703 | 0.00076 |
| Monk-2  | 0.00376 | 0.00246 | 0.00106 | 0.01566 | 0.01728 | 0.00625 |
| Monk-3  | 0.00712 | 0.29374 | 0.00083 | 0.00289 | 0.25591 | 0.00708 |


For 1 and 2 we should split on a5 and for 3 a2.

### Assignment 4
To maximize the information gain we want to choose an attribute that we are likely to know the classification of. This 
means that the entropy of each subset should be small.

We can use information gain as a heuristic because that with a high information gain, we know that the split will lead to 
a purer node with less (or 0) entropy and when this is the case we can classify that data with very good precision.

### Assignment 5

![Monk-1 tree](/Users/sam/ML/Lab1/5_tree.png)

| Dataset | E_train | E_Test  |
|---------|---------|---------|
| Monk-1  | 0.0     | 0.1713  |
| Monk-2  | 0.0     | 0.30787 |
| Monk-3  | 0.0     | 0.05556 |

I was wrong about my prediction that M1 was the hardest, instead it seems that M2 was the hardest. A perfect tree was 
made for the training set. This means that the trees were probably over fit to some extent.

### Assignment 6

When building a decision tree, we might overfit the model to patterns that just exists in the training data but not in 
real world. The idea of pruning is to cut of branches that would lead to this in order to get a model with lower variance.

A problem with pruning is that we might simplify the model too much which raises the bias. 

### Assignment 7


![](/Users/sam/ML/Lab1/7_Monk1.png)


![](/Users/sam/ML/Lab1/7_Monk3.png)
