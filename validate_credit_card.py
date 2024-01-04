def validate(n):
    sum = 0
    rev_no_space_str = reversed(list(str(n)))
    count = 0
    for i in rev_no_space_str:
        if i and count%2==0:
            sum+=int(i)
        if i and count%2!=0:
            newNum = (int(i) * 2) if (int(i) * 2)<9 else (int(i) * 2)-9
            sum+=int(newNum)
        count += 1
    return True if sum%10==0 else False


print(validate(1714)) #--> False
print(validate(12345)) #--> False
print(validate(891))  #--> False
print(validate(123))  #--> False
print(validate(1))  #--> False
print(validate(2121))  #--> True
print(validate(1230))  #--> True