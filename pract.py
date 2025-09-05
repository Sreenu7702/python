def rsravan(s,sub):
    for i in range(len(s)-1,-1,-1):
        if s[i]==sub:
            return i
s="hello hello hello"
sub='o'
print(rsravan(s,sub))

txt="banana"
print(txt.rfind('a'))

#alnum():
def alnum(s):
    if len(s)==0:
        return False
    for ch in s:
        if not (('A'<=ch<='Z') or ('a'<=ch<='z') or ('0'<=ch<='9')):
            return False
    return True
print(alnum("hello123"))
print(alnum("hello 123"))

def find(s,sub):
    if sub== " ":
        return 0
    for i in range(len(s)-len(sub)+1):
        if s[i:i+len(sub)]==sub:
            return i
    return -1
print(find("hello","lo"))