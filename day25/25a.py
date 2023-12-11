import math
lines = [f.strip() for f in open('input', 'r')]

def sign(s):
    if s >= 0:
        return 1
    elif s < 0:
        return -1 

digits = {'=':-2,'-':-1,'0':0,'1':1,'2':2}
revdigits= {-2:'=',-1:'-',0:'0',1:'1',2:'2'}
def to_dec(s):
    ret = 0
    p = 1
    for k in reversed(s):
        ret += p * digits[k]
        p *= 5
    return ret

def to_snafu(s, power):
    factor = 5 ** power
    #print(f"evaluating pow {factor}")
    digit = sign(s) * (abs(s) // factor)
    carry = 0
    if digit >= 3:
        carry = 1
        s -= 5**(power + 1)
        digit = sign(s) * (abs(s) // factor)
    elif digit <= -3:
        carry = -1
        s += 5**(power + 1)
        digit = sign(s) * (abs(s) // factor)

    s = s - digit * factor
    #print(power, carry, digit, s)
    assert(digit >= -2 and digit <= 2)
    recarry = 0
    rest = []
    if power > 0:
        recarry, rest = to_snafu(s, power - 1)
    digit += recarry
    if digit > 2:
        carry += 1
        digit -= 5
    elif digit < -2:
        carry -= 1
        digit += 5
    return carry, [digit] + rest


def to_snafu2(s):
    carry, ret = to_snafu(s,  math.floor(math.log(s) / math.log(5)))
    if carry:
        ret = [carry] + ret
    return ''.join([revdigits[i] for i in ret])


for l in lines:
    d=to_dec(l)
    s = to_snafu2(d)
    assert(s == l)

s = 0
for l in lines:
    s += to_dec(l)

print(s)
print(to_snafu2(s))

