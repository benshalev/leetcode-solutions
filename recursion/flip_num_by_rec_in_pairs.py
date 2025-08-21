# take a num like: 138
#return: 183
#71 -> 17
# 1234 -> 2143

def flip_in_pairs(num):
    if num <= 9:
        return num
    return (flip(num % 100) + 100 * flip_in_pairs(num // 100) )

def flip(num):
    a = num // 10
    b = num % 10
    return b*10 + a

print(flip_in_pairs(12))
print(flip_in_pairs(1234))
print(flip_in_pairs(12345))
