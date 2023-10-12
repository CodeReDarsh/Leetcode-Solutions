class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        myset = set()
        for e in emails:
            local,domain = e.split("@")
            local = local.split("+")[0]
            local = local.replace(".","")
            myset.add((local,domain))
        return len(myset)