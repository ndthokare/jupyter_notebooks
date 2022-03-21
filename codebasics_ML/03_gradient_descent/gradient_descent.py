import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def gradient_descent(x,y,plt):
    m_curr = b_curr = 0
    iterations = 1000
    n = len(x)
    learning_rate = 0.08
    # line_x = np.linspace(-15, 15, 100)

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print("iteration {}, m {}, b {}, cost {}".format(i,m_curr,b_curr, cost))
        # line_y = m_curr * line_x + b_curr
        # plt.plot(line_x, line_y, linewidth=0.5)
    return [m_curr,b_curr]


x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

plt.scatter(x,y)
[slope, y_intercept] = gradient_descent(x,y,plt)
line_x = x
line_y = slope * line_x + y_intercept
plt.plot(line_x, line_y, linewidth=0.5)

plt.grid()
plt.legend(["slope: {:.2f}\ny-intercept: {:.2f}".format(round(slope,2),round(y_intercept,2))])
plt.show()