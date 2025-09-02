ip = ['sravani', 'sravan', 'kumar', 'kumari', 'lalitha', 'lalith', 'arjun', 'lakshmi', 'nandini']

def guess_gender(name):
    female_endings = ('i', 'a')
    if name.lower().endswith(female_endings):
        return 'female'
    else:
        return 'male'

op = [tuple((name, guess_gender(name)) for name in ip)]

print(op)


#largest and second largest in a list
ip = [10, 2, 2, 4, 3, 5]

lg = ip[0]   
slg = ip[0]  

for x in ip:
    if x > lg:
        slg = lg
        lg = x
    elif x > slg and x != lg:
        slg = x

print("largest:", lg)
print("second largest:", slg)
