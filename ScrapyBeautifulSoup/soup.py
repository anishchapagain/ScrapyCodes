from bs4 import BeautifulSoup
from urllib2 import urlopen
from time import sleep  # be nice
import csv

BASE_URL = "http://www.chicagoreader.com"
COUNT = 0


def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")


def get_category_links(section_url, count):
    soup = make_soup(section_url)
    boccat = soup.find("dl", "boccat")
    # category_links = [BASE_URL + dd.a["href"] for dd in boccat.findAll("dd")]
    category_links = [(i,dd) for i,dd in enumerate(boccat.findAll("dd"),1) if dd<= 10]
    return category_links


def get_category_winner(category_url):
    soup = make_soup(category_url)
    category = soup.find("h1", "headline").string
    winner = [h2.string for h2 in soup.findAll("h2", "boc1")]
    runners_up = [h2.string for h2 in soup.findAll("h2", "boc2")]
    return {"category": category,
            "category_url": category_url,
            "winner": winner,
            "runners_up": runners_up}


def write_csv(mydict):
    with open('soup.csv', 'wb') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in mydict.items():
            if type(value) is not list:
                value = value.encode('utf-8')
                writer.writerow([key, value])


if __name__ == '__main__':
    count = 0
    food_n_drink = ("http://www.chicagoreader.com/chicago/"
                    "best-of-chicago-2011-food-drink/BestOf?oid=4106228")

    categories = get_category_links(food_n_drink, count)
    print categories

    data = []  # a list to store our dictionaries
    for category in categories:
        winner = get_category_winner(category)
        # print winner
        data.append(winner)
        write_csv(winner)
        sleep(1)  # be nice

        # fp = open('soup.csv', 'wb')
        # fp.write("\n".join(data))
        # print data
