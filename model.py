def naredi(n):
    with open("velika.txt", "w") as f:
        for _ in range(n):
            print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", file=f)


naredi(10**8)