from database import Database
db = Database()

while True:
    user_raisedby = input("\n [+] Enter your name: ")
    while len(user_raisedby) < 2:
        print("\n [ERROR] Please enter some data.")
        user_raisedby = input(" [+] Enter your name: ")
        if not len(user_raisedby) < 2:
            break

    user_shortdesc = input("\n [+] Enter your issue: ")
    while len(user_shortdesc) < 2:
        print("\n [ERROR] Please enter some data.")
        user_shortdesc = input(" [+] Enter your issue: ")
        if not len(user_shortdesc) < 2:
            break

    db.ent_data(user_raisedby, user_shortdesc)

    user_quit = input("\n [-] Quit? (Y/[N]) ").lower()
    if user_quit == "y":
        print("\n [INFO] Committing data and closing.")
        break

    user_raisedby = None
    user_shortdesc = None

db.close_cursor()