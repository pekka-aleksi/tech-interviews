Bag of Words: Very Simple REST API
===

This was for a senior python developer position with an emphasis on the ability to handle text data.
This tested for creating your own implementation of a Bag of Words algorithm, and creating an API to query it.


The test data `wikipedia.txt` is changed into `english.csv` with this code
 (This is just so if you want to try this with your own text)
```
import pandas as pd

df = pd.read_csv('wikipedia.txt', sep='|', header=None)

preprocessed_df = df[0].str.split('.', expand=True).unstack().dropna().reset_index(drop=True).to_frame()

preprocessed_df.index.name = 'Record ID'
preprocessed_df.columns = ['Title']
preprocessed_df['Languages'] = "English"

preprocessed_df.reset_index().to_csv('english.csv')
```

If the proper `data/english.csv` exists you can run `python create_models.py`
which should create `temp/stemmed_records.csv` - this has all but the text characters stripped out and the text has been normalized; and then the 'bag of words' model is created as `temp/BIGBAG_WITH_INDEX.pkl`

Once the `temporary` directory has the 2 proper files in place, you can run `python main.py` and access the API for the 'bagged words' at

```
http://localhost:5000/api/?records=0

{
  "5": 1, 
  "27": 1, 
  "49": 1, 
  "64": 1, 
  "73": 1, 
  "74": 1, 
  "79": 1, 
  "95": 1, 
  "102": 1, 
  "129": 1, 
  "139": 1, 
  "159": 1, 
  "169": 1, 
  "185": 1, 
  "198": 1, 
  "207": 1, 
  "210": 1, 
  "218": 1, 
  "225": 1, 
  "237": 2
}
```


https://en.wikipedia.org/wiki/Bag-of-words_model has a very good example of the model itself.
Apparently a reference implementation too.

