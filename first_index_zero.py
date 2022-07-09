def task(array):
    return array.index('0')
print(task("111111111110000000000000000"))

def task(array):
    for index, value in enumerate(array):
        if value == "0":
            return index
print(task("111111111110000000000000000"))




