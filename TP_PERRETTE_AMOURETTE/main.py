import datetime
import random
from flask import *


class user:
    def __init__(self, name):
        self.name = name
        self.bal = 0

    def change_balance(self, amount):
        self.bal += amount


app = Flask(__name__)
transactions = [["ana", "bob", datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S"), str(random.randint(0, 100))],
                ["paul", "franck", datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S"), str(random.randint(0, 100))],
                ["paul", "franck", datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S"), str(random.randint(0, 100))],
                ["paul", "franck", datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S"), str(random.randint(0, 100))],
                ["paul", "franck", "11/08/2022 12:48:18", str(random.randint(0, 100))],
                ]
p1 = user("ana")
users = [user('bob'), p1]


def sort_transaction(trs):
    return sorted(trs, key=lambda i: i[2])


@app.route('/user', methods=["POST"])
def user_transactions():
    ut = []
    user = request.form.get("uname")
    for t in transactions:
        if t[0] == user or t[1] == user:
            ut.append(t)

    s = '<body style = "background-image: url(' + "'https://images.pexels.com/photos/1103970/pexels-photo-1103970.jpeg'"\
        + ');">'
    for u in users:
        if user == u.name:
            strbal = "Your current balance is " + str(u.bal) + "<br><br>"
            break

    s += strbal + '<table border="1" bgcolor="#FFFFFF">' \
        '<thead><tr><th colspan="4" bgcolor="A0A8A6">Transactions</th>' \
        '</tr></thead>' \
        '<tbody><tr>' \
        '<td>Sender</td>' \
        '<td>Recipient</td>' \
        '<td>Date</td>' \
        '<td>Amount</td>' \
        '</tr>'

    for tra in sort_transaction(ut):
        s += '<tr>'
        for item in tra:
            s += '<td>' + item + '</td>'
        s += '</tr>'
    s += '</tbody>'

    return s + '</table>\n</body>', 201


@app.route('/')
def home():
    form = ''\
        '<body style = "background-image: url(' + "'https://images.pexels.com/photos/1103970/pexels-photo-1103970.jpeg'"\
        + ');">' \
        '<form action="/confirm" method="POST"> ' \
        '<label for="sname">Sender:</label><br>  <input type="text" id="sname" name="sname"><br>  ' \
        '<label for="rname">Recipient:</label><br>  <input type="text" id="rname" name="rname"><br>' \
        '<label for="amnt">Amount:</label><br>  <input type="number" id="amnt" name="amnt">' \
        '<br><br><input type="submit" id "submit name="submit" value="Add Transaction">' \
        '</form>' \
        '<form action="/user" method="POST">'\
        '<label for="uname">Select user</label><input type="text" id="uname" name ="uname"> ' \
        '<input type="submit" value="Transaction history">' \
        ' \n'
    s = '' \
        '<table border="1" bgcolor="#FFFFFF">' \
        '<thead><tr><th colspan="4" bgcolor="A0A8A6">Transactions</th>' \
        '</tr></thead>' \
        '<tbody><tr>' \
        '<td>Sender</td>' \
        '<td>Recipient</td>' \
        '<td>Date</td>' \
        '<td>Amount</td>' \
        '</tr>'

    for tra in sort_transaction(transactions):
        s += '<tr>'
        for item in tra:
            s += '<td>' + item + '</td>'
        s += '</tr>'
    s += '</table></tbody>'

    return form + s + '</table>\n</body>', 200


@app.route('/confirm', methods=['POST'])
def addtransaction():

    for u in users:
        if

    transactions.append([request.form.get("sname"),
                         request.form.get("rname"),
                         datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S"),
                         request.form.get("amnt")])

    return '<body style="text-align:center; background-image: url(' +\
           "'https://images.pexels.com/photos/1103970/pexels-photo-1103970.jpeg'" + \
           ');">' \
           'Transaction added to database<br>' \
           '<form action="/" method="PUT"><input type="submit" value="Confirm"> </form>'\
           '</body>', 201


app.run(host='0.0.0.0', debug=True)
