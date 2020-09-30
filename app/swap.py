from typing import List, Tuple
import math 

vowels = "aeiouyäöå"

def change_words(original: str):
    original_splitted = original.split(" ")
    word_list = original.split()
    last_handled_word_index = 0
    # Take pairs. We're only interested full pairs, not uneven one
    for i in range(math.floor(len(word_list)/2)):
        first_word_index = 2*i
        replacement = get_new_words(word_list[first_word_index], word_list[first_word_index+1])
        indices = find_indices_to_replace(original_splitted, word_list, first_word_index, last_handled_word_index)
        original_splitted[indices[0]] = replacement[0]
        original_splitted[indices[1]] = replacement[1]
        # We have to start search from next index next time, as second found index is swapped already
        last_handled_word_index = indices[1]+1
    return " ".join(original_splitted)

def find_indices_to_replace(splitted_input: List[str], word_list: List[str], search_index: int, last_handled_index: int) -> Tuple[int, int]:
    first_swap_word_index = splitted_input.index(word_list[search_index], last_handled_index)
    second_swap_word_index = splitted_input.index(word_list[search_index+1], last_handled_index)
    return (first_swap_word_index, second_swap_word_index)

def length_to_swap(word: str) -> int:
    looked_index = -1
    for index, char in enumerate(word):
        if char in vowels:
            looked_index = index
        elif looked_index > -1:
            return looked_index
    return len(word)-1

def get_new_words(word1: str, word2: str) -> Tuple[str, str]:
    word1_split_index = length_to_swap(word1)
    word2_split_index = length_to_swap(word2)
    return (f"{word2[:word2_split_index+1]}{word1[word1_split_index+1:]}", f"{word1[:word1_split_index+1]}{word2[word2_split_index+1:]}")