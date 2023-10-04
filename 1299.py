class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max = -1
        for i in range(len(arr)-1,-1,-1):
            if max < arr[i]:
                max, arr[i] = arr[i], max
            else:
                arr[i] = max
        
        return arr