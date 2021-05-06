
# Linear integer interpolation
#
def linear_integer_interpolation(f, interval, segments):
    # subdivision of the interval
    print(interval[0], interval[1], segments)
    x_step_size = int((interval[1] - interval[0]) / segments)
    print("X Step Size:", x_step_size)
    solutions = []
    x_before = interval[0]

    epsilon = 0.1
    while x_before <= interval[1] + epsilon:
        y_before = f(x_before)
        x_after =  x_before + x_step_size
        # compute the rounded value of the original function to be interpolated
        y_after = f(x_after)
        # in this time interval, we look for y=a*x+b linear interpolation
        # compute the slope
        slope = (y_after-y_before) / x_step_size
        # we keep the rounded value of the slope
        a = round(slope)
        # given this rounded slope, search for the best b
        # the simplest way to go (TODO better), look for the segment fits
        # the middle point
        # ord_orig such that the light pass by the middle point
        ord_orig = y_after - a * x_after
        b = round(ord_orig)
        x_before = x_after
        solutions.append((a, b))
    return solutions
      

if __name__ == "__main__":
    # short example
    from numpy import sin, cos, linspace
    import matplotlib.pyplot as plt
    def f(x):
        return 609.11 -10.11 * sin(0.32*x) + 125.221 *cos(0.452 * x)

    interval = [10, 50]
    segments = 15
    # plot the f function
    x = linspace(interval[0], interval[1], 1000)
    plt.plot(x, f(x), label='f(x)')
    # compute the interpolated curve
    interp = linear_integer_interpolation(f, [10, 50], segments)
    print("Solution:", interp)
    x_approx = []
    y_approx = []
    x_step_size = (interval[1] - interval[0]) / segments
    for kk in range(segments + 1):
        x = interval[0] + kk * x_step_size
        a, b = interp[kk]
        y = a * x + b
        x_approx.append(x)
        y_approx.append(y)

    plt.plot(x_approx, y_approx, label='linear integer interpolation')
    plt.grid()
    plt.legend()
    plt.show()
