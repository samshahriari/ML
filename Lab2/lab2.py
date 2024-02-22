import numpy as np, random, math
from scipy.optimize import minimize
import matplotlib.pyplot as plt

np.random.seed(100)

def linear_kernel(x, y): #funkar
    return np.dot(x, y)

def polynomial_kernel(x,y):
    xT = np.transpose(x)
    return (np.dot(xT, y) + 1 )**degree

def RBF_kernel(x,y):
    return math.exp(-np.linalg.norm(np.subtract(x,y))**2/(2*(sigma**2)))

def kernel(x, y):
    if kernel_choice == 1:
        return linear_kernel(x,y)
    if kernel_choice == 2:
        return polynomial_kernel(x, y)
    return RBF_kernel(x, y)

def calculate_P():
    for i in range(N):
        for j in range(N):
            P[i][j] = targets[i] * targets[j] * kernel(inputs[i], inputs[j])


def objective(alpha):
    sumL = 0
    for i in range(N):
        for j in range(N):
            sumL += alpha[i] * alpha[j] * P[i][j]
    return 0.5 * sumL - np.sum(alpha)

def zerofun(alpha):
    return np.dot(alpha, targets)

C = 1000
kernel_choice = 3
degree = 3
sigma = 1

Ax = 1.5
Ay = 0.5
Bx = 0
By = -0.5
samples = 20
std = 0.4
oneClusterA = False

if oneClusterA:
    classA = np.random.randn(samples, 2) * std + [Ax, Ay]
else:
    classA = np.concatenate((np.random.randn(math.floor(samples/2), 2) * std + [Ax, Ay],  np.random.randn(math.ceil(samples/2), 2) * std + [-Ax, Ay]))
classB = np.random.randn(samples, 2) * std + [Bx, By]




inputs = np.concatenate((classA, classB))
targets = np.concatenate((np.ones(classA.shape[0]), -np.ones(classB.shape[0])))
N = inputs.shape[0]  # Number of rows (samples)
permute = list(range(N))
np.random.shuffle(permute)
inputs = inputs[permute, :]
targets = targets[permute]



# Show the plot on the screen

P = np.zeros((N, N))
calculate_P()

ret = minimize(objective, np.zeros(N), bounds=[(0, C) for x in range(N)], constraints={'type': 'eq', 'fun': zerofun})
print("found solution", ret["success"])
alpha = ret['x']
non_zero_alphas = [(i, v, inputs[i], targets[i]) for i, v in enumerate(alpha) if v > 10e-5]
b = -non_zero_alphas[0][3]
for i in range(N):
    b+= alpha[i]*targets[i]*kernel(non_zero_alphas[0][2], inputs[i])

def ind(s):
    sum = -b
    for tup in non_zero_alphas:
        sum += tup[1]*tup[3]*kernel(s, tup[2])
    return sum


x_min = min([x[0] for x in inputs]) - 5*std
x_max = max([x[0] for x in inputs]) +  5*std
y_min = min([x[1] for x in inputs]) - 5*std
y_max = max([x[1] for x in inputs]) + 5*std
xgrid = np.linspace(x_min, x_max)
ygrid = np.linspace(y_min, y_max)



grid = np.array([[ind((x, y)) for x in xgrid] for y in ygrid])




plt.plot([p[0] for p in classA], [p[1] for p in classA], 'b.')
plt.plot([p[0] for p in classB], [p[1] for p in classB], 'r.')
if ret["success"]:
    plt.plot([p[2][0] for p in non_zero_alphas], [p[2][1] for p in non_zero_alphas], 'g*')



plt.axis('equal')
plt.grid()
plt.contour(xgrid, ygrid, grid, levels=[-1.0, 0.0, 1.0], colors=['red', 'black', 'blue'], linewidths=[1, 3, 1])
if kernel_choice == 1:
    plt.suptitle("samples = %d, std = %.2f, found solution = %r\n kernel = 1, C = %.2f" % (
    samples, std, ret["success"], C))
    plt.savefig('plots/svmplot_kernel1_std%.2f_samples%d_%r_sigma%d_p%d_C%.2f.png' % (std, samples, ret["success"], sigma, degree, C))
elif kernel_choice ==2:
    plt.suptitle("samples = %d, std = %.2f, found solution = %r\n kernel = 2, p = %d, C = %.2f" % (
    samples, std, ret["success"], degree, C))
    plt.savefig('plots/svmplot_kernel2_std%.2f_samples%d_%r_p%d_C%.2f.png' % (std, samples, ret["success"], degree, C))
else:
    plt.suptitle("samples = %d, std = %.2f, found solution = %r\n kernel = 3, sigma = %.2f, C = %.2f" % (
    samples, std, ret["success"], sigma, C))
    plt.savefig('plots/svmplot_kernel3_std%.2f_samples%d_%r_sigma%.2f_C%2.f.png' % (std, samples, ret["success"], sigma, C))


plt.show()
