import math


def f(t, w):
    print("calculating with t = %.12f and w = %.12f" % (t, w))
    return t**2 * w - math.exp(t*w)


def k1(h, t, w):
    result = h*f(t, w)
    print("K1 = %.12f" % result)
    return result


def k2(h, t, w):
    result = h*f(t + h/4.0, w + k1(h, t, w)/4.0)
    print("K2 = %.12f" % result)
    return result


def k3(h, t, w):
    result = h*f(t + 3.0*h/8.0, w + 3.0*k1(h, t, w) /
                 32.0 + 9.0*k2(h, t, w)/32.0)
    print("K3 = %.12f" % result)
    return result


def k4(h, t, w):
    result = h*f(t + 12.0*h/13.0, w + 1932.0*k1(h, t, w)/2197.0 -
                 7200.0*k2(h, t, w)/2197.0 + 7296.0*k3(h, t, w)/2197.0)
    print("K4 = %.12f" % result)
    return result


def k5(h, t, w):
    result = h*f(t + h, w + 439.0*k1(h, t, w)/216.0 - 8.0*k2(h, t,
                 w) + 3680.0*k3(h, t, w)/513.0 - 845.0*k4(h, t, w)/4104.0)
    print("K5 = %.12f" % result)
    return result


def k6(h, t, w):
    result = h*f(t + h/2.0, w - 8.0*k1(h, t, w)/27.0 + 2.0*k2(h, t, w) - 3544.0 *
                 k3(h, t, w)/2565.0 + 1859.0*k4(h, t, w)/4104.0 - 11.0*k5(h, t, w)/40.0)
    print("K6 = %.12f" % result)
    return result


def omega(w, k1, k3, k4, k5):
    result = w + 25.0*k1/216.0 + 1408.0*k3/2565.0 + 2197.0*k4/4104.0 - k5/5.0
    print("omega = %.12f" % result)
    return result


def omegatil(w, k1, k3, k4, k5, k6):
    result = w + 16.0*k1/135.0 + 6656.0*k3/12825.0 + \
        28561.0*k4/56430.0 - 9.0*k5/50.0 + 2.0*k6/55.0
    print("omega til = %.12f" % result)
    return result


def q(h, w, k1, k2, k3, k4, k5, k6, ordemmenor):
    result = 0.84 * (tolerancia*h/abs(omega(w, k1, k3, k4, k5) -
                     omegatil(w, k1, k3, k4, k5, k6)))**(1.0/ordemmenor)
    print("q = %.12f" % result)
    return result


# h = float(input("Digite o h: "))
# t = float(input("Digite o t: "))
# w = float(input("Digite o y(0): "))
h = 3.1133
t = -0.1
w = -0.6098
tolerancia = 0.1

print("omega i+1: %.12f" %
      omega(w, k1(h, t, w), k3(h, t, w), k4(h, t, w), k5(h, t, w)))

print("omega til i+1: %.12f" % omegatil(w, k1(h, t, w), k3(h, t, w),
                                        k4(h, t, w), k5(h, t, w), k6(h, t, w)))

k1r = k1(h, t, w)
k2r = k2(h, t, w)
k3r = k3(h, t, w)
k4r = k4(h, t, w)
k5r = k5(h, t, w)
k6r = k6(h, t, w)


print("q: %.12f" % q(h, w, k1r, k2r, k3r, k4r, k5r, k6r, 4))
