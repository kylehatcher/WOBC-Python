import sys

def phone_number(num):
    print('({}{}{}) {}{}{}-{}{}{}{}'.format(num[0],num[1],num[2],num[3],num[4],num[5],num[6],num[7],num[8],num[9]))

nums=[]
if len(sys.argv) < 11:
    m = len(sys.argv)
else:
    m=11
for i in range(1,m):
    for x in sys.argv[i]:
            try:
                nums.append(int(x))
            except:
                next
if len(nums) > 9:
    phone_number(nums)
else:
    print('Please enter 10 numbers')