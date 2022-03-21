import math

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model


def gradient_descent(x,y,plt):
    m_curr = b_curr = 0
    iterations = 1000
    n = len(x)
    learning_rate = 0.0002
    # line_x = np.linspace(-15, 15, 100)
    i = 0
    stop = False
    cost_rising = False
    while not stop:
        cost_close = False
        if cost_rising:
            learning_rate /= 10
        cost_rising = False
        while (not cost_close) and (not cost_rising):
            i = i+1
            y_predicted = m_curr * x + b_curr
            cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
            md = -(2/n)*sum(x*(y-y_predicted))
            bd = -(2/n)*sum(y-y_predicted)
            m_curr = m_curr - learning_rate * md
            b_curr = b_curr - learning_rate * bd

            y_predicted_new = m_curr * x + b_curr
            cost_new = (1 / n) * sum([val ** 2 for val in (y - y_predicted_new)])
            print("learning_rate {}, iteration {}, m {}, b {}, cost {}".format(learning_rate, i,m_curr,b_curr, cost))
            if math.isclose(cost, cost_new, abs_tol=1e-06):
                cost_close = True
                stop = True
            elif cost_new > cost:
                cost_rising = True

            # line_y = m_curr * line_x + b_curr
            # plt.plot(line_x, line_y, linewidth=0.5)
        #print("Stopped at iteration ".format(i))
    return [m_curr,b_curr]


df = pd.read_csv("test_scores.csv")
x = np.array(df.math)
y = np.array(df.cs)

plt.scatter(x,y)
[slope, y_intercept] = gradient_descent(x,y,plt)
line_x = x
line_y = slope * line_x + y_intercept
plt.plot(line_x, line_y, linewidth=0.5)

def predict_with_sklearn():
    df = pd.read_csv("test_scores.csv")
    reg = linear_model.LinearRegression()
    reg.fit(df[['math']], df.cs)
    return [reg.coef_, reg.intercept_]

print("Modelling with sk-learn")
[coef_, intercept_] = predict_with_sklearn()
print("slope: {}\ny-intercept: {}".format(coef_,intercept_))

plt.grid()
plt.legend(["slope: {:.2f}\ny-intercept: {:.2f}".format(round(slope,2),round(y_intercept,2))])
plt.show()
