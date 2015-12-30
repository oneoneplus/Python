#coding=utf-8
from bs4 import BeautifulSoup
import urllib2


of = open('proxy.txt' , 'w')

for page in range(1, 6):
    url ='http://www.xicidaili.com/nn/' + str(page)
    print url
    url1 = urllib2.Request(url)
    url1.add_header('User-agent', 'Mozilla 5.10')
    html_doc = urllib2.urlopen(url1).read()
    
    #html_doc = html.read()
    soup = BeautifulSoup(html_doc)
    trs = soup.find('table', id='ip_list').find_all('tr')
    for tr in trs[1:]:
        tds = tr.find_all('td')
        ip = tds[2].text.strip()
       
        port = tds[3].text.strip()
        protocol = tds[6].text.strip()
        if protocol == 'HTTP' or protocol == 'HTTPS':
            of.write('%s=%s:%s\n' % (protocol, ip, port) )
            #print '%s=%s:%s' % (protocol, ip, port)

of.close()
