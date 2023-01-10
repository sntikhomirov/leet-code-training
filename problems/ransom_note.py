class Solution:
    def can_construct(self, ransom_note: str, magazine: str) -> bool:
        ransom_set = set(ransom_note)
        result = False
        for letter in ransom_set:
            if ransom_note.count(letter) <= magazine.count(letter):
                result = True
            else:
                return False
        return result


def main():
    check = Solution()
    print(check.can_construct('a', 'b'))
    print(check.can_construct('aa', 'ab'))
    print(check.can_construct('aa', 'aab'))


if __name__ == "__main__":
    main()
