t = int(input().strip())

for t_itr in range(t):
    n = int(input().strip())
    if n == 0:
        return 1
    
    if n%2 == 0 :
        return utopianTree(n-1) + 1
    else:
        return 2 * utopianTree(n-1)