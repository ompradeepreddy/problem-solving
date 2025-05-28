class Solution:
	def reverseNumber(self,n):
		n1=str(n)
		return n1[::-1]
sol=Solution()
print(sol.reverseNumber(123))
print(sol.reverseNumber(121))