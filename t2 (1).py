#calculate the repair cost between two words without using  a computer. calculate the levistn edit distance between "start" and  "stare"

def levenshtein_distance(word1, word2):
    m, n = len(word1), len(word2)
    
    # Create matrix
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],      # deletion
                    dp[i][j-1],      # insertion
                    dp[i-1][j-1]     # substitution
                )
    
    return dp[m][n]

# Test
word1 = "start"
word2 = "stare"
distance = levenshtein_distance(word1, word2)
print(f"Levenshtein distance between '{word1}' and '{word2}': {distance}")