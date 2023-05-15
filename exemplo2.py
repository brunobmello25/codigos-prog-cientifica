import math


def f(w, t):
    return math.exp(t-w)


def f1(w, t):
    return math.exp(t-w) - math.exp(2*t - 2*w)


def f2(w, t):
    return math.exp(t-w) - 3*math.exp(2*t - 2*w) + 2*math.exp(3*t - 3*w)


def f3(w, t):
    return -1 * (math.exp(t-w) - 6*math.exp(3*t - 3*w)) * math.exp(t-w)


def taylor(w, t, h):
    return f(w, t) + (h/2.0)*f1(w, t) + ((h**2)/6.0)*f2(w, t) + ((h**3)/24.0)*f3(w, t)


def nextw(w, t, h):
    return w + h*taylor(w, t, h)


h = 0.5
t = 0.5
w = 1.2142
print("%.4f" % nextw(w, t, h))
