class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk=[]
        pair=[[p,s] for p,s in zip(position,speed)]
        pair.sort(reverse=True)
        print(pair)
        for p,s in pair:
            if not stk:
                stk.append((target-p)/s)
            else:
                stk.append((target-p)/s)
                if stk[-1]<=stk[-2]:
                    stk.pop()

        return len(stk)