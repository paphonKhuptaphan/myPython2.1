def Product(num):
    sum = 0
    for i in range(num):
      price = int(input("PriceOfProduct %d " % (i+1)))
    sum += price
    return sum

def tax (sum):
    vat = sum/100*7
    return vat

def total(a,b):
    t = a-b
    return total
def discount(z,s,x):
    pro = z+s+x
    return pro

num = int(input("Product Quantity"))
sum = z+s+x(num)
p   = int(intput("รับค่าส่วนลด"))
print("ราคารวม %.2f" % total(sum,pro(sum)))
print("ภาษี %.2f" % tax(sum))
print("โปรโมชั่น %.2f" % pro(sum))
print("TotalOfProduct %.2f" % total(sum, tax(sum), discount(sum)))






    
    