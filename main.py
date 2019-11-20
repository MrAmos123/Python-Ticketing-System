from database import Database
from flask import Flask, request, render_template    

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def my_form_post():
    user_raisedby = request.form['user_raisedby']
    user_shortdesc = request.form['user_shortdesc']
    return "%s\n%s" % (user_raisedby, user_shortdesc)

if __name__ == '__main__':
    app.run(debug=True)

# MOVE TO ANOTHER FILE
#db = Database()
#while True:
#    user_raisedby = input("\n [+] Enter your name: ")
#    while len(user_raisedby) < 2:
#        print("\n [ERROR] Please enter some data.")
#        user_raisedby = input(" [+] Enter your name: ")
#        if not len(user_raisedby) < 2:
#            break
#
#    user_shortdesc = input("\n [+] Enter your issue: ")
#    while len(user_shortdesc) < 2:
#        print("\n [ERROR] Please enter some data.")
#        user_shortdesc = input(" [+] Enter your issue: ")
#        if not len(user_shortdesc) < 2:
#            break
#
#    db.ent_data(user_raisedby, user_shortdesc)
#
#    user_quit = input("\n [-] Quit? (Y/[N]) ").lower()
#    if user_quit == "y":
#        print("\n [INFO] Committing data and closing.")
#        break
#
#    user_raisedby = None
#    user_shortdesc = None
#
#
#
#db.close_cursor()