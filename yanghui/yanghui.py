#!/usr/bin/env python
# yanghui

def print_yanghui(n):
    if n <= 0:
        return null
    listyang = []
    for i in range(1,n+1):
        listyang.append(['1'] * i)

    if n > 2:
        for i in range(2, n):
            for j in range(1, i):
                listyang[i][j] = str(int(listyang[i-1][j-1]) + int(listyang[i-1][j]))

    for i in range(0, n):
        listyang[i] = '\t' * (n-i) + '\t\t'.join(listyang[i])
        print listyang[i]


if __name__ == "__main__":
    n = 10
    print 'n=',n
    print_yanghui(n)
