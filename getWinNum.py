# coding:utf-8

import urllib2
import codecs
import os
import numpy as np

##################################################
# function define
##################################################
def getWinNum():
    url = 'https://www.mizuhobank.co.jp/takarakuji/numbers/backnumber/num'
    num = 1;
    fp_out = open('win_num.csv', 'w')

    while num <= 4301:
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
                tmp = [row[i: i+21] for i in range(0, len(row), 21)]
                tmp2 = tmp[1].split('<')
                fp_out.write(tmp2[0])
                ct = 0
            elif '<td class="alnRight">'in row:
                tmp = [row[i: i+21] for i in range(0, len(row), 21)]
                tmp2 = tmp[1].split('<')
                fp_out.write(','+tmp2[0])
                ct += 1
                if ct == 3:
                    ct = 0
                    fp_out.write('\n')
        num += 20
        fp.close()
    fp_out.close()
#########################
def getWinNum_n3_last12months():
    url = 'https://www.mizuhobank.co.jp/takarakuji/numbers/backnumber/num3-2016'
    fp_out = open('win_num_n3_last12month.csv', 'w')
    num = 12;
    tmp_list = list()
    tmp_string = 0
    ct = 0

    while num >= 1:
        tmp_url = url + str(num).zfill(2) + '.html'
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
                tmp_list.append(tmp_string)
                ct = 0
        num -= 1
        fp.close()

    for item in reversed(tmp_list):
        fp_out.write(item)
        fp_out.write('\n')
    fp_out.close()
#########################
def getWinNum_n3_latest():
    url = 'https://www.mizuhobank.co.jp/takarakuji/numbers/numbers3/index.html'
    fp_out = open('win_num_n3_latest.csv', 'w')
    tmp_list = list()
    tmp_string = 0
    ct = 0

    print url

    fp = urllib2.urlopen(url)
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
            tmp_list.append(tmp_string)
            ct = 0
    fp.close()

    for item in reversed(tmp_list):
        fp_out.write(item)
        fp_out.write('\n')
    fp_out.close()
#########################
def getWinNum_n4_last12months():
    url = 'https://www.mizuhobank.co.jp/takarakuji/numbers/backnumber/num4-2016'
    fp_out = open('win_num_n4_last12month.csv', 'w')
    num = 12;
    tmp_list = list()
    tmp_string = 0
    ct = 0

    while num >= 1:
        tmp_url = url + str(num).zfill(2) + '.html'
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
                tmp_list.append(tmp_string)
                ct = 0
        num -= 1
        fp.close()

    for item in reversed(tmp_list):
        fp_out.write(item)
        fp_out.write('\n')
    fp_out.close()
#########################
def getWinNum_n4_latest():
    url = 'https://www.mizuhobank.co.jp/takarakuji/numbers/numbers4/index.html'
    fp_out = open('win_num_n4_latest.csv', 'w')
    tmp_list = list()
    tmp_string = 0
    ct = 0
    print url

    fp = urllib2.urlopen(url)
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
            tmp_list.append(tmp_string)
            ct = 0
    fp.close()

    for item in reversed(tmp_list):
        fp_out.write(item)
        fp_out.write('\n')
    fp_out.close()
#########################
def combine_latest():
    list_n3 = list()
    list_n4 = list()
    fp = open('win_num_latest.csv', 'w')

    fp_n3 = open('win_num_n3_latest.csv', 'r')
    for row in fp_n3:
        list_n3.append(row)

    fp_n4 = open('win_num_n4_latest.csv', 'r')
    for row in fp_n4:
        list_n4.append(row)

    for n3_item in list_n3:
        n3_tmp = n3_item.replace('\n','').split(',')
        for n4_item in list_n4:
            n4_tmp = n4_item.split(',')
            if n3_tmp[0]==n4_tmp[0] and n3_tmp[1]==n4_tmp[1]:
                tmp = n3_item.replace('\n','') + ',' + n4_tmp[2]
                #print tmp
                fp.write(tmp)
    fp.close()
#########################
def combine_last12month():
    list_n3 = list()
    list_n4 = list()
    fp = open('win_num_last12month.csv', 'w')

    fp_n3 = open('win_num_n3_last12month.csv', 'r')
    for row in fp_n3:
        list_n3.append(row)

    fp_n4 = open('win_num_n4_last12month.csv', 'r')
    for row in fp_n4:
        list_n4.append(row)

    for n3_item in list_n3:
        n3_tmp = n3_item.replace('\n','').split(',')
        for n4_item in list_n4:
            n4_tmp = n4_item.split(',')
            if n3_tmp[0]==n4_tmp[0] and n3_tmp[1]==n4_tmp[1]:
                tmp = n3_item.replace('\n','') + ',' + n4_tmp[2]
                #print tmp
                fp.write(tmp)
    fp.close()
##################################################
#getWinNum()

getWinNum_n3_last12months()
getWinNum_n3_latest()
getWinNum_n4_last12months()
getWinNum_n4_latest()
combine_latest()
combine_last12month()

os.system('echo 回別,抽せん日,ナンバーズ3,ナンバーズ4 > tmp.csv')
os.system('cat win_num.csv >> tmp.csv')
os.system('cat win_num_last12month.csv >> tmp.csv')
os.system('cat win_num_latest.csv >> tmp.csv')
