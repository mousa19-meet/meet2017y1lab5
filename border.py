def draw_border(n , m, border, fill):
    print(m*border)
    for i in range (n):
        print(border + ((m-2) * fill) + border)
    print(m*border) 
