import datetime
import random

from flask import *

app = Flask(__name__)
names = ['Zorro']

transactions = [["ana", "bob", datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S"), str(random.randint(0, 100))],
                ["paul", "franck", "11/08/2022 11:42:18", str(random.randint(0, 100))],
                ]

def aff_transaction(transactions):
    transactions = sorted(transactions, key=lambda i: i[2])
    return transactions

@app.route('/')
def hello():
    st = 'Transactions <ul>' + ''.join([])
    for n in aff_transaction(transactions):
        st += '<li> '
        for o in n:
            st += o + ' '
    return st + '</ul>\n', 200


@app.route('/user/<uname>', methods=['PUT'])
def add(uname):
    names.append(uname)
    return 'User ' + uname + ' added.\n', 201


@app.route('/user/<uname>', methods=['DELETE'])
def rem(uname):


    if uname not in names:
        return 'User ' + uname + ' does not exists.\n', 404
    names.remove(uname)
    return 'User ' + uname + 'removed.\n', 200


app.run(host='0.0.0.0', debug=True)
