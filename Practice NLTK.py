import nltk
from nltk.corpus import stopwords

s = '''Good muffins cost $3.88\nin New York.  Please buy me
    ... two of them.\n\nThanks.'''
    
tokens = nltk.wordpunct_tokenize(s)

filtered = [w for w in tokens if not w in set(stopwords.words('english'))]
