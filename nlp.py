#Stop words example

# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# eg = "This is an example for stop word filteration"
# stop = set(stopwords.words('english'))
# words = word_tokenize(eg)
# filtered = [w for w in words if not w in stop]
# print(filtered)



#stemming
#import nltk
# from nltk.stem import PorterStemmer
# from nltk.tokenize import sent_tokenize, word_tokenize
#
# words = ["game", "gaming", "gamed", "games"]
# ps = PorterStemmer()
#
# for word in words:
#     print(ps.stem(word))


 #for sentence
# from nltk.stem import PorterStemmer
# from nltk.tokenize import sent_tokenize, word_tokenize
#
# ps = PorterStemmer()
#
# sentence = "gaming, the gamers play games"
# words = word_tokenize(sentence)
#
# for word in words:
#     print(word + ":" + ps.stem(word))

# import nltk
# from nltk.stem import PorterStemmer
#
# stemmer = PorterStemmer()
#
# print(stemmer.stem('eating'))



# speech tagging
# import nltk
# from nltk import word_tokenize, pos_tag
# text = "I am learning python"
# tokens = word_tokenize(text)
# print(pos_tag(tokens))


# #WORDNET(get definitions and examples from wordnet)
# import nltk
# from nltk.corpus import wordnet
# syn = wordnet.synsets("friend")
# print(syn[0].definition())
# print(syn[0].examples())

#WORDNET(get synonyms from wordnet)
import nltk
from nltk.corpus import wordnet
synonyms = []
for syn in wordnet.synsets('Computer'):
  for lemma in syn.lemmas():
        synonyms.append(lemma.name())
print(synonyms)

#WORDNET(get antonyms from wordnet)

# import nltk
# from nltk.corpus import wordnet
# antonyms = []
# for syn in wordnet.synsets("good"):
#     for l in syn.lemmas():
#      if l.antonyms():
#             antonyms.append(l.antonyms()[0].name())
# print(set(antonyms))

#
# Lemmatization
# import nltk
# from nltk.stem import WordNetLemmatizer
# lemmatizer = WordNetLemmatizer()
# print(lemmatizer.lemmatize('playing', pos="v"))
# print(lemmatizer.lemmatize('playing', pos="n"))
# print(lemmatizer.lemmatize('better', pos="a"))
# print(lemmatizer.lemmatize('playing', pos="r"))











