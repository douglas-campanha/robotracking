from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time 
import json 
import os 
  
class Social_bot: 
    def __init__( self ): 
        
      self.login_page = "https://www.facebook.com/"
        
        #self.page_ref = "https://www.facebook.com/pages/?category=your_pages&ref=bookmarks"
        
        self.chromium_path = os.path.abspath( "chromedriver" )
        
      self.browser_session = None
        
      
        self.browser_visit = 0
        
      self.login = 0
        
      self.time_pattern = 5
        
        self.user_xpath = "//input[@id='email']"
        
        self.pass_xpath = "//input[@id='pass']"
        
        self.user = None
        
        self.password = None
        
        self.logout_fb = ["/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/span[1]/div[1]/div[1]/i[1]", 
                         "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]", 
                         "//div[@class='oajrlxb2 s1i5eluu gcieejh5 bn081pho humdl8nn izx4hr6d rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys d1544ag0 qt6c0cv9 tw6a2znq i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l beltcj47 p86d2i9g aot14ch1 kzx2olss cbu4d94t taijpn5t ni8dbmo4 stjgntxs k4urcfbm tv7at329']//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 pfnyh3mw taijpn5t bp9cbjyn owycx6da btwxx1t3 c4xchbtz by2jbhx6']"] 
        
        self.fb_page_partial = None
        
        self.fb_posting = ["/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]", 
                           "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]", 
                           "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[4]/div[1]"] 
        
      
        self.textContents = None
                                                                                
    def initiate_chrome( self ): 
      
        if self.browser_session == None: 
            self.browser_session = webdriver.Chrome(self.chromium_path) 
            return 1
        else: 
            return -1
      
    def close_session( self ): 
      
        if self.browser_session == None: 
            return
        else: 
            self.browser_session.close() 
            self.browser_session.quit() 
            self.browser_session = None
            return 1
          
    def page_load( self , path = None ): 
      
        if path == None: 
                if self.browser_session == None: 
                return -1
            else: 
                self.browser_session.get(self.login_page) 
                self.browser_visit+=1
        else: 
                if self.browser_session == None: 
                return -1
            else: 
                                        self.browser_session.get( path ) 
                self.browser_visit+=1
      
    def reverse_visit( self , back_v = None ): 
      
      
      if self.browser_visit == None: 
                  return -1
        else: 
                    if back_v == None : 
                for vp in range( self.browser_visit ): 
                    self.browser_session.back() 
                self.browser_visit = 0
                return 1
            else: 
                            for vp in range( back_v ): 
                    self.browser_session.back() 
                    self.browser_visit - = vp 
                return 1
              
    def do_login( self, user_name = None, user_pass = None ): 
      
      
        if self.browser_session == None or self.login == 1: 
                  return -1
        elif user_name != None or user_pass != None : 
            return -1
        else: 
                          self.browser_session.find_element_by_xpath(self.user_xpath).send_keys(self.user) 
            self.browser_session.find_element_by_xpath(self.pass_xpath).send_keys(self.password, Keys.ENTER) 
            self.browser_visit+=1
            self.login = 1
            return 1
          
    def do_logout(self): 
      
      if self.browser_session == None or self.login == 0: 
                  return -1
        else: 
                            try: 
                      self.browser_session.find_element_by_xpath( 
                                      self.logout_fb[0]).click() 
                        self.time_patterns() 
                        self.browser_session.find_element_by_xpath( 
                                      self.logout_fb[1]).click() 
                        self.time_patterns() 
                        self.browser_session.find_element_by_xpath( 
                                      self.logout_fb[2]).click() 
                return 1
            except: 
                return -1
              
    def time_patterns( self , tp = None ): 
      
      
      
        if tp == None : 
            time.sleep( self.time_pattern ) 
            return 1
        else: 
            self.time_pattern = tp 
            time.sleep( self.time_pattern ) 
            return 1
          
    def page_navigation_partial( self , pg_name ): 
      
      
        if self.browser_session == None: 
                  return -1
        else: 
                        self.browser_session. 
                    find_element_by_partial_link_text(pg_name).click() 
                  self.browser_visit+=1
      
    def page_posting(self): 
      
      
        if self.browser_session == None: 
                  return -1
        else: 
                          self.browser_session.find_element_by_xpath( 
                                  self.fb_posting[0]).click() 
                self.time_patterns() 
            self.browser_session.find_element_by_xpath( 
                          self.fb_posting[1]).send_keys( 
                                  Keys.ENTER, self.textContents) 
                self.time_patterns() 
                self.browser_session.find_element_by_xpath( 
                                      self.fb_posting[2]).click() 
                self.time_patterns() 
            self.reverse_visit(1) 
            self.time_patterns() 
            return 1
          
    def credential_loads_using_json(self): 
      
      
      try: 
            with open("credentials_load.json") as filePointer: 
                contents = filePointer.read() 
    contents = json.loads(contents) 
    self.fb_page_partial = contents["Page Names"] 
            self.user = contents["Email Address"] 
            self.password = contents["Password"] 
      del(contents) 
            return 1
        except: 
            return -1
          
    def text_posting_content_load(self): 
        try: 
            with open("PostingContents.txt","r") as filePointer: 
                textContents = filePointer.read() 
                self.textContents = textContents 
            return 1
        except: 
            return -1
          
def soc_bot(): 
    
    
    bot = Social_bot()  
      
    
    
    bot.initiate_chrome() 
      
    
    bot.credential_loads_using_json() 
      
    
    bot.text_posting_content_load() 
      
    
    bot.page_load() 
      
    
    bot.do_login() 
      
    ask_to_block_notif = input("[+] Perform these tasks:\n1.Accept the 2FA if required to do \n2. Once FB Page Load, Please Block the Show Notification Dialog box. Once done, Please press to start the posting Script(Y/N) > ") 
      
    
    
    if ask_to_block_notif.upper() == "Y": 
      
        bot.page_load(bot.page_ref) 
        
        bot.time_patterns() 
        
        for link in bot.fb_page_partial: 
                bot.page_navigation_partial(link) 
                  bot.time_patterns() 
                  bot.page_posting() 
                  print("[+] Posting Done on {}".format(link)) 
        
        bot.do_logout()  
        
        bot.close_session() 
        print( "[+] Posting Work Done!" ) 
        
        return 1
    else: 
        bot.close_session() 
        return -1   
  
if __name__ == "__main__": 
    print("SOCIAL BOT SCRIPT INITIATED") 
    soc_bot()
