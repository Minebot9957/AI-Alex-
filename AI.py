
#Import 
import pyttsx3
import speech_recognition
from datetime import date, datetime
import wikipedia
from youtube_search import YoutubeSearch
import webbrowser
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import playsound
from gtts import gTTS
from selenium.webdriver.chrome.service import Service
import requests
from bs4 import BeautifulSoup
import pyautogui

robot_mouth = pyttsx3.init()   
robot_ear = speech_recognition.Recognizer()
wikipedia.set_lang("vi")
path = ChromeDriverManager().install()
#Robot hear
         def speak(you):
             print("Robot : {}".format(you))
             tts = gTTS(text=you, lang="vi", )
             filename = "sound.mp3"
             tts.save(filename)
             playsound.playsound(filename)
             os.remove(filename)
         def get_voice():         
            with speech_recognition.Microphone()as mic:
               robot_ear.adjust_for_ambient_noise(mic)
               print("Robot : Xin chào bạn")
               audio = robot_ear.listen(mic)
               print('Robot:...')
               try:   
                     you = robot_ear.recognize_google(audio,language="vi")
                     print ('You:' + you)   
               except:         
                     print("...")
         def get_text():
             for i in range(3):
                 text = get_voice()
                 if text:
                     return text.lower()
                 elif i < 2:
                     speak("Bot không nghe rõ, bạn có thể nói lại không ?")
             time.sleep(10)
             stop()
             return 0            
         def playmusic():
             global run
             music_dir = 'D:\\music'          
             songs = os.listdir(music_dir)
             os.startfile(os.path.join(music_dir,songs[0]))
             run = False          
         def gg_search(you):
             search_for = get_text.split('kiếm', 1) [1]
             speak('Ok bây bê')
             driver = webdriver.Chrome(path)
             driver.get("https://www.google.com")
             que = driver.find_element_by_xpath("//input[@name'q']")
             que.send_keys(str(search_for))
             que.send_keys(Keys.RETURN)
         def play_youtube():
             speak('mời bạn chọn bài hát')
             time.sleep(2)
             text = get_text() 
             while True :    
                   result = YoutubeSearch(text, max_results = 10).to_dict()
                   if result :
                      break
             url = 'https://www.youtube.com' + result [2] ['url_suffix'] 
             webbrowser.open(url)
             speak("bài hát của bạn đã được mở")
         def tell_me():
             try:
                 speak("Bạn muốn nghe về gì ạ!")
                 text = get_text()
                 contents = wikipedia.summary(text).split('\n')
                 speak(contents[0])
                 time.sleep(20)
                 for conten in contents[1:]:
                     speak("Bạn muốn nghe tiếp hay không ?")
                     ans = you
                     if "không" in ans:
                         break
                     speak(content)
                     time.sleep(20)
                     
                 speak("Cảm ơn bạn đã lắng nghe!")
             except:
                 speak("Sen không định nghĩa được ngôn ngữ của bạn!")    
         def stop():
             speak("hẹn gặp lại")
         
         def talk():
             now = datetime.now()
             day_time = int(now.strftime('%H'))
             if day_time < 12 :   
                speak('Chào buổi sáng')
             elif day_time < 18 :
                speak('Chào buổi chiều')
             else :
                speak('Chào buổi tối')
         def ngay():
             today = date.today()  
             speak(today.strftime('Hôm nay là ngày %d tháng %m năm %Y'))
         def gio():
             now = datetime.now()
             speak(now.strftime(' %H %M '))             
                        
                                                             
                                                  
         
          
         def call_sen():
             speak("Xin chào, bạn tên là gì nhỉ?")
             time.sleep(2)
             name = get_text()
             if name:
                 speak("Chào bạn {}".format(name))
                 time.sleep(1)
                 speak("Bạn cần Sen giúp gì ạ!")
                 time.sleep(2)
             while True:
             you = get_text()
             if not you:
                 break           

            if you == '':
              speak('Tôi chưa nghe thấy bạn!')
            elif 'Xin chào' in you:
                  talk()
                       
            elif 'thời tiết' in you: 
                  robot_brain = 'its rainning'
            elif 'ngày' in you :
                  ngay()
                   
            elif 'giờ' in you :
                  gio() 
                  
            elif 'Tìm' in you :
                   pass
            elif 'video'in you :
                  new = 2 
                  url = 'https://www.youtube.com'
                  webbrowser.open(url,new=new);
                  speak("Của bạn đây")
            elif 'Google' in you :
                  webbrowser.open('https://www.google.com.vn/',new=2)
                  robot_brain="Của bạn đây"      
            elif  "chơi nhạc" in you :
                     play_youtube()
            elif 'từ điển' in you :
                  tell_me()
            elif 'dừng' in you : 
                  speak('Chào')
                  
            else:
                  speak("Chưa có chức năng này")
         call_sen()                  
            
            

            

                    
        
   
                   
        
                     
   