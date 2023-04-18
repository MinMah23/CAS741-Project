# This function checks that if f should be considered as a function or a float number

def checkF(f, t):
    try:
        f_float = float(f)
        return f_float
    except ValueError:
        pass
    try:
        func = eval(f)
        time_func = func(t)
        return time_func
    except ValueError:
        pass
    return f
