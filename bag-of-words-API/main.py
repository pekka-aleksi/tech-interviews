from flask import Flask, request, jsonify

app = Flask(__name__)



import pickle
from create_models import get_preprocessed_records, RETURN_ENCODED_string

with open('temp/BIGBAG_WITH_INDEX.pkl', 'rb') as newbag:
    bag = pickle.load(newbag)

records = get_preprocessed_records('data/english.csv')

print(records)


# for some reason the variable rules ARE NOT WORKING with this setup
# maybe it's a python 2 thing where the flask version is old
@app.route('/api/')
def get_bow_vector():

    global bag
    record = request.args.get('record')

    print(type(record))
    
    ret = RETURN_ENCODED_string(record=record, recs_to_use=records, bag_to_use=bag)

    return jsonify(ret)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
