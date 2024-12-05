class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp=[[False]*len(s) for i in range(len(s))]
        start=0
        max_len=1
            
        length=len(s)
        if length<2:
                return s

        for i in range (length):
                dp[i][i]=True
                    
        for j in range(1,length):
                for i in range(j-1,-1,-1):
                        if s[i]==s[j]:
                                if j-i<3 or dp[i+1][j-1]:
                                        dp[i][j]=True
                                        if j-i+1>max_len:
                                                start=i
                                                max_len=j-i+1
                                        
        return s[start:start+max_len]
                    
        
                             
                
                                    
        
sol=Solution()
print(sol.longestPalindrome("aaaa"))