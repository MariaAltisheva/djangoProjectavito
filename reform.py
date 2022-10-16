import csv, sqlite3

con = sqlite3.connect("db.sqlite3")
cur = con.cursor()

with open('fixture/ads.csv', 'r', encoding='utf-8') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['Id'], i['name'], i['author'], i['price'], i['description'], i['address'], i['is_published']) for i in
             dr]

cur.executemany(
    "INSERT INTO ads_ads (id, name, author, price, description, address, is_published) VALUES (?, ?, ?, ?, ?, ?, ?);",
    to_db)
con.commit()

with open('fixture/categories.csv', 'r', encoding='utf-8') as fin:  # `with` statement available in 2.5+
    dr = csv.DictReader(fin)
    to_db = [(i['id'], i['name']) for i in dr]

cur.executemany(
    "INSERT INTO ads_category (id, name) VALUES (?, ?);", to_db)
con.commit()
con.close()