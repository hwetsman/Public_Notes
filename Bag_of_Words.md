`from sklearn.feature_extraction.text import CountVectorizer
vertorizer = CountVectorizer()
string1="This is a string of words"
string2="And here is another string"
string3="Finally, we have another example of a string of words"
list1=[string1,string2,string3]
bag_of_words = vectorizer.fit(list1)
bag_of_words = vercotizer.transform(list1)`

vectorizer.vocabulary_ returns a dict of words in the corpus by their feature index
vectorizer.stop_words_ returns a set of words that were ignored

The default for stop_words is None. "If ‘english’, a built-in stop word list for English is used. 
There are several known issues with ‘english’ and you should consider an alternative"
You can get stopwords from nltk
`from nltk.corpus import stopwords
sw = stopwords.words('english')`

To lower the demensionality of features, we want to stem words. Making your own stemming function is problematic. There are 
stemming functions already there done by professional linguists. 
`from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer('english')
stemmer.stem('responsive')`
'respons'
`stemmer.stem('unresponsive')`
'unrespons'
This may be a limit for this stemmer. You may not want un to be maintained in stemming. 
You want to stem before you create bag of words.

TFIDF
tf = 'term frequency' - greater weight to those words that occur more frequently in the document
idf = 'inverse document frequency' - lesser weight to those words that occur more frequently in the corpus
This coding makes the words in a document that are rare in the corpus stand out and gives more information for predicting
labels from each document.
