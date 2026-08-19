class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for c in tokens:
            if c not in {"+","-","*","/"}:
                stack.append(int(c))
            elif c=="+":
                second=stack.pop()
                first=stack.pop()
                res=first+second
                stack.append(res)
            elif c=="-":
                second=stack.pop()
                first=stack.pop()
                res=first-second
                stack.append(res)
            elif c=="*":
                second=stack.pop()
                first=stack.pop()
                res=first*second
                stack.append(res)
            elif c=="/":
                second=stack.pop()
                first=stack.pop()
                res=int(first/second)
                stack.append(res)
        return stack[-1]