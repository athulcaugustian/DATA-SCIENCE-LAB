import nltk
nltk.download('punkt')
new="The big cat ate little mouse who was after a fresh cheese."
new_tokens=nltk.word_tokenize(new)
print(new_tokens)

new_tag=nltk.pos_tag(new_tokens)
print(new_tag)
grammar=r"NP:{<DT>?<JJ>*<NN>}"
chunkParser=regexpParser.grammar(new_tag)
chunked=chunkParser.parser
print(chunked)