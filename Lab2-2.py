print("ตรวจสอบคะเเนน")
a=int(input("รับค่าคะเเนน"))
if a>=80 and a<=100:
    print("เกรดA")
elif a>=70 and a<=79:
    print("เกรดB")
elif a>=60 and a<=69:
    print("เกรดC")
elif a>=50 and a<=59:
    print("เกรดD")
elif a>=0 and a<=49:
    print("เกรดF")    
else:
    print("กรุณากรอกข้อมูลใหม่ให้ถูกต้อง 0-100")