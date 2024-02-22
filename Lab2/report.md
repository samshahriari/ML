# Lab 2: Support Vector Machines (DD2421)
Sam Shahriari
2024-02-22

### Move the clusters around and change their sizes to make it easier or harder for the classifier to find a decent boundary. Pay attention to when the optimizer (minimize function) is not able to find a solution at all.
The linear SVM is bad at finding solutions when data points overlap in either the x1 or x2 plane. This can happen if standard deviation is too big or if one of the classes is split into two clusters. 

![](./plots/svmplot_kernel1_std0.40_samples20_False_sigma1_p2.png)

By removing one of the blue clusters

![](./plots/svmplot_kernel1_std0.40_samples20_True_sigma1_p2.png)

or lowering deviation

![](./plots/svmplot_kernel1_std0.20_samples20_True_sigma1_p2.png)

we instead get a positive result. The same effect would also occur if moving the clusters away from each other. Changing the size can improve accuracy but that more depends on randomness.

![](./plots/svmplot_kernel1_std0.40_samples5_True_sigma1_p2.png)


### Implement the two non-linear kernels. You should be able to classify very hard data sets with these.
We can now create an SVM for the example that did not work previously

![](./plots/svmplot_kernel2_std0.40_samples20_True_p2.png)
![](./plots/svmplot_kernel3_std0.40_samples20_True_sigma1.png)

### The non-linear kernels have parameters; explore how they influencethe decision boundary. Reason about this in terms of the bias-variance trade-off.
#### Polynomial kernel
By having an higher exponent we get an SVM that adapts more to the given dataset, leading to higher variance and lower bias. 

![](./plots/svmplot_kernel2_std0.40_samples20_True_p2.png)
![](./plots/svmplot_kernel2_std0.40_samples20_True_p3.png)
![](./plots/svmplot_kernel2_std0.40_samples20_True_p4.png)
![](./plots/svmplot_kernel2_std0.40_samples20_True_p5.png)
![](./plots/svmplot_kernel2_std0.40_samples20_True_p6.png)
![](./plots/svmplot_kernel2_std0.40_samples20_True_p7.png)
![](./plots/svmplot_kernel2_std0.40_samples20_True_p8.png)
![](./plots/svmplot_kernel2_std0.40_samples20_True_p9.png)
![](./plots/svmplot_kernel2_std0.40_samples20_True_p10.png)


#### RBF
With the radial kernel the results seems to be the opposite. Higher sigma leads to higher bias and lower variance.

![](./plots/svmplot_kernel3_std0.40_samples20_True_sigma0.40.png)
![](./plots/svmplot_kernel3_std0.40_samples20_True_sigma0.60.png)
![](./plots/svmplot_kernel3_std0.40_samples20_True_sigma0.80.png)
![](./plots/svmplot_kernel3_std0.40_samples20_True_sigma1.00.png)
![](./plots/svmplot_kernel3_std0.40_samples20_True_sigma2.00.png)
![](./plots/svmplot_kernel3_std0.40_samples20_True_sigma4.00.png)
![](./plots/svmplot_kernel3_std0.40_samples20_True_sigma5.00.png)

### Explore the role of the slack parameter C. What happens for very large/small values?
The slack parameter dictates how large of a penalty a point inside the margin will give. With a larger C the penalty will get bigger and thus the margin will be smaller.

![](./plots/svmplot_kernel1_std0.40_samples20_True_sigma1_p10_C1.00.png)
![](./plots/svmplot_kernel1_std0.40_samples20_True_sigma1_p10_C10.00.png)
![](./plots/svmplot_kernel1_std0.40_samples20_True_sigma1_p10_C100.00.png)

![](./plots/svmplot_kernel2_std0.40_samples20_True_p3_C1.00.png)
![](./plots/svmplot_kernel2_std0.40_samples20_True_p3_C10.00.png)

![](./plots/svmplot_kernel3_std0.40_samples20_True_sigma1.00_C 1.png)
![](./plots/svmplot_kernel3_std0.40_samples20_True_sigma1.00_C10.png)
![](./plots/svmplot_kernel3_std0.40_samples20_True_sigma1.00_C100.png)

### Imagine that you are given data that is not easily separable. When should you opt for more slack rather than going for a more complex model (kernel) and vice versa?
Here we have the bias variance trade off once again, also the type of data matters. If we for example have two classes where one class is in the middle of the other class,
a linear would not be able to properly classify the data despite allowing for much slack. If we on the other hand know that the dataset contains some noise, allowing slack would be able to mitigate that.