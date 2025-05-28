class Solution:
    def isPrime(self, n):
        if n <= 1:
            return False 
        c = 0
        for i in range(1, n):
            if n % i == 0:
                c += 1
        if c > 1:
            return False
        else:
            return True
sol=Solution()
print(sol.isPrime(5))