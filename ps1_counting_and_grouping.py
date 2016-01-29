def item_order(order):
    s = 0
    h = 0
    w = 0

    order.lower()
    words = order.split(' ')
    for word in words:
        if word == "salad":
            s += 1
        if word == "hamburger":
            h += 1
        if word == "water":
            w += 1
            
    return "salad:" + str(s) + " hamburger:" + str(h) + " water:" + str(w)
