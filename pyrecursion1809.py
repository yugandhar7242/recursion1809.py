


#####sum of n numbers using recursion
def summ(n):
    if n==1:
        return n
    return n+summ(n-1)
n=10
print(summ(n))


###### string palindrome using recursion
def palin(s,i,j):
    if i>j:
        return True
    if s[i]!=s[j]:
        return False
    return palin(s,i+1,j-1)

s='racecar'
i=0
j=len(s)-1
print(palin(s,i,j))
        


#####find fibonaci number using recursion.
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)
n=7
print(fib(n))
13