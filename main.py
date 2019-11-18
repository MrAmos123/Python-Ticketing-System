from database import Database

while True:
    user_raisedby = input(" [+] Enter your name: ")
    user_shortdesc = input(" [+] Enter your issue: ")
    user_quit = input(" [-] Quit? (Y/[N]) ").lower()
    if user_quit == "y":
        break

db = Database()
print(" [INFO] Submitting data...")
db.ent_data(user_raisedby, user_shortdesc)
print(" [INFO] Data successfully submitted.")