class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hp={}
        for i in range(len(strs)):
            s=strs[i]
            key="".join(sorted(s))
            if key in hp:
                hp[key].append(s)
            else:
                hp[key]=[s]

        return list(hp.values())