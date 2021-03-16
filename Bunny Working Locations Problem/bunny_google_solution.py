def solution(x, y):
    # asum = 0
    # for n in range(1, (x+y)):
    #     asum += n
    n = x+y-1
    asum = int((n*(n+1))/2)
    return str(asum-(y-1))

assert solution(3,2) == "9"
assert solution(5,10) == "96"
