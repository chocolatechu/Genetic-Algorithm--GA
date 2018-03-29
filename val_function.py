from object_function import object_function


def val_function(decode):
    y = []
    for i in decode:
        y.append(object_function(i))
    return y