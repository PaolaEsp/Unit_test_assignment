# line function
def y_value(a, b, x_val):
    m = (b[1] -a[1]) / (b[0] -a[0])
    bint = a[1] - m * a[0]
    y_val = m * x_val + bint
    return y_val





