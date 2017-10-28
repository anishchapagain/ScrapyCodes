from pyquery import PyQuery as pq
from urllib2 import urlopen
from time import sleep  # be nice
import csv

BASE_URL = "http://www.chicagoreader.com"


def read_url(url):
    """ Read given Url , Returns pq() of page"""
    html = urlopen(url).read()
    return pq(html)


def get_category_links(section_url):
    response = read_url(section_url)
    dl = response.find("dl.boccat")
    category_links = [[BASE_URL + url.attrib['href'], url.text] for url in dl.find("dd a")]
    return category_links


def get_category_winner(category):
    category_url = category[0]
    print(category_url)

    response = read_url(category_url)
    category_title = response.find("h1.headline").text()
    winner = [h2.text for h2 in response.find("h2.boc1 a")]
    runners_up = [h2.text for h2 in response.find("h2.boc2 a")]
    return {"category": category_title,
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
    food_n_drink = ("http://www.chicagoreader.com/chicago/best-of-chicago-2011-food-drink/BestOf?oid=4106228")
    categories = get_category_links(food_n_drink)
    # print categories

    data = []  # a list to store our dictionaries
    for category in categories:
        winner = get_category_winner(category)
        print (winner)


        data.append(winner)
        write_csv(winner)
        sleep(1)  # be nice

        # fp = open('soup.csv', 'wb')
        # fp.write("\n".join(data))
        # print data
