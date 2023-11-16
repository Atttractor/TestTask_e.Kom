from tinydb import TinyDB

db = TinyDB('db.json')

db.insert({"form1_name": "Form 1 (email, phone)",
           "form1_email": "email",
           "form1_phone": "phone"})
db.insert({"form2_name": "Form 2 (email, date, phone)",
           "form2_email": "email",
           "form2_date": "date",
           "form2_phone": "phone"})
db.insert({"form3_name": "Form 3 (email, date, phone)",
           "form3_text": "text",
           "form3_date": "date",
           "form3_phone": "phone"})
