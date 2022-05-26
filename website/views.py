import webbrowser
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.exceptions import *
from selenium import webdriver as wb
from selenium.common.exceptions import *
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import chromedriver_autoinstaller as chromedriver
import chromedriver_binary


def website(request):
    return render(request, 'index.html', {})

def search_item(request):
    item = ''
    if request.method == 'POST':
        item = request.POST.get('textfield')
    
        wbd = wb.Chrome('/usr/bin/chromedriver')
        #webdriver_path = '/usr/bin/chromedriver'
        amazon_url = 'https://www.amazon.com/'
        bam_url = 'https://www.booksamillion.com/'
        tb_url = 'https://www.thriftbooks.com/'
        gw_url = 'https://www.etsy.com/'
        
        search_url = amazon_url + ("s?k=%s" % (item))
        print(search_url)
        wbd.get(search_url)
        price = wbd.find_elements_by_class_name('a-price-whole')
        p = 'Amazon Price: $' + price[0].text
        l = 'Link: ' + search_url
        
        search_url2 = bam_url + ("search?filter=&id=8535225791705&query=%s" % (item))
        print(search_url2)
        wbd.get(search_url2)
        price2 = wbd.find_elements_by_class_name('our-price')
        p2 = 'Bam Price: ' +  price2[0].text
        l2 = "Link: " + search_url2
        
        search_url3 = tb_url + ('browse/?b.search=%s')
        print(search_url3)
        wbd.get(search_url3)
        price3 = wbd.find_elements_by_class_name('SearchResultListItem-dollarAmount')
        p3 = 'Thriftbooks Price: $' + price3[0].text
        l3 = 'Link: ' + search_url3
        
        search_url4 = gw_url + ('search?q=')
        print(search_url4)
        wbd.get(search_url4)
        price4 = wbd.find_elements_by_class_name('currency-value')
        p4 = 'Etsy: ' + price4[0].text
        l4 = 'Link: ' + search_url4
        
        
        return render(request, 'index.html', {
            'aprice': p, 
            'alink': l, 
            'fprice': p2, 
            'flink': l2, 
            'bprice': p3,
            'blink': l3,
            'cprice': p4,
            'clink': l4
            })
    
    
