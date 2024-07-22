x = []


def func():
    global x
    x = [3]


func()
print(x)
