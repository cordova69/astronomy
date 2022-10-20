class Solution:
   def solve(self, numeral):
      d = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
      ans = 0
      n = len(numeral)
      for (idx, c) in enumerate(numeral):
         if idx < n - 1 and d[c] < d[numeral[idx + 1]]:
            ans -= d[c]
         else:
            ans += d[c]
      return ans

ob = Solution()
numeral = input("Enter Roman number: ")
print(ob.solve(numeral.upper()))

# numeral[i] in 'AEIOUaeiou'