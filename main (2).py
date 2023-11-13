'''

s=0
x = input('Nhap x: ')
y = input('Nhap y: ')
x = float(x)
y = float(y)

while (x-y >=0): 
  s=s+1
  x=x-y
  
print ("s= ", s)
print ("x= ", x)

'''


s=1
x = input('nhap X= ')
y = input('nhap Y= ')
x = float(x)
y = float(y)

while(x>0):
  s=s*y
  x=x-1

print('s= ',s)
