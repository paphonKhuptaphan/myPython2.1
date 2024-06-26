
def Circle(r):
    area = 22/2*r**2
    print("พื้นที่วงกลม %.2f" % area)
    
    return area

h = float(input("รับค่ารัศมี"))
Circle(h)