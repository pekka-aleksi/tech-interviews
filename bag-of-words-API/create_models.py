import pandas as pd
import pickle
from nltk.stem import PorterStemmer
import string
import collections
import os


def get_preprocessed_records(filename):
    # we assume for now that the index column is unique - although it shouldn't matter for this exercise
    df = pd.read_csv(filename,
                     low_memory=False,
                     usecols=['Record ID', 'Title', 'Languages'],
                     index_col=['Record ID'],
                     encoding='utf8')  # assume original data is in UTF8 since we need to remove special chars
       
    df.index = df.index.astype(str)

    """
                    Languages                                              Title
    Record ID                                                                   
    (Uk)EN000561198       NaN  Mesozoic radiolarian biostratigraphy of Japan ...
    (Uk)EN000561204       NaN  Significance of Mesozoic radiolarians for tect...
    (Uk)EN000561216       NaN  Tectonostratigraphy of Mino terrane: Jurassic ...
    (Uk)EN000561228       NaN  Age of the covering strata in the Kurosegawa T...
    (Uk)EN000561230       NaN  Jurassic-Early Cretaceous tectonic evolution o...
    """

    # we could be removing duplicates and cleaning up the Record IDs too but since not being asked to do so, let's
    # ignore it for now

    df = df[df.Languages == 'English']  # strip out the non-english titles at this point
    df = df[['Title']]  # basically our data is one Series (dealt with as a DataFrame)

    df = df.apply(lambda r: r.str.replace('[{}]'.format(string.punctuation), ''))
    """                                                             Title
    Record ID                                                         
    (Uk)RN000444200  Tectonic and paleoclimatic significance of a p...
    (Uk)RN000444212  Molluscan death assemblages on the Amazon Shel...
    (Uk)RN000444224  Postglacial Permian stratigraphy and geography...
    (Uk)RN000444236  Rudists as gregarious sedimentdwellers not ree...
    (Uk)RN000444248  Lakelevel fluctuations at Ljustjaernen central...
    """

    df = df.apply(lambda r: r.str.lower())
    """                                                             Title
    Record ID                                                         
    (Uk)RN000444200  tectonic and paleoclimatic significance of a p...
    (Uk)RN000444212  molluscan death assemblages on the amazon shel...
    (Uk)RN000444224  postglacial permian stratigraphy and geography...
    (Uk)RN000444236  rudists as gregarious sedimentdwellers not ree...
    (Uk)RN000444248  lakelevel fluctuations at ljustjaernen central...
    """

    df = df['Title'].str.split(expand=True).fillna('')
    # the expand parameter 'explodes' the titles into lots of cols

    """                          0             1              2                 3   \
    Record ID                                                                     
    (Uk)RN000444200     tectonic           and  paleoclimatic      significance   
    (Uk)RN000444212    molluscan         death    assemblages                on   
    (Uk)RN000444224  postglacial       permian   stratigraphy               and   
    (Uk)RN000444236      rudists            as     gregarious  sedimentdwellers   
    (Uk)RN000444248    lakelevel  fluctuations             at      ljustjaernen  """

    df = df.apply(lambda r: r.str.replace('\d+', 'number'))

    return df


def create_stemmed_records(df):
    stemmer = PorterStemmer()

    sdf = pd.DataFrame([[" ".join([stemmer.stem(word) for word in row if len(word)])] for _, row in df.iterrows()],
                       index=df.index, columns=['Title'])

    return sdf


def create_bag_of_words(df):
    BIGBAG = set()

    for rowbag in [v for _, v in df['Title'].str.split(' ').iteritems()]:
        BIGBAG = BIGBAG.union({*rowbag})

    BIGBAG_WITH_INDEX = {word: i for i, word in enumerate(BIGBAG)}

    return BIGBAG_WITH_INDEX


def RETURN_ENCODED_string(record, recs_to_use, bag_to_use):

    encoded_record = recs_to_use.loc[record].replace('', pd.np.nan).dropna().to_frame()
    # the only thing we DON'T re-create is the bag of words itself

    # we re-create the STEMMED records at this point every time
    X = create_stemmed_records(encoded_record)

    vector_indices = collections.Counter()

    for word in X.Title:
        word_index = bag_to_use[word]
        vector_indices[word_index] += 1

    return dict(vector_indices)  # our function is returning RECORD vs. index_vector(STEMMED_WORDS)


if __name__ == '__main__':

    if not os.path.exists('temp/'):
        os.makedirs('temp/')
        
    print("Getting preprocessed records!")
        
    records = get_preprocessed_records('data/english.csv')
    print("Creating stemmed records!")
    stemmed_records = create_stemmed_records(records)
    print("Saving stemmed records to disk!")
    stemmed_records.to_csv('temp/stemmed_records.csv', index=True, encoding='utf8')
    print("Creating bag of words!")
    BAG = create_bag_of_words(stemmed_records)

    with open('temp/BIGBAG_WITH_INDEX.pkl', 'wb') as baghandler:
        print("Saving bag of words to disk!")
        pickle.dump(BAG, baghandler, protocol=pickle.HIGHEST_PROTOCOL)
        