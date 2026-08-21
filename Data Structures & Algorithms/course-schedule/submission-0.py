class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hp={i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            hp[crs].append(pre)
        visit=set()

        def dfs(crs):
            if crs in visit:
                return False
            if hp[crs]==[]:
                return True

            visit.add(crs)
            for pre in hp[crs]:
                if not dfs(pre): return False
            visit.remove(crs)
            hp[crs]=[]
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True

