# this file is solving the problem of physics
import math
import random
from scipy.constants import pi, G
import matplotlib.pyplot as plt


def force_earth_globe(n, dr, m_s, rho, dphi, k_):
    # adding the sums of the single forces
    # setting force sum adn mass sum
    sum_f = 0
    sum_m = 0
    # iterating through steps
    for i in range(n_steps):
        phi = dphi * i
        a = math.cos(phi) - k_
        r_r = math.sin(phi)
        r = math.sqrt(a ** 2 + r_r ** 2)
        V_r = pi * 2 * r_r * dphi * dr
        m_r = V_r * rho
        F = G * m_s * m_r * a * (r ** 3)
        sum_f += F
        sum_m += m_r
    # returning values
    return sum_f, sum_m, r


def force_earth_point(m, r, m_s):
    return G * (m * m_s / (r ** 2))


if __name__ == "__main__":
    n_steps = 100
    DR = 0.1
    m_stein = 1
    # Rho = 5510
    Rho = 3000
    DPhi = pi / n_steps
    n_samples = 8
    # samples of range
    k_samples = sorted([random.random() * 2 for n in range(n_samples)])
    # collecting samples
    data_globe = []
    data_point = []
    for k in k_samples:
        f, m, r = force_earth_globe(n=n_steps, dr=DR, m_s=m_stein, rho=Rho, dphi=DPhi, k_=k)
        data_globe.append(f)
        f = force_earth_point(m=m, m_s=m_stein, r=r)
        data_point.append(f)
    # printing data
    plt.plot(k_samples, data_globe, c='red', linestyle='-', marker='o', label='Globe-Data')
    plt.plot(k_samples, data_point, c='blue', linestyle='-', marker='o', label='Point-Data')
    # showing plot
    plt.xlabel('k')
    plt.ylabel('Force')
    plt.legend()
    plt.show()
