# line function
def y_value((x1, y1), (x2, y2), x_val):
    m = (y2 -y1) / (x2 -x1)
    b = y1 - m * x1
    y_val = m * x_val + b
    return y_val





