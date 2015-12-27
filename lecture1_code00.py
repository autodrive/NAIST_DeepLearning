"""
Deep Learning and Neural Networks

Advanced Research Seminar I/III
Graduate School of Information Science
Nara Institute of Science and Technology
January 2014
Instructor:
Kevin Duh, IS Building Room A-705
Office hours: after class, or appointment by email (x@is.naist.jp where x=kevinduh)

http://cl.naist.jp/~kevinduh/a/deep2014/
"""

import numpy as np
import numpy.random as nr
from sklearn.datasets.samples_generator import make_blobs
import pylab

def linear_model(w, x):
    """
    y = wT x
    :param x: data to fit. [1 x (len(x))]
    :param w: weight to fit the data. [1 x (len(x) + 1)]
    :return:
    """
    w_array = np.array(w)
    x_array = np.concatenate((x, [1.0]))
    return np.dot(w_array, x_array)


def sigmoid_z(z):
    return 1.0 / (1.0 + np.exp(-z))


def sigmoid_x(w, x):
    """
    :param x: data to fit. [1 x (len(x))]
    :param w: weight to fit the data. [1 x (len(x) + 1)]
    :return:
    """
    return sigmoid_z(linear_model(w, x))


def d_sigmoid_dz(z):
    return sigmoid_z(z) * (1-sigmoid_z(z))


def d_sigmoid_dx(x, w):
    return d_sigmoid_dz(linear_model(x, w))


def generate_training_data(n_samples=50):
    """
    random points
    :param n_samples:
    :return:
    """
    X, Y = make_blobs(n_samples=n_samples, centers=2, random_state=0, cluster_std=0.60)
    return X, Y


def contour_sigmoid_2d(w, X, Y):
    """
    :param w: weight as training result [1 x 3]
    :param X: training data, [n x 2]
    :param Y: training label, [n x 1]
    :return:
    """
    # plot the line, the points, and the nearest vectors to the plane
    xx = np.linspace(-1, 5, 10)
    yy = np.linspace(-1, 5, 10)

    X1, X2 = np.meshgrid(xx, yy)
    Z = np.empty(X1.shape)
    for (i, j), x1 in np.ndenumerate(X1):
        x2 = X2[i, j]
        Z[i, j] = sigmoid_x(w, [x1, x2])
    levels = np.arange(0.0, 1.0 + 0.05, 0.1)
    pylab.contour(X1, X2, Z, levels)
    pylab.scatter(X[:, 0], X[:, 1], c=Y, cmap=pylab.cm.Paired)
    pylab.axis('tight')
    pylab.show()


# def stochastic_gradient_descent(w0, x_array, y_array, gamma, heuristic=True, b_plot=False):
#     """
#     try to find w minimizing the loss function through sample by sample iteration
#     :param w0: initial weight. list. [(len(x) + 1) x 1]
#     :param x_array: [n_sample x len(x)]
#     :param y_array: [n_sample x 1]
#     :param gamma: learning rate, scala, 0< gamma
#     :param heuristic: heuristic learning rate, bool, If True, gamma(k) = gamma/k
#     :return:
#     """
#     if x_array.shape[1] + 1 > len(w0):
#         w0 += [1.0] * (x_array.shape[1] + 1 - len(w0))
#     elif x_array.shape[1] + 1 < len(w0):
#         w0 = w0[:x_array.shape[1] + 1]
#
#     w = (w0)
#     counter = 1
#     w_list = [w0]
#     for x, y in zip(x_array, y_array,):
#         b = w[-1]
#         error = sigmoid_x(x, w[:-1], b) - y
#         factor = ((-gamma)*error*d_sigmoid_dx(x, w[:-1], b))
#         w[:-1] += factor * x
#         w[-1] = factor * b
#         w_list.append(w)
#
#         counter += 1
#         if heuristic:
#             gamma *= (1.0/counter)
#     return w_list


def main():
    n = 4
    w = [1] * (n + 1)
    x = 2 * nr.random(n) - 1
    result = linear_model(w, x)
    print(result)

    w_2d = [1, 1, 1]
    X, Y = generate_training_data()
    contour_sigmoid_2d(w_2d, X, Y)


if __name__ == '__main__':
    main()
