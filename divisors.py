class Solution:
    def divisors(self, n):
        s = []
        for i in range(1, n+1):
            if n % i == 0:
                s.append(i)
        return s
sol=Solution()
print(sol.divisors(6))