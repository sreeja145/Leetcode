nums=[8,7,2,5,3,1]
target=10
s=set()
is_pair=-1
for i in nums:
    if target-i in s:
        print(target-i,i)
        is_pair=0
    else:
        s.add(i)

if is_pair==-1:
    print("pair not found")
