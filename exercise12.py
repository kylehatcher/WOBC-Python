import sys

class Number:
    def __init__(self, num1, num2, prime, div, gcd, lcm):
        self.num1 = num1
        self.num2 = num2
        self.prime = prime
        self.div = div
        self.gcd = gcd
        self.lcm = lcm
    
    def is_prime(n):
        if n.num1 <= 1 or n.num1 % 1 > 0:
            n.prime = False
        for i in range(2, n.num1):
            if n.num1 % i == 0:
                n.prime = False
        
    def get_divisors(n):
        for i in range(1, n.num1+1):
            if n.num1 % i == 0:
                n.div.append(i)
        
    def get_gcd(n):
        if n.num1 > n.num2:
            num = n.num1
        else:
            num = n.num2
        for i in range(1,num+1):
            if n.num1 % i == 0 and n.num2 % i ==0:
                n.gcd = i
        
    def get_lcm(n):
        if n.num1 > n.num2:
            num = n.num1
        else:
            num = n.num2
        lcm = []
        for i in range(1,num+1):
            if n.num1*i in lcm:
                n.lcm=n.num1*i
                break
            elif n.num2*i in lcm:
                n.lcm=n.num2*i
                break
            lcm.append(n.num1*i)
            lcm.append(n.num2*i)

if len(sys.argv) == 3:
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
    except:
        next
    if num1 > 0 and num2 > 0:
        n = Number(num1, num2, True, [], 0, 0)
        Number.is_prime(n)
        Number.get_divisors(n)
        Number.get_gcd(n)
        Number.get_lcm(n)
        print("Prime? {}".format(n.prime))
        print("Factors: {}".format(n.div))
        print("GCD n and m: {}".format(n.gcd))
        print("LCM n and m: {}".format(n.lcm))
