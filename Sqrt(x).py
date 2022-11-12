class Solution:
    def mySqrt(self, x: int) -> int:

        if x==0 or x==1:
            return(x)
        elif x==2:
            return(1)
        for i in range(x):
            if i*i>=x:
                root=i
                break
            else:
                root=0

        if x-(root*root)== 0:
            root=root
        else:
            root=root-1
              
        return(root)
