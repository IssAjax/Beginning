#Ransom Note //leetcode 
'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #set self
        self.ransomNote = ransomNote
        self.magazine = magazine

        #Empty list to append and remove from 
        tion = []
        if len(ransomNote) >= 1 and len(magazine) <= 100000:
            #Append the ransomnote characters to the list
            for i in ransomNote.lower():
                tion.append(i)

            #remove the characters from the magazine and if the var doesn't exist continue
            for t in magazine.lower():
                if t not in tion:
                    continue
                tion.remove(t)

            #Set bool values to the list 
            if tion == []:
                return f'{tion} is empty {True}'
            else:
                return f'{tion} still exists {False}'
        else:
            return 'out of range'

#running through __main__ 
if __name__ == '__main__':
    s = Solution()
    #canConstruct(ransomNote, magazine)
    #order and 
    print(s.canConstruct("abaz", "aabcz"))
        
