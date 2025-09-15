#smallest number and second smallest
ip=[10,2,2,4,3,5]
sm=ip[0]
ssm=ip[0]
for x in ip:
    if x<sm:
        ssm=sm
        sm=x
    elif x<ssm and x!=sm:
        ssm=x
print("smallest:",sm)
print("second smallest:",ssm)