import nltk
def prerequisites():
    print(nltk.data.path) # to check the paths list

    """ Downloading all the dependencies to a specific directory locally and then uploading nltk_data.zip to a layer. """
    nltk.download("punkt", download_dir=str("nltk_data"))
    nltk.download("stopwords", download_dir=str("nltk_data"))
    nltk.download("averaged_perceptron_tagger", download_dir=str("nltk_data"))

    """ 
    The files in the layer can be accessed as 'opt/nltk_data'. Hence adding the path to the nltk.data.path list.
    nltk.data.path.append("opt/nltk_data")
    
    """

prerequisites()