#The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
# such that each number is the sum of the two preceding ones, starting from 0

#les the the two method to solve this problem

#1, regular recursion: time:O(n**2)

def fib(n):
    if n==1:
        return 1
    if n==0:
        return 0
    var1=fib(n-1)
    var2=fib(n-2)
    
    return var1 + var2

print(fib(4))# which is very slow 

#2, dynamic programming : time:O(n) # using the hash map to memorize task that have already done

#top down approces : or memorization using recurssion
def fibo(x):
    memo={1:1,0:0}
    if x in memo:
        return memo[x]
    else:
        memo[x]=fibo(x-1)  + fibo(x-2)
        return memo[x]
    
      
    
print(fibo(4))

# now lest see the bottom up: dynamic using the loop


