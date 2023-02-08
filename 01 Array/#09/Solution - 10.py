'''
        arr.sort()
        soln = arr[-1]-arr[0]
        print(arr)
        mn=min(arr)
        mx=max(arr)
        
        for i in range(1,n):
            if arr[i]-k <0:
                mn = arr[0]+k
            else:
                mn = min(arr[0]+k,arr[i]-k)
            mx = max(arr[-1]-k,arr[i-1]+k)
            soln = min(mx-mn, soln)
        return soln
        '''