def fibonacci(n, memo={}):
   if n in memo:
       return memo[n]
 
   if n <= 1:
       return n
 
   memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
   return memo[n]
 
 
# Main Program
n = int(input("Enter the value of n: "))
print("Fibonacci Number =", fibonacci(n))

Tabulation:
def fibonacci_tab(n):
   if n <= 1:
       return n
 
   dp = [0] * (n + 1)
   dp[0] = 0
   dp[1] = 1
 
   for i in range(2, n + 1):
       dp[i] = dp[i - 1] + dp[i - 2]
 
   return dp[n]
 
# Driver Code
n = int(input("Enter n: "))
print(f"Fibonacci({n}) = {fibonacci_tab(n)}")

 
