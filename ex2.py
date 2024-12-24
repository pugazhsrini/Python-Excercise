# count vowels in a string

def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

print(count_vowels("Hello World"))



# Reverse a String


def rev_string(st):
    reversed_str = ""
    for char in st:
        reversed_str = char + reversed_str  
    return reversed_str

s = input()
print(rev_string(s))

#occurence of each char in string

a= input()
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)




