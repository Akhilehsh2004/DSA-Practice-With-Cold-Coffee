class Solution:
    @staticmethod
    def getLucky(s: str, k: int) -> int:
        # Step 1: Convert string into the integer by replacing letters with their positions
        num = "".join(str(ord(char) - ord('a') + 1) for char in s)

        # Step 2: Sum the digits k times
        for _ in range(k):
            num = sum(int(digit) for digit in str(num))

        return num

# Example usage:
s = "zbax"
k = 2
print(Solution.getLucky(s, k))  # Output: 8
