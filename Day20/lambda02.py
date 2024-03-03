def show_data(m):
    return lambda a:a*m
n=show_data(3)
print(n(11))