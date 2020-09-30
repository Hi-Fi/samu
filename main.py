from flask import Flask, request, jsonify
import json
import math
app = Flask(__name__)

vowels = "aeiouyäöå"

@app.route('/v1/samu', methods=['POST'])
def word_change():
    json_data = request.json
    return jsonify(change_words(json_data))

def change_words(original):
    original_splitted = original.split(" ")
    word_list = original.split()
    for i in range(math.floor(len(word_list)/2)):
        interesting_index = 2*i
        replacement = newWords(word_list[interesting_index], word_list[interesting_index+1])
        first_original_index = original_splitted.index(word_list[interesting_index])
        second_original_index = original_splitted.index(word_list[interesting_index+1])
        original_splitted[first_original_index] = replacement[0]
        original_splitted[second_original_index] = replacement[1]
    return " ".join(original_splitted)

def endOfSwap(word):
    looked_index = -1
    for index, char in enumerate(word):
        if char in vowels:
            looked_index = index
        elif looked_index > -1:
            return looked_index
    return len(word)-1

def newWords(word1, word2):
    word1_split_index = endOfSwap(word1)
    word2_split_index = endOfSwap(word2)
    return (f"{word2[:word2_split_index+1]}{word1[word1_split_index+1:]}", f"{word1[:word1_split_index+1]}{word2[word2_split_index+1:]}")

if __name__ == '__main__':
    app.run(threaded=True, port=5000)