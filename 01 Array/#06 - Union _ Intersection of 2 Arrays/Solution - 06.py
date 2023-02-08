#User function Template for python3

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        #code here
        s=set(())
        t=min(n,m)
        for i in range(t):
            s.add(a[i])
            s.add(b[i])
        arr=[]
        num=0
        if n<=m:
            num = m
            arr = b
        else:
            num = n
            arr = a
        for i in range(min(n,m),num):
            s.add(arr[i])
        return(len(s))

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n,m=[int(x) for x in input().strip().split()]
        
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        ob=Solution()
        
        print(ob.doUnion(a,n,b,m))
# } Driver Code Ends