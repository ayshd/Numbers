# coding:utf-8

import urllib2
import codecs
import os
import numpy as np
import csv
import datetime

#print datetime.date.today().year
#print datetime.date.today().month
#print datetime.date.today().day

fname = 'win_num.csv'

##################################################
# みずほ銀行HPから（B表）A表以前の当せん番号を取得
# Accessed: 2017/03/13
# 第1回～第4349回
##################################################
def tableB():
    url = 'https://www.mizuhobank.co.jp/takarakuji/numbers/backnumber/num'
    num = 1
    fp_out = open(fname, 'w')

    while num <= 4341:
        tmp_url = url + str(num).zfill(4) + '.html'
        print tmp_url

        fp = urllib2.urlopen(tmp_url)
        html = fp.read()
        fp.close()

        fp = open('html.txt', 'w')
        fp.write(html)
        fp.close()

        fp = open('html.txt', 'r')
        for row in fp:
            if '<th class="bgf7f7f7">' in row:
                tmp = row.split('>')
                tmp2 = tmp[1].split('<')
                fp_out.write(tmp2[0])
                ct = 0
            elif '<td class="alnRight">'in row:
                tmp = row.split('>')
                tmp2 = tmp[1].split('<')
                fp_out.write(','+tmp2[0])
                ct += 1
                if ct == 3:
                    ct = 0
                    fp_out.write('\n')
        num += 20
        fp.close()
    fp_out.close()
    os.system('rm html.txt')
##################################################


##################################################
# みずほ銀行HPから（A表）先月から過去1年間の当せん番号を取得
# Accessed: 2017/03/13
# 第4350回～第4608回
##################################################
def tableA():
    #ナンバーズ3
    list_n3 = list()
    url_n3 = 'https://www.mizuhobank.co.jp/takarakuji/numbers/backnumber/num3-'

    #ナンバーズ4
    list_n4 = list()
    url_n4 = 'https://www.mizuhobank.co.jp/takarakuji/numbers/backnumber/num4-'

    fp_out = open(fname, 'a')

    #ナンバーズ3 201702 -- 201701
    year = datetime.date.today().year
    month = datetime.date.today().month - 1
    tmp_string = 0
    ct = 0

    while month >= 1:
        tmp_url = url_n3 + str(year) + str(month).zfill(2) + '.html'
        print tmp_url

        fp = urllib2.urlopen(tmp_url)
        html = fp.read()
        fp.close()

        fp = open('html.txt', 'w')
        fp.write(html)
        fp.close()

        fp = open('html.txt', 'r')
        for row in fp:
            if '<th colspan="4" class="alnCenter bgf7f7f7">' in row:
                tmp = row.split('>')
                tmp2 = tmp[1].split('<')
                tmp_string = tmp2[0] + ','
                ct = 0
            elif '<td colspan="4" class="alnCenter">'in row:
                tmp = row.split('>')
                tmp2 = tmp[1].split('<')
                tmp_string = tmp_string + tmp2[0] + ','
                ct += 1
            elif '<td colspan="4" class="alnCenter extension"><strong>' in row:
                tmp = row.split('>')
                tmp2 = tmp[2].split('<')
                tmp_string = tmp_string + tmp2[0]
                ct += 1
                if ct == 2:
                    list_n3.append(tmp_string)
                    ct = 0
        fp.close()
        month -= 1


    #ナンバーズ3 201612 -- 201603
    year  = datetime.date.today().year - 1
    month = 12
    tmp_string = 0
    ct = 0

    while month >= datetime.date.today().month:
        tmp_url = url_n3 + str(year) + str(month).zfill(2) + '.html'
        print tmp_url

        fp = urllib2.urlopen(tmp_url)
        html = fp.read()
        fp.close()

        fp = open('html.txt', 'w')
        fp.write(html)
        fp.close()

        fp = open('html.txt', 'r')
        for row in fp:
            if '<th colspan="4" class="alnCenter bgf7f7f7">' in row:
                tmp = row.split('>')
                tmp2 = tmp[1].split('<')
                tmp_string = tmp2[0] + ','
                ct = 0
            elif '<td colspan="4" class="alnCenter">'in row:
                tmp = row.split('>')
                tmp2 = tmp[1].split('<')
                tmp_string = tmp_string + tmp2[0] + ','
                ct += 1
            elif '<td colspan="4" class="alnCenter extension"><strong>' in row:
                tmp = row.split('>')
                tmp2 = tmp[2].split('<')
                tmp_string = tmp_string + tmp2[0]
                ct += 1
                if ct == 2:
                    list_n3.append(tmp_string)
                    ct = 0
        fp.close()
        month -= 1

    #ナンバーズ4 201701
    year  = datetime.date.today().year
    month = datetime.date.today().month - 1
    ct = 0

    while month >= 1:
        tmp_url = url_n4 + str(year) + str(month).zfill(2) + '.html'
        print tmp_url

        fp = urllib2.urlopen(tmp_url)
        html = fp.read()
        fp.close()

        fp = open('html.txt', 'w')
        fp.write(html)
        fp.close()

        fp = open('html.txt', 'r')
        ct = 0
        for row in fp:
            if '<th colspan="4" class="alnCenter bgf7f7f7">' in row: # times
                tmp = row.split('>')
                tmp2 = tmp[1].split('<')
                tmp_string = tmp2[0] + ','
                ct = 0
            elif '<td colspan="4" class="alnCenter">'in row: # date
                tmp = row.split('>')
                tmp2 = tmp[1].split('<')
                tmp_string = tmp_string + tmp2[0] + ','
                ct += 1
            elif '<td colspan="4" class="alnCenter extension"><strong>' in row: # wining numbers
                tmp = row.split('>')
                tmp2 = tmp[2].split('<')
                tmp_string = tmp_string + tmp2[0]
                ct += 1
                if ct == 2:
                    list_n4.append(tmp_string)
                    ct = 0
        fp.close()
        month -= 1

    #ナンバーズ4 201612--201602
    year = datetime.date.today().year - 1
    month = 12
    ct = 0
    while month >= datetime.date.today().month:
        tmp_url = url_n4 + str(year) + str(month).zfill(2) + '.html'
        print tmp_url

        fp = urllib2.urlopen(tmp_url)
        html = fp.read()
        fp.close()

        fp = open('html.txt', 'w')
        fp.write(html)
        fp.close()

        fp = open('html.txt', 'r')
        ct = 0
        for row in fp:
            if '<th colspan="4" class="alnCenter bgf7f7f7">' in row:
                tmp = row.split('>')
                tmp2 = tmp[1].split('<')
                tmp_string = tmp2[0] + ','
                ct = 0
            elif '<td colspan="4" class="alnCenter">'in row:
                tmp = row.split('>')
                tmp2 = tmp[1].split('<')
                tmp_string = tmp_string + tmp2[0] + ','
                ct += 1
            elif '<td colspan="4" class="alnCenter extension"><strong>' in row:
                tmp = row.split('>')
                tmp2 = tmp[2].split('<')
                tmp_string = tmp_string + tmp2[0]
                ct += 1
                if ct == 2:
                    list_n4.append(tmp_string)
                    ct = 0
        fp.close()
        month -= 1

    for item_n3 in reversed(list_n3):
        tmp_n3 = item_n3.replace('\n','').split(',')
        for item_n4 in reversed(list_n4):
            tmp_n4 = item_n4.split(',')
            if tmp_n3[0]==tmp_n4[0] and tmp_n3[1]==tmp_n4[1]:
                tmp = item_n3.replace('\n','') + ',' + tmp_n4[2]
                #print tmp
                fp_out.write(tmp)
                fp_out.write('\n')
    fp_out.close()
    os.system('rm html.txt')
