

hrs = input("Enter hours:")
hrs = float(hrs)
rt = input("enter rt per hrs:")
rt = float(rt)
pay = hrs*rt
if hrs>40:
    pay = rt*40 + ((hrs-40)*rt*1.5)
print(pay)
  
