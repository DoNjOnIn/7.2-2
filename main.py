import random

def print1(A,i,j):
    if i <len(A):
        if j <len(A[i]):
            print(A[i][j], end=' ')
            print1(A,i,j+1)
        else:
            print()
            print1(A,i+1,0)
    else:
        return


def minm(A,a,i,j,mnum):
    if i < len(A):
        if j < len(A[i]):
            if A[i][j]<mnum:
                mnum=A[i][j]
                minm(A,a,i,j+1,mnum)
            else:
                minm(A, a, i, j + 1,mnum)
        else:
            a.append(mnum)
            if i+1<len(A):
                minm(A, a, i + 1, 0, A[i + 1][0])
    return a

def maxl(a,i,maxn):
    if i < len(a):
        if a[i]>maxn:
            maxn=a[i]
            return maxl(a,i+1,maxn)
        else:
            return maxl(a, i + 1, maxn)
    else:
        return maxn

def create(A,low,high,i,j):
    if i < len(A):
        if j < len(A[i]):
            A[i][j] = random.randint(low, high)
            create(A,low,high,i,j+1)
        create(A,low,high,i+1,0)
    return


def main():
    M = int(input('К-сть рядків?='))
    N = int(input('К-сть стовпчиків?='))
    low = int(input('Low='))
    high = int(input('High='))
    a=[]
    A = [[0] * M for i in range(N)]
    create(A,low,high,0,0)
    print1(A,0,0)
    print('-------------')
    print('All min-'+str(minm(A,a,0,0,A[0][0])))
    print('Max of min='+str(maxl(a,0,a[0])))




if __name__=='__main__':
    main()