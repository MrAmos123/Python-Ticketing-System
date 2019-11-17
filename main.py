from database import Database

user_raisedby = input(" [+] Enter your name: ")
user_shortdesc = input(" [+] Enter your issue: ")
db = Database()
print(" [INFO] Submitting data...")
db.ent_data(user_raisedby, user_shortdesc)
print(" [INFO] Data successfully submitted.")