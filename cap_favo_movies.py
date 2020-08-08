#captrue top 500 movies name
import urllib.request as rq
from lxml import etree

def worker(pageNo):
    # define params
    url = "https://movie.douban.com/top250?start=" + str(25 * pageNo)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

    # parse html code and then convert to xpath form.
    req = rq.Request(url, headers=headers)
    html = rq.urlopen(req).read().decode("utf-8")
    html = etree.HTML(html)

    # locate to films node beginning.
    lis = html.xpath("//ol[@class='grid_view']/li")
    cnt = 0
    for each in lis:
        # name
        chsName = "/".join(each.xpath("div/div[2]/div[@class='hd']/a/span[1]/text()"))
        engName = "/".join(each.xpath("div/div[2]/div[@class='hd']/a/span[2]/text()"))
        name = chsName + engName

        # brief of movie
        brief = "/".join(each.xpath("div/div[2]/div[@class='bd']/p[2]/span/text()"))

        # star rank
        star = "/".join(each.xpath("div/div[2]/div[@class='bd']/div/span[2]/text()"))

        # write to top250.csv
        with open("top250.csv", 'a', encoding='utf-8') as hd:
            hd.write("\"{}\",".format(pageNo * 25 + cnt + 1))
            hd.write("\"{}\"," . format(name))
            hd.write("\"{}\"," . format(brief))
            hd.write("\"{}\"".format(star))
            hd.write("\n")
        cnt = cnt + 1

def main():
    with open("./tmp/top250.csv", 'w', encoding="utf-8") as hd:
        hd.write("NO,name,brief,star\n")
    for i in range(10):
        worker(i)
main()