import requests
import json
import sqlite3

url = 'https://uselessfacts.jsph.pl/random.json?language=en'

response = requests.get(url)
print(f"status code: {response.status_code}")
print(f"headers: {response.headers}")

data = response.json()

with open("random_faqtebi.json", "w") as randomfaqtebi:
    json.dump(data, randomfaqtebi, indent = 4)

with open("random_faqtebi.json", "r") as randomfaqtebi:
    randomfact = json.load(randomfaqtebi)

fact = data.get("text")
print(f"random fact: {fact}")


conn = sqlite3.connect("randomfacts.db")
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS randomfacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fact TEXT
    )
''')

c.execute("""
INSERT INTO randomfacts (fact) VALUES (?)
""", (fact,))


conn.commit()
conn.close()