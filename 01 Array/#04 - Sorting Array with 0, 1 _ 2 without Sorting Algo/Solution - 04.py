#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        c0 = arr.count(0)
        c1 = arr.count(1)
        c2 = arr.count(2)
        for i in range(c0):
            arr[i] = 0
        for i in range(c0,c0+c1):
            arr[i] = 1
        for i in range(c0+c1,c0+c1+c2):
            arr[i] = 2
                


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends