import lxml.html
from lxml.etree import XPath as xpath
from lxml import etree
import requests

# xpath1 = "tbody/tr"
# r = requests.post(url,data)
# html = lxml.html.fromstring(r.text)
# rows = html.xpath(xpath1)
# data = list()
# for row in rows:
#     data.append([c.text for c in row.getchildren()])

# header = [text(th) for th in table.xpath('//th')]  # 1
# data = [[text(td) for td in tr.xpath('td')]
#         for tr in table.xpath('//tr')]  # 2
# data = [row for row in data if len(row) == len(header)]  # 3
# data = pd.DataFrame(data, columns=header)

def football(url, date):
    html = lxml.html.parse(pages)

    rows_xpath = xpath("//*[@id='content-primary']/table[1]/tbody/tr[td[1]/span/span//text()='%s']" % (date))
    time_xpath = xpath("td[1]/span/span//text()[2]")
    team_xpath = xpath("td[2]/a/text()")
    result_xpath = xpath("td[3]/a/span/text()")
    place_xpath = xpath("td[4]/a/text()")

    details = []
    for row in rows_xpath(html):
        time = time_xpath(row)[0].strip()
        team = team_xpath(row)[0]
        score = result_xpath(row)[0]
        venue = place_xpath(row)[0]
        details.append([time, team, score, venue])

    return details

# http://stackoverflow.com/questions/29448934/extracting-information-from-a-table-on-a-website-using-python-lxml-xpath
# http://stackoverflow.com/questions/29595105/extract-information-from-website-using-xpath-python
def earthquake(page):
    response = requests.get(page)
    print("Finding >>> ", page)
    print("Status : ",response.status_code)
    # print("Response Type >>> ", response.content)

    details = []
    response = lxml.html.parse(page)
    rows = response.xpath("//div[@class='block2-content']//table[contains(.,'Date')]/tr[position()>1]")
    print("count >> ", rows.__len__())

    count=0
    for row in rows:
        edate = row.xpath('td[1]/span//text()')[0]
        etime = row.xpath('td[2]/span//text()')[0]
        elatitude = row.xpath('td[3]/span//text()')[0]
        elongitude = row.xpath('td[4]/span//text()')[0]
        emagnitude = row.xpath('td[5]/span//text()')[0]
        epicentre = row.xpath('td[6]/span/a//text()')[0]
        if edate:
            # details.append([edate[0], etime[0], elatitude[0], elongitude[0], emagnitude[0], epicentre[0]])
            details.append([edate, etime, elatitude, elongitude, emagnitude, epicentre])
            count = count +1

        # if count > 5:
        #     print(details)
        #     quit()


    return details


if __name__ == '__main__':
    # url = "http://gbgfotboll.se/information/?scr=table&ftid=62068"
    # date = '2016-11-06'
    # print(football(url,date))

    pages = ["http://www.seismonepal.gov.np/index.php?action=earthquakes&show=recent&page=%s" %
             page for page in xrange(1, 2)]
    for page in pages:
        data = earthquake(page)
        print(data)
