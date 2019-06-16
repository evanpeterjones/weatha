import time
import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.wunderground.com/forecast/us/nc/boone/KNCBLOWI29'

def pull(url):
    "return beautful soup, bitches"
    page = requests.get(url)
    return bs(page.text, 'html.parser')

def buildTag():
    'return a current date class tag'
    tag   = 'col-'+str(time.localtime().tm_year)

    #get month
    month = time.localtime().tm_mon
    mont  = str(month) if month >= 10 else '0'+str(month)

    #get day
    d     = time.localtime().tm_mday
    day   = str(d) if d >= 10 else '0'+str(d)

    tag  += mont + day + 'T000000'
    return tag

def high(html):
    return html.findAll('div', {'class' : 'col col-20190615T000000'})

def tes(html, tag):
    return html.find_all('span', class_='wu-value-to')

def low(html):
    return html.find_all('div', class_=buildTag())
test = pull(url)
high = high(test)
low = low(test)
