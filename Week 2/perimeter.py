#Get the dimensions of the shape
width1 = float(input("Enter width 1:"))
width2 = float(input("Enter width 2 :"))
height1 = float(input("Enter height 1:"))
height2 = float(input("Enter height 2:"))
price_per_meter = float(input("Enter price per meter: "))

#get the total perimeter
perimeter = width1 + height1 + width2 + height2
total_price = perimeter + price_per_meter
print('The total fence required =', str(perimeter))
print('Total price', price_per_meter)