
def beautifulDays(i, j, k):
    count=0
    for day in range(i,j+1):
        if abs(day-int(("".join(reversed(str(day))))))%k==0:
            count += 1
    return count