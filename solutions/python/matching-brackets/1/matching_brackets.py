def is_paired(input_string: str) -> bool:
    pairs = {')': '(', ']': '[', '}': '{'}
    openings = set(pairs.values())
    stack = []

    for ch in input_string:
        if ch in openings:
            stack.append(ch)
        if ch in pairs:
            if not stack:
                return False
            top = stack.pop()
            if top != pairs[ch]: 
                return False 
    
    if stack: 
        return False
    return True