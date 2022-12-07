import csv
import datetime

import pandas
import pandas as pd
from flask import *

app = Flask(__name__)
transactions = pd.DataFrame
userstab = pd.DataFrame


def read_data():
    global transactions
    global userstab
    transactions = pd.read_csv("data/transactions.csv", sep=',',
                               dtype={'sender': str, 'recipient': str, 'datetime': str, 'amount': int})
    userstab = pd.read_csv("data/users.csv")




def write_tr(tr):
    with open("data/transactions.csv", newline='', mode='a') as trfile:
        trwriter = csv.writer(trfile, delimiter=',')
        trwriter.writerow(tr)

def write_users():
        userstab.to_csv(path_or_buf="data/users.csv",index=False)

def write_user(user):
    with open("data/users.csv", newline='', mode='a') as ufile:
        uwriter = csv.writer(ufile, delimiter=',')
        uwriter.writerow(user)

def write_transactions():
    with open("data/transactions.csv", newline='', mode='w') as trfile:
        trwriter = csv.writer(trfile, delimiter=',')
        trwriter.writerows(transactions.values)

def sort_transaction(trs):
    return sorted(trs, key=lambda i: i[2])


@app.route('/user', methods=["POST"])
def user_transactions():
    ut = []
    strbal = "This user does not exist ! <br><br>"
    user = request.form.get("uname")
    for t in transactions.values:
        if t[0] == user or t[1] == user:
            ut.append(t)

    s = '<body style = "background-image: url(' \
        "'https://images.pexels.com/photos/1103970/pexels-photo-1103970.jpeg'" \
        ');">'

    for u in userstab.values:
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
    global userstab

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
    if newSender:
        userstab = pd.concat([userstab,pd.DataFrame({'name':[sname], 'balance':[-amount]})] , ignore_index=True)
    if newRecipient:
        userstab = pd.concat([userstab,pd.DataFrame({'name':[rname], 'balance':[amount]})] , ignore_index=True)
    write_users()
    # add transaction to history
    write_tr([sname, rname, datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S"), amount])
    return '<body style="text-align:center; background-image: url(' + \
           "'https://images.pexels.com/photos/1103970/pexels-photo-1103970.jpeg'" + \
           ');">' \
           'Transaction added to database<br>' \
           '<form action="/" method="PUT"><input type="submit" value="Confirm"> </form>' \
           '</body>', 201


app.run(host='0.0.0.0', debug=True)
