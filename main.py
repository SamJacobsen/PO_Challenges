VOWELS = "aeiou"


def repeated(s: str) -> bool:
    return s in (s + s)[1: -1]


def get_vowel_substrings(s: str) -> list:
    if s and s.isalpha():
        vowel_indexes: list = []
        answer = set()

        for index, c in enumerate(s):
            if c in VOWELS:
                answer.add(c)
                vowel_indexes.append(index)

        answer = answer.union(index_substrings(vowel_indexes, s))
        return sorted(answer)
    return []


def get_consonant_substrings(s: str) -> list:
    if s and s.isalpha():
        consonant_indexes: list = []
        answer = set()

        for index, c in enumerate(s):
            if c not in VOWELS:
                answer.add(c)
                consonant_indexes.append(index)

        answer = answer.union(index_substrings(consonant_indexes, s))
        return sorted(answer)
    return []


def index_substrings(indexes: list, s: str) -> set:
    answer = set()
    while len(indexes) > 1:
        start = indexes.pop(0)
        for index in indexes:
            sub_string = s[start:index+1]
            answer.add(sub_string)
    return answer


if __name__ == "__main__":
    print(get_vowel_substrings("apple"))
    print(get_vowel_substrings("hmm"))
    print(get_consonant_substrings("aviation"))
    print(get_consonant_substrings("motor"))
    print()
    print(repeated("a"))
    print(repeated("ababab"))
    print(repeated("aba"))
    print(repeated("abcabcabcabc"))
    print(repeated("aaxxtaaxztaaxxt"))
