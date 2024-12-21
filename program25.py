tpl=eval(input("enter tuple:"))
length=len(tpl)
mean=sum=0
for i in range(0,length):
    sum+=tpl[i]
mean=sum/length
print("given tupple is:",tpl)
print("mean of given tuple is:",mean)
         