##################################################



##################################################
# みずほ銀行HPからナンバーズの当せん番号を取得
# Accessed: 2017/03/13
# 第4609回～第4617回
##################################################
def latest():
    #ナンバーズ3
    list_n3 = list()
    url_n3 = 'https://www.mizuhobank.co.jp/takarakuji/numbers/numbers3/index.html'
    #ナンバーズ4
    list_n4 = list()
    url_n4 = 'https://www.mizuhobank.co.jp/takarakuji/numbers/numbers4/index.html'

    fp_out = open(fname, 'a')

    tmp_string = 0

    print url_n3
    fp = urllib2.urlopen(url_n3)
    html = fp.read()
    fp.close()

    fp = open('html.txt', 'w')
    fp.write(html)
    fp.close()

    fp = open('html.txt', 'r')
    ct = 0
    for row in fp:
        if '<th colspan="4" class="alnCenter bgf7f7f7">' in row:
            tmp = row.split('>')
            tmp2 = tmp[1].split('<')
            tmp_string = tmp2[0] + ','
            ct = 0
        elif '<td colspan="4" class="alnCenter">'in row:
            tmp = row.split('>')
            tmp2 = tmp[1].split('<')
            tmp_string = tmp_string + tmp2[0] + ','
            ct += 1
        elif '<td colspan="4" class="alnCenter extension"><strong>' in row:
            tmp = row.split('>')
            tmp2 = tmp[2].split('<')
            tmp_string = tmp_string + tmp2[0]
            ct += 1
        if ct == 2:
            list_n3.append(tmp_string)
            ct = 0
    fp.close()

    print url_n4
    fp = urllib2.urlopen(url_n4)
    html = fp.read()
    fp.close()

    fp = open('html.txt', 'w')
    fp.write(html)
    fp.close()

    fp = open('html.txt', 'r')
    ct = 0
    for row in fp:
        if '<th colspan="4" class="alnCenter bgf7f7f7">' in row:
            tmp = row.split('>')
            tmp2 = tmp[1].split('<')
            tmp_string = tmp2[0] + ','
            ct = 0
        elif '<td colspan="4" class="alnCenter">'in row:
            tmp = row.split('>')
            tmp2 = tmp[1].split('<')
            tmp_string = tmp_string + tmp2[0] + ','
            ct += 1
        elif '<td colspan="4" class="alnCenter extension"><strong>' in row:
            tmp = row.split('>')
            tmp2 = tmp[2].split('<')
            tmp_string = tmp_string + tmp2[0]
            ct += 1
        if ct == 2:
            list_n4.append(tmp_string)
            ct = 0
    fp.close()

    for item_n3 in reversed(list_n3):
        tmp_n3 = item_n3.replace('\n','').split(',')
        for item_n4 in reversed(list_n4):
            tmp_n4 = item_n4.split(',')
            if tmp_n3[0]==tmp_n4[0] and tmp_n3[1]==tmp_n4[1]:
                tmp = item_n3.replace('\n','') + ',' + tmp_n4[2]
                #print tmp
                fp_out.write(tmp)
                fp_out.write('\n')
    fp_out.close()
    os.system('rm html.txt')
##################################################

tableB() # 第1回～第4308回
tableA() # 第4309回～第4568回
latest() # 第4569回～第4576回
