import time
import json
import urllib.request
from selenium import webdriver
from PIL import Image
import csv
import pandas as pd
import itertools
import os
from selenium.common.exceptions import NoSuchElementException
from requests import get
ifile  = open('us.csv', "r")
lis=[]
read = csv.reader(ifile)

for row in read :
    lis.append(row)
print(lis)
flat_list = [item for sublist in lis for item in sublist]
print(flat_list)
driver = webdriver.Chrome()

ctt=0
driver.get("https://www.booking.com/index.en-gb.html?label=gen173nr-1DCAEoggI46AdIM1gEaGyIAQGYAQm4ARnIAQzYAQPoAQGIAgGoAgO4Aq257OgFwAIB;sid=01a97bbef71c9ad8434dee5f2cd326eb;keep_landing=1&sb_price_type=total&")
for jk in flat_list:
    driver.find_element_by_id("ss").clear()
    driver.find_element_by_id("ss").send_keys(jk)
    aa=str(jk)
    print(aa)


    if ctt==0:

        driver.find_element_by_css_selector(
            "#frm > div.xp__fieldset.accommodation > div.xp__dates.xp__group > div.xp__dates-inner > div:nth-child(2) > div > div > div > div > span").click()
        time.sleep(3)

        inp = input("enter check in date mm/dd/yy     ")



        li = inp.split("/")
        time.sleep(4)
        for i in range(3):
            li[i] = int(li[i])
        time.sleep(5)
        sto = (driver.find_element_by_css_selector(
            "#frm > div.xp__fieldset.accommodation > div.xp__dates.xp__group > div.xp-calendar > div > div > div.bui-calendar__content > div:nth-child(1) > div").text)

        lis2 = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                'November', 'December']
        stol = sto.split(" ")
        stol1 = stol[0]
        stol2 = stol[1]
        ind = 0
        for i in range(0, 12):
            if stol1 == lis2[i]:
                ind = i + 1

        cl = li[0] - ind

        for i in range(0, cl):
            driver.find_element_by_css_selector(
                "#frm > div.xp__fieldset.accommodation > div.xp__dates.xp__group > div.xp-calendar > div > div > div.bui-calendar__control.bui-calendar__control--next").click()

        xy = driver.find_elements_by_css_selector("td.bui-calendar__date")
        for i in xy:

            if i.text == " " or i.text == "":
                continue
            else:
                print(i.text)
                yy = int(i.text)
                if yy == li[1]:
                    i.click()
                    break
        driver.find_element_by_css_selector("span.xp__guests__count").click()
        ctt=ctt+1
        driver.find_element_by_css_selector("#xp__guests__inputs-container > div > div > div.sb-group__field.sb-group__field-adults > div > div.bui-stepper__wrapper > button.bui-button.bui-button--secondary.bui-stepper__subtract-button").click()
    driver.find_element_by_css_selector("button.sb-searchbox__button  ").click()
    name = []
    star = []
    rating = []
    review = []
    price = []
    distfrcen = []
    mrp = []
    imge = []

    dict = {}
    ct = 0
    os.mkdir("/home/piyush/PycharmProjects/untitled/UK/"+aa)
    while 23:
        time.sleep(20)
        st = driver.find_elements_by_css_selector(
            "div.sr_item.sr_item_new.sr_item_default.sr_property_block.sr_flex_layout")

        for j in st:

            st0 = j.find_element_by_css_selector("span.sr-hotel__name").text
            st0=st0.replace('/', '-')
            dict['name'] = st0
            print(st0)
            name.append(st0)

            try:
                st1 = j.find_element_by_css_selector("i.bk-icon-wrapper.bk-icon-stars.star_track").get_attribute(
                    'title')
                print(st1)
                star.append(st1)
                dict['star'] = st1
            except:
                star.append("not avai")
                print("xx")
                dict['star'] = "not avail"
            try:
                st2 = j.find_element_by_css_selector("div.bui-review-score__badge").text
                rating.append(st2)
                dict['rating'] = st2
                print(st2)

            except:
                rating.append("not avai")
                dict['rating'] = "not avail"
            try:
                st3 = j.find_element_by_css_selector("div.bui-review-score__text").text
                review.append(st3)
                print(st3)
                dict['review'] = st3

            except:
                review.append("not avai")
                dict['review'] = "not avai"

            try:
                st4 = j.find_element_by_css_selector(
                    "div.bui-price-display__value.prco-inline-block-maker-helper ").text
                price.append(st4)
                dict['price'] = "RS " + st4[1:]

            except:
                price.append("not avai")
                dict['price'] = "not avai"
            try:
                s5 = j.find_element_by_css_selector("span.distfromdest.jq_tooltip").text
                distfrcen.append(s5)
                print(s5)
                dict['distfromcentre'] = s5
            except:
                distfrcen.append("not avai")
                dict['distfromcentre'] = "not avail"
            try:
                st16=j.find_element_by_css_selector("div.rollover-s1.lastbooking").text
                dict['last bookings']=st16
                print(st16)
            except:

                dict['last bookings']="not avail"
            try:
                st17=j.find_element_by_css_selector("div.rollover-s2.sr--x-times-last-time").text
                dict['latest booking']=st17
            except:
                dict['latest booking']="not avail"


            try:
                frct=0
                brin=0
                nopr=0
                st7=j.find_elements_by_css_selector("sup.sr_room_reinforcement")

                for llk in st7:
                    print(llk.text)
                    if llk.text=="FREE cancellation":
                        dict['free cancelation'] = "Yes"
                        frct=frct+1
                    if llk.text=="Breakfast included":
                        dict['Breakfast included']="Yes"
                        brin=brin+1
                    if llk.text=="No prepayment needed":
                        dict['No prepayment needed']="Yes"

                if frct==0:
                    dict['free cancelation']="No"
                if brin==0:
                    dict['Breakfast included']="No"
                if nopr==0:
                    dict['No prepayment needed']="No"





            except:
                dict['free cancelation']="NO"
                dict['Breakfast included'] = "NO"
                dict['No prepayment needed']="No"
            try:

                st8=j.find_element_by_css_selector("svg.bk-icon.-iconset-thumbs_up_square.pp-icon-valign--tbottom")
                dict['preferd partner property']="yes"
            except:
                dict['preferd partner property']="no"
            try:

                st9=j.find_element_by_css_selector("div.sr-badges__row")
                dict['great value today']="yes"
            except:
                dict['great value today']="no"


            try:
                s6 = j.find_element_by_css_selector(
                    "div.bui-price-display__original.prco-inline-block-maker-helper").text
                mrp.append(s6)
                dict['mrp'] = "Rs"+s6[1:]
                print(s6)
            except:
                mrp.append("not avai")
                dict['mrp'] = "not avail"
            ct = ct + 1
            stru = str(ct) + "|"
            os.mkdir("/home/piyush/PycharmProjects/untitled/UK/"+aa+"/" + stru + st0)

            try:
                s7 = j.find_element_by_css_selector("img.hotel_image")
                stre = s7.get_attribute('src')
                ww = "/home/piyush/PycharmProjects/untitled/UK/"+aa+"/" + stru + st0 + "/"
                urllib.request.urlretrieve(stre, st0)
                time.sleep(3)
                im = Image.open("file1").convert("RGB")
                im.save(ww + st0 + ".jpg", "jpeg")
            except:
                imge.append("not avail")

            ww = "/home/piyush/PycharmProjects/untitled/UK/"+aa+"/" + stru + st0 + "/"
            with open(ww + st0 + ".txt", 'w') as json_file:
                json.dump(dict, json_file)
            dict = {}
        try:
            driver.find_element_by_css_selector("#search_results_table > div.bui-pagination.results-paging")
            try:
                driver.find_element_by_css_selector(
                    "#search_results_table > div.bui-pagination.results-paging > nav > ul > li.bui-pagination__item.bui-pagination__next-arrow.bui-pagination__item--disabled")
                break
            except:
                driver.find_element_by_css_selector(
                    "#search_results_table > div.bui-pagination.results-paging > nav > ul > li.bui-pagination__item.bui-pagination__next-arrow").click()
        except:
            break
