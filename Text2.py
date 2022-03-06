def longestPalindrome(s):
    if len(s)<1:
        return ""
    stp=0
    endp=0
    for i in range(len(s)):
        a=expend(s,i,i)
        b=expend(s,i,i+1)
        if(a>b and a>=endp-stp+1):
            stp=i-int(a/2)
            endp=i+int(a/2)
        elif (b>=a and b>=endp-stp+1):
            stp=i-int(b/2)+1
            endp=i+int(b/2)
    return s[stp:endp+1]
def expend(s,m,n):
    while (m >= 0 and n < len(s) and s[m] == s[n]):
        m -= 1
        n += 1
    return n-m-1
s=input()
print(longestPalindrome(s))


