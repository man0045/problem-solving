n=int(input(" enterbv"))
likes = 2
cumulative = 2
if n > 1:
    for i in range(2,n+1):
        shares = likes * 3
        likes = shares // 2
        cumulative += likes
    print(cumulative)