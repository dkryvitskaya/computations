# Напишите функцию, которая складывает два рациональных числа
# Структуру данных для хранения чисел выберите и реализуйте сами



def sum_rat(a, b):
  n=(a[0]*b[1]+b[0]*a[1],b[1]*a[1])
  k=0
  while k<n[0]:
    k += 1
    if n[1]%k==0 and n[0]%k==0:
      n=(n[0]/k,n[1]/k)
  return n
def rat_print(a):
  return "{0}/{1}".format(a[0],a[1])

print(rat_print(sum_rat((5,2),(6,4)))) 
