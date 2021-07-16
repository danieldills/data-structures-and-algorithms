open_brackets = ["[", "{", "("]
closed_brackets = ["]", "}", ")"]

def validate_brackets(str):
    stack = []
    for i in str:
        if i in open_brackets:
            stack.append(i)
        elif i in closed_brackets:
            brackets = closed_brackets.index(i)
            if ((len(stack) > 0) and (open_brackets[brackets] == stack[len(stack) -1])):
                stack.pop()
            else:
                return False, "Unbalanced"
    if len(stack) == 0:
        return True, "Balanced"
    else:
        return False, "Unbalanced"
