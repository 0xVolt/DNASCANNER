# Script to implement sliding window functionality on an entered DNA sequence to count the frequency of nucleotides
# This script is a temporary program to test working with json files in exporting data from a dictionary in Python

# Import json library
import json

# Function to implement sliding window functionality
def slidingWindow(seq, windowWidth):
    A = dict()
    length = len(seq)
    
    for i in range(length - windowWidth + 1):
        aCount = 0
        for j in range(i, windowWidth + i):
            if seq[j] == 'a':
                aCount += 1
        A[i] = aCount

    return A

# Sample DNA sequence obtained from an online generator
seq = 'aaaacggttcccccagccggatccttcttcaaacgtacctgagacgtcc'

# Passing in window size of 3
ret = slidingWindow(seq, 3)

# Serializing by exporting data to a JSON object
retJSON = json.dumps(ret, indent=4)

# Printing results
print(retJSON)