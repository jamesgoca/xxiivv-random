from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import webbrowser
import os
import csv

def main():
	if not os.path.isfile("links.csv"):
		xxvvii_ring_page = "https://webring.xxiivv.com/"

		page = urlopen(xxvvii_ring_page)

		soup = BeautifulSoup(page, "html.parser")

		names = soup.findAll("li")

		links = [n.a for n in names]

		print(links)

		with open("links.csv", "w+") as link_file:
			filewriter = csv.writer(link_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
			for l in links:
				filewriter.writerow([l["href"], l.text])

	with open("links.csv", "r") as link_file:
		filereader = csv.reader(link_file, delimiter=',')
		final_links = []
		for l in filereader:
			final_links.append([l[0], l[1]])

	random_link = random.choice(final_links)

	print(random_link)

	print("Opening {}".format(random_link[1]))

	webbrowser.open(random_link[0])

if __name__ == "__main__":
	main()