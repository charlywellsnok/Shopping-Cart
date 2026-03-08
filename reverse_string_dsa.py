Qu. Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.








class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #First create an empty stack
        #add the stack values to the stack
        #then pop it
        #put it back at the index position

        stack = []
        for char in s:
            stack.append(char)

        for i in range(len(s)):
            s[i] = stack.pop()
