class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Solution with O(n) space complexity but faster than with O(1) space
        f = [0] + flowerbed + [0]
        for i in range(1,len(f)-1):
            if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
                f[i] = 1
                n -= 1
        return n<=0
        
        """
        Solution with O(1) space complexity

        if n == 0: return True
        for i in range(len(flowerbed)):
            if ((i == 0 or flowerbed[i-1] == 0)
            and (flowerbed[i] == 0)
            and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0)):
                flowerbed[i] = 1
                n-=1
        return n<=0
        """
        