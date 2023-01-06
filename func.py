import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize
from sklearn import linear_model
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('stopwords')
from nltk.corpus import stopwords

def preprocess(phrase):
    if type(phrase) != str:
            raise TypeError("Please type the string")
    phrase = re.sub('[^\w\s]',' ', phrase)
    phrase = phrase.lower()
    text_tokens = word_tokenize(phrase)
    pattern = re.compile(r'\b(' + r'|'.join(stopwords.words('english')) + r')\b\s*')
    phrase = pattern.sub('', phrase)
    return(phrase)


# p = supp_virg("Je m'étais un peu lassé du style de Dreamworks Animations ; mais après le film , j'avais vraiment kiffé ce renouvellement de faire un mélange entre l'animation américaine et des touches d'animation japonaise. Et j'ai trouvé ce second film sur le Chat Potté excellent bien que le premier reste supérieur mais de peu. Le scénario est assez innovant mais il y a quelques facilités et la mise en image est vraiment très belle.")
# print(p)

# from modules import preprocess
