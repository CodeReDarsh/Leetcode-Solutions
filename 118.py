class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        row = 0
        while row < numRows:
            arr = []
            for i in range(row+1):
                if i-1<0 or len(res) == 0 or i == len(res[row-1]):
                    arr.append(1)
                else:
                    arr.append(res[row-1][i-1] + res[row-1][i])
            res.append(arr)
            row+=1
        return res
