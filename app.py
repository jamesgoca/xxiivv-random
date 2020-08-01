from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import webbrowser

def main():
	xxvvii_ring_page = "https://webring.xxiivv.com/"

	page = urlopen(xxvvii_ring_page)

	soup = BeautifulSoup(page, "html.parser")

	names = soup.findAll("li")

	links = [n.a for n in names]

	random_link = random.choice(links)

	print("Opening {}".format(random_link.text))

	webbrowser.open(random_link["href"])

if __name__ == "__main__":
	main()