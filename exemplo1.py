

def f(w, t):
    return (w**2 + w)/t


def f1(w, t):
    return (2.0*(w**3) + 2.0*(w**2))/(t**2)


def f2(w, t):
    return (6.0*(w**4) + 6.0*(w**3))/(t**2)


def f3(w, t):
    return (24.0*(w**6) + 42.0*(w**5) + 6.0*(w**4) - 12.0*(w**3))/(t**3)


def taylor(w, t, h):
    return f(w, t) + (h/2.0)*f1(w, t) + ((h**2)/6.0)*f2(w, t) + ((h**3)/24.0)*f3(w, t)


def nextw(w, t, h):
    return w + h*taylor(w, t, h)


h = 0.2
t = 2.80
w = -1.200
print("%.3f" % nextw(w, t, h))
