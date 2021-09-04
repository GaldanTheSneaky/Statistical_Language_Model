import nltk
from nltk import bigrams, trigrams, ngrams
from nltk.corpus import reuters
from collections import Counter, defaultdict
import random

def main():
    model = defaultdict(lambda: defaultdict(lambda: 0))
    for sentence in reuters.sents():
        for w1, w2, w3, w4 in ngrams(sentence, 4, pad_right=True, pad_left=True):
            model[(w1, w2, w3)][w4] += 1

    for w1_w2_w3 in model:
        total_count = float(sum(model[w1_w2_w3].values()))
        for w4 in model[w1_w2_w3]:
            model[w1_w2_w3][w4] /= total_count

    text = ["Japan", "has", "raised"]
    print(dict(model["Japan", "has", "raised"]))

    sentence_finished = False

    while not sentence_finished:
        r = random.random()
        accumulator = .0

        for word in model[tuple(text[-3:])].keys():
            accumulator += model[tuple(text[-3:])][word]
            if accumulator >= r:
                text.append(word)
                break

        if text[-3:] == [None, None, None]:
            sentence_finished = True

    print(' '.join([t for t in text if t]))


if __name__ == "__main__":
    main()