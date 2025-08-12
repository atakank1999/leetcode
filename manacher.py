def longest_palindrome_manacher(s: str) -> str:
    if not s:
        return ""
    
    # Step 1: Transform
    T = "^#" + "#".join(s) + "#$"
    n = len(T)
    P = [0] * n
    center = right = 0
    
    # Step 2: Process
    for i in range(1, n - 1):
        mirror = 2 * center - i
        letter = T[i]
        
        if i < right:
            P[i] = min(right - i, P[mirror])
        
        # Try expanding beyond current radius
        while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
            P[i] += 1
        
        # Update center/right if we expanded beyond right
        if i + P[i] > right:
            center, right = i, i + P[i]
    
    # Step 3: Find max
    max_len = max(P)
    center_index = P.index(max_len)
    
    # Step 4: Map back to s
    start = (center_index - max_len) // 2
    return s[start:start + max_len]


s = "acbbca"
print(longest_palindrome_manacher(s))
