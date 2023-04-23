def tile_cost(h,w,c):
    return h*w*c

c = float(input("Enter the cost per m^2 for the floor plan : "))

print(tile_cost(10,10,c))