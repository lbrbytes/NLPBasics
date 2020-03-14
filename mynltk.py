import string
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet


def GiveMeSomeText():
    mytext = "Welcome to the world of programming. Java is just as stupid as Human language ! However it makes " \
             " you earn $100 and sometimes £2000 per hour starting 30-12-1531 or may be 1531-12-30"
    return mytext;


def Tokenize(sometext: string, language: string = "english"):
    # tokenize with a regular expression
    # I have defined regular expressions for currency (actually $ and £)
    # I have defined regular expressions for dates as : dd-mm-yyyy and yyyy-mm-dd
    # You can define your own regular expressions depending on your needs (even in a seperate configuration file
    patterns4currency = "\w+\$[\d\.]+|\£[\d\.]+"
    patterns4dates = "[\d{4}\-\d{2}\-\d{2}]+"
    mypatterns = patterns4currency + patterns4dates + "|\S+"
    mytokenizer = nltk.RegexpTokenizer(mypatterns);
    tokens = mytokenizer.tokenize(sometext)
    # tokens = nltk.word_tokenize(sometext, language)
    return tokens;


def nltk_to_wordnet_POSTags(tag):
    # Maps NLTK POS tags to the first character wordnet lemmatizer accepts
    tag = tag[0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)


def lemmatizeMyText(mylemmatizer, POStxt):
    # returns a list of lemmatized text for POS tagged one
    return ([mylemmatizer.lemmatize(w[0], nltk_to_wordnet_POSTags(w[1])) for w in POStxt]);


def rmvStopWords(lmzTxt: string, language: string = "english"):
    stopWords = set(stopwords.words(language))
    lems_without_sw = [word for word in lmzTxt if not word in stopWords]
    return (lems_without_sw);


def rmvPonct(lmzTxt: string):
    # getting list of ponctuations: could be enriched by adding any kind of symbols
    lstponct = string.punctuation
    cleanWords = [word for word in lmzTxt if not word in lstponct]
    return (cleanWords)


def main():
    # 0.Getting some stupid text
    sometxt = GiveMeSomeText()
    print(sometxt)

    # 1.Tokenizing (word level)
    print("****** TOKENIZATION (WORDS)")
    tokenizedTxt = Tokenize(sometxt)
    print(tokenizedTxt)

    # 2.POS tagging
    postxt = nltk.pos_tag(tokenizedTxt)
    print("****** PART OF SPEECH TAGGING")
    print(postxt)

    # 3.Lemmatization using Wordnet
    print("****** LEMMATIZATION")
    mylemmatizer = nltk.WordNetLemmatizer()
    lemmatizedTxt = lemmatizeMyText(mylemmatizer, postxt)
    print(lemmatizedTxt)

    # 4.Stopping words
    print("****** REMOVING STOP WORDS")
    txtRoots = rmvStopWords(lemmatizedTxt)
    print(txtRoots)

    # 5.Removing ponctuations
    print("****** REMOVING PONCTUATION")
    cleanTxtRoots = rmvPonct(txtRoots)
    print(cleanTxtRoots)


main()
