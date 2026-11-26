class Solution:

    def next_number(self, n):
        digit_sum = 0

        while n > 0:
            digit = n % 10
            digit_sum += digit ** 2
            n //= 10

        return digit_sum

    def isHappy(self, n: int) -> bool:
        # Implement Floyd's cycle detection here
        slow=n
        fast=self.next_number(n)
        while slow!=fast:
            slow=self.next_number(slow)
            fast=self.next_number(self.next_number(fast))

        if slow==1:
            return True
        else:
            return False