class Solution:
    def isValid(self, s: str) -> bool:
        hp={
            ")":"(",
            "}":"{",
            "]":"["
        }

        stack=[]
        for c in s:
            if c in hp.values():
                stack.append(c)
            elif c in hp.keys():
                if not stack:
                    return False
                if stack[-1]!=hp[c]:
                    return False
                else:
                    stack.pop()
        if not stack:
            return True
        else:
            return False