import nltk
def prerequisites():
    nltk.download("punkt", download_dir=str("/tmp/punkt"))
    nltk.download("stopwords", download_dir=str("/tmp/stopwords"))
    nltk.download("averaged_perceptron_tagger", download_dir=str("/tmp/averaged_perceptron_tagger"))
    nltk.data.path.append("/tmp/punkt")
    nltk.data.path.append("/tmp/stopwords")
    nltk.data.path.append("/tmp/averaged_perceptron_tagger")