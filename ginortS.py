a=input()
upper=[x for x in a if x.isupper()]
lower=[x for x in a if x.islower()]
digit_odd=[x for x in a if x.isdigit() and int(x)%2!=0]
digit_even=[x for x in a if x.isdigit() and int(x)%2==0]
upper.sort()
lower.sort()
digit_odd.sort()
digit_even.sort()
t=''
for i in lower,upper,digit_odd,digit_even:
    for j in i:
        t=t+j
print(t)
