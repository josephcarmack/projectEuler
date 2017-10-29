def problem1(number2go2):
    s=0.0
    for i in range(number2go2):
        if(i%3==0 or i%5==0):
            s += i
    return s

print(problem1(1000))
