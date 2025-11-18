class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        result = []
        sorted_word = sorted(self.word)
        for candidate in word_list:
            if sorted(candidate.lower()) == sorted_word:
                result.append(candidate)
        return result
