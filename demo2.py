from textblob import TextBlob
import nltk
nltk.download('averaged_perceptron_tagger')
myString = "Parts of speech: an article, to run, fascinating, quickly, and, of"
output = TextBlob(myString)
print(output.tags)