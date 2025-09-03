#Swapcaase
def swapcase(s):
    res=" "
    for ch in s:
        if ch.islower():
            res +=ch.upper()
        elif ch.isupper():
            res +=ch.lower()
        else:
            res +=ch
    return res
print(swapcase("sreenu"))

#strip,lstrip,rstrip
def my_lstrip(s):
    while len(s) > 0 and s[0] == " ":
        s = s[1:]
    return s

def my_rstrip(s):
    while len(s) > 0 and s[-1] == " ":
        s = s[:-1]
    return s

def my_strip(s):
    return my_lstrip(my_rstrip(s))

txt = "   Sreenu Welcome   "
print(my_strip(txt))
print(my_lstrip(txt))
print(my_rstrip(txt))

#count
def count(s,sub):
    count=0
    for i in range(len(s)-len(sub)+1):
        if s[i:i+len(sub)] == sub:
            count += 1
    return count
print(count("banana","an"))

#replace
def replace(s,old,new):
    res=" "
    i=0
    while i<len(s):
        if s[i:i+len(old)]==old:
            res += new
            i += len(old)
        else:
            res += s[i]
            i +=1
    return res
print(replace("banana","an","xy"))