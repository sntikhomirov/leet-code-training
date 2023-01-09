class Solution:
    """
    Given an integer n, return a string array answer (1-indexed) where:

    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.\n
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true.
    """
    def fizzbuzz(self, n: int) -> list[str]:
        answer = []
        for i in range(1, n+1):
            if i % 15 == 0:
                answer.append('FizzBuzz')
            elif i % 3 == 0:
                answer.append('Fizz')
            elif i % 5 == 0:
                answer.append('Buzz')
            else:
                answer.append(str(i))

        return answer


def main():
    check = Solution()
    print(check.fizzbuzz(n=3))
    print(check.fizzbuzz(n=5))
    print(check.fizzbuzz(n=15))


if __name__ == "__main__":
    main()
