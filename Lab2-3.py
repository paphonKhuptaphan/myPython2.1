print("โปรเเกรมหาค่าดัชนีมวลกายBMI")
a=int(input("รับค่าน้ำหนักตัว"))
b=int(input("รับค่าส่วนสูง"))
b=b/100
b=b**2
BMI=a/b
print("กำลังคำนวณBMI"+str(BMI))
if BMI<=18.50: 
    print("น้ำหนักน้อย/ผอม")
elif BMI<=22.9:
    print("เท่าคนปกติ")
elif BMI<=24.9:
    print("ท้วม/โรคอ้วนระดับ1")
elif BMI<=29.9:
    print("อ้วน/โรคอ้วนระดับ2")
elif BMI>=30:
    print("อ้วนมาก/โรคอ้วนระดับ3")
else:
    print("Thanks")