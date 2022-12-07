import csv
import datetime

import pandas
import pandas as pd
from flask import *

app = Flask(__name__)
transactions = pd.DataFrame
userstab = pd.DataFrame
IV = 0b01111000011000010111001101101000


def read_data():
    global transactions
    global userstab
    transactions = pd.read_csv("data/transactions.csv", sep=',',
                               dtype={'sender': str, 'recipient': str, 'datetime': str, 'amount': int, 'h' : str})
    userstab = pd.read_csv("data/users.csv")




def write_tr(tr):
    with open("data/transactions.csv", newline='', mode='a') as trfile:
        trwriter = csv.writer(trfile, delimiter=',')
        trwriter.writerow(tr)

def write_users():
        userstab.to_csv(path_or_buf="data/users.csv",index=False, mode='w')

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

def comp(a,b):
    return a ^ b

def XDDD(c):
    a = IV
    i = 0
    binlen = bin(len(c))
    binlen = binlen.replace("0b","")
    rest = len(c) % 4
    padding = "\x80" + "\0"* (3 - rest) if rest else ""
    restbin = len(binlen) % 4
    paddingbin = "\0" * (4 - restbin) if restbin else ""
    c += padding + binlen + paddingbin
    while i < len(c):
        A = ord(c[i]) << 24
        B = ord(c[i+1]) << 16
        C = ord(c[i+2]) << 8
        D = ord(c[i+3])
        a = comp(a, A+B+C+D)
        i = i + 4
    return hex(a)[2:]

@app.route('/verif')
def verif():
    a = ""
    for u in userstab.values:
        c = str(u[0])+str(float(u[1]))
        h = XDDD(c)
        if h == u[2]:
            a += "* " + str(u[0])+": est correcte" + "<br>"
        else:
            a += "* " + str(u[0])+": n'est pas correcte !!!!" + "<br>"

    for t in transactions.values:
        c = str(t[0])+str(t[1])+str(t[2])+str(t[3])
        h = XDDD(c)
        if h == t[4]:
            a += "* La transaction " + str(t) +": est correcte" + "<br>"
        else:
            a += "* La transaction " + str(t) +": n'est pas correcte !!!!" + "<br>"

    return "Page de verification : <br>" + a


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
        c = sname+str(float(-amount))
        h = XDDD(c)
        userstab = pd.concat([userstab,pd.DataFrame({'name':[sname], 'balance':[-amount], 'h':[h]})] , ignore_index=True)
    if newRecipient:
        c = rname+str(float(amount))
        h = XDDD(c)
        userstab = pd.concat([userstab,pd.DataFrame({'name':[rname], 'balance':[amount], 'h':[h]})] , ignore_index=True)
    write_users()
    # add transaction to history
    date = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    c = sname+rname+str(date)+str(amount)
    h = XDDD(c)
    write_tr([sname, rname, date, amount, h])
    return '<body style="text-align:center; background-image: url(' + \
           "'https://images.pexels.com/photos/1103970/pexels-photo-1103970.jpeg'" + \
           ');">' \
           'Transaction added to database<br>' \
           '<form action="/" method="PUT"><input type="submit" value="Confirm"> </form>' \
           '</body>', 201


app.run(host='0.0.0.0', debug=True)
