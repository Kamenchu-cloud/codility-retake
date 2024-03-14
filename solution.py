    
#     # Given an array S consisting of N strings, where every string is of the same length M
#     # You are expected to find a pair of strings in the array S such that there exists a position in which both of the strings have the same letter
#     # Both the index in array S and the positions in the strings are numbered from zero.

def solution(S):
    # Use nested loops 

    # First, a function "solution" is defined that takes in a parameter S which is a list of strings according to the question as input.
    # There are two variables initialized to store the length of the list S and the length of string(
    #  n = len(S) calculates the length of the list S which represents the number of strings in the array.
    #  m = len(S[0] calculates the length of the first string in the list S)
    # A nested loop is used whereby the outer loop i.e "for i in range(n):" is used to iterate over each index i where "n" is the number of strings in the array.
    # A middle loop is used whereby the line "for j in range(i + 1, n):" iterates over each index j while ensuring that we only compare each pair of strings once and avoid unnecessary duplication.
    # An inner loop is used whereby the line "for k in range(m):" iterates over each index k whereby m represents the he length of each string in the array S.
    # The inner loop represents each position in the strings that we will compare.
    # A conditional statement is used whereby the line "if S[i][k] == S[j][k]:", at each character position k, we compare the characters of the strings at indices i and j.
    # If the characters at position k in both strings are equal, it means we have found a common letter at that position for the pair of strings.
    # When a match is found, we return an array [i, j, k] representing the indices of the strings (i and j) and the position of the common letter (k).
    # If there are no common letters at any position we return an empty array [].

    n = len(S)
    m = len(S[0])
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(m):
                if S[i][k] == S[j][k]:
                    return [i, j, k]
    
    return []

# Test cases:
T1 = ["abc", "bca", "dbe"]
print(solution(T1))  

T2 = ["zzzz", "ferz", "zdsr", "fgtd"]
print(solution(T2))  

T3 = ["gr", "sd", "rg"]
print(solution(T3))  

T4 = ["bdafg", "ceagi"]
print(solution(T4))  
