from bs4 import BeautifulSoup

from Locators.tweetsLocator import TweetsLocators

import time


class Tweet:
    scollheight=0
    def __init__(self, page):
        self.page = webdriver.Chrome()
        self.page.get(page)
        time.sleep(10)
        self.soup = BeautifulSoup(self.page.page_source, 'html.parser')

    def scroll(self, driver, timeout):
        scroll_pause_time = timeout

        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(scroll_pause_time)

            # Calculate new scroll height and compare with last scroll height

            new_height = driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                # If heights are the same it will exit the function
                break
            last_height = new_height

    def tweets_split(self ):

        scroll_pause_time = 5
        tweets = []
        # Get scroll height
        last_height = self.page.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.page.maximize_window()

            self.page.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page

            time.sleep(2)

            elements = self.page.find_elements_by_class_name( "r-1re7ezh.r-1loqt21.r-1q142lx.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-3s2u2q.r-qvutc0.css-4rbku5.css-18t94o4.css-901oao");

            l2 = [j.get_attribute('href') for j in elements]

            tweets.extend(l2)

            # Calculate new scroll height and compare with last scroll height

            new_height = self.page.execute_script("return document.body.scrollHeight")
            if new_height == last_height :
                break
            last_height = new_height



        print('hani hna')



        print('Nbre tweets    : ' + str(len(tweets)))

        return len(tweets), tweets

    @property
    def tweets_replies(self):

        i = 0
        # print('TweetsNumber :' +str(tweetsNumber)+'\n')
        tweetsNumber, elements = self.tweets_split()
        self.page.execute_script("window.scrollTo(0, 0)")
        self.page.refresh()
        time.sleep(4)
        print('Tweets received   : ' + str(len(elements)))

        while i < tweetsNumber:
            long, elements = self.tweets_split()

            self.page.execute_script("arguments[0].click();", elements[i])
            time.sleep(2)
            print(self.page.current_url)

            try:

                twe = self.page.find_element_by_class_name("css-901oao.r-hkyrab.r-1k78y06.r-1blvdjr.r-16dba41.r-ad9z0x.r-bcqeeo.r-bnwqim.r-qvutc0.r-1vmecro")
                print("The Tweet is : \n")
                print(twe.text)
                rep = self.page.find_elements_by_class_name(
                    "css-901oao.r-hkyrab.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-bnwqim.r-qvutc0")
                for re in rep:
                    print(re.text)
            except NoSuchElementException:
                pass

            time.sleep(3)
            self.page.execute_script("window.history.go(-1)")
            self.page.refresh()
            i = i + 1

        self.page.quit()

    @property
    def twitter_account(self):
        return "twitter account Name"

