"""
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]] 
"""
# bruteforce method 
"""
1.	We know anagram means we can create different words with the same characters.
2.	So to check whether we have anagrams or not, we can simply sort the word and then check that sorted word with other words (which  should also be sorted). If both are the same, then it is an anagram, so we can add it to the group.
3.	Whether there is an anagram or not, a word should be grouped, so we create the group array by adding the first word. Then we use a  loop to check the other words to see whether they are anagrams or not.
4.	To know whether we already checked this word or not, we use a visited array with False. When we have checked it, we turn it into True so that we can avoid duplicates in the group array. Also, we don’t want to create duplicate groups.

▶ Step 1: Initial Setup
visited = [False, False, False, False, False, False]
output = []

▶ Step 2: First outer loop (i = 0)

strs[0] = "eat" and visited[0] = False
Create new group: group = ["eat"], mark visited[0] = True

Inner loop j = 1 to 5:
j = 1 → "tea" → sorted("eat") == sorted("tea") ✅
→ Add to group: group = ["eat", "tea"], visited[1] = True

j = 2 → "tan" → sorted("eat") != sorted("tan") ❌
j = 3 → "ate" → sorted("eat") == sorted("ate") ✅
→ Add to group: group = ["eat", "tea", "ate"], visited[3] = True

j = 4 → "nat" → not equal ❌
j = 5 → "bat" → not equal ❌

→ Add ["eat", "tea", "ate"] to output.

▶ Step 3: Next iterations
i = 1 → visited already ✅ → skip

✅ Final Output:
[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

"""
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        visited = [False] * n
        output = []
        for i in range(n):
            if visited[i] == False:
                group = [strs[i]]
                visited[i] = True
                for j in range(i+1,n):
                    if visited[j] == False and sorted(strs[i]) == sorted(strs[j]):
                        group.append(strs[j])
                        visited[j] = True
                output.append(group)
        return output

# optimal method

from collections import defaultdict
def groupAnagrams(strs):
    n = len(strs)
    anagram_groups = defaultdict(list)
    for word in strs:
        count =[0]*26
        for char in word:
            count[ord(char) - ord("a")] += 1
        key = tuple(count) # key cannot be list which is mutable 
        anagram_groups[key].append(word) # since we are using the deafultdict(list)
        # it will create the key and append the word to the list if the key is not already there
    return list(anagram_groups.values())