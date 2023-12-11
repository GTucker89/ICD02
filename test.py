import nltk
from nltk.corpus import wordnet

# Download WordNet data
nltk.download('wordnet')

def generate_noun_list(num_nouns=1000):
    nouns = set()
    count = 0

    for synset in list(wordnet.all_synsets(pos='n')):
        for lemma in synset.lemmas():
            nouns.add(lemma.name())
            count += 1
            if count >= num_nouns:
                return list(nouns)[:num_nouns]

# Generate a list of 1000 nouns
noun_list = generate_noun_list(1000)

# Print the first 50 nouns as an example
print(noun_list[:50])
