import time, sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from requests import request as rq
from selenium.webdriver import Chrome, ChromeOptions
from random import randint,shuffle
import datetime
import schedule
import pandas as pd
import tweepy
import random

class AutoTweet:
    options = ChromeOptions()
    options.add_argument('-headless')
    def __init__(self,yourId,yourPassWord,filename):
        self.driver = webdriver.Chrome(executable_path=rf'C:\Users\username\Desktop') #ここを必要あれば変更(path部分)
        self.yourId = yourId
        self.yourPassWord = yourPassWord
        self.df = pd.read_csv(filename)

    def Login(self):
        url = "https://twitter.com/login"
        self.driver.get(url)

        print(self.driver.current_url)
        """
        self.driver.find_element_by_xpath('//*[@id="doc"]/div/div[1]/div[1]/div[2]/div[2]/div/a[2]').click()
        """
        time.sleep(5)
        id = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/main/div/div/form/div/div[1]/label/div/div[2]/div/input')
        id.send_keys(self.yourId)
        time.sleep(5)
        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/main/div/div/form/div/div[2]/label/div/div[2]/div/input')
        password.send_keys(self.yourPassWord)
        time.sleep(5)
        print(self.driver.current_url)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/main/div/div/form/div/div[3]/div/div/span/span').click()

    def tweet(self,twi):
        """
            引数で渡された文章をツイートする関数。
            tweetは140文字以内。
        """
        if len(twi) > 140:
            print("This tweet is too long")
        else:
            try:
                time.sleep(10)
                elem = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/header/div/div/div/div/div[3]/a')
                elem.click()
                time.sleep(10)
                elem = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div/div/div/div[2]/div')
                elem.click()
                time.sleep(10)
                print("before send key")
                elem.send_keys(twi)
                print("input_done")
                time.sleep(5)
                elem = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]')
                elem.click()
                print("OK")
                elem.send_keys(Keys.CONTROL, Keys.ENTER)

            except KeyboardInterrupt:
                print("\nprogram was ended.\n")
                sys.exit()
            
            except:
                url = "https://twitter.com/home"
                self.driver.get(url)

    def autoIINE(self):
        """
            自動でイイネする関数。
            だいたい一回で10イイネする。
            1日のイイネ制限は1200なので注意。
        """
        self.driver.refresh()
        time.sleep(3)
        for j in range(3,5):
            for i in range(1,11):
                time.sleep(0.5)
                try:
                    elements = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div/div/div[2]/div/div/section/div/div/div/div['+str(i)+']/div/article/div/div[2]/div[2]/div['+str(j)+']/div[3]/div')       
                    elements.click()
                except:
                    pass
    
    def tweetChoice(self):
        """
            filenameには1列のカラムを持つcsvファイルを指定
            ヘッダ名は"tweets",各行には140字以内のツイートを書く
        """
        wlen = len(self.df)
        randomIndex = randint(0,wlen-1)

        return self.df["tweets"].iloc[randomIndex]

    def shuffleString(string):
        li = []
        for i in string:
            li.append(i)

        li = shuffle(li)
        return ''.join(li)
        

            
    def quit_chrome(self):      
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    tweet1 = AutoTweet("メアド","パスワード","csvファイル名")

    tweet1.Login()
    time.sleep(10)
    """
    tweet2.Login()
    time.sleep(10)
    """

    while(True):
        try:
            s='ここにランダムツイートの内容をかく'
            sr = ''.join(random.sample(s, len(s)))
            print(sr)
            tweet1.tweet(sr)
            time.sleep(60*15) #時間の指定をしてツイートする

        except KeyboardInterrupt:
                print("\nprogram was ended.\n")
                tweet1.quit_chrome()
                sys.exit()