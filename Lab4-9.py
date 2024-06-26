def bmi(kg,cm):
    B = kg/cm
    print("ค่าดัชนีมวลกาย = %.2f " % B)
    return B

def compare(b):
    if b < 18.5:
        print ("ผอม / น้ำหนักน้อย")
    elif b < 23:
        print("ปกติ / สุขภาพดี")
    elif b < 25:
        print ("ท้วม / โรคอ้วนระดับ 1")
    elif b < 29:
        print ("อ้วน / โรคอ้วนระดับ 2")
    elif b < 30:
        print ("อ้วนมาก, / โรคอ้วนระดับ 3")

kg = float(input("รับค่าน้ำหนัก:"))
cm = float(input("รับค่าสูง:"))

compare(bmi(kg,cm))