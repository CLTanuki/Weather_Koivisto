__author__ = 'CLTanuki'
#-*- coding: utf-8 -*-

import urllib
import BeautifulSoup
import time

localtime = time.localtime()
date = time.strftime("%Y %m", localtime)


def tprt(text):
    i = str(text).find(':') + 2
    returnAngie = str(text)[i:str(text).find("</l", i)]
    rV = returnAngie.replace('&#0176;', '')
    rV = rV.translate(None, ' C')
    return rV


def prt(text):
    i = str(text).find(':') + 1
    returnAngie = str(text)[i:str(text).find("</l", i)]
    return returnAngie


def lirt(text):
    i = str(text).find('i>') + 2
    returnAngie = str(text)[i:str(text).find("</l", i)]
    return returnAngie


def srt(text):
    i = str(text).find(':') + 2
    returnAngie = str(text)[i:str(text).find("</l", i)]
    return returnAngie


def main():
    url = str('http://www.pasp.ru/op-info-weather?mode=current')
    page = urllib.urlopen(url)
    soup = BeautifulSoup.BeautifulSoup(page.read(), fromEncoding="utf-8")
    target = soup.findAll('div', attrs={'class': "operational-information"})
    del target[0]
    for one in target:
        dt_div = one.find('div', attrs={'class': "date-time"})
        dt = date + ' ' + dt_div.b.string + ' ' + dt_div.span.string
        temp = one.find('li', attrs={'class': "temperature"})
        pressure = one.find('li', attrs={'class': "pressure"})
        stuff = one.findAll('li')
        humidity = stuff[2]
        wd = stuff[3]
        avs = stuff[4]
        ms = stuff[5]
        wl = stuff[6]
        print dt + ',' + tprt(temp) + ',' + prt(srt(pressure).replace('мм.рт.ст.', '')) + ',' + srt(str(humidity).replace('%', '')) + ',' + srt(str(wd).replace(' гр.', '')) + ',' + srt(str(avs).replace(' м/с', '')) + ',' + srt(str(ms).replace(' м/с', '')) + ',' + srt(str(wl).replace(' cм', ''))


main()