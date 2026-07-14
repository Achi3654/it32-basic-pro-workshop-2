Quantity = int(input("จำนวนปืน:"))
cost_p = int(input("ซื้อกระบอกละ:"))
sell_p = int(input("ขายกระบอกละ:"))
team_mem = int(input("จำนวนลูกน้อง:"))
kumrai = (sell_p - cost_p)

A = (Quantity * cost_p)
b = (Quantity * sell_p)
C = (kumrai)
D = (kumrai*20/100 )
E = (kumrai*80/100/team_mem)

print("ต้นทุน:",A)
print("ขายได้:",b)
print("กำไร:",C)
print("บอสได้เงิน:",D)
print("ลูกน้องได้:",E)


