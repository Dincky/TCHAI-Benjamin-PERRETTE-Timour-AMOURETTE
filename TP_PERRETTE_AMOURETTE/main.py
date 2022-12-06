import csv
import datetime
import pandas as pd
from flask import *


app = Flask(__name__)


def read_data():
    transactions = pd.read_csv("data/transactions.csv", sep=',',
                               dtype={'sender': str, 'recipient': str, 'datetime': str, 'amount': int})
    print(transactions.to_html())
    userstab = pd.read_csv("data/users.csv")
    return transactions, userstab


transactions, userstab = read_data()


def write_tr(tr):
    with open("data/transactions.csv", newline='\r',mode='a') as trfile:
        trwriter = csv.writer(trfile, delimiter=',')
        trwriter.writerow(tr)


def write_user(user):
    with open("data/users.csv", newline='\r',mode='a') as ufile:
        uwriter = csv.writer(ufile, delimiter=',')
        uwriter.writerow(user)


def sort_transaction(trs):
    return sorted(trs, key=lambda i: i[2])


@app.route('/user', methods=["POST"])
def user_transactions():
    ut = []
    strbal = "This user does not exist ! <br><br>"
    user = request.form.get("uname")
    print(user)
    for t in transactions.values:
        print("t " + t[0] + " " + t[1])
        if t[0] == user or t[1] == user:
            ut.append(t)

    s = '<body style = "background-image: url(' \
        "'https://images.pexels.com/photos/1103970/pexels-photo-1103970.jpeg'" \
        ');">'

    for u in userstab.values:
        print(u[0], u[1])
        if user == u[0]:
            strbal = "Your current balance is " + str(u[1]) + "<br><br>"
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
        print("tra:")
        print(tra)
        s += '<tr>'
        for item in tra:
            s += '<td>' + str(item) + '</td>'
        s += '</tr>'
    s += '</tbody>'

    return s + '</table>\n</body>', 201


@app.route('/')
def home():
    read_data()
    form = '' \
           '<body style = "background-image: url(' \
           + "'https://images.pexels.com/photos/1103970/pexels-photo-1103970.jpeg'" \
           + ');">' \
             '<form action="/confirm" method="POST"> ' \
             '<label for="sname">Sender:</label><br>  <input type="text" id="sname" name="sname"><br>  ' \
             '<label for="rname">Recipient:</label><br>  <input type="text" id="rname" name="rname"><br>' \
             '<label for="amnt">Amount:</label><br>  <input type="number" id="amnt" name="amnt">' \
             '<br><br><input type="submit" id "submit name="submit" value="Add Transaction">' \
             '</form>' \
             '<form action="/user" method="POST">' \
             '<label for="uname">Select user</label><input type="text" id="uname" name ="uname"> ' \
             '<input type="submit" value="Transaction history">' \
             ' <div bgcolor="FFFFFF">\n' \
             'test'
    s = transactions.to_html()
    return form + s + '</div>\n</table>\n</body>', 200


@app.route('/confirm', methods=['POST'])
def addtransaction():
    newSender = True
    newRecipient = True
    sname = request.form.get("sname")
    rname = request.form.get("rname")
    amount = int(request.form.get("amnt"))

    for u in userstab.values:
        if u[0] == sname:
            newSender = False
            u[1] -= amount
        if u[0] == rname:
            newRecipient = False
            u[1] += amount
    print(newSender, newRecipient)
    if newSender:
        write_user([sname, -amount])
    if newRecipient:
        write_user([rname, amount])

    # add transaction to history
    write_tr([sname,rname,datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S"),amount])

    return '<body style="text-align:center; background-image: url(' + \
           "'https://images.pexels.com/photos/1103970/pexels-photo-1103970.jpeg'" + \
           ');">' \
           'Transaction added to database<br>' \
           '<form action="/" method="PUT"><input type="submit" value="Confirm"> </form>' \
           '</body>', 201


app.run(host='0.0.0.0', debug=True)
