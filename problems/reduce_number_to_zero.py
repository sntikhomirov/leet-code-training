class Solution:
    """
    Given an integer num, return the number of steps to reduce it to zero.

    In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
    """
    def number_of_steps(self, num: int) -> int:
        steps = 0
        while num != 0:
            if num % 2 == 0:
                num = num / 2
            else:
                num = num - 1
            steps += 1
        return steps


def main():
    check = Solution()
    print(check.number_of_steps(num=14))
    print(check.number_of_steps(num=8))
    print(check.number_of_steps(num=123))


if __name__ == "__main__":
    main()
