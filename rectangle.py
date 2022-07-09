def task(x1, y1, x2, y2, x3, y3, x4, y4):
    if x3 > x1 and x3 < x2 and y3 > y2 and y3 < y4:
        lenght = x2 - x3
        width = y1 - y3
        s = lenght * width
        return s
    else:
        return "Не входит"
print(task(1,1,2,2,3,3,4,4))

