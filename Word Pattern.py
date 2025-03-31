class Solution:
  def wordPattern(self, pattern: str, s: str) -> bool:
    words = s.split()
    if len(pattern) != len(words):
      return False

    char_to_word = {}
    word_to_char = {}

    for char, word in zip(pattern, words):
      if char not in char_to_word:
        char_to_word[char] = word
      if word not in word_to_char:
        word_to_char[word] = char

      if char_to_word[char] != word or word_to_char[word] != char:
        return False

    return True
