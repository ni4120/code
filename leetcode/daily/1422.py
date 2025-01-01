class Solution:
    def maxScore(self, s: str) -> int:
        s_arr = list(s)
        
        result = []
        for i in range(1,len(s_arr)):
            left = []
            right = []

            left = s_arr[:i]
            right = s_arr[i:]
            
            sum = left.count("0") + right.count("1")
            result.append(sum)
        
        return(max(result))
        

